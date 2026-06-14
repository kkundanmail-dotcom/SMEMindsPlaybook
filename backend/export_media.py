"""
Export the recorded narration from the TTS cache into real, organized audio files.

Produces, under  exports/audio/ :
  <voice>/<module>/00_intro.mp3, 01_scene.mp3, ... , NN_outro.mp3   (one file per slot)
  <voice>/<module>/_full.mp3                                        (whole-module narration, with pauses)
  manifest.json                                                     (index of everything)

Run AFTER the cache is populated (pregen_tts.py):
    cd backend
    python export_media.py            # both voices
    python export_media.py ritu       # one voice
"""
import os, sys, re, json, base64, hashlib, sqlite3, subprocess, shutil, tempfile

BASE = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE, "smeminds.db")
CACHE_DIR = os.path.join(BASE, ".tts_cache")
OUT_DIR = os.path.join(os.path.dirname(BASE), "exports", "audio")
DEFAULT_MODEL = "bulbul:v3"
VOICES = ["ritu", "shubh"]
LEAD_MS = 240        # silence before each clip (matches the player lead-in)
PAUSE_MS = 650       # silence after each clip (matches SCENE_PAUSE)

def find_ffmpeg():
    p = shutil.which("ffmpeg")
    if p:
        return p
    guess = os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.1-full_build\bin\ffmpeg.exe")
    return guess if os.path.exists(guess) else None

FFMPEG = find_ffmpeg()

def clean(t):
    t = re.sub(r"\s*\|\s*", " ", t or "")
    return re.sub(r"\s+", " ", t).strip()

def slug(s):
    s = re.sub(r"[^A-Za-z0-9]+", "-", (s or "").lower()).strip("-")
    return (s[:48] or "module")

def resolve_model():
    model = ""
    try:
        with sqlite3.connect(DB_PATH) as c:
            row = c.execute("SELECT value FROM app_config WHERE key='sarvam'").fetchone()
        if row:
            model = (json.loads(row[0]).get("model") or "").strip()
    except Exception:
        pass
    return model or os.environ.get("SARVAM_TTS_MODEL", "").strip() or DEFAULT_MODEL

def cache_path(model, speaker, text):
    key = hashlib.sha256((model + "|" + speaker + "|" + text).encode()).hexdigest()
    return os.path.join(CACHE_DIR, key + ".txt")

def collect_modules():
    """Per-module narration slots, in play order (intro, scenes, outro)."""
    with sqlite3.connect(DB_PATH) as c:
        c.row_factory = sqlite3.Row
        rows = c.execute("SELECT id, data FROM modules ORDER BY pillar, id").fetchall()
    mods = []
    for r in rows:
        m = json.loads(r["data"])
        vs = m.get("video_script") or {}
        scenes = vs.get("scenes") or []
        if not scenes:
            continue
        slots = [{"type": "intro", "text": clean((m.get("title", "") + ". | " + vs.get("tagline", "")))}]
        for sc in scenes:
            slots.append({"type": "scene", "text": clean(sc.get("vo", ""))})
        slots.append({"type": "outro", "text": clean(vs.get("cta", ""))})
        mods.append({
            "id": m.get("id") or r["id"],
            "number": m.get("number") or m.get("id") or r["id"],
            "title": m.get("title", ""),
            "slots": slots,
        })
    return mods

def decode_clip(model, speaker, text, dst):
    p = cache_path(model, speaker, text)
    if not text or not os.path.exists(p):
        return False
    with open(p, "r") as f:
        b64 = f.read().strip()
    with open(dst, "wb") as f:
        f.write(base64.b64decode(b64))
    return True

def build_full(model, speaker, mod, clip_paths, dst):
    """Concatenate a module's clips into one narration track with lead-in + pauses."""
    if not FFMPEG:
        return False, "ffmpeg not found"
    present = [(i, p) for i, p in enumerate(clip_paths) if p]
    if not present:
        return False, "no clips"
    tmpd = tempfile.mkdtemp(prefix="smaud_")
    try:
        segs = []
        for k, (i, src) in enumerate(present):
            seg = os.path.join(tmpd, "seg_%03d.mp3" % k)
            af = "adelay=%d|%d,apad=pad_dur=%s" % (LEAD_MS, LEAD_MS, PAUSE_MS / 1000.0)
            r = subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-i", src,
                                "-af", af, "-ar", "44100", "-ac", "2",
                                "-c:a", "libmp3lame", "-b:a", "160k", seg],
                               capture_output=True, text=True)
            if r.returncode != 0:
                return False, r.stderr.strip()[:200]
            segs.append(seg)
        listf = os.path.join(tmpd, "list.txt")
        with open(listf, "w") as f:
            for s in segs:
                f.write("file '%s'\n" % s.replace("\\", "/"))
        r = subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
                            "-i", listf, "-c:a", "libmp3lame", "-b:a", "160k", dst],
                           capture_output=True, text=True)
        if r.returncode != 0:
            return False, r.stderr.strip()[:200]
        return True, "ok"
    finally:
        shutil.rmtree(tmpd, ignore_errors=True)

def main():
    voices = [v for v in sys.argv[1:] if v in VOICES] or VOICES
    model = resolve_model()
    mods = collect_modules()
    os.makedirs(OUT_DIR, exist_ok=True)
    print("Model: %s  |  Voices: %s  |  Modules: %d  |  ffmpeg: %s"
          % (model, ", ".join(voices), len(mods), "yes" if FFMPEG else "NO (per-scene only)"))
    print("-" * 60)
    manifest = {"model": model, "voices": voices, "modules": []}
    made = missing = fulls = 0
    for mod in mods:
        mentry = {"id": mod["id"], "title": mod["title"], "voices": {}}
        for spk in voices:
            folder = os.path.join(OUT_DIR, spk, "%s_%s" % (str(mod["id"]).replace(".", "-"), slug(mod["title"])))
            os.makedirs(folder, exist_ok=True)
            clip_paths, files = [], []
            for i, slot in enumerate(mod["slots"]):
                name = "%02d_%s.mp3" % (i, slot["type"])
                dst = os.path.join(folder, name)
                if decode_clip(model, spk, slot["text"], dst):
                    clip_paths.append(dst); files.append(name); made += 1
                else:
                    clip_paths.append(None)
                    if slot["text"]:
                        missing += 1
            full_ok = False
            if any(clip_paths):
                ok, msg = build_full(model, spk, mod, clip_paths, os.path.join(folder, "_full.mp3"))
                full_ok = ok
                if ok:
                    fulls += 1
                else:
                    print("  ! full track failed (%s / %s): %s" % (mod["id"], spk, msg))
            mentry["voices"][spk] = {"folder": os.path.relpath(folder, OUT_DIR), "clips": files, "full": full_ok}
        manifest["modules"].append(mentry)
        print("  %-6s %s" % (mod["id"], mod["title"][:48]))
    with open(os.path.join(OUT_DIR, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    print("-" * 60)
    print("Per-scene clips written: %d   |   missing-from-cache: %d   |   full tracks: %d"
          % (made, missing, fulls))
    print("Output: %s" % OUT_DIR)
    if missing:
        print("NOTE: %d narration lines weren't in the cache yet — finish pregen_tts.py, then re-run." % missing)

if __name__ == "__main__":
    main()
