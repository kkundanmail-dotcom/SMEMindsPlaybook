"""
SMEMinds Playbook Backend — user registration + progress sync.
Run: uvicorn main:app --reload --port 8000
"""
import os, json, sqlite3, hashlib, hmac, secrets, time, base64
import urllib.request, urllib.error
from contextlib import contextmanager
from typing import Optional, Any
import jwt
from urllib.parse import urlparse
from fastapi import FastAPI, HTTPException, Depends, Header, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field
from typing import Literal

BASE = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE, "smeminds.db")

def _load_or_create_secret(env_var: str, filename: str, *, announce: bool = False) -> str:
    """Env var wins; otherwise persist a random secret next to the DB so tokens
    survive restarts without ever falling back to a publicly-known default."""
    val = os.environ.get(env_var, "").strip()
    if val:
        return val
    path = os.path.join(BASE, filename)
    if os.path.exists(path):
        with open(path) as f:
            stored = f.read().strip()
        if stored:
            return stored
    secret = secrets.token_urlsafe(48)
    with open(path, "w") as f:
        f.write(secret)
    try:
        os.chmod(path, 0o600)
    except OSError:
        pass
    if announce:
        print(f"[smeminds] {env_var} not set — generated one in backend/{filename}")
    return secret

JWT_SECRET = _load_or_create_secret("SMEMINDS_JWT_SECRET", ".jwt_secret")
ADMIN_KEY = _load_or_create_secret("SMEMINDS_ADMIN_KEY", ".admin_key", announce=True)
JWT_ALGO = "HS256"
JWT_TTL = 60 * 60 * 24 * 30  # 30 days

# ── SUBSCRIPTION / PAYWALL ────────────────────────────────────
# Razorpay test-mode keys (set env vars to go live). When unset, the API runs
# in MOCK mode: orders are simulated and verification auto-succeeds, so the full
# subscribe → activate flow works end-to-end without real keys.
RAZORPAY_KEY_ID = os.environ.get("RAZORPAY_KEY_ID", "")
RAZORPAY_KEY_SECRET = os.environ.get("RAZORPAY_KEY_SECRET", "")
RAZORPAY_MOCK = not (RAZORPAY_KEY_ID and RAZORPAY_KEY_SECRET)

# Plan catalog (prices in ₹/INR). Yearly = ~20% off monthly×12.
# These are DEFAULTS — admins can override them at runtime (stored in app_config).
DEFAULT_PLANS = [
    {
        "id": "free", "name": "Free", "monthly": 0, "yearly": 0,
        "tagline": "Experience the value before you commit",
        "cta": "Current Plan",
        "features": [
            "First 3 modules free", "Community access (read-only)",
            "2 downloadable templates", "Progress tracking",
        ],
    },
    {
        "id": "growth", "name": "Growth", "monthly": 499, "yearly": 4790,
        "tagline": "For sellers ready to scale", "popular": False,
        "cta": "Choose Growth",
        "features": [
            "Complete Playbook (all 63 modules)", "New modules as released",
            "Full community access", "All resource downloads", "Monthly webinars",
        ],
    },
    {
        "id": "professional", "name": "Professional", "monthly": 1499, "yearly": 14390,
        "tagline": "Everything you need to win", "popular": True,
        "cta": "Choose Professional",
        "features": [
            "Everything in Growth", "Live Q&A sessions", "Seller templates library",
            "Marketplace calculators", "Certification",
        ],
    },
    {
        "id": "elite", "name": "Elite", "monthly": 4999, "yearly": 47990,
        "tagline": "Done-with-you expert support", "popular": False,
        "cta": "Choose Elite",
        "features": [
            "Everything in Professional", "Expert consultation", "Account audit",
            "Strategy sessions", "Premium resources",
        ],
    },
]

DEFAULT_PAYWALL = {
    "free_modules": 3,            # first N modules unlocked for free users
    "free_articles_per_month": 5,
    "free_downloads": 2,
    "video_preview_pct": 30,
    "preview_pct": 20,            # % of a locked lesson shown as a teaser
}

# 9 Growth Pillars metadata — drives the dashboard "Amazon Growth Journey".
DEFAULT_PILLARS = [
    {"p": "p1", "num": "01", "name": "Account Management", "cat": "Amazon Foundation",           "color": "#10b981", "sops": 22, "hours": 3, "level": "Beginner",     "desc": "Seller Central setup, account health, compliance, suspension appeals, tax & fee optimisation."},
    {"p": "p2", "num": "02", "name": "Selection",          "cat": "Catalogue Excellence",        "color": "#ff6b35", "sops": 25, "hours": 4, "level": "Beginner",     "desc": "Product research, ASIN creation, variations, browse nodes, localisation & bulk uploads."},
    {"p": "p3", "num": "03", "name": "Efficiency",         "cat": "Listing Optimization Engine", "color": "#6366f1", "sops": 20, "hours": 3, "level": "Intermediate", "desc": "SEO & keyword strategy, image optimisation, A+ content, pricing & listing quality."},
    {"p": "p4", "num": "04", "name": "Traffic",            "cat": "Customer Acquisition Engine",  "color": "#3b82f6", "sops": 18, "hours": 4, "level": "Intermediate", "desc": "Sponsored Products / Brands / Display, DSP, external traffic, influencer & organic SEO."},
    {"p": "p5", "num": "05", "name": "Conversion",         "cat": "Revenue Growth Engine",       "color": "#22c55e", "sops": 15, "hours": 3, "level": "Intermediate", "desc": "CRO, A/B testing, promotions, coupons, Subscribe & Save, cross-sell & upsell."},
    {"p": "p6", "num": "06", "name": "Speed",              "cat": "Operations Excellence",       "color": "#f59e0b", "sops": 20, "hours": 4, "level": "Advanced",     "desc": "FBA, inventory planning, forecasting, replenishment, Buy Box & SLA monitoring."},
    {"p": "p7", "num": "07", "name": "Tools",              "cat": "Seller Intelligence Stack",   "color": "#8b5cf6", "sops": 24, "hours": 4, "level": "Advanced",     "desc": "Brand Analytics, Search Query Performance, Ad Console, Helium 10, Jungle Scout & AI tools."},
    {"p": "p8", "num": "08", "name": "Brand Registry",     "cat": "Brand Growth Framework",      "color": "#ec4899", "sops": 18, "hours": 3, "level": "Advanced",     "desc": "Enrolment, Brand Store, A+ content, Sponsored Brands, Vine & Brand Analytics."},
    {"p": "p9", "num": "09", "name": "Brand Protection",   "cat": "Marketplace Defense System",  "color": "#ef4444", "sops": 22, "hours": 4, "level": "Expert",       "desc": "Trademark protection, Transparency, Project Zero, counterfeit & hijacker enforcement."},
]

# Editable marketing/site content shown on the dashboard.
DEFAULT_CONTENT = {
    "hero_eyebrow": "Amazon India · Ex-Amazonians Built · 400+ Brands",
    "hero_title": "Your Complete Amazon",
    "hero_accent": "Growth Playbook",
    "hero_subtitle": "Master every growth lever on Amazon India. 63 expert modules across 9 pillars — from selection strategy to account management, compliance & brand protection, powered by SMEMinds AI.",
    "journey_eyebrow": "The Growth Operating System",
    "journey_title": "Amazon Growth Journey",
    "stats": [
        {"label": "Modules", "value": "63", "suffix": ""},
        {"label": "SOPs", "value": "250", "suffix": "+"},
        {"label": "Templates", "value": "100", "suffix": "+"},
        {"label": "Checklists", "value": "50", "suffix": "+"},
        {"label": "Calculators", "value": "20", "suffix": "+"},
        {"label": "Certification", "value": "★", "suffix": ""},
    ],
}

# ── DB ────────────────────────────────────────────────────────
def init_db():
    with sqlite3.connect(DB_PATH) as c:
        c.execute("""CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            pass_hash TEXT NOT NULL,
            salt TEXT NOT NULL,
            name TEXT,
            role TEXT,
            created_at INTEGER NOT NULL
        )""")
        c.execute("""CREATE TABLE IF NOT EXISTS progress (
            user_id INTEGER PRIMARY KEY,
            data TEXT NOT NULL,
            updated_at INTEGER NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )""")
        c.execute("""CREATE TABLE IF NOT EXISTS modules (
            id TEXT PRIMARY KEY,
            pillar TEXT NOT NULL,
            number TEXT NOT NULL,
            title TEXT NOT NULL,
            data TEXT NOT NULL,
            updated_at INTEGER NOT NULL
        )""")
        c.execute("""CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            session_id TEXT,
            event_type TEXT NOT NULL,
            module_id TEXT,
            referrer TEXT,
            referrer_host TEXT,
            utm_source TEXT,
            utm_medium TEXT,
            utm_campaign TEXT,
            user_agent TEXT,
            path TEXT,
            created_at INTEGER NOT NULL
        )""")
        c.execute("CREATE INDEX IF NOT EXISTS idx_events_created ON events(created_at)")
        c.execute("CREATE INDEX IF NOT EXISTS idx_events_type ON events(event_type)")
        c.execute("CREATE INDEX IF NOT EXISTS idx_events_type_created ON events(event_type, created_at)")
        c.execute("CREATE INDEX IF NOT EXISTS idx_events_module ON events(module_id, created_at)")
        c.execute("CREATE INDEX IF NOT EXISTS idx_modules_pillar ON modules(pillar)")
        c.execute("""CREATE TABLE IF NOT EXISTS certificates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cert_id TEXT UNIQUE NOT NULL,
            user_id INTEGER NOT NULL UNIQUE,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            modules_visited INTEGER NOT NULL,
            modules_total INTEGER NOT NULL,
            quizzes_taken INTEGER NOT NULL,
            issued_at INTEGER NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )""")
        # ── Subscriptions: one active row per user (soft paywall) ──
        c.execute("""CREATE TABLE IF NOT EXISTS subscriptions (
            user_id INTEGER PRIMARY KEY,
            plan TEXT NOT NULL DEFAULT 'free',
            status TEXT NOT NULL DEFAULT 'active',
            billing_cycle TEXT,
            started_at INTEGER,
            expires_at INTEGER,
            razorpay_order_id TEXT,
            razorpay_payment_id TEXT,
            amount INTEGER,
            updated_at INTEGER NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )""")
        # ── App config: key/value JSON store (paywall limits, editable) ──
        c.execute("""CREATE TABLE IF NOT EXISTS app_config (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL,
            updated_at INTEGER NOT NULL
        )""")
        # ── Billing orders: binds each Razorpay order to the plan/amount it
        #    was created for, so /billing/verify can't be called with a forged
        #    plan or a replayed signature ──
        c.execute("""CREATE TABLE IF NOT EXISTS billing_orders (
            order_id TEXT PRIMARY KEY,
            user_id INTEGER NOT NULL,
            plan TEXT NOT NULL,
            cycle TEXT NOT NULL,
            amount_paise INTEGER NOT NULL,
            status TEXT NOT NULL DEFAULT 'created',
            created_at INTEGER NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )""")
        # ── Coupons: admin-managed discount codes ──
        c.execute("""CREATE TABLE IF NOT EXISTS coupons (
            code TEXT PRIMARY KEY,
            percent_off INTEGER NOT NULL DEFAULT 0,
            plan TEXT,
            max_redemptions INTEGER NOT NULL DEFAULT 0,
            redeemed INTEGER NOT NULL DEFAULT 0,
            expires_at INTEGER,
            active INTEGER NOT NULL DEFAULT 1,
            created_at INTEGER NOT NULL
        )""")
        # ── Migration: add richer onboarding/profile columns to existing DBs ──
        _have = {r[1] for r in c.execute("PRAGMA table_info(users)").fetchall()}
        for col in ("phone", "company", "business_type", "marketplace",
                    "gst", "revenue_range", "experience", "onboarded"):
            if col not in _have:
                c.execute(f"ALTER TABLE users ADD COLUMN {col} TEXT")
        c.commit()
    with sqlite3.connect(DB_PATH) as c:
        c.execute("PRAGMA journal_mode=WAL")

@contextmanager
def db():
    conn = sqlite3.connect(DB_PATH, timeout=10)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA busy_timeout=5000")
    conn.execute("PRAGMA synchronous=NORMAL")
    conn.execute("PRAGMA foreign_keys=ON")
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()

# ── Tiny in-memory rate limiter (per-process; fine for a single-host app) ──
_RL_BUCKETS: dict = {}

def _rate_limit(key: str, limit: int, window_sec: int):
    """Raise 429 when `key` exceeds `limit` hits per `window_sec`."""
    now = time.time()
    bucket = _RL_BUCKETS.setdefault(key, [])
    cutoff = now - window_sec
    while bucket and bucket[0] < cutoff:
        bucket.pop(0)
    if len(bucket) >= limit:
        raise HTTPException(429, "Too many requests — please slow down")
    bucket.append(now)
    if len(_RL_BUCKETS) > 10_000:  # bound memory under abuse
        _RL_BUCKETS.clear()

def _client_ip(request: Request) -> str:
    return request.client.host if request.client else "unknown"

# ── AUTH ──────────────────────────────────────────────────────
def hash_password(password: str, salt: Optional[str] = None):
    if not salt:
        salt = secrets.token_hex(16)
    h = hashlib.pbkdf2_hmac("sha256", password.encode(), salt.encode(), 200_000)
    return h.hex(), salt

def verify_password(password: str, pass_hash: str, salt: str) -> bool:
    h, _ = hash_password(password, salt)
    return secrets.compare_digest(h, pass_hash)

def make_token(user_id: int, email: str) -> str:
    payload = {"uid": user_id, "email": email, "exp": int(time.time()) + JWT_TTL}
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGO)

def current_user(authorization: Optional[str] = Header(None)) -> dict:
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(401, "Missing token")
    try:
        return jwt.decode(authorization.split(" ", 1)[1], JWT_SECRET, algorithms=[JWT_ALGO])
    except jwt.PyJWTError:
        raise HTTPException(401, "Invalid or expired token")

# ── MODELS ────────────────────────────────────────────────────
class RegisterIn(BaseModel):
    email: str
    password: str
    name: Optional[str] = ""
    role: Optional[str] = ""
    phone: Optional[str] = ""
    company: Optional[str] = ""
    business_type: Optional[str] = ""
    marketplace: Optional[str] = ""
    gst: Optional[str] = ""
    revenue_range: Optional[str] = ""
    experience: Optional[str] = ""

class LoginIn(BaseModel):
    email: str
    password: str

class ForgotIn(BaseModel):
    email: str

class ProfileIn(BaseModel):
    name: Optional[str] = None
    role: Optional[str] = None
    phone: Optional[str] = None
    company: Optional[str] = None
    business_type: Optional[str] = None
    marketplace: Optional[str] = None
    gst: Optional[str] = None
    revenue_range: Optional[str] = None
    experience: Optional[str] = None
    onboarded: Optional[str] = None

class ProgressIn(BaseModel):
    visited: list[Any] = []
    checklists: dict[str, Any] = {}
    quizScores: dict[str, Any] = {}
    feedback: list[Any] = []

class ModuleIn(BaseModel):
    id: str
    pillar: Optional[str] = ""
    number: Optional[str] = ""
    title: str
    difficulty: Optional[str] = ""
    time: Optional[str] = ""
    overview: Optional[str] = ""
    content: Optional[str] = ""
    process_flow: Optional[str] = ""
    tools: Optional[str] = ""
    videos: list[Any] = []
    checklist: list[str] = []
    quiz: list[Any] = []

EVENT_TYPES = {"app_open", "module_view", "paywall_view", "quiz_submit", "feedback_submit"}

class EventIn(BaseModel):
    event_type: str = Field(max_length=40)
    module_id: Optional[str] = Field(None, max_length=20)
    referrer: Optional[str] = Field(None, max_length=500)
    utm_source: Optional[str] = Field(None, max_length=100)
    utm_medium: Optional[str] = Field(None, max_length=100)
    utm_campaign: Optional[str] = Field(None, max_length=100)
    path: Optional[str] = Field(None, max_length=500)
    session_id: Optional[str] = Field(None, max_length=64)

# ── APP ───────────────────────────────────────────────────────
app = FastAPI(title="SMEMinds Playbook API", version="1.0")
# Origins default to "*" because the playbook runs from file:// (Origin: null).
# Set SMEMINDS_CORS_ORIGINS="https://playbook.smeminds.com,..." in production.
_cors = [o.strip() for o in os.environ.get("SMEMINDS_CORS_ORIGINS", "*").split(",") if o.strip()]
app.add_middleware(
    CORSMiddleware,
    allow_origins=_cors,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(GZipMiddleware, minimum_size=1024)

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/api/health")
def health():
    return {"ok": True, "ts": int(time.time())}

_PROFILE_COLS = ("phone", "company", "business_type", "marketplace",
                 "gst", "revenue_range", "experience", "onboarded")

def _user_public(row):
    """Full client-facing user object (profile fields included)."""
    u = {"email": row["email"], "name": row["name"] or "", "role": row["role"] or ""}
    for col in _PROFILE_COLS:
        try:
            u[col] = row[col] or ""
        except (IndexError, KeyError):
            u[col] = ""
    return u

@app.post("/api/register")
def register(body: RegisterIn, request: Request):
    _rate_limit(f"register:{_client_ip(request)}", limit=10, window_sec=300)
    email = body.email.strip().lower()
    if not email or "@" not in email:
        raise HTTPException(400, "Invalid email")
    if len(body.password) < 8:
        raise HTTPException(400, "Password must be at least 8 characters")
    pass_hash, salt = hash_password(body.password)
    now = int(time.time())
    with db() as c:
        try:
            cur = c.execute(
                """INSERT INTO users (email, pass_hash, salt, name, role, phone, company,
                                      business_type, marketplace, gst, revenue_range, experience, created_at)
                   VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                (email, pass_hash, salt, body.name or "", body.role or "", body.phone or "",
                 body.company or "", body.business_type or "", body.marketplace or "",
                 body.gst or "", body.revenue_range or "", body.experience or "", now),
            )
        except sqlite3.IntegrityError:
            raise HTTPException(409, "An account with this email already exists")
        uid = cur.lastrowid
        c.execute(
            "INSERT INTO progress (user_id, data, updated_at) VALUES (?,?,?)",
            (uid, json.dumps({"visited": [], "checklists": {}, "quizScores": {}, "feedback": []}), now),
        )
        row = c.execute("SELECT * FROM users WHERE id=?", (uid,)).fetchone()
    return {"token": make_token(uid, email), "user": _user_public(row),
            "subscription": _get_subscription(uid)}

@app.post("/api/login")
def login(body: LoginIn, request: Request):
    _rate_limit(f"login:{_client_ip(request)}", limit=15, window_sec=300)
    email = body.email.strip().lower()
    with db() as c:
        row = c.execute("SELECT * FROM users WHERE email=?", (email,)).fetchone()
    if not row or not verify_password(body.password, row["pass_hash"], row["salt"]):
        raise HTTPException(401, "Invalid email or password")
    return {
        "token": make_token(row["id"], row["email"]),
        "user": _user_public(row),
        "subscription": _get_subscription(row["id"]),
    }

@app.get("/api/me")
def me(user=Depends(current_user)):
    with db() as c:
        row = c.execute("SELECT * FROM users WHERE id=?", (user["uid"],)).fetchone()
    if not row:
        raise HTTPException(404, "User not found")
    return {"user": _user_public(row), "subscription": _get_subscription(user["uid"])}

@app.patch("/api/profile")
def update_profile(body: ProfileIn, user=Depends(current_user)):
    """Update onboarding/profile fields for the signed-in user."""
    fields, vals = [], []
    allowed = {"name", "role"} | set(_PROFILE_COLS)
    data = body.model_dump(exclude_none=True) if hasattr(body, "model_dump") else body.dict(exclude_none=True)
    for k, v in data.items():
        if k in allowed:
            fields.append(f"{k}=?"); vals.append(v)
    if not fields:
        with db() as c:
            row = c.execute("SELECT * FROM users WHERE id=?", (user["uid"],)).fetchone()
        return {"user": _user_public(row)}
    vals.append(user["uid"])
    with db() as c:
        c.execute(f"UPDATE users SET {', '.join(fields)} WHERE id=?", vals)
        row = c.execute("SELECT * FROM users WHERE id=?", (user["uid"],)).fetchone()
    return {"user": _user_public(row)}

@app.post("/api/forgot-password")
def forgot_password(body: ForgotIn, request: Request):
    """Account-non-revealing password-reset hook. Email delivery requires SMTP
    configuration (SMEMINDS_SMTP_HOST). Until then we return a clear message so
    no user is left wondering; the provider integration plugs in here."""
    _rate_limit(f"forgot:{_client_ip(request)}", limit=5, window_sec=300)
    smtp_ready = bool(os.environ.get("SMEMINDS_SMTP_HOST"))
    if smtp_ready:
        # TODO: mint a short-lived reset token (model after make_token) + email it.
        return {"message": "If an account exists for that email, a secure reset link is on its way."}
    return {"message": "Password reset by email isn't configured on this server yet. "
                       "Please ask your SMEMinds admin to reset your password."}

@app.get("/api/progress")
def get_progress(user=Depends(current_user)):
    with db() as c:
        row = c.execute("SELECT data, updated_at FROM progress WHERE user_id=?", (user["uid"],)).fetchone()
    if not row:
        return {"visited": [], "checklists": {}, "quizScores": {}, "feedback": [], "updated_at": 0}
    data = json.loads(row["data"])
    data["updated_at"] = row["updated_at"]
    return data

@app.put("/api/progress")
def put_progress(body: ProgressIn, user=Depends(current_user)):
    """Merge-write: progress only ever grows, so a stale offline cache can
    never erase newer server state (visited is unioned, maps are key-merged,
    feedback entries are deduped on content)."""
    now = int(time.time())
    with db() as c:
        row = c.execute("SELECT data FROM progress WHERE user_id=?", (user["uid"],)).fetchone()
        try:
            current = json.loads(row["data"]) if row else {}
        except Exception:
            current = {}
        # union (progress only grows), deduped, and intersected with REAL module ids
        # so stale ids from an old structure can never inflate the count past 100%.
        real_ids = {str(r["id"]) for r in c.execute("SELECT id FROM modules").fetchall()}
        visited = [v for v in dict.fromkeys(
            [str(v) for v in (current.get("visited") or [])] +
            [str(v) for v in body.visited]
        ) if not real_ids or v in real_ids]
        checklists = dict(current.get("checklists") or {})
        checklists.update(body.checklists or {})
        quiz_scores = dict(current.get("quizScores") or {})
        quiz_scores.update(body.quizScores or {})
        feedback = list(current.get("feedback") or [])
        seen = {json.dumps(f, sort_keys=True) for f in feedback if isinstance(f, (dict, list, str))}
        for f in body.feedback or []:
            key = json.dumps(f, sort_keys=True) if isinstance(f, (dict, list, str)) else repr(f)
            if key not in seen:
                feedback.append(f)
                seen.add(key)
        payload = {
            "visited": visited,
            "checklists": checklists,
            "quizScores": quiz_scores,
            "feedback": feedback,
        }
        c.execute(
            """INSERT INTO progress (user_id, data, updated_at) VALUES (?,?,?)
               ON CONFLICT(user_id) DO UPDATE SET data=excluded.data, updated_at=excluded.updated_at""",
            (user["uid"], json.dumps(payload), now),
        )
    return {"ok": True, "updated_at": now}

# ── ADMIN ─────────────────────────────────────────────────────
def _check_admin(key: Optional[str]):
    if not key or not secrets.compare_digest(key, ADMIN_KEY):
        raise HTTPException(403, "Forbidden")

@app.get("/api/admin/users")
def admin_list_users(x_admin_key: Optional[str] = Header(None)):
    _check_admin(x_admin_key)
    with db() as c:
        rows = c.execute(
            """SELECT u.id, u.email, u.name, u.role, u.created_at,
                      json_array_length(json_extract(p.data,'$.visited')) AS modules_visited,
                      json_array_length(json_extract(p.data,'$.feedback')) AS feedback_count,
                      p.updated_at AS last_active
               FROM users u LEFT JOIN progress p ON p.user_id = u.id
               ORDER BY u.created_at DESC"""
        ).fetchall()
    return [dict(r) for r in rows]

@app.get("/api/admin/users/{user_id}/progress")
def admin_user_progress(user_id: int, x_admin_key: Optional[str] = Header(None)):
    _check_admin(x_admin_key)
    with db() as c:
        u = c.execute("SELECT id, email, name, role, created_at FROM users WHERE id=?", (user_id,)).fetchone()
        if not u:
            raise HTTPException(404, "User not found")
        p = c.execute("SELECT data, updated_at FROM progress WHERE user_id=?", (user_id,)).fetchone()
    progress = json.loads(p["data"]) if p else {"visited": [], "checklists": {}, "quizScores": {}, "feedback": []}
    progress["updated_at"] = p["updated_at"] if p else 0
    return {"user": dict(u), "progress": progress}

@app.get("/api/admin/stats")
def admin_stats(x_admin_key: Optional[str] = Header(None)):
    _check_admin(x_admin_key)
    with db() as c:
        total_users = c.execute("SELECT COUNT(*) AS n FROM users").fetchone()["n"]
        rows = c.execute("SELECT data FROM progress").fetchall()
    total_visits = 0
    total_quizzes = 0
    total_feedback = 0
    for r in rows:
        try:
            d = json.loads(r["data"])
            total_visits += len(d.get("visited", []))
            total_quizzes += len(d.get("quizScores", {}))
            total_feedback += len(d.get("feedback", []))
        except Exception:
            pass
    return {
        "total_users": total_users,
        "total_module_visits": total_visits,
        "total_quizzes_taken": total_quizzes,
        "total_feedback": total_feedback,
    }

# ── MODULES (admin CRUD) ──────────────────────────────────────
def _pillar_from_id(mid: str) -> str:
    head = mid.split(".")[0] if "." in mid else mid
    return f"p{head}" if head.isdigit() else head

@app.get("/api/admin/modules")
def admin_list_modules(x_admin_key: Optional[str] = Header(None)):
    _check_admin(x_admin_key)
    with db() as c:
        rows = c.execute(
            "SELECT id, pillar, number, title, updated_at FROM modules ORDER BY id"
        ).fetchall()
    return [dict(r) for r in rows]

@app.get("/api/admin/modules/{module_id}")
def admin_get_module(module_id: str, x_admin_key: Optional[str] = Header(None)):
    _check_admin(x_admin_key)
    with db() as c:
        row = c.execute("SELECT data, updated_at FROM modules WHERE id=?", (module_id,)).fetchone()
    if not row:
        raise HTTPException(404, "Module not found")
    data = json.loads(row["data"])
    data["updated_at"] = row["updated_at"]
    return data

@app.put("/api/admin/modules/{module_id}")
def admin_update_module(module_id: str, body: ModuleIn, x_admin_key: Optional[str] = Header(None)):
    _check_admin(x_admin_key)
    if body.id != module_id:
        raise HTTPException(400, "Path id must match body id")
    pillar = body.pillar or _pillar_from_id(body.id)
    payload = {
        "id": body.id, "pillar": pillar, "number": body.number or body.id,
        "title": body.title, "difficulty": body.difficulty or "",
        "time": body.time or "", "overview": body.overview or "",
        "content": body.content or "", "process_flow": body.process_flow or "",
        "tools": body.tools or "", "videos": body.videos or [],
        "checklist": body.checklist or [], "quiz": body.quiz or [],
    }
    now = int(time.time())
    with db() as c:
        c.execute(
            """INSERT INTO modules (id, pillar, number, title, data, updated_at) VALUES (?,?,?,?,?,?)
               ON CONFLICT(id) DO UPDATE SET pillar=excluded.pillar, number=excluded.number,
                 title=excluded.title, data=excluded.data, updated_at=excluded.updated_at""",
            (body.id, pillar, payload["number"], body.title, json.dumps(payload), now),
        )
    return {"ok": True, "updated_at": now}

_TEASER_FIELDS = ("id", "pillar", "number", "title", "difficulty", "time", "overview")

@app.delete("/api/admin/modules/{module_id}")
def admin_delete_module(module_id: str, x_admin_key: Optional[str] = Header(None)):
    _check_admin(x_admin_key)
    with db() as c:
        cur = c.execute("DELETE FROM modules WHERE id=?", (module_id,))
        if cur.rowcount == 0:
            raise HTTPException(404, "Module not found")
    return {"ok": True, "deleted": module_id}

@app.get("/api/modules")
def public_list_modules(authorization: Optional[str] = Header(None)):
    """Paywall-aware module list. Anonymous/free callers get teaser fields only;
    premium subscribers (valid bearer token) get full module bodies."""
    premium = False
    free_count = int(_get_paywall_config().get("free_modules", 3) or 0)
    if authorization and authorization.startswith("Bearer "):
        try:
            payload = jwt.decode(authorization.split(" ", 1)[1], JWT_SECRET, algorithms=[JWT_ALGO])
            premium = _get_subscription(payload["uid"]).get("is_premium", False)
        except jwt.PyJWTError:
            pass
    with db() as c:
        rows = c.execute("SELECT data FROM modules ORDER BY pillar, id").fetchall()
    modules = [json.loads(r["data"]) for r in rows]
    if premium:
        return modules
    out = []
    for i, m in enumerate(modules):
        if i < free_count:
            out.append(m)
        else:
            out.append({k: m.get(k) for k in _TEASER_FIELDS})
    return out

# ── EVENTS / TRAFFIC ──────────────────────────────────────────
# First labels of search/social hosts ("google" matches google.com, www.google.co.in)
_SEARCH_LABELS = ("google", "bing", "duckduckgo", "yahoo", "yandex", "baidu")
_SOCIAL_LABELS = ("facebook", "fb", "twitter", "linkedin", "instagram", "youtube",
                  "reddit", "tiktok", "pinterest", "whatsapp", "telegram")
# Exact registrable domains (also match their subdomains)
_SOCIAL_DOMAINS = ("x.com", "t.co", "youtu.be")

def _categorize_source(utm_source: Optional[str], referrer_host: Optional[str]) -> str:
    if utm_source:
        return utm_source.strip().lower()
    if not referrer_host:
        return "direct"
    h = referrer_host.lower()
    labels = h.split(".")
    if any(lbl in _SEARCH_LABELS for lbl in labels):
        return "search"
    if any(lbl in _SOCIAL_LABELS for lbl in labels):
        return "social"
    if any(h == d or h.endswith("." + d) for d in _SOCIAL_DOMAINS):
        return "social"
    return h

def _host_of(url: Optional[str]) -> Optional[str]:
    if not url:
        return None
    try:
        return urlparse(url).hostname or None
    except Exception:
        return None

@app.post("/api/events")
def track_event(body: EventIn, request: Request):
    if body.event_type not in EVENT_TYPES:
        raise HTTPException(400, "Unknown event type")
    _rate_limit(f"events:{_client_ip(request)}", limit=120, window_sec=60)
    user_id = None
    auth = request.headers.get("authorization", "")
    if auth.startswith("Bearer "):
        try:
            payload = jwt.decode(auth[7:], JWT_SECRET, algorithms=[JWT_ALGO])
            user_id = payload.get("uid")
        except jwt.PyJWTError:
            pass
    ua = (request.headers.get("user-agent") or "")[:300]
    ref_host = _host_of(body.referrer)
    with db() as c:
        c.execute(
            """INSERT INTO events (user_id, session_id, event_type, module_id, referrer,
                                   referrer_host, utm_source, utm_medium, utm_campaign,
                                   user_agent, path, created_at)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",
            (user_id, body.session_id, body.event_type, body.module_id, body.referrer,
             ref_host, body.utm_source, body.utm_medium, body.utm_campaign, ua,
             body.path, int(time.time())),
        )
    return {"ok": True}

@app.get("/api/admin/traffic")
def admin_traffic(days: int = 30, x_admin_key: Optional[str] = Header(None)):
    _check_admin(x_admin_key)
    since = int(time.time()) - days * 86400
    with db() as c:
        totals_row = c.execute(
            "SELECT COUNT(*) AS n, COUNT(DISTINCT session_id) AS sessions, COUNT(DISTINCT user_id) AS users FROM events WHERE created_at >= ?",
            (since,),
        ).fetchone()
        opens = c.execute(
            "SELECT COUNT(*) AS n FROM events WHERE event_type='app_open' AND created_at >= ?",
            (since,),
        ).fetchone()["n"]
        module_views = c.execute(
            "SELECT COUNT(*) AS n FROM events WHERE event_type='module_view' AND created_at >= ?",
            (since,),
        ).fetchone()["n"]
        # By source — categorize per row, then aggregate in Python (sqlite has no fancy CASE here)
        rows = c.execute(
            """SELECT utm_source, referrer_host, COUNT(*) AS n
               FROM events WHERE event_type='app_open' AND created_at >= ?
               GROUP BY utm_source, referrer_host""",
            (since,),
        ).fetchall()
        source_counts: dict[str, int] = {}
        for r in rows:
            src = _categorize_source(r["utm_source"], r["referrer_host"])
            source_counts[src] = source_counts.get(src, 0) + r["n"]
        sources = [{"source": k, "count": v} for k, v in sorted(source_counts.items(), key=lambda x: -x[1])]

        top_modules = [dict(r) for r in c.execute(
            """SELECT module_id, COUNT(*) AS views FROM events
               WHERE event_type='module_view' AND module_id IS NOT NULL AND created_at >= ?
               GROUP BY module_id ORDER BY views DESC LIMIT 20""",
            (since,),
        ).fetchall()]

        utm_campaigns = [dict(r) for r in c.execute(
            """SELECT utm_campaign, COUNT(*) AS n FROM events
               WHERE utm_campaign IS NOT NULL AND utm_campaign != '' AND created_at >= ?
               GROUP BY utm_campaign ORDER BY n DESC LIMIT 20""",
            (since,),
        ).fetchall()]

        utm_mediums = [dict(r) for r in c.execute(
            """SELECT utm_medium, COUNT(*) AS n FROM events
               WHERE utm_medium IS NOT NULL AND utm_medium != '' AND created_at >= ?
               GROUP BY utm_medium ORDER BY n DESC LIMIT 20""",
            (since,),
        ).fetchall()]

        # Daily totals
        daily = [dict(r) for r in c.execute(
            """SELECT strftime('%Y-%m-%d', datetime(created_at,'unixepoch','localtime')) AS day,
                      SUM(CASE WHEN event_type='app_open' THEN 1 ELSE 0 END) AS opens,
                      SUM(CASE WHEN event_type='module_view' THEN 1 ELSE 0 END) AS views
               FROM events WHERE created_at >= ?
               GROUP BY day ORDER BY day""",
            (since,),
        ).fetchall()]

        recent = [dict(r) for r in c.execute(
            """SELECT event_type, module_id, utm_source, referrer_host, user_id, created_at
               FROM events ORDER BY created_at DESC LIMIT 30"""
        ).fetchall()]

        # Hour-of-day totals (0–23)
        hourly_rows = c.execute(
            """SELECT CAST(strftime('%H', datetime(created_at,'unixepoch','localtime')) AS INTEGER) AS hour, COUNT(*) AS n
               FROM events WHERE event_type IN ('app_open','module_view') AND created_at >= ?
               GROUP BY hour""",
            (since,),
        ).fetchall()
        hourly = [0] * 24
        for r in hourly_rows:
            hourly[r["hour"]] = r["n"]

        # Day-of-week × hour heatmap (rows 0..6 = Sun..Sat)
        heat_rows = c.execute(
            """SELECT CAST(strftime('%w', datetime(created_at,'unixepoch','localtime')) AS INTEGER) AS dow,
                      CAST(strftime('%H', datetime(created_at,'unixepoch','localtime')) AS INTEGER) AS hour,
                      COUNT(*) AS n
               FROM events WHERE created_at >= ?
               GROUP BY dow, hour""",
            (since,),
        ).fetchall()
        heatmap = [[0] * 24 for _ in range(7)]
        for r in heat_rows:
            heatmap[r["dow"]][r["hour"]] = r["n"]

        # Pillar-level view aggregation (first character of module_id)
        pillar_rows = c.execute(
            """SELECT substr(module_id, 1, 1) AS pnum, COUNT(*) AS views
               FROM events WHERE event_type='module_view' AND module_id IS NOT NULL AND created_at >= ?
               GROUP BY pnum""",
            (since,),
        ).fetchall()
        pillar_views = [
            {"pillar": "p" + r["pnum"], "views": r["views"]}
            for r in pillar_rows if r["pnum"] and r["pnum"].isdigit()
        ]

    return {
        "window_days": days,
        "totals": {
            "events": totals_row["n"],
            "sessions": totals_row["sessions"] or 0,
            "authenticated_users": totals_row["users"] or 0,
            "app_opens": opens,
            "module_views": module_views,
        },
        "sources": sources,
        "top_modules": top_modules,
        "utm_campaigns": utm_campaigns,
        "utm_mediums": utm_mediums,
        "daily": daily,
        "hourly": hourly,
        "heatmap": heatmap,
        "pillar_views": pillar_views,
        "recent": recent,
    }

# ── SARVAM TTS (premium Indian-English voices for module videos) ──
# The API key lives ONLY in the backend — entered in /admin or via SARVAM_API_KEY
# env var. The browser only ever calls this proxy. Clips are cached on disk.
SARVAM_URL = "https://api.sarvam.ai/text-to-speech"
DEFAULT_SARVAM_MODEL = "bulbul:v3"
# English voices offered in the player (override via SARVAM_VOICES="id:Label:Gender,..." or admin config)
SARVAM_VOICES = [
    {"id": "ritu",  "label": "Ritu",  "gender": "Female"},
    {"id": "shubh", "label": "Shubh", "gender": "Male"},
]
_env_voices = os.environ.get("SARVAM_VOICES", "").strip()
if _env_voices:
    try:
        SARVAM_VOICES = []
        for part in _env_voices.split(","):
            vid, lab, gen = (part.split(":") + ["", ""])[:3]
            if vid.strip():
                SARVAM_VOICES.append({"id": vid.strip().lower(), "label": (lab or vid).strip(), "gender": (gen or "").strip()})
    except Exception:
        pass
_TTS_CACHE_DIR = os.path.join(BASE, ".tts_cache")

def _sarvam_voices():
    cfg = _get_config("sarvam", {}) or {}
    return cfg.get("voices") if isinstance(cfg.get("voices"), list) and cfg.get("voices") else SARVAM_VOICES

def _sarvam_cfg():
    """Resolve the Sarvam config — admin-entered config wins over the env var."""
    cfg = _get_config("sarvam", {}) or {}
    key = (cfg.get("key") or os.environ.get("SARVAM_API_KEY", "")).strip()
    model = (cfg.get("model") or os.environ.get("SARVAM_TTS_MODEL", "") or DEFAULT_SARVAM_MODEL).strip()
    src = "admin" if cfg.get("key") else ("env" if os.environ.get("SARVAM_API_KEY") else "none")
    return {"key": key, "model": model, "enabled": bool(key), "source": src}

class TTSIn(BaseModel):
    text: str = Field(max_length=2000)
    speaker: str = Field(max_length=40)

@app.get("/api/tts/voices")
def tts_voices():
    """Public: which premium voices are available (drives the video voice picker)."""
    cfg = _sarvam_cfg()
    return {"enabled": cfg["enabled"], "provider": "sarvam", "model": cfg["model"], "voices": _sarvam_voices()}

@app.post("/api/tts")
def tts(body: TTSIn, request: Request):
    """Synthesise narration via Sarvam Bulbul; cached per (model, speaker, text)."""
    cfg = _sarvam_cfg()
    if not cfg["enabled"]:
        raise HTTPException(503, "Premium voice not configured")
    spk = body.speaker.strip().lower()
    if spk not in {v["id"] for v in _sarvam_voices()}:
        raise HTTPException(400, "Unknown speaker")
    text = (body.text or "").strip()[:2000]
    if not text:
        raise HTTPException(400, "Empty text")
    _rate_limit(f"tts:{_client_ip(request)}", limit=150, window_sec=60)
    ckey = hashlib.sha256((cfg["model"] + "|" + spk + "|" + text).encode()).hexdigest()
    os.makedirs(_TTS_CACHE_DIR, exist_ok=True)
    cpath = os.path.join(_TTS_CACHE_DIR, ckey + ".txt")
    if os.path.exists(cpath):
        with open(cpath) as f:
            return {"audio": "data:audio/mpeg;base64," + f.read(), "cached": True}
    b64 = _sarvam_synth(cfg, spk, text)
    try:
        with open(cpath, "w") as f:
            f.write(b64)
    except Exception:
        pass
    return {"audio": "data:audio/mpeg;base64," + b64, "cached": False}

def _sarvam_synth(cfg, speaker, text):
    payload = json.dumps({
        "text": text, "target_language_code": "en-IN", "model": cfg["model"],
        "speaker": speaker, "output_audio_codec": "mp3", "pace": 1.0,
    }).encode()
    req = urllib.request.Request(SARVAM_URL, data=payload, method="POST",
        headers={"Content-Type": "application/json", "api-subscription-key": cfg["key"]})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            data = json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        raise HTTPException(502, f"Sarvam error: {e.read().decode()[:200]}")
    except Exception as e:
        raise HTTPException(502, f"Sarvam unreachable: {e}")
    audios = data.get("audios") or []
    if not audios:
        raise HTTPException(502, "Sarvam returned no audio")
    return audios[0]

# ── Admin: Sarvam key management (key never returned to the client) ──
class SarvamCfgIn(BaseModel):
    key: Optional[str] = None
    model: Optional[str] = None

def _sarvam_admin_status():
    cfg = _sarvam_cfg(); k = cfg["key"]
    return {"enabled": cfg["enabled"], "model": cfg["model"], "source": cfg["source"],
            "voices": _sarvam_voices(),
            "key_masked": ("•••• " + k[-4:]) if len(k) >= 4 else ("set" if k else "")}

@app.get("/api/admin/sarvam")
def admin_get_sarvam(x_admin_key: Optional[str] = Header(None)):
    _check_admin(x_admin_key)
    return _sarvam_admin_status()

@app.put("/api/admin/sarvam")
def admin_set_sarvam(body: SarvamCfgIn, x_admin_key: Optional[str] = Header(None)):
    _check_admin(x_admin_key)
    cfg = dict(_get_config("sarvam", {}) or {})
    if body.key is not None:
        kk = body.key.strip()
        if kk:
            cfg["key"] = kk
        else:
            cfg.pop("key", None)          # empty string clears the stored key
    if body.model is not None and body.model.strip():
        cfg["model"] = body.model.strip()
    _set_config("sarvam", cfg)
    return {"ok": True, **_sarvam_admin_status()}

@app.post("/api/admin/sarvam/test")
def admin_test_sarvam(x_admin_key: Optional[str] = Header(None)):
    _check_admin(x_admin_key)
    cfg = _sarvam_cfg()
    if not cfg["enabled"]:
        raise HTTPException(400, "No API key set")
    spk = _sarvam_voices()[0]["id"]
    b64 = _sarvam_synth(cfg, spk, "SME Minds premium voice is now active.")
    return {"ok": True, "speaker": spk, "sample": "data:audio/mpeg;base64," + b64}

# ── CERTIFICATES ──────────────────────────────────────────────
# Eligibility threshold — override via env vars at deploy time
CERT_MIN_MODULES_VISITED_PCT = int(os.environ.get("SMEMINDS_CERT_MIN_MODULES_PCT", "80"))
CERT_VERIFY_BASE = os.environ.get("SMEMINDS_CERT_VERIFY_BASE", "http://127.0.0.1:8000/api/certificate/verify")

def _user_progress(user_id: int):
    with db() as c:
        row = c.execute("SELECT data FROM progress WHERE user_id=?", (user_id,)).fetchone()
    if not row:
        return {"visited": [], "quizScores": {}, "checklists": {}, "feedback": []}
    return json.loads(row["data"])

def _total_modules():
    with db() as c:
        n = c.execute("SELECT COUNT(*) AS n FROM modules").fetchone()["n"]
    return int(n or 0)

def _known_module_ids() -> set:
    with db() as c:
        rows = c.execute("SELECT id FROM modules").fetchall()
    return {r["id"] for r in rows}

def _eligibility_snapshot(user_id: int):
    progress = _user_progress(user_id)
    total = _total_modules() or 63  # fallback if DB not seeded
    raw_visited = progress.get("visited") or []
    known = _known_module_ids()
    if known:
        # Count only real module ids — a forged progress blob of duplicates or
        # junk ids must not mint a certificate
        visited = len({str(v) for v in raw_visited} & known)
    else:
        visited = len(set(str(v) for v in raw_visited))
    quizzes = len(progress.get("quizScores") or {})
    threshold = max(1, int(round(total * CERT_MIN_MODULES_VISITED_PCT / 100)))
    return {
        "modules_visited": visited,
        "modules_total": total,
        "quizzes_taken": quizzes,
        "threshold_modules": threshold,
        "threshold_pct": CERT_MIN_MODULES_VISITED_PCT,
        "eligible": visited >= threshold,
    }

@app.get("/api/certificate/eligibility")
def cert_eligibility(user=Depends(current_user)):
    snap = _eligibility_snapshot(user["uid"])
    with db() as c:
        existing = c.execute("SELECT cert_id, issued_at FROM certificates WHERE user_id=?", (user["uid"],)).fetchone()
    if existing:
        snap["already_issued"] = True
        snap["cert_id"] = existing["cert_id"]
        snap["issued_at"] = existing["issued_at"]
    else:
        snap["already_issued"] = False
    return snap

@app.post("/api/certificate/issue")
def cert_issue(user=Depends(current_user)):
    uid = user["uid"]
    with db() as c:
        u = c.execute("SELECT email, name FROM users WHERE id=?", (uid,)).fetchone()
    if not u:
        raise HTTPException(404, "User not found")
    snap = _eligibility_snapshot(uid)
    # Idempotent: if a cert already exists, return it instead of issuing again
    with db() as c:
        existing = c.execute(
            "SELECT cert_id, name, email, modules_visited, modules_total, quizzes_taken, issued_at FROM certificates WHERE user_id=?",
            (uid,),
        ).fetchone()
    if existing:
        return {**dict(existing), "already_issued": True, "verify_url": f"{CERT_VERIFY_BASE}/{existing['cert_id']}"}
    if not snap["eligible"]:
        raise HTTPException(
            403,
            f"Not yet eligible: need {snap['threshold_modules']} modules visited "
            f"({snap['threshold_pct']}% of {snap['modules_total']}), currently at {snap['modules_visited']}."
        )
    display_name = (u["name"] or "").strip() or u["email"].split("@")[0]
    now = int(time.time())
    year = time.strftime("%Y", time.localtime(now))
    # Unguessable id — sequential ids let anyone enumerate every holder's name
    # through the public verify endpoint
    cert_id = f"SME-{year}-{secrets.token_hex(4).upper()}"
    try:
        with db() as c:
            c.execute(
                """INSERT INTO certificates (cert_id, user_id, name, email, modules_visited, modules_total, quizzes_taken, issued_at)
                   VALUES (?,?,?,?,?,?,?,?)""",
                (cert_id, uid, display_name, u["email"], snap["modules_visited"],
                 snap["modules_total"], snap["quizzes_taken"], now),
            )
    except sqlite3.IntegrityError:
        # Concurrent issue for the same user — return the row that won
        with db() as c:
            existing = c.execute(
                "SELECT cert_id, name, email, modules_visited, modules_total, quizzes_taken, issued_at FROM certificates WHERE user_id=?",
                (uid,),
            ).fetchone()
        return {**dict(existing), "already_issued": True, "verify_url": f"{CERT_VERIFY_BASE}/{existing['cert_id']}"}
    return {
        "cert_id": cert_id, "user_id": uid, "name": display_name, "email": u["email"],
        "modules_visited": snap["modules_visited"], "modules_total": snap["modules_total"],
        "quizzes_taken": snap["quizzes_taken"], "issued_at": now,
        "already_issued": False, "verify_url": f"{CERT_VERIFY_BASE}/{cert_id}",
    }

@app.get("/api/certificate/me")
def cert_me(user=Depends(current_user)):
    with db() as c:
        row = c.execute(
            """SELECT cert_id, name, email, modules_visited, modules_total, quizzes_taken, issued_at
               FROM certificates WHERE user_id=?""",
            (user["uid"],),
        ).fetchone()
    if not row:
        raise HTTPException(404, "No certificate issued for this user")
    d = dict(row)
    d["verify_url"] = f"{CERT_VERIFY_BASE}/{d['cert_id']}"
    return d

@app.get("/api/certificate/verify/{cert_id}")
def cert_verify(cert_id: str, request: Request):
    """Public verification endpoint — returns minimal info to confirm authenticity."""
    _rate_limit(f"certverify:{_client_ip(request)}", limit=30, window_sec=60)
    with db() as c:
        row = c.execute(
            "SELECT cert_id, name, modules_visited, modules_total, issued_at FROM certificates WHERE cert_id=?",
            (cert_id,),
        ).fetchone()
    if not row:
        raise HTTPException(404, "Certificate not found")
    return {
        "valid": True,
        "cert_id": row["cert_id"],
        "name": row["name"],
        "modules_completed": f"{row['modules_visited']}/{row['modules_total']}",
        "issued_at": row["issued_at"],
        "issued_at_human": time.strftime("%d %b %Y", time.localtime(row["issued_at"])),
        "issuer": "SMEMinds",
    }

@app.get("/api/admin/certificates")
def admin_certificates(x_admin_key: Optional[str] = Header(None)):
    _check_admin(x_admin_key)
    with db() as c:
        rows = c.execute(
            """SELECT cert_id, user_id, name, email, modules_visited, modules_total, quizzes_taken, issued_at
               FROM certificates ORDER BY issued_at DESC"""
        ).fetchall()
    return [dict(r) for r in rows]

# ── SUBSCRIPTIONS / SOFT PAYWALL ──────────────────────────────
class OrderIn(BaseModel):
    plan: str
    cycle: Literal["monthly", "yearly"] = "monthly"

class VerifyIn(BaseModel):
    razorpay_order_id: str
    razorpay_payment_id: Optional[str] = None
    razorpay_signature: Optional[str] = None

# ── Generic config store (app_config table) ──────────────────
def _get_config(key: str, default):
    with db() as c:
        row = c.execute("SELECT value FROM app_config WHERE key=?", (key,)).fetchone()
    if not row:
        return default
    try:
        return json.loads(row["value"])
    except Exception:
        return default

def _set_config(key: str, value):
    now = int(time.time())
    with db() as c:
        c.execute(
            """INSERT INTO app_config (key, value, updated_at) VALUES (?,?,?)
               ON CONFLICT(key) DO UPDATE SET value=excluded.value, updated_at=excluded.updated_at""",
            (key, json.dumps(value), now),
        )

def _get_paywall_config() -> dict:
    cfg = dict(DEFAULT_PAYWALL)
    stored = _get_config("paywall", None)
    if isinstance(stored, dict):
        cfg.update(stored)
    return cfg

def _get_plans() -> list:
    plans = _get_config("plans", None)
    return plans if isinstance(plans, list) and plans else DEFAULT_PLANS

def _plan_index() -> dict:
    return {p["id"]: p for p in _get_plans()}

def _paid_plan_ids() -> set:
    return {p["id"] for p in _get_plans()
            if int(p.get("monthly", 0) or 0) > 0 or int(p.get("yearly", 0) or 0) > 0}

def _get_pillars() -> list:
    pil = _get_config("pillars", None)
    return pil if isinstance(pil, list) and pil else DEFAULT_PILLARS

def _get_content() -> dict:
    cfg = dict(DEFAULT_CONTENT)
    stored = _get_config("content", None)
    if isinstance(stored, dict):
        cfg.update(stored)
    return cfg

def _get_subscription(uid: int) -> dict:
    """Return the user's effective subscription, lazily expiring stale paid plans."""
    now = int(time.time())
    with db() as c:
        row = c.execute(
            """SELECT plan, status, billing_cycle, started_at, expires_at,
                      razorpay_payment_id, amount FROM subscriptions WHERE user_id=?""",
            (uid,),
        ).fetchone()
    if not row:
        return {"plan": "free", "status": "active", "billing_cycle": None,
                "started_at": None, "expires_at": None, "is_premium": False}
    d = dict(row)
    # A paid plan is anything that isn't free — based on the stored row, so an
    # admin removing a plan from the catalog doesn't silently strip subscribers
    is_paid = d["plan"] != "free"
    expired = is_paid and d["expires_at"] and d["expires_at"] < now
    if expired:
        # Lazily downgrade to free on read
        with db() as c:
            c.execute(
                "UPDATE subscriptions SET plan='free', status='expired', updated_at=? WHERE user_id=?",
                (now, uid),
            )
        d.update({"plan": "free", "status": "expired", "billing_cycle": None,
                  "started_at": None, "expires_at": None, "amount": None})
        is_paid = False
    d["is_premium"] = is_paid and d["status"] == "active"
    d.pop("razorpay_payment_id", None)  # client never needs the payment id
    return d

def _activate_subscription(uid: int, plan: str, cycle: str,
                           order_id: Optional[str], payment_id: Optional[str], amount: int):
    now = int(time.time())
    days = 365 if cycle == "yearly" else 30
    start_from = now
    with db() as c:
        row = c.execute(
            "SELECT plan, status, expires_at FROM subscriptions WHERE user_id=?", (uid,)
        ).fetchone()
    # Renewing the same plan before expiry extends from the current expiry —
    # paying early must not discard remaining time
    if row and row["plan"] == plan and row["status"] == "active" \
            and row["expires_at"] and row["expires_at"] > now:
        start_from = row["expires_at"]
    expires = start_from + days * 86400
    with db() as c:
        c.execute(
            """INSERT INTO subscriptions
                 (user_id, plan, status, billing_cycle, started_at, expires_at,
                  razorpay_order_id, razorpay_payment_id, amount, updated_at)
               VALUES (?,?,?,?,?,?,?,?,?,?)
               ON CONFLICT(user_id) DO UPDATE SET
                 plan=excluded.plan, status=excluded.status, billing_cycle=excluded.billing_cycle,
                 started_at=excluded.started_at, expires_at=excluded.expires_at,
                 razorpay_order_id=excluded.razorpay_order_id,
                 razorpay_payment_id=excluded.razorpay_payment_id,
                 amount=excluded.amount, updated_at=excluded.updated_at""",
            (uid, plan, "active", cycle, now, expires, order_id, payment_id, amount, now),
        )
    return {"plan": plan, "status": "active", "billing_cycle": cycle,
            "started_at": now, "expires_at": expires, "is_premium": True}

def _razorpay_create_order(amount_paise: int, receipt: str) -> Optional[dict]:
    """Create a real Razorpay order. Returns None in mock mode."""
    if RAZORPAY_MOCK:
        return None
    payload = json.dumps({
        "amount": amount_paise, "currency": "INR",
        "receipt": receipt, "payment_capture": 1,
    }).encode()
    auth = base64.b64encode(f"{RAZORPAY_KEY_ID}:{RAZORPAY_KEY_SECRET}".encode()).decode()
    req = urllib.request.Request(
        "https://api.razorpay.com/v1/orders", data=payload, method="POST",
        headers={"Authorization": "Basic " + auth, "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        raise HTTPException(502, f"Razorpay order failed: {e.read().decode()[:200]}")
    except Exception as e:
        raise HTTPException(502, f"Razorpay unreachable: {e}")

def _verify_razorpay_signature(order_id: str, payment_id: str, signature: str) -> bool:
    if RAZORPAY_MOCK:
        return False
    expected = hmac.new(
        RAZORPAY_KEY_SECRET.encode(), f"{order_id}|{payment_id}".encode(), hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(expected, signature or "")

@app.get("/api/plans")
def list_plans():
    """Public plan catalog + paywall config for the pricing UI."""
    return {"plans": _get_plans(), "paywall": _get_paywall_config(),
            "currency": "INR", "mock_payments": RAZORPAY_MOCK}

@app.get("/api/pillars")
def list_pillars():
    """Public 9-pillar metadata for the dashboard Growth Journey."""
    return {"pillars": _get_pillars()}

@app.get("/api/content")
def get_content():
    """Public editable site content (hero, journey heading, stat strip)."""
    return _get_content()

@app.get("/api/subscription")
def get_subscription(user=Depends(current_user)):
    sub = _get_subscription(user["uid"])
    idx = _plan_index()
    return {**sub, "paywall": _get_paywall_config(),
            "plan_detail": idx.get(sub["plan"], idx.get("free", {"id": "free", "name": "Free"}))}

@app.post("/api/billing/order")
def billing_order(body: OrderIn, user=Depends(current_user)):
    plan = body.plan
    cycle = body.cycle
    plans = _get_plans()
    idx = {p["id"]: p for p in plans}
    paid = {p["id"] for p in plans
            if int(p.get("monthly", 0) or 0) > 0 or int(p.get("yearly", 0) or 0) > 0}
    if plan not in paid:
        raise HTTPException(400, "Choose a paid plan to subscribe")
    amount = int(idx[plan]["yearly"] if cycle == "yearly" else idx[plan]["monthly"])
    if amount <= 0:
        raise HTTPException(400, f"{idx[plan]['name']} has no {cycle} price")
    amount_paise = amount * 100
    now = int(time.time())
    receipt = f"sme_{user['uid']}_{plan}_{now}"
    rp = _razorpay_create_order(amount_paise, receipt)
    order_id = rp["id"] if rp else f"order_mock_{receipt}_{secrets.token_hex(4)}"
    # Bind the order to user/plan/amount server-side; verify trusts only this row
    with db() as c:
        c.execute(
            """INSERT INTO billing_orders (order_id, user_id, plan, cycle, amount_paise, status, created_at)
               VALUES (?,?,?,?,?,'created',?)""",
            (order_id, user["uid"], plan, cycle, amount_paise, now),
        )
    if rp:  # real Razorpay order
        return {
            "mock": False, "key_id": RAZORPAY_KEY_ID, "order_id": order_id,
            "amount": rp["amount"], "currency": rp["currency"],
            "plan": plan, "cycle": cycle, "plan_name": idx[plan]["name"],
        }
    return {
        "mock": True, "key_id": None, "order_id": order_id,
        "amount": amount_paise, "currency": "INR",
        "plan": plan, "cycle": cycle, "plan_name": idx[plan]["name"],
    }

@app.post("/api/billing/verify")
def billing_verify(body: VerifyIn, user=Depends(current_user)):
    with db() as c:
        order = c.execute(
            "SELECT order_id, user_id, plan, cycle, amount_paise, status FROM billing_orders WHERE order_id=?",
            (body.razorpay_order_id,),
        ).fetchone()
    if not order or order["user_id"] != user["uid"]:
        raise HTTPException(404, "Order not found")
    if order["status"] != "created":
        raise HTTPException(409, "Order already processed")
    if RAZORPAY_MOCK:
        # Mock mode (server-side flag only): the order exists and belongs to
        # this user — accept without a signature. Never reachable with live keys.
        pass
    else:
        if not (body.razorpay_payment_id and body.razorpay_signature):
            raise HTTPException(400, "Missing payment confirmation fields")
        if not _verify_razorpay_signature(body.razorpay_order_id, body.razorpay_payment_id, body.razorpay_signature):
            raise HTTPException(400, "Payment signature verification failed")
    # Mark paid atomically — a replayed verify loses the UPDATE race
    with db() as c:
        cur = c.execute(
            "UPDATE billing_orders SET status='paid' WHERE order_id=? AND status='created'",
            (order["order_id"],),
        )
        if cur.rowcount == 0:
            raise HTTPException(409, "Order already processed")
    plan, cycle = order["plan"], order["cycle"]
    sub = _activate_subscription(user["uid"], plan, cycle,
                                 order["order_id"], body.razorpay_payment_id,
                                 order["amount_paise"] // 100)
    idx = _plan_index()
    return {"ok": True, "subscription": sub, "plan_detail": idx.get(plan, {"id": plan})}

@app.get("/api/admin/subscriptions")
def admin_subscriptions(x_admin_key: Optional[str] = Header(None)):
    _check_admin(x_admin_key)
    with db() as c:
        rows = c.execute(
            """SELECT s.user_id, u.email, u.name, s.plan, s.status, s.billing_cycle,
                      s.started_at, s.expires_at, s.amount, s.updated_at
               FROM subscriptions s LEFT JOIN users u ON u.id = s.user_id
               ORDER BY s.updated_at DESC"""
        ).fetchall()
    return [dict(r) for r in rows]

# ── ADMIN: executive dashboard · subscriber actions · billing · coupons · analytics ──
def _plan_price_map():
    out = {}
    for p in _get_plans():
        out[p.get("id")] = {"monthly": p.get("monthly", 0) or 0, "yearly": p.get("yearly", 0) or 0,
                            "name": p.get("name", p.get("id"))}
    return out

def _monthly_value(plan, cycle, prices):
    pm = prices.get(plan)
    if not pm:
        return 0
    return round((pm["yearly"] or 0) / 12.0) if cycle == "yearly" else (pm["monthly"] or 0)

def _module_total():
    with db() as c:
        n = c.execute("SELECT COUNT(*) n FROM modules").fetchone()["n"]
    return n or 63

@app.get("/api/admin/dashboard")
def admin_dashboard(x_admin_key: Optional[str] = Header(None)):
    _check_admin(x_admin_key)
    now = int(time.time()); d30 = now - 30 * 86400
    prices = _plan_price_map(); total_mods = _module_total()
    with db() as c:
        users_total = c.execute("SELECT COUNT(*) n FROM users").fetchone()["n"]
        new_30 = c.execute("SELECT COUNT(*) n FROM users WHERE created_at>=?", (d30,)).fetchone()["n"]
        subs = c.execute("SELECT plan, status, billing_cycle, expires_at FROM subscriptions").fetchall()
        certs = c.execute("SELECT COUNT(*) n FROM certificates").fetchone()["n"]
        orders = c.execute("SELECT amount_paise, created_at FROM billing_orders WHERE status='paid'").fetchall()
        prog = c.execute("SELECT data FROM progress").fetchall()
        sign = c.execute("SELECT created_at FROM users WHERE created_at>=?", (now - 13 * 86400,)).fetchall()
    active_paid = 0; mrr = 0; expired = 0; plan_dist = {}
    for s in subs:
        paid_active = s["plan"] != "free" and s["status"] == "active" and (not s["expires_at"] or s["expires_at"] >= now)
        if s["plan"] != "free" and s["status"] == "active" and s["expires_at"] and s["expires_at"] < now:
            expired += 1
        if paid_active:
            active_paid += 1
            mrr += _monthly_value(s["plan"], s["billing_cycle"] or "monthly", prices)
            plan_dist[s["plan"]] = plan_dist.get(s["plan"], 0) + 1
    plan_dist["free"] = max(0, users_total - active_paid)
    revenue_total = sum((o["amount_paise"] or 0) for o in orders) / 100.0
    rev_30 = sum((o["amount_paise"] or 0) for o in orders if o["created_at"] >= d30) / 100.0
    # learning
    learners = 0; pct_sum = 0.0; completed = 0; quizzes = 0
    for r in prog:
        try:
            data = json.loads(r["data"]); vis = len(data.get("visited") or []); quizzes += len(data.get("quizScores") or {})
        except Exception:
            vis = 0
        if vis > 0:
            learners += 1
            pct = min(1.0, vis / float(total_mods)); pct_sum += pct
            if pct >= 0.999:
                completed += 1
    avg_progress = round((pct_sum / learners) * 100) if learners else 0
    completion_rate = round((completed / learners) * 100) if learners else 0
    # 14-day series (signups + revenue), oldest→newest
    days = []
    for i in range(13, -1, -1):
        day = now - i * 86400; start = day - (day % 86400)
        days.append({"t": start, "signups": 0, "revenue": 0})
    def _bucket(ts):
        for b in days:
            if b["t"] <= ts < b["t"] + 86400:
                return b
        return None
    for s in sign:
        b = _bucket(s["created_at"]);  b and b.__setitem__("signups", b["signups"] + 1)
    for o in orders:
        b = _bucket(o["created_at"]);  b and b.__setitem__("revenue", b["revenue"] + (o["amount_paise"] or 0) / 100.0)
    churn_rate = round((expired / (active_paid + expired)) * 100) if (active_paid + expired) else 0
    return {
        "subscribers": {"total": users_total, "paid": active_paid, "free": plan_dist["free"], "new_30": new_30},
        "revenue": {"mrr": mrr, "arr": mrr * 12, "total": round(revenue_total), "last_30": round(rev_30)},
        "learning": {"learners": learners, "avg_progress": avg_progress, "completion_rate": completion_rate,
                     "certs": certs, "quizzes": quizzes, "modules_total": total_mods},
        "churn": {"expired": expired, "rate": churn_rate},
        "plan_distribution": plan_dist,
        "series": days,
        "mock_payments": RAZORPAY_MOCK,
    }

@app.get("/api/admin/users/{uid}")
def admin_user_detail(uid: int, x_admin_key: Optional[str] = Header(None)):
    _check_admin(x_admin_key)
    with db() as c:
        u = c.execute("SELECT * FROM users WHERE id=?", (uid,)).fetchone()
        if not u:
            raise HTTPException(404, "User not found")
        pr = c.execute("SELECT data, updated_at FROM progress WHERE user_id=?", (uid,)).fetchone()
        cert = c.execute("SELECT cert_id, issued_at, modules_visited, modules_total FROM certificates WHERE user_id=?", (uid,)).fetchone()
        orders = c.execute("SELECT order_id, plan, cycle, amount_paise, status, created_at FROM billing_orders WHERE user_id=? ORDER BY created_at DESC", (uid,)).fetchall()
    visited = 0; quizzes = 0
    if pr:
        try:
            data = json.loads(pr["data"]); visited = len(data.get("visited") or []); quizzes = len(data.get("quizScores") or {})
        except Exception:
            pass
    return {"id": u["id"], "created_at": u["created_at"], "user": _user_public(u),
            "subscription": _get_subscription(uid),
            "progress": {"visited": visited, "quizzes": quizzes,
                         "modules_total": _module_total(),
                         "updated_at": pr["updated_at"] if pr else None},
            "certificate": dict(cert) if cert else None,
            "orders": [dict(o) for o in orders]}

class SubActionIn(BaseModel):
    action: str
    plan: Optional[str] = None
    cycle: Optional[str] = "yearly"
    days: Optional[int] = None

@app.post("/api/admin/users/{uid}/subscription")
def admin_set_subscription(uid: int, body: SubActionIn, x_admin_key: Optional[str] = Header(None)):
    _check_admin(x_admin_key)
    now = int(time.time())
    with db() as c:
        if not c.execute("SELECT id FROM users WHERE id=?", (uid,)).fetchone():
            raise HTTPException(404, "User not found")
    act = body.action
    if act == "set":
        plan = body.plan or "free"
        if plan == "free":
            with db() as c:
                c.execute("""INSERT INTO subscriptions (user_id, plan, status, updated_at) VALUES (?, 'free', 'active', ?)
                             ON CONFLICT(user_id) DO UPDATE SET plan='free', status='active',
                               billing_cycle=NULL, expires_at=NULL, updated_at=?""", (uid, now, now))
        else:
            cycle = body.cycle if body.cycle in ("monthly", "yearly") else "yearly"
            amt = _plan_price_map().get(plan, {}).get(cycle, 0)
            _activate_subscription(uid, plan, cycle, "admin-grant", "admin-grant", amt)
    elif act == "extend":
        days = int(body.days or 30)
        with db() as c:
            row = c.execute("SELECT plan, expires_at FROM subscriptions WHERE user_id=?", (uid,)).fetchone()
        if not row or row["plan"] == "free":
            raise HTTPException(400, "No paid plan to extend")
        base = max(row["expires_at"] or now, now)
        with db() as c:
            c.execute("UPDATE subscriptions SET expires_at=?, status='active', updated_at=? WHERE user_id=?",
                      (base + days * 86400, now, uid))
    elif act in ("suspend", "cancel"):
        st = "suspended" if act == "suspend" else "cancelled"
        with db() as c:
            c.execute("UPDATE subscriptions SET status=?, updated_at=? WHERE user_id=?", (st, now, uid))
    elif act == "resume":
        with db() as c:
            c.execute("UPDATE subscriptions SET status='active', updated_at=? WHERE user_id=?", (now, uid))
    else:
        raise HTTPException(400, "Unknown action")
    return {"ok": True, "subscription": _get_subscription(uid)}

@app.post("/api/admin/users/{uid}/reset-password")
def admin_reset_password(uid: int, x_admin_key: Optional[str] = Header(None)):
    _check_admin(x_admin_key)
    temp = "Sme-" + secrets.token_hex(4)
    ph, salt = hash_password(temp)
    with db() as c:
        n = c.execute("UPDATE users SET pass_hash=?, salt=? WHERE id=?", (ph, salt, uid)).rowcount
    if not n:
        raise HTTPException(404, "User not found")
    return {"ok": True, "temp_password": temp}

@app.post("/api/admin/users/{uid}/impersonate")
def admin_impersonate(uid: int, x_admin_key: Optional[str] = Header(None)):
    _check_admin(x_admin_key)
    with db() as c:
        u = c.execute("SELECT id, email FROM users WHERE id=?", (uid,)).fetchone()
    if not u:
        raise HTTPException(404, "User not found")
    return {"ok": True, "token": make_token(u["id"], u["email"]), "email": u["email"]}

@app.delete("/api/admin/users/{uid}")
def admin_delete_user(uid: int, x_admin_key: Optional[str] = Header(None)):
    _check_admin(x_admin_key)
    with db() as c:
        c.execute("DELETE FROM progress WHERE user_id=?", (uid,))
        c.execute("DELETE FROM subscriptions WHERE user_id=?", (uid,))
        c.execute("DELETE FROM certificates WHERE user_id=?", (uid,))
        c.execute("DELETE FROM billing_orders WHERE user_id=?", (uid,))
        n = c.execute("DELETE FROM users WHERE id=?", (uid,)).rowcount
    if not n:
        raise HTTPException(404, "User not found")
    return {"ok": True}

@app.get("/api/admin/orders")
def admin_orders(x_admin_key: Optional[str] = Header(None)):
    _check_admin(x_admin_key)
    with db() as c:
        rows = c.execute("""SELECT o.order_id, o.user_id, u.email, u.name, u.gst, o.plan, o.cycle,
                                   o.amount_paise, o.status, o.created_at
                            FROM billing_orders o LEFT JOIN users u ON u.id = o.user_id
                            ORDER BY o.created_at DESC LIMIT 500""").fetchall()
    return [dict(r) for r in rows]

class CouponIn(BaseModel):
    code: str
    percent_off: int = 0
    plan: Optional[str] = None
    max_redemptions: int = 0
    expires_at: Optional[int] = None

@app.get("/api/admin/coupons")
def admin_coupons(x_admin_key: Optional[str] = Header(None)):
    _check_admin(x_admin_key)
    with db() as c:
        rows = c.execute("SELECT * FROM coupons ORDER BY created_at DESC").fetchall()
    return [dict(r) for r in rows]

@app.post("/api/admin/coupons")
def admin_create_coupon(body: CouponIn, x_admin_key: Optional[str] = Header(None)):
    _check_admin(x_admin_key)
    code = (body.code or "").strip().upper()
    if not code:
        raise HTTPException(400, "Coupon code is required")
    pct = max(0, min(100, int(body.percent_off or 0)))
    now = int(time.time())
    with db() as c:
        c.execute("""INSERT INTO coupons (code, percent_off, plan, max_redemptions, redeemed, expires_at, active, created_at)
                     VALUES (?,?,?,?,0,?,1,?)
                     ON CONFLICT(code) DO UPDATE SET percent_off=excluded.percent_off, plan=excluded.plan,
                       max_redemptions=excluded.max_redemptions, expires_at=excluded.expires_at, active=1""",
                  (code, pct, body.plan or None, int(body.max_redemptions or 0), body.expires_at, now))
    return {"ok": True, "code": code}

@app.delete("/api/admin/coupons/{code}")
def admin_delete_coupon(code: str, x_admin_key: Optional[str] = Header(None)):
    _check_admin(x_admin_key)
    with db() as c:
        c.execute("DELETE FROM coupons WHERE code=?", ((code or "").strip().upper(),))
    return {"ok": True}

@app.get("/api/admin/analytics")
def admin_analytics(x_admin_key: Optional[str] = Header(None)):
    _check_admin(x_admin_key)
    with db() as c:
        pop = c.execute("""SELECT module_id, COUNT(*) n FROM events
                           WHERE module_id IS NOT NULL AND module_id<>'' GROUP BY module_id
                           ORDER BY n DESC LIMIT 10""").fetchall()
        src = c.execute("""SELECT COALESCE(NULLIF(utm_source,''), NULLIF(referrer_host,''), 'Direct') s, COUNT(*) n
                           FROM events GROUP BY s ORDER BY n DESC LIMIT 8""").fetchall()
        bt = c.execute("SELECT COALESCE(NULLIF(business_type,''),'Unspecified') t, COUNT(*) n FROM users GROUP BY t ORDER BY n DESC LIMIT 8").fetchall()
        mk = c.execute("SELECT COALESCE(NULLIF(marketplace,''),'Unspecified') t, COUNT(*) n FROM users GROUP BY t ORDER BY n DESC LIMIT 8").fetchall()
        titles = {r["id"]: r["title"] for r in c.execute("SELECT id, title FROM modules").fetchall()}
    return {
        "popular_modules": [{"id": r["module_id"], "title": titles.get(r["module_id"], r["module_id"]), "count": r["n"]} for r in pop],
        "lead_sources": [{"source": r["s"], "count": r["n"]} for r in src],
        "business_types": [{"label": r["t"], "count": r["n"]} for r in bt],
        "marketplaces": [{"label": r["t"], "count": r["n"]} for r in mk],
    }

def _ago(sec: int) -> str:
    sec = max(0, int(sec))
    if sec < 3600: return f"{sec // 60}m ago"
    if sec < 86400: return f"{sec // 3600}h ago"
    return f"{sec // 86400}d ago"

@app.get("/api/admin/notifications")
def admin_notifications(x_admin_key: Optional[str] = Header(None)):
    _check_admin(x_admin_key)
    now = int(time.time()); items = []
    with db() as c:
        for r in c.execute("SELECT id, name, email, created_at FROM users WHERE created_at>=? ORDER BY created_at DESC LIMIT 8", (now - 2 * 86400,)).fetchall():
            items.append({"type": "signup", "text": (r["name"] or r["email"]) + " signed up", "sub": _ago(now - r["created_at"]), "tab": "users", "uid": r["id"], "t": r["created_at"]})
        for r in c.execute("SELECT plan, amount_paise, status, created_at FROM billing_orders WHERE status IN ('created','failed') ORDER BY created_at DESC LIMIT 8").fetchall():
            items.append({"type": "payment", "text": f"Payment {r['status']} · {r['plan']} (₹{(r['amount_paise'] or 0)//100})", "sub": _ago(now - r["created_at"]), "tab": "invoices", "t": r["created_at"]})
        for r in c.execute("SELECT name, issued_at FROM certificates WHERE issued_at>=? ORDER BY issued_at DESC LIMIT 6", (now - 7 * 86400,)).fetchall():
            items.append({"type": "cert", "text": (r["name"] or "A learner") + " earned a certificate", "sub": _ago(now - r["issued_at"]), "tab": "certificates", "t": r["issued_at"]})
        for r in c.execute("""SELECT s.user_id, u.email, u.name, s.plan, s.expires_at FROM subscriptions s LEFT JOIN users u ON u.id=s.user_id
                              WHERE s.plan<>'free' AND s.status='active' AND s.expires_at IS NOT NULL AND s.expires_at>? AND s.expires_at<?
                              ORDER BY s.expires_at ASC LIMIT 8""", (now, now + 7 * 86400)).fetchall():
            days = max(0, (r["expires_at"] - now) // 86400)
            items.append({"type": "expiry", "text": f"{r['name'] or r['email'] or 'A subscriber'}'s {r['plan']} expires in {days}d", "sub": "renewal due", "tab": "users", "uid": r["user_id"], "t": r["expires_at"]})
    items.sort(key=lambda x: x["t"], reverse=True)
    return {"count": len(items), "items": items[:20]}

# ── ADMIN: editable config (plans / paywall / pillars / content) ──
class ConfigIn(BaseModel):
    value: Any

@app.get("/api/admin/config")
def admin_get_config(x_admin_key: Optional[str] = Header(None)):
    """Everything the admin editor needs, with defaults applied."""
    _check_admin(x_admin_key)
    return {
        "plans": _get_plans(),
        "paywall": _get_paywall_config(),
        "pillars": _get_pillars(),
        "content": _get_content(),
        "defaults": {
            "plans": DEFAULT_PLANS, "paywall": DEFAULT_PAYWALL,
            "pillars": DEFAULT_PILLARS, "content": DEFAULT_CONTENT,
        },
        "mock_payments": RAZORPAY_MOCK,
    }

@app.put("/api/admin/plans")
def admin_save_plans(body: ConfigIn, x_admin_key: Optional[str] = Header(None)):
    _check_admin(x_admin_key)
    if not isinstance(body.value, list) or not body.value:
        raise HTTPException(400, "Plans must be a non-empty list")
    for p in body.value:
        if not isinstance(p, dict) or "id" not in p or "name" not in p:
            raise HTTPException(400, "Each plan needs at least id and name")
        p["monthly"] = int(p.get("monthly", 0) or 0)
        p["yearly"] = int(p.get("yearly", 0) or 0)
    _set_config("plans", body.value)
    return {"ok": True, "plans": _get_plans()}

@app.put("/api/admin/paywall")
def admin_save_paywall(body: ConfigIn, x_admin_key: Optional[str] = Header(None)):
    _check_admin(x_admin_key)
    if not isinstance(body.value, dict):
        raise HTTPException(400, "Paywall config must be an object")
    merged = dict(DEFAULT_PAYWALL)
    for k in DEFAULT_PAYWALL:
        if k in body.value:
            try:
                merged[k] = int(body.value[k])
            except Exception:
                pass
    _set_config("paywall", merged)
    return {"ok": True, "paywall": merged}

@app.put("/api/admin/pillars")
def admin_save_pillars(body: ConfigIn, x_admin_key: Optional[str] = Header(None)):
    _check_admin(x_admin_key)
    if not isinstance(body.value, list) or not body.value:
        raise HTTPException(400, "Pillars must be a non-empty list")
    for p in body.value:
        if not isinstance(p, dict) or "p" not in p:
            raise HTTPException(400, "Each pillar needs a 'p' id (e.g. p1)")
        p["sops"] = int(p.get("sops", 0) or 0)
        p["hours"] = int(p.get("hours", 0) or 0)
    _set_config("pillars", body.value)
    return {"ok": True, "pillars": _get_pillars()}

@app.put("/api/admin/content")
def admin_save_content(body: ConfigIn, x_admin_key: Optional[str] = Header(None)):
    _check_admin(x_admin_key)
    if not isinstance(body.value, dict):
        raise HTTPException(400, "Content must be an object")
    merged = dict(DEFAULT_CONTENT)
    for k, v in body.value.items():
        if k == "stats":
            if not isinstance(v, list) or not all(
                isinstance(s, dict) and "label" in s and "value" in s for s in v
            ):
                raise HTTPException(400, "stats must be a list of {label, value[, suffix]} objects")
        elif not isinstance(v, str):
            raise HTTPException(400, f"Content field '{k}' must be a string")
        merged[k] = v
    _set_config("content", merged)
    return {"ok": True, "content": merged}

# ── ADMIN UI ──────────────────────────────────────────────────
@app.get("/admin", include_in_schema=False)
def admin_ui():
    return FileResponse(os.path.join(BASE, "admin.html"))

@app.get("/cert-preview", include_in_schema=False)
def cert_preview():
    return FileResponse(os.path.join(BASE, "cert-preview.html"))

@app.get("/logo.jpg", include_in_schema=False)
def logo():
    candidates = [
        r"K:\Project Krishna_2026\Logo\Final Logos\SMEMinds Logo.jpeg",
        r"K:\Official\4. SME-Minds.com\Marketing\Logo\Final Logos\SMEMinds Logo.jpeg",
        r"C:\Users\kunda\OneDrive\Desktop\SMEMinds Logo.jpeg",
    ]
    for c in candidates:
        if os.path.exists(c):
            return FileResponse(c, media_type="image/jpeg")
    # Fall back to the playbook's cached base64 copy
    cache = os.path.join(os.path.dirname(BASE), "src", "logo_b64.txt")
    if os.path.exists(cache):
        import base64
        from fastapi.responses import Response
        with open(cache) as f:
            b64 = f.read().strip()
        return Response(content=base64.b64decode(b64), media_type="image/jpeg")
    raise HTTPException(404, "Logo not available")

@app.get("/", include_in_schema=False)
def root():
    return {"ok": True, "service": "SMEMinds Playbook API", "admin_ui": "/admin", "docs": "/docs"}
