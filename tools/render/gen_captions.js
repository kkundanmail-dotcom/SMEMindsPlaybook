/*
 * Standalone caption (.vtt) generator — mirrors render.js timing without recording video.
 * Fast: a few seconds per module. Writes/overwrites <out>/<voice>/<mid>.vtt next to each film.
 *
 *   node gen_captions.js --voice ritu,shubh --out ../../exports/video_v2
 */
const { chromium } = require("playwright");
const { execFileSync } = require("child_process");
const crypto = require("crypto");
const fs = require("fs");
const path = require("path");

const PROJ = path.resolve(__dirname, "..", "..");
const INDEX = path.join(PROJ, "index.html");
const CACHE = path.join(PROJ, "backend", ".tts_cache");
const LEAD_MS = 240, PAUSE_MS = 650, LOGO_MS = 4500;

function arg(flag, def) { const i = process.argv.indexOf(flag); return i >= 0 ? process.argv[i + 1] : def; }
const VOICES = arg("--voice", "ritu,shubh").split(",").map((v) => v.trim()).filter(Boolean);
const MODEL = arg("--model", "bulbul:v3");
const OUT_BASE = path.resolve(arg("--out", path.join(PROJ, "exports", "video")));

function findBin(name) {
  const w = path.join(process.env.LOCALAPPDATA || "",
    "Microsoft\\WinGet\\Packages\\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\\ffmpeg-8.1.1-full_build\\bin", name + ".exe");
  return fs.existsSync(w) ? w : name;
}
const FFPROBE = findBin("ffprobe");
function cacheFile(voice, text) {
  const key = crypto.createHash("sha256").update(MODEL + "|" + voice + "|" + text).digest("hex");
  return path.join(CACHE, key + ".txt");
}
function probeMs(mp3) {
  const out = execFileSync(FFPROBE, ["-v", "error", "-show_entries", "format=duration", "-of", "default=nw=1:nk=1", mp3]).toString().trim();
  return Math.round(parseFloat(out) * 1000) || 0;
}
function stamp(ms) {
  ms = Math.max(0, Math.round(ms));
  const h = Math.floor(ms / 3600000); ms -= h * 3600000;
  const m = Math.floor(ms / 60000); ms -= m * 60000;
  const s = Math.floor(ms / 1000), f = ms - s * 1000;
  const p = (n, w) => String(n).padStart(w, "0");
  return `${p(h, 2)}:${p(m, 2)}:${p(s, 2)}.${p(f, 3)}`;
}

(async () => {
  const browser = await chromium.launch({ channel: "msedge", headless: true });
  const page = await browser.newPage();
  await page.goto("file:///" + INDEX.replace(/\\/g, "/"), { waitUntil: "load" });
  await page.waitForFunction(() => window.SMVideo && typeof window.SMVideo.renderTexts === "function", null, { timeout: 60000 });
  const mids = await page.evaluate(() => window.SMVideo.list());

  let written = 0;
  const tmp = path.join(__dirname, "_captmp");
  fs.mkdirSync(tmp, { recursive: true });
  for (const voice of VOICES) {
    for (const mid of mids) {
      const slots = await page.evaluate((m) => window.SMVideo.renderTexts(m), mid);
      if (!slots) continue;
      // measure each narrated clip → deterministic cumulative offsets
      const durs = [], clips = [];
      for (let i = 0; i < slots.length; i++) {
        const s = slots[i];
        if (s.type === "logo") { durs.push(LOGO_MS); continue; }
        const cf = cacheFile(voice, s.text);
        if (s.text && fs.existsSync(cf)) {
          const mp3 = path.join(tmp, "c.mp3");
          fs.writeFileSync(mp3, Buffer.from(fs.readFileSync(cf, "utf8").trim(), "base64"));
          const ms = probeMs(mp3);
          clips.push({ idx: i, ms }); durs.push(LEAD_MS + ms + PAUSE_MS);
        } else { durs.push(LEAD_MS + PAUSE_MS); }
      }
      const offs = []; let acc = 0;
      for (let i = 0; i < durs.length; i++) { offs.push(acc); acc += durs[i]; }
      let vtt = "WEBVTT\n\n";
      clips.forEach((c) => {
        const txt = (slots[c.idx].text || "").trim(); if (!txt) return;
        const st = offs[c.idx] + LEAD_MS, en = st + c.ms;
        vtt += `${stamp(st)} --> ${stamp(en)}\n${txt}\n\n`;
      });
      const safe = String(mid).replace(/\./g, "-");
      const dir = path.join(OUT_BASE, voice);
      if (!fs.existsSync(dir)) continue;   // only write where films exist
      fs.writeFileSync(path.join(dir, `${safe}.vtt`), vtt, "utf8");
      written++;
    }
  }
  try { fs.rmSync(tmp, { recursive: true, force: true }); } catch (e) {}
  await browser.close();
  console.log(`captions written: ${written}`);
})();
