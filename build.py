import os
import re
import sys
import base64
import html as html_mod
from io import BytesIO

BASE = os.path.dirname(os.path.abspath(__file__))

REQUIRED_SOURCES = ['template.html', 'style.css', 'app.js', 'tools.js', 'video.js', 'tools.html']

# Display size is <=220px wide (sidebar/login/footer); certificate prints up to
# ~A4. 880px wide covers 2x retina + print without shipping a 5692px original.
LOGO_MAX_WIDTH = 880
LOGO_JPEG_QUALITY = 82
FAVICON_SIZE = 64

def read_file(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Required build input missing: {filepath}")
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def _optimize_logo(raw: bytes):
    """Downscale + recompress the logo; also derive a small PNG favicon.
    Returns (logo_b64, favicon_b64). Falls back to the original bytes if
    Pillow is unavailable."""
    try:
        from PIL import Image
    except ImportError:
        print("  (Pillow not installed — embedding original logo unresized)")
        return base64.b64encode(raw).decode(), ""
    im = Image.open(BytesIO(raw)).convert("RGB")
    if im.width > LOGO_MAX_WIDTH:
        im = im.resize((LOGO_MAX_WIDTH, round(im.height * LOGO_MAX_WIDTH / im.width)),
                       Image.LANCZOS)
    buf = BytesIO()
    im.save(buf, "JPEG", quality=LOGO_JPEG_QUALITY, optimize=True)
    logo_b64 = base64.b64encode(buf.getvalue()).decode()

    fav = im.copy()
    fav.thumbnail((FAVICON_SIZE, FAVICON_SIZE), Image.LANCZOS)
    fbuf = BytesIO()
    fav.save(fbuf, "PNG", optimize=True)
    favicon_b64 = base64.b64encode(fbuf.getvalue()).decode()
    return logo_b64, favicon_b64

def get_logo_assets():
    """Returns (logo_data_uri, favicon_data_uri).
    Priority: official K: drive > Desktop fallback > cached b64 (offline)."""
    official_jpg = r'K:\Official\4. SME-Minds.com\Marketing\Logo\Final Logos\SMEMinds Logo.jpeg'
    desktop_jpg  = r'C:\Users\kunda\OneDrive\Desktop\SMEMinds Logo.jpeg'
    cache_logo   = os.path.join(BASE, 'src', 'logo_b64.txt')
    cache_fav    = os.path.join(BASE, 'src', 'favicon_b64.txt')

    for src in [official_jpg, desktop_jpg]:
        if os.path.exists(src):
            with open(src, 'rb') as f:
                raw = f.read()
            logo_b64, favicon_b64 = _optimize_logo(raw)
            with open(cache_logo, 'w') as f:
                f.write(logo_b64)
            if favicon_b64:
                with open(cache_fav, 'w') as f:
                    f.write(favicon_b64)
            print(f"  Logo loaded from: {src} ({len(logo_b64)//1024} KB embedded)")
            return (f"data:image/jpeg;base64,{logo_b64}",
                    f"data:image/png;base64,{favicon_b64}" if favicon_b64 else "")

    logo_uri, fav_uri = "", ""
    if os.path.exists(cache_logo):
        with open(cache_logo) as f:
            logo_uri = "data:image/jpeg;base64," + f.read().strip()
        print("  Logo loaded from cache (logo_b64.txt)")
    if os.path.exists(cache_fav):
        with open(cache_fav) as f:
            fav_uri = "data:image/png;base64," + f.read().strip()
    return logo_uri, fav_uri

def get_ai_icon():
    """SMEMinds AI Assistant avatar + matching favicon from the brand icon.
    Returns (avatar_uri[128px], favicon_uri[64px]). Priority: K: drive > cache."""
    src_png   = r'K:\Project Krishna_2026\Logo\Final Logos\Icon Logo.png'
    cache     = os.path.join(BASE, 'src', 'ai_icon_b64.txt')
    cache_fav = os.path.join(BASE, 'src', 'ai_favicon_b64.txt')

    def uri(b):
        return f"data:image/png;base64,{b}"

    if os.path.exists(src_png):
        try:
            from PIL import Image
            base = Image.open(src_png).convert('RGBA')
            av = base.copy(); av.thumbnail((128, 128), Image.LANCZOS)
            b1 = BytesIO(); av.save(b1, 'PNG', optimize=True)
            avatar_b64 = base64.b64encode(b1.getvalue()).decode()
            fav = base.copy(); fav.thumbnail((64, 64), Image.LANCZOS)
            b2 = BytesIO(); fav.save(b2, 'PNG', optimize=True)
            fav_b64 = base64.b64encode(b2.getvalue()).decode()
        except ImportError:
            with open(src_png, 'rb') as f:
                avatar_b64 = fav_b64 = base64.b64encode(f.read()).decode()
        with open(cache, 'w') as f: f.write(avatar_b64)
        with open(cache_fav, 'w') as f: f.write(fav_b64)
        print(f"  AI icon loaded from: {src_png} (avatar {len(avatar_b64)//1024} KB, favicon {len(fav_b64)//1024} KB)")
        return uri(avatar_b64), uri(fav_b64)

    avatar_uri = fav_uri = ""
    if os.path.exists(cache):
        with open(cache) as f: avatar_uri = uri(f.read().strip())
        print("  AI icon loaded from cache (ai_icon_b64.txt)")
    if os.path.exists(cache_fav):
        with open(cache_fav) as f: fav_uri = uri(f.read().strip())
    return avatar_uri, fav_uri

def get_outro_video():
    """Animated SMEMinds logo MP4 played at the end of every module video.
    Embedded once (shared); base64 data URI. Priority: K: drive > cache."""
    src = r'K:\Project Krishna_2026\Logo\Final Logos\Animated Logo_2.mp4'
    cache = os.path.join(BASE, 'src', 'outro_video_b64.txt')
    if os.path.exists(src):
        with open(src, 'rb') as f:
            b64 = base64.b64encode(f.read()).decode()
        with open(cache, 'w') as f:
            f.write(b64)
        print(f"  Outro logo video embedded: {len(b64)//1024} KB base64 (from {src})")
        return "data:video/mp4;base64," + b64
    if os.path.exists(cache):
        with open(cache) as f:
            print("  Outro logo video from cache (outro_video_b64.txt)")
            return "data:video/mp4;base64," + f.read().strip()
    print("  (No outro video found — videos will end on the CTA card)")
    return ""

def load_modules_from_db():
    """If backend DB exists and has modules, use those (lets admin edits show up)."""
    import sqlite3, json
    db_path = os.path.join(BASE, "backend", "smeminds.db")
    if not os.path.exists(db_path):
        return None
    try:
        with sqlite3.connect(db_path) as c:
            c.row_factory = sqlite3.Row
            rows = c.execute("SELECT data FROM modules ORDER BY pillar, id").fetchall()
        if not rows:
            return None
        return [json.loads(r["data"]) for r in rows]
    except Exception as e:
        print(f"  (DB read failed, falling back to content_*.py: {e})")
        return None

def load_all_modules():
    db_modules = load_modules_from_db()
    if db_modules:
        print(f"  SOURCE: backend DB (smeminds.db) — {len(db_modules)} modules")
        print(f"  NOTE: content_*.py edits are IGNORED while the DB has modules; edit via /admin")
        return db_modules
    try:
        from content_1 import pillar1_modules
        from content_2 import pillar2_modules
        from content_3 import pillar3_modules
        from content_4 import pillar4_modules
        from content_5 import pillar5_modules
        from content_6 import pillar6_modules
        from content_7 import pillar7_modules
        from content_8 import pillar8_modules
        from content_9 import pillar9_modules
    except Exception as e:
        print(f"FATAL: could not import content files: {e}")
        sys.exit(1)
    mods = (pillar1_modules + pillar2_modules + pillar3_modules +
            pillar4_modules + pillar5_modules + pillar6_modules +
            pillar7_modules + pillar8_modules + pillar9_modules)
    print(f"  SOURCE: content_*.py — {len(mods)} modules")
    return mods

# Pillar accent colours (kept in sync with backend DEFAULT_PILLARS; the DB
# app_config copy wins when present so admin colour edits flow through)
_PILLAR_COLORS_DEFAULT = {
    "p1": "#10b981", "p2": "#ff6b35", "p3": "#6366f1", "p4": "#3b82f6",
    "p5": "#22c55e", "p6": "#f59e0b", "p7": "#8b5cf6", "p8": "#ec4899", "p9": "#ef4444",
}

def get_pillar_colors():
    import sqlite3, json
    db_path = os.path.join(BASE, "backend", "smeminds.db")
    colors = dict(_PILLAR_COLORS_DEFAULT)
    if os.path.exists(db_path):
        try:
            with sqlite3.connect(db_path) as c:
                row = c.execute("SELECT value FROM app_config WHERE key='pillars'").fetchone()
            if row:
                for p in json.loads(row[0]):
                    if p.get("p") and p.get("color"):
                        colors[p["p"]] = p["color"]
        except Exception:
            pass
    return colors

def _hex_to_rgba(hex_color, alpha):
    h = hex_color.lstrip("#")
    if len(h) != 6:
        return f"rgba(255,107,53,{alpha})"
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return f"rgba({r},{g},{b},{alpha})"

_PFLOW_ARROW = (
    "<span class='pflow-arrow' aria-hidden='true'>"
    "<svg width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='currentColor' "
    "stroke-width='2.5' stroke-linecap='round' stroke-linejoin='round'>"
    "<path d='M5 12h14'/><path d='m13 6 6 6-6 6'/></svg></span>"
)

def modernize_process_flow(pf, accent):
    """Convert the legacy fixed-860px SVG step strips into a responsive HTML
    component (numbered cards + arrows; stacks vertically on phones).
    Returns the original markup untouched whenever the SVG doesn't match the
    generated single-row pattern — never breaks unknown content."""
    if not pf or "<svg" not in pf or "flow-step" not in pf:
        return pf
    try:
        rect_tags = [t for t in re.findall(r"<rect[^>]*>", pf) if "flow-step" in t]
        steps = []
        for tag in rect_tags:
            x = re.search(r'\bx="([\d.]+)"', tag)
            w = re.search(r'width="([\d.]+)"', tag)
            if not x or not w:
                return pf
            fill = re.search(r'style="[^"]*fill:\s*(#[0-9a-fA-F]{6})', tag)
            steps.append({"x0": float(x.group(1)), "x1": float(x.group(1)) + float(w.group(1)),
                          "accent": fill.group(1) if fill else None, "lines": []})
        if not steps:
            return pf
        steps.sort(key=lambda s: s["x0"])
        for tag, content in re.findall(r"(<text[^>]*class=\"flow-text\"[^>]*>)([^<]*)</text>", pf):
            tx = re.search(r'\bx="([\d.]+)"', tag)
            if not tx:
                return pf
            xv = float(tx.group(1))
            home = next((s for s in steps if s["x0"] - 2 <= xv <= s["x1"] + 2), None)
            if home is None:
                return pf
            home["lines"].append(content.strip())
        if any(not s["lines"] for s in steps):
            return pf

        cards = []
        for i, s in enumerate(steps):
            label = " ".join(s["lines"])
            goal = ' pflow-goal' if s["accent"] else ''
            style = f" style=\"--pf:{s['accent']};--pf-tint:{_hex_to_rgba(s['accent'], 0.13)}\"" if s["accent"] else ""
            cards.append(
                f"<div class='pflow-step{goal}'{style}>"
                f"<span class='pflow-num'>{i + 1}</span>"
                f"<span class='pflow-label'>{label}</span></div>"
            )
        track = _PFLOW_ARROW.join(cards)
        return (
            f"<div class='pflow' style=\"--pf:{accent};--pf-tint:{_hex_to_rgba(accent, 0.13)}\">"
            f"<span class='pflow-eyebrow'>Process Flow</span>"
            f"<div class='pflow-track'>{track}</div></div>"
        )
    except Exception:
        return pf

_TABLE_RE = re.compile(r'<table\b.*?</table>', re.S | re.I)

def wrap_tables(markup):
    """Wrap each content table in a horizontally-scrollable container so wide
    tables scroll instead of breaking the layout on phones."""
    if not markup or '<table' not in markup:
        return markup
    return _TABLE_RE.sub(lambda m: '<div class="table-wrap">' + m.group(0) + '</div>', markup)

def generate_modules(all_modules):
    esc = lambda s: html_mod.escape(str(s), quote=True)
    html = ""
    quiz_warnings = []
    pillar_colors = get_pillar_colors()
    flows_converted = 0

    for m in all_modules:
        # Difficulty badge class
        diff_lower = m.get('difficulty','').lower()
        diff_class = 'badge-beginner' if diff_lower=='beginner' else \
                     'badge-intermediate' if diff_lower=='intermediate' else \
                     'badge-advanced' if diff_lower=='advanced' else 'badge-expert'

        # Tools section
        tools_html = m.get('tools','')

        # Videos section — YouTube card links (no embed = no Error 153)
        # Amazon Seller University videos have embedding disabled by channel owner.
        video_html = ""
        videos = m.get('videos', [])
        if videos:
            cards = ""
            for v in videos:
                vid_id  = v["id"]
                vid_title = esc(v["title"])
                cards += (
                    "<a class='yt-card' href='https://www.youtube.com/watch?v=" + vid_id + "' target='_blank' rel='noopener'>"
                    "<div class='yt-card-thumb'>"
                    "<img src='https://img.youtube.com/vi/" + vid_id + "/mqdefault.jpg' "
                    "alt='" + vid_title + "' loading='lazy' "
                    "onerror=\"this.parentElement.style.background='#1e3a5f'\">"
                    "<div class='yt-card-play'>"
                    "<svg viewBox='0 0 68 48' xmlns='http://www.w3.org/2000/svg' width='44' height='31'>"
                    "<path d='M66.5 7.7c-.8-2.9-3-5.2-5.9-6C55.8 0 34 0 34 0S12.2 0 7.4 1.7c-2.9.8-5.1 3.1-5.9 6C0 12.5 0 24 0 24s0 11.5 1.5 16.3c.8 2.9 3 5.2 5.9 6C12.2 48 34 48 34 48s21.8 0 26.6-1.7c2.9-.8 5.1-3.1 5.9-6C68 35.5 68 24 68 24s0-11.5-1.5-16.3z' fill='#ff0000' fill-opacity='0.9'/>"
                    "<path d='M45 24 27 14v20' fill='#fff'/>"
                    "</svg>"
                    "</div>"
                    "</div>"
                    "<div class='yt-card-info'>"
                    "<span class='yt-card-label'>Amazon Seller University</span>"
                    "<p class='yt-card-title'>" + vid_title + "</p>"
                    "<span class='yt-card-cta'>Watch on YouTube &nbsp;↗</span>"
                    "</div>"
                    "</a>"
                )
            video_html = (
                "<div class='video-container'>"
                "<h4>Related Videos</h4>"
                "<div class='yt-cards'>" + cards + "</div>"
                "</div>"
            )

        # Checklist — class names must be dot-free so querySelectorAll works
        checklist_html = ""
        checklist = m.get('checklist', [])
        mid = m['id']
        mid_cls = mid.replace('.', '_')
        if checklist:
            items = ""
            for c in checklist:
                items += "<li><label><input type='checkbox' class='chk_" + mid_cls + "' onchange='updateChecklist(\"" + mid + "\")'> " + c + "</label></li>"
            checklist_html = "<div class='checklist-container'><h4>Module Checklist</h4><ul>" + items + "</ul></div>"

        # Quiz — index-based grading: free text never enters attribute values,
        # so apostrophes in options/answers can't break parsing or scoring
        quiz_html = ""
        quiz = m.get('quiz', [])
        if quiz:
            q_items = ""
            for i, q in enumerate(quiz):
                opts_list = q.get('options', [])
                try:
                    ans_idx = opts_list.index(q["answer"])
                except ValueError:
                    ans_idx = -1
                    quiz_warnings.append(f"{mid} Q{i+1}: answer not found among options")
                opts = ""
                for oi, opt in enumerate(opts_list):
                    opts += "<label><input type='radio' name='q_" + mid_cls + "_" + str(i) + "' value='" + str(oi) + "'> " + esc(opt) + "</label>"
                q_items += "<div class='quiz-q' data-ans='" + str(ans_idx) + "'><p><strong>Q" + str(i+1) + ":</strong> " + esc(q["question"]) + "</p>" + opts + "<div class='q-exp' style='display:none'>" + q.get("explanation","") + "</div></div>"
            quiz_html = "<div class='quiz-container' id='quiz_" + mid + "'><h4>Module Quiz</h4>" + q_items + "<button class='btn btn-primary' onclick='submitQuiz(\"" + mid + "\")'>Submit Quiz</button><div class='quiz-result' id='quiz_res_" + mid + "'></div></div>"

        # Feedback
        feedback_html = f"""
        <div class='feedback-container'>
            <h4>📊 Rate This Module</h4>
            <p style='color:var(--text-muted);font-size:13px;margin-bottom:4px'>How useful was this module?</p>
            <div class='star-rating' id='stars_{m["id"]}'>
                <span onclick='rateModule("{m["id"]}",1)'>★</span>
                <span onclick='rateModule("{m["id"]}",2)'>★</span>
                <span onclick='rateModule("{m["id"]}",3)'>★</span>
                <span onclick='rateModule("{m["id"]}",4)'>★</span>
                <span onclick='rateModule("{m["id"]}",5)'>★</span>
            </div>
            <textarea id='fb_help_{m["id"]}' placeholder='What did you find most helpful?' style='user-select:text'></textarea>
            <textarea id='fb_imp_{m["id"]}'  placeholder='What could be improved?' style='user-select:text'></textarea>
            <select id='fb_role_{m["id"]}'>
                <option value=''>Select your role...</option>
                <option value='New Seller'>New Seller</option>
                <option value='Experienced Seller'>Experienced Seller</option>
                <option value='Account Manager'>Account Manager</option>
                <option value='Consultant'>Consultant</option>
                <option value='Other'>Other</option>
            </select>
            <br><br>
            <button class='btn btn-accent' onclick='submitFeedback("{m["id"]}")'>Submit Feedback</button>
        </div>"""

        # Process flow
        process_flow = m.get('process_flow','')

        title_esc = esc(m["title"])

        # SMEMinds Studio module-film poster (clickable → mounts the player)
        video_poster = ""
        vscript = m.get('video_script')
        if vscript and vscript.get('scenes'):
            _tot = sum(max(8, min(26, int(s.get('sec', 16)))) for s in vscript['scenes']) + 7 + 8
            _dur = f"{_tot // 60}:{_tot % 60:02d}"
            video_poster = (
                "<div class='mod-video' id='mvid_" + mid + "' data-mid='" + mid + "'>"
                "<button class='mvid-poster' type='button' aria-label='Play the module video' "
                "onclick=\"SMVideo.open('" + mid + "', this.closest('.mod-video'))\">"
                "<span class='mvid-grad'></span><span class='mvid-rings'></span>"
                "<img class='mvid-logo brand-logo' alt='SMEMinds'>"
                "<span class='mvid-poster-txt'>"
                "<span class='mvid-eyebrow'>SMEMinds Studio &middot; Module Film</span>"
                "<span class='mvid-poster-title'>" + esc(m["number"]) + " &mdash; " + title_esc + "</span>"
                "<span class='mvid-poster-sub'>Tap to play the " + _dur + " narrated explainer</span>"
                "</span>"
                "<span class='mvid-playbtn'><svg viewBox='0 0 24 24'><path d='M8 5v14l11-7z'/></svg></span>"
                "<span class='mvid-badge'>&#9654; " + _dur + "</span>"
                "</button></div>"
            )

        # Each module ships as an inert <template>: ~13k elements stay out of
        # the live DOM until app.js ensureModuleDom() instantiates on first visit
        pillar_cls = m.get('pillar') or ('p' + str(m['id']).split('.')[0])
        module_html = f"""
        <template class='module-tpl' data-module='{m["id"]}'>
        <div class='module-section {pillar_cls}' id='module_{m["id"]}'>
            <div class='module-header'>
                <div class='module-header-top'>
                    <div>
                        <h2>{m["number"]} — {title_esc}</h2>
                        <div class='module-meta'>
                            <span class='badge badge-diff {diff_class}'>{esc(m.get("difficulty",""))}</span>
                            <span class='badge badge-time'>⏱ {esc(m.get("time",""))}</span>
                        </div>
                    </div>
                    <div class='module-logo-block'>
                        <img class='module-logo-img brand-logo' alt='SMEMinds'>
                    </div>
                </div>
            </div>
            <div class='module-body'>
                <div class='overview-content'>{wrap_tables(m.get("overview",""))}</div>
                {video_poster}
                <div class='module-content'>{wrap_tables(m.get("content",""))}</div>
                {process_flow}
                {wrap_tables(tools_html)}
                {video_html}
                {checklist_html}
                {quiz_html}
                {feedback_html}
            </div>
        </div>
        </template>"""
        html += module_html

    if quiz_warnings:
        print("  WARNING — quiz answers that match no option (graded as unanswerable):")
        for w in quiz_warnings:
            print(f"    - {w}")
    return html

def substitute(doc, token, payload, allow_tokens=()):
    """Replace `token` in doc; refuse payloads that smuggle other tokens in."""
    stray = [t for t in re.findall(r'\{\{ [A-Z_]+ \}\}', payload) if t not in allow_tokens]
    if stray:
        raise ValueError(f"Payload for {token} contains template tokens: {stray}")
    return doc.replace(token, payload)

def build():
    print("Building SMEMinds Playbook...")

    src = lambda name: os.path.join(BASE, 'src', name)
    template   = read_file(src('template.html'))
    css        = read_file(src('style.css'))
    js         = read_file(src('app.js'))
    tools_js   = read_file(src('tools.js'))
    video_js   = read_file(src('video.js'))
    tools_html = read_file(src('tools.html'))

    logo_uri, favicon_uri = get_logo_assets()
    ai_icon_uri, ai_favicon_uri = get_ai_icon()
    all_modules = load_all_modules()
    if not all_modules:
        print("FATAL: no modules loaded")
        sys.exit(1)
    modules_html = generate_modules(all_modules)

    # Video script registry (SMEMinds Studio module films)
    import json as _json
    video_scripts = {}
    for m in all_modules:
        vs = m.get('video_script')
        if vs and vs.get('scenes'):
            video_scripts[m['id']] = {
                'title': m.get('title', ''), 'number': m.get('number', m['id']),
                'tagline': vs.get('tagline', ''), 'scenes': vs.get('scenes', []),
                'cta': vs.get('cta', ''),
            }
    # Marketing overview film (non-module) — keyed 'overview', mounted on the dashboard
    _ov_path = os.path.join(BASE, 'src', 'overview_video.json')
    if os.path.exists(_ov_path):
        try:
            with open(_ov_path, encoding='utf-8') as _f:
                _ov = _json.load(_f)
            if _ov.get('scenes'):
                video_scripts['overview'] = _ov
                print(f"  Overview film: {len(_ov['scenes'])} scenes")
        except Exception as _e:
            print(f"  WARN overview video: {_e}")
    print(f"  Video scripts: {len(video_scripts)} module films")

    final_html = template
    final_html = substitute(final_html, '{{ CSS }}', css)
    # app.js legitimately contains {{ LOGO_B64 }} (single shared embed)
    final_html = substitute(final_html, '{{ JS }}', js + "\n\n" + tools_js + "\n\n" + video_js,
                            allow_tokens=('{{ LOGO_B64 }}',))
    final_html = substitute(final_html, '{{ TOOLS }}', tools_html)
    final_html = substitute(final_html, '{{ MODULES }}', modules_html)
    final_html = substitute(final_html, '{{ FAVICON_B64 }}', ai_favicon_uri or favicon_uri)
    final_html = final_html.replace('{{ VIDEO_SCRIPTS }}', _json.dumps(video_scripts, ensure_ascii=False))
    final_html = final_html.replace('{{ AI_ICON_B64 }}', ai_icon_uri)
    final_html = final_html.replace('{{ LOGO_B64 }}', logo_uri)

    leftover = sorted(set(re.findall(r'\{\{ [A-Z_]+ \}\}', final_html)))
    if leftover:
        print(f"FATAL: unsubstituted tokens in output: {leftover}")
        sys.exit(1)
    embeds = final_html.count('data:image/jpeg;base64')
    if logo_uri and embeds != 1:
        print(f"FATAL: expected exactly 1 logo embed, found {embeds}")
        sys.exit(1)

    out_path = os.path.join(BASE, 'index.html')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(final_html)

    size_kb = os.path.getsize(out_path) / 1024
    print(f"[OK] Successfully built: index.html ({size_kb:.0f} KB, {len(all_modules)} modules)")

if __name__ == "__main__":
    build()
