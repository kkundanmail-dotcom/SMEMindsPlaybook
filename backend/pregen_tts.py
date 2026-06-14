"""
Pre-generate ALL module-video narration once with Sarvam (Ritu + Shubh) and
store it in the same on-disk cache the /api/tts proxy reads from. After this runs,
every video plays from cache — the Sarvam API is never called again (no recurring
credits). Run it ONE time after saving your Sarvam key in /admin (or SARVAM_API_KEY).

    cd backend
    python pregen_tts.py            # both voices
    python pregen_tts.py ritu       # one voice only
"""
import os, sys, re, json, time, hashlib, sqlite3
import urllib.request, urllib.error

BASE = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE, "smeminds.db")
CACHE_DIR = os.path.join(BASE, ".tts_cache")
SARVAM_URL = "https://api.sarvam.ai/text-to-speech"
DEFAULT_MODEL = "bulbul:v3"
VOICES = ["ritu", "shubh"]          # matches SARVAM_VOICES in main.py

def clean(t):                       # mirrors clean() in src/video.js
    t = re.sub(r"\s*\|\s*", " ", t or "")
    return re.sub(r"\s+", " ", t).strip()

def resolve_key_model():
    """Admin-saved key wins, else env var — same precedence as the backend."""
    key, model = "", ""
    try:
        with sqlite3.connect(DB_PATH) as c:
            row = c.execute("SELECT value FROM app_config WHERE key='sarvam'").fetchone()
        if row:
            cfg = json.loads(row[0])
            key = (cfg.get("key") or "").strip()
            model = (cfg.get("model") or "").strip()
    except Exception:
        pass
    key = key or os.environ.get("SARVAM_API_KEY", "").strip()
    model = model or os.environ.get("SARVAM_TTS_MODEL", "").strip() or DEFAULT_MODEL
    return key, model

def collect_texts():
    """Every distinct narration line the player will request, per module."""
    with sqlite3.connect(DB_PATH) as c:
        c.row_factory = sqlite3.Row
        rows = c.execute("SELECT data FROM modules ORDER BY pillar, id").fetchall()
    texts = []
    for r in rows:
        m = json.loads(r["data"])
        vs = m.get("video_script") or {}
        scenes = vs.get("scenes") or []
        if not scenes:
            continue
        texts.append(clean((m.get("title", "") + ". | " + vs.get("tagline", ""))))  # intro
        for sc in scenes:
            texts.append(clean(sc.get("vo", "")))                                    # scene
        texts.append(clean(vs.get("cta", "")))                                       # outro
    # de-dupe, drop empties
    seen, out = set(), []
    for t in texts:
        if t and t not in seen:
            seen.add(t); out.append(t)
    return out

def cache_path(model, speaker, text):
    key = hashlib.sha256((model + "|" + speaker + "|" + text).encode()).hexdigest()
    return os.path.join(CACHE_DIR, key + ".txt")

def synth(key, model, speaker, text):
    payload = json.dumps({
        "text": text, "target_language_code": "en-IN", "model": model,
        "speaker": speaker, "output_audio_codec": "mp3", "pace": 1.0,
    }).encode()
    req = urllib.request.Request(SARVAM_URL, data=payload, method="POST",
        headers={"Content-Type": "application/json", "api-subscription-key": key})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=40) as resp:
                data = json.loads(resp.read().decode())
            audios = data.get("audios") or []
            if not audios:
                raise RuntimeError("no audio in response")
            return audios[0]
        except urllib.error.HTTPError as e:
            body = e.read().decode()[:160]
            if e.code in (429, 500, 502, 503) and attempt < 3:
                wait = 2 ** attempt
                print(f"   {e.code}, retrying in {wait}s")
                time.sleep(wait); continue
            raise RuntimeError(f"HTTP {e.code}: {body}")
        except Exception as e:
            if attempt < 3:
                time.sleep(2 ** attempt); continue
            raise

def main():
    voices = [v for v in sys.argv[1:] if v in VOICES] or VOICES
    key, model = resolve_key_model()
    if not key:
        print("ERROR: No Sarvam API key found.")
        print("  → Save it in the admin panel (AI Voice tab) or set SARVAM_API_KEY, then re-run.")
        sys.exit(1)
    os.makedirs(CACHE_DIR, exist_ok=True)
    texts = collect_texts()
    total = len(texts) * len(voices)
    chars = sum(len(t) for t in texts) * len(voices)
    print(f"Model: {model}  |  Voices: {', '.join(voices)}")
    print(f"Lines per voice: {len(texts)}  |  Total clips: {total}  |  ~{chars:,} characters (one-time)")
    print("-" * 56)
    made = cached = failed = 0
    t0 = time.time()
    for spk in voices:
        for i, text in enumerate(texts):
            p = cache_path(model, spk, text)
            if os.path.exists(p):
                cached += 1; continue
            try:
                b64 = synth(key, model, spk, text)
                with open(p, "w") as f:
                    f.write(b64)
                made += 1
                if made % 20 == 0:
                    print(f"  {spk}: {made} generated, {cached} cached")
                time.sleep(0.15)            # be polite to the API
            except Exception as e:
                failed += 1
                print(f"  ! {spk} failed on: {text[:50]!r} — {e}")
    dt = int(time.time() - t0)
    print("-" * 56)
    print(f"Done in {dt}s.  Generated: {made}  |  Already cached: {cached}  |  Failed: {failed}")
    print(f"Cache: {CACHE_DIR}")
    if failed == 0:
        print("[OK] All narration is cached. Playback will NOT use any further API credits.")
    else:
        print("Some clips failed — re-run to fill the gaps (cached ones are skipped).")

if __name__ == "__main__":
    main()
