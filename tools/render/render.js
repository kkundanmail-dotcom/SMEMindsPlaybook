/*
 * SMEMinds offline film renderer.
 * Drives each module video through the engine's deterministic render mode in headless Edge,
 * records the visuals, builds a frame-offset narration track from the TTS cache, and muxes an MP4.
 *
 *   node render.js --mid 1.1 --voice ritu                 # one module
 *   node render.js --all --voice ritu                     # every module
 *   node render.js --all --voice ritu --w 1920 --h 1080   # 1080p
 *
 * Requires: playwright (+ system Edge), ffmpeg/ffprobe on PATH or the winget location.
 */
const { chromium } = require("playwright");
const { execFileSync, execFile } = require("child_process");
const crypto = require("crypto");
const fs = require("fs");
const path = require("path");
const os = require("os");

// ---- paths / config ----
const PROJ = path.resolve(__dirname, "..", "..");
const INDEX = path.join(PROJ, "index.html");
const CACHE = path.join(PROJ, "backend", ".tts_cache");
const OUTROOT = path.join(PROJ, "exports", "video");
const WORK = path.join(__dirname, "_work");
const LEAD_MS = 240, PAUSE_MS = 650, LOGO_MS = 4500;

function findBin(name) {
  const winget = path.join(process.env.LOCALAPPDATA || "",
    "Microsoft\\WinGet\\Packages\\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\\ffmpeg-8.1.1-full_build\\bin", name + ".exe");
  if (fs.existsSync(winget)) return winget;
  return name; // assume on PATH
}
const FFMPEG = findBin("ffmpeg"), FFPROBE = findBin("ffprobe");

// ---- args ----
function arg(flag, def) { const i = process.argv.indexOf(flag); return i >= 0 ? process.argv[i + 1] : def; }
const VOICES = arg("--voice", "ritu").split(",").map((v) => v.trim()).filter(Boolean);
const MODEL = arg("--model", "bulbul:v3");
const W = parseInt(arg("--w", "1920"), 10), H = parseInt(arg("--h", "1080"), 10);
const ONE = arg("--mid", null);
const ALL = process.argv.includes("--all");
const CONC = Math.max(1, parseInt(arg("--conc", "1"), 10));
const FORCE = process.argv.includes("--force");   // re-render even if the MP4 exists
const ENCODER = arg("--enc", "x264");             // x264 (CPU, best quality) | qsv (HW, Intel iGPU)
const DSF = Math.max(1, parseInt(arg("--dsf", "2"), 10));  // device scale factor — supersample for crisp text/logo
const OUT_BASE = (function () { const i = process.argv.indexOf("--out"); return i >= 0 ? path.resolve(process.argv[i + 1]) : OUTROOT; })();

function cacheFile(voice, text) {
  const key = crypto.createHash("sha256").update(MODEL + "|" + voice + "|" + text).digest("hex");
  return path.join(CACHE, key + ".txt");
}
function probeMs(mp3) {
  const out = execFileSync(FFPROBE, ["-v", "error", "-show_entries", "format=duration",
    "-of", "default=nw=1:nk=1", mp3]).toString().trim();
  return Math.round(parseFloat(out) * 1000) || 0;
}
function sh(bin, args) {
  return new Promise((res, rej) => execFile(bin, args, { maxBuffer: 1 << 26 }, (e, so, se) =>
    e ? rej(new Error((se || e.message || "").toString().slice(0, 400))) : res(so)));
}

async function renderOne(browser, voice, mid) {
  const safe = String(mid).replace(/\./g, "-");
  const out = path.join(OUT_BASE, voice, `${safe}.mp4`);
  fs.mkdirSync(path.join(OUT_BASE, voice), { recursive: true });
  if (!FORCE && fs.existsSync(out) && fs.statSync(out).size > 50000) {
    console.log(`  • ${voice}/${mid} already rendered — skipping`);
    return { mid, voice, out, skipped: true };
  }
  const work = path.join(WORK, voice, safe);
  fs.mkdirSync(work, { recursive: true });

  // record the film in a fresh recording context
  const ctx = await browser.newContext({
    viewport: { width: W, height: H }, deviceScaleFactor: DSF,  // supersample → crisp text, logo, no aliasing
    recordVideo: { dir: work, size: { width: W, height: H } },
  });
  const rp = await ctx.newPage();
  const recStart = Date.now();                        // recording begins ~at page creation
  rp.on("pageerror", (e) => console.log(`    [pageerror] ${e.message}`));
  await rp.goto("file:///" + INDEX.replace(/\\/g, "/"), { waitUntil: "load" });
  await rp.waitForFunction(() => window.SMVideo && typeof window.SMVideo.renderTexts === "function", null, { timeout: 60000 });
  try { await rp.evaluate(() => document.fonts && document.fonts.ready); } catch (e) {}

  // 1) exact narration text per timeline slot (from the engine itself)
  const slots = await rp.evaluate((m) => window.SMVideo.renderTexts(m), mid);
  if (!slots) { await ctx.close(); throw new Error("no script for " + mid); }

  // 2) decode each clip from cache + measure → per-slot window durations (ms)
  const clips = [];   // {idx, mp3, ms}
  const durs = [];
  let missing = 0;
  for (let i = 0; i < slots.length; i++) {
    const s = slots[i];
    if (s.type === "logo") { durs.push(LOGO_MS); continue; }
    const cf = cacheFile(voice, s.text);
    if (s.text && fs.existsSync(cf)) {
      const mp3 = path.join(work, `clip_${String(i).padStart(2, "0")}.mp3`);
      fs.writeFileSync(mp3, Buffer.from(fs.readFileSync(cf, "utf8").trim(), "base64"));
      const ms = probeMs(mp3);
      clips.push({ idx: i, mp3, ms });
      durs.push(LEAD_MS + ms + PAUSE_MS);
    } else {
      if (s.text) missing++;
      durs.push(LEAD_MS + PAUSE_MS);   // empty/missing → brief beat
    }
  }
  if (missing) console.log(`  ! ${mid}: ${missing} clip(s) missing from cache — those scenes will be silent`);

  // slot start offsets (ms) within the film
  const offs = [];
  let acc = 0;
  for (let i = 0; i < durs.length; i++) { offs.push(acc); acc += durs[i]; }
  const totalMs = acc;

  // 3) clean the page to just the film, then play deterministically
  await rp.evaluate(() => {
    const box = document.createElement("div");
    box.id = "__renderbox";
    box.style.cssText = "position:fixed;inset:0;z-index:2147483647;background:#0b1020;";
    document.body.appendChild(box);
    const st = document.createElement("style");
    st.textContent = "body>*:not(#__renderbox){display:none!important}" +
      "#__renderbox .vp-controls,#__renderbox .vp-big,#__renderbox .vp-scrim{display:none!important}" +
      "*{cursor:none!important}::-webkit-scrollbar{width:0;height:0}";
    document.head.appendChild(st);
    window.__renderbox = box;
  });

  const preRollMs = Date.now() - recStart;          // blank lead (load + setup) before scene 0
  await rp.evaluate(([m, d]) => window.SMVideo.renderPlay(m, window.__renderbox, d), [mid, durs]);
  // Drive each scene from Node (wall-clock) — immune to background-tab timer throttling.
  for (let i = 0; i < durs.length; i++) {
    await rp.waitForTimeout(durs[i]);
    await rp.evaluate(() => window.SMVideo.renderStep());
  }
  await rp.waitForFunction(() => window.__SMRENDER_DONE === true, null, { timeout: 15000 });
  // actual on-screen appearance time of each scene (eliminates step-latency drift)
  const marks = await rp.evaluate(() => window.__SMRENDER_MARKS || []);
  await rp.waitForTimeout(250);                      // let the last frame settle

  const video = rp.video();
  await ctx.close();                                 // flushes the .webm
  const webm = await video.path();

  // map slot index -> real ms offset from scene 0
  const t0 = marks.length ? marks[0].t : 0;
  const relById = {};
  marks.forEach((m) => { relById[m.i] = m.t - t0; });
  const lastRel = marks.length ? (marks[marks.length - 1].t - t0) : 0;
  const audioBedMs = Math.max(totalMs, lastRel + durs[durs.length - 1]);

  // 3b) emit a sidecar .vtt caption track (one cue per narrated slot) — "60% watch with sound off"
  const vttPath = out.replace(/\.mp4$/, ".vtt");
  (function writeVtt() {
    function stamp(ms) {
      ms = Math.max(0, Math.round(ms));
      const h = Math.floor(ms / 3600000); ms -= h * 3600000;
      const m = Math.floor(ms / 60000); ms -= m * 60000;
      const s = Math.floor(ms / 1000), f = ms - s * 1000;
      const p = (n, w) => String(n).padStart(w, "0");
      return `${p(h, 2)}:${p(m, 2)}:${p(s, 2)}.${p(f, 3)}`;
    }
    let vtt = "WEBVTT\n\n";
    // One cue per narrated clip, timed to the deterministic slot offsets (monotonic, never overlap).
    clips.forEach((c) => {
      const txt = (slots[c.idx] && slots[c.idx].text || "").trim();
      if (!txt) return;
      const st = offs[c.idx] + LEAD_MS;
      const en = st + c.ms;
      vtt += `${stamp(st)} --> ${stamp(en)}\n${txt}\n\n`;
    });
    try { fs.writeFileSync(vttPath, vtt, "utf8"); } catch (e) {}
  })();

  // 4) build the offset narration track using the real scene marks
  const audio = path.join(work, "narration.mp3");
  if (clips.length) {
    const inputs = ["-f", "lavfi", "-t", (audioBedMs / 1000).toFixed(3), "-i", "anullsrc=r=44100:cl=mono"];
    clips.forEach((c) => inputs.push("-i", c.mp3));
    const fc = [];
    clips.forEach((c, k) => { const at = Math.round((relById[c.idx] != null ? relById[c.idx] : offs[c.idx]) + LEAD_MS); fc.push(`[${k + 1}:a]aresample=44100,pan=mono|c0=c0,adelay=${at}[a${k}]`); });
    const mixIns = clips.map((_, k) => `[a${k}]`).join("") + "[0:a]";
    fc.push(`${mixIns}amix=inputs=${clips.length + 1}:normalize=0:dropout_transition=0[mix]`);
    await sh(FFMPEG, ["-y", "-loglevel", "error", ...inputs, "-filter_complex", fc.join(";"),
      "-map", "[mix]", "-ar", "44100", "-ac", "1", "-c:a", "libmp3lame", "-b:a", "128k", audio]);
  }

  // 5) trim the pre-roll and mux into the final MP4 (HW encode via QSV; CPU x264 fallback)
  const hasSub = fs.existsSync(vttPath);
  function muxArgs(venc) {
    const a = ["-y", "-loglevel", "error", "-ss", (preRollMs / 1000).toFixed(3), "-i", webm];
    if (clips.length) a.push("-i", audio);
    if (hasSub) a.push("-i", vttPath);
    a.push("-map", "0:v:0");
    if (clips.length) a.push("-map", "1:a:0");
    if (hasSub) a.push("-map", (clips.length ? 2 : 1) + ":0");
    // gradfun dithers away gradient banding; crf 18 + animation tune keeps flat slides crisp
    if (venc === "qsv") a.push("-c:v", "h264_qsv", "-global_quality", "18", "-preset", "slow", "-pix_fmt", "nv12", "-vf", "gradfun=0.8:16,format=nv12");
    else a.push("-c:v", "libx264", "-crf", "18", "-preset", "medium", "-tune", "animation", "-pix_fmt", "yuv420p", "-vf", "gradfun=0.8:16");
    a.push("-r", "30");
    if (clips.length) a.push("-c:a", "aac", "-b:a", "96k", "-ac", "1", "-af", "loudnorm=I=-14:TP=-1.5:LRA=11");
    if (hasSub) a.push("-c:s", "mov_text");
    a.push("-movflags", "+faststart", "-shortest", out);
    return a;
  }
  try { await sh(FFMPEG, muxArgs(ENCODER)); }
  catch (e) { if (ENCODER === "qsv") await sh(FFMPEG, muxArgs("x264")); else throw e; }

  const sz = (fs.statSync(out).size / 1048576).toFixed(1);
  console.log(`  ✓ ${voice}/${mid} → ${path.relative(PROJ, out)}  (${(totalMs / 1000).toFixed(1)}s, ${sz} MB)`);
  try { fs.rmSync(work, { recursive: true, force: true }); } catch (e) {}
  return { mid, voice, out, totalMs };
}

(async () => {
  fs.mkdirSync(WORK, { recursive: true });
  const browser = await chromium.launch({ channel: "msedge", headless: true,
    args: ["--autoplay-policy=no-user-gesture-required", "--mute-audio",
      "--disable-background-timer-throttling", "--disable-backgrounding-occluded-windows",
      "--disable-renderer-backgrounding", "--disable-features=IntensiveWakeUpThrottling,CalculateNativeWinOcclusion"] });
  const probe = await browser.newPage();
  await probe.goto("file:///" + INDEX.replace(/\\/g, "/"), { waitUntil: "domcontentloaded" });
  await probe.waitForFunction(() => window.SMVideo && typeof window.SMVideo.list === "function");
  let mids = await probe.evaluate(() => window.SMVideo.list());
  await probe.close();

  if (ONE) mids = [ONE];
  else if (!ALL) { console.log("specify --mid <id> or --all"); await browser.close(); return; }

  // build the full task list (voice × module)
  const tasks = [];
  for (const v of VOICES) for (const mid of mids) tasks.push({ voice: v, mid });
  console.log(`Rendering ${tasks.length} film(s) | voices=${VOICES.join(",")} | ${W}x${H} | concurrency=${CONC}`);
  const t0 = Date.now();

  let next = 0, fin = 0;
  const done = [], failed = [];
  async function worker() {
    while (next < tasks.length) {
      const { voice, mid } = tasks[next++];
      try { const r = await renderOne(browser, voice, mid); if (!r.skipped) done.push(r); else done.push(r); }
      catch (e) { failed.push({ voice, mid, err: e.message }); console.log(`  ✗ ${voice}/${mid}: ${e.message}`); }
      fin++;
      const el = (Date.now() - t0) / 1000, rate = el / Math.max(1, fin), eta = Math.round(rate * (tasks.length - fin));
      console.log(`  … ${fin}/${tasks.length} complete | elapsed ${Math.round(el)}s | ETA ~${Math.round(eta / 60)}m`);
    }
  }
  await Promise.all(Array.from({ length: Math.min(CONC, tasks.length) }, worker));
  await browser.close();

  console.log("-".repeat(56));
  console.log(`Done in ${Math.round((Date.now() - t0) / 60000)}m. OK: ${done.length}  Failed: ${failed.length}`);
  if (failed.length) failed.forEach((f) => console.log(`  ✗ ${f.voice}/${f.mid}: ${f.err}`));
})();
