// HackMeridian demo video v2 assembler. Usage: node assemble-v2.cjs   (media stays in ~/Movies, nothing is written here)
// Picture first (always), then audio only when all 13 narration wavs exist.
// Picture is scaled to 1806x1016 and padded so the 64 px bottom strip never covers content (same as assemble.cjs).
const { chromium } = require(process.env.PW || "/Users/pedrosaragossy/.hermes/hermes-agent/node_modules/playwright");
const fs = require("fs");
const path = require("path");
const { execFileSync } = require("child_process");

const V2 = path.join(process.env.HOME, "Movies/hackmeridian-rail-video/v2");
const WK = path.join(V2, "work");
const FF = "/opt/homebrew/bin/ffmpeg";
fs.mkdirSync(WK, { recursive: true });
const LIME = "#C6F24E", INK = "#0E0F11", FG = "#E8E9EB", MUTED = "#A8ABB0";

// ---- picture segments: [input, in-start s, duration s]; clip middles drop the 2 s pad. Still = image, looped.
const clip = (n, s, d) => [path.join(V2, "clips", `b${n}.mp4`), s, d];
// B7: 72 s raw take -> 26 s, cut points found from frame-change times of the response pane
const b7 = [[8.4, 3.6], [13.9, 4.4], [20.4, 0.8], [25.4, 2.4], [28.1, 0.8], [33.9, 4.3], [40.5, 1.5], [45.8, 1.5], [58.0, 1.5], [59.3, 0.7], [66.4, 4.6]];
const beats = [ // name, start (video s), length, segments
  ["B1", 0, 19, [clip(1, 2, 19)]],
  ["B2", 19, 12, [clip(2, 2, 12)]],
  ["B2b", 31, 14, [[path.join(WK, "b2b-a.png"), 0, 9], [path.join(WK, "b2b-b.png"), 0, 5]]],
  ["B3", 45, 12, [clip(3, 2, 12)]],
  ["B4", 57, 13, [clip(4, 2, 13)]],
  ["B5", 70, 10, [clip(5, 2, 10)]],
  ["B6", 80, 14, [clip(6, 2, 14)]],
  ["B7", 94, 26, b7.map(([s, d]) => clip(7, s, d))],
  ["B8", 120, 10, [clip(8, 2, 9), [path.join(V2, "clips/b8.mp4"), 10.99, 1, "last"]]],
  ["B9a", 130, 23, [clip(9, 2.25, 23)]],      // click at 25.25 in the clip = end of B9a
  ["B9b", 153, 13, [clip(9, 25.25, 13)]],     // MATCH frame (25.40 in clip) = 153.15 s
  ["B10", 166, 16, [clip(10, 2, 16)]],
  ["B11", 182, 13, [[path.join(V2, "stills/S12.png"), 0, 13]]],
];
const TOTAL = 195, MATCH_T = 153 + 0.15;
const wav = { B1: "B01", B2: "B02", B2b: "B02b", B3: "B03", B4: "B04", B5: "B05", B6: "B06", B7: "B07", B8: "B08", B9a: "B09", B9b: "B10", B10: "B11", B11: "B12" };

const FONT = `<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">`;
const BASE = `*{box-sizing:border-box}body{margin:0;font-family:Inter,system-ui,sans-serif;-webkit-font-smoothing:antialiased}`;
const pill = (text, css, extra = "") => `${FONT}<style>${BASE}html,body{background:transparent}
  div{position:absolute;bottom:8px;${css};padding:8px 20px;border-radius:10px;background:${INK};color:${FG};font-size:24px;font-weight:600;white-space:nowrap;${extra}}</style><div>${text}</div>`;
const cap = (t) => pill(t, "right:40px", `font-size:22px;font-weight:400;color:${MUTED}`);
const OVER = {
  label: [pill("Stellar testnet · test keys", "left:40px", `border:2px solid ${LIME}`), 0, TOTAL],
  lower: [pill("Narration: AI voice generated from Pedro's voice", "left:50%;transform:translateX(-50%)"), 0, 8],
  wto: [cap("Source: WTO, trade finance"), 21, 31],
  b7: [cap("Live on Stellar testnet · open rail API"), 94, 120],
  b8: [cap("Stellar testnet transaction, public explorer"), 120, 130],
};
const card = (last) => `${FONT}<style>${BASE}body{background:${INK};color:${FG};width:1920px;height:1080px;display:grid;place-content:center;text-align:center;gap:34px;padding:0 120px}</style>
  <div style="font-size:60px;font-weight:700;letter-spacing:-.02em;color:${LIME}">Radox · tokenized real-world assets on Stellar</div>
  <div style="font-size:30px;color:${MUTED};line-height:1.45">token_sale, yield_distributor, maturity_settlement · Stellar mainnet since June–July 2026 · <span style="color:${LIME}">github.com/pwsaragossy/radox</span> (contracts only)</div>
  <div style="font-size:38px;margin-top:30px;opacity:${last ? 1 : 0}">New: <b style="color:${LIME}">Radox Custody Rail</b> · built at HackMeridian · Stellar testnet</div>`;

(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  const shot = async (html, file, transparent) => {
    await p.setContent(html, { waitUntil: "load" });
    await p.evaluate(() => document.fonts.ready).catch(() => {});
    await p.waitForTimeout(800);
    await p.screenshot({ path: path.join(WK, file), omitBackground: !!transparent });
  };
  await shot(card(false), "b2b-a.png");
  await shot(card(true), "b2b-b.png");
  for (const [k, [h]] of Object.entries(OVER)) await shot(h, k + ".png", true);
  await b.close();

  // picture
  const segs = beats.flatMap(([, , , s]) => s);
  const args = ["-v", "error", "-y"];
  for (const [f, ss, d, last] of segs) {
    if (f.endsWith(".png")) args.push("-loop", "1", "-framerate", "30", "-t", String(d), "-i", f);
    else args.push("-ss", String(ss), "-t", String(d), "-i", f);
  }
  const ovk = Object.keys(OVER);
  for (const o of ovk) args.push("-loop", "1", "-framerate", "30", "-t", String(TOTAL), "-i", path.join(WK, o + ".png"));
  let g = segs.map(([, , d, last], i) => `[${i}:v]${last ? `trim=start=0,setpts=PTS-STARTPTS,tpad=stop_mode=clone:stop_duration=${d + 1},trim=end=${d},setpts=PTS-STARTPTS,` : `trim=duration=${d},setpts=PTS-STARTPTS,tpad=stop_mode=clone:stop_duration=1,trim=end=${d},setpts=PTS-STARTPTS,`}fps=30,scale=1806:1016,pad=1920:1080:57:0:color=0x0E0F11,setsar=1,format=yuv420p[s${i}];`).join("");
  g += segs.map((_, i) => `[s${i}]`).join("") + `concat=n=${segs.length}:v=1:a=0[v0];`;
  ovk.forEach((o, k) => { const [, a, z] = OVER[o]; g += `[v${k}][${segs.length + k}:v]overlay=0:0:enable='between(t,${a},${z - 0.001})'[v${k + 1}];`; });
  g = g.replace(/;$/, "");
  const silent = path.join(V2, "rail-demo-v2-silent.mp4");
  const venc = ["-c:v", "libx264", "-profile:v", "high", "-preset", "medium", "-crf", "18", "-r", "30", "-pix_fmt", "yuv420p"];
  execFileSync(FF, [...args, "-filter_complex", g, "-map", `[v${ovk.length}]`, "-t", String(TOTAL), ...venc, silent]);
  console.log("picture", silent);

  // audio
  const dir = path.join(V2, "narration");
  const missing = beats.map(([n]) => wav[n]).filter((w) => !fs.existsSync(path.join(dir, w + ".wav")));
  if (missing.length) { console.log("MISSING " + missing.join(" ")); return; }
  const a = ["-v", "error", "-y", "-i", silent];
  const starts = beats.map(([n, s]) => (n === "B9b" ? MATCH_T + 0.3 : s + 0.4));
  beats.forEach(([n]) => a.push("-i", path.join(dir, wav[n] + ".wav")));
  const af = beats.map((_, i) => `[${i + 1}:a]aresample=48000,aformat=channel_layouts=mono,adelay=${Math.round(starts[i] * 1000)}:all=1[a${i}];`).join("")
    + beats.map((_, i) => `[a${i}]`).join("") + `amix=inputs=${beats.length}:normalize=0:duration=longest,loudnorm=I=-16:TP=-1.5:LRA=7,apad,atrim=0:${TOTAL - 2},apad=whole_dur=${TOTAL}[aout]`;
  const out = path.join(V2, "rail-demo-v2.mp4");
  execFileSync(FF, [...a, "-filter_complex", af, "-map", "0:v", "-map", "[aout]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "1", "-t", String(TOTAL), "-movflags", "+faststart", out]);
  console.log("final", out, "starts", starts.join(" "));
})().catch((e) => { console.error(e); process.exit(1); });
