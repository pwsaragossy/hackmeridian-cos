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

// ---- picture segments: [input, in-start s, duration s]. Beat length = 0.4 s lead + wav + 1.2 s tail (min 6 s), read from the wavs at render time.
const clip = (n, s, d) => [path.join(V2, "clips", `b${n}.mp4`), s, d];
const wav = { B1: "B01", B2: "B02", B2b: "B02b", B3: "B03", B4: "B04", B5: "B05", B6: "B06", B7: "B07", B8: "B08", B9a: "B09", B9b: "B10", B10: "B11", B11: "B12" };
const dur = (n) => parseFloat(execFileSync("ffprobe", ["-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path.join(V2, "narration", wav[n] + ".wav")]).toString());
const fr = (x) => Math.ceil(x * 30 - 1e-6) / 30;
const len = (n, tail = 1.2) => fr(Math.max(6, 0.4 + dur(n) + tail));
const L = {}; for (const n of Object.keys(wav)) L[n] = len(n);
L.B2b = fr(0.4 + dur("B2b") + 1.2);
L.B9b = fr(0.45 + dur("B9b") + 6.05);   // click, MATCH at +0.15, "Match" at +0.45, then >= 6 s silent hold on MATCH
L.B11 = fr(0.4 + dur("B11") + 2.0);     // the 2 s silent tail comes after the last word
// B7 (beat-relative s, speech times from whisper word timestamps of B07.wav + 0.4 s lead): "open a shipment" 4.06, "transaction on the public
// explorer" 5.84-7.42, "Next handover" 8.0, "wrong company" 10.5-10.98, "deliver" ~14.2. Raw take cut points come from frame-change times of the response pane.
// 28.3 = first clean frame of the handover 200 (two signers), frozen under "Both companies sign" until the 409 click.
const b7 = [[4.7, 5.8], [13.9, 2.6], [28.3, 2.1, "hold"], [34.5, 3.3, "hold"], [59.3, 0.4]];
const b7Sum = b7.reduce((t, x) => t + x[1], 0);
const B7TAIL = [66.6, Math.max(0.5, L.B7 - b7Sum)];
if (Math.abs(dur("B7") - 14.24) > 0.5) console.warn("B07.wav changed: re-check the B7 cut points against the word times");
const reveal = fr(L.B2b * 0.6);
const beats = [ // name, segments
  ["B1", [clip(1, 2, L.B1)]],
  ["B2", [clip(2, 2, L.B2)]],
  ["B2b", [[path.join(WK, "b2b-a.png"), 0, reveal], [path.join(WK, "b2b-b.png"), 0, L.B2b - reveal]]],
  ["B3", [clip(3, 2, L.B3)]],
  ["B4", [clip(4, 2, L.B4)]],
  ["B5", [clip(5, 2, L.B5)]],
  ["B6", [clip(6, 2, L.B6)]],
  ["B7", [...b7, B7TAIL].map(([s, d, h]) => [...clip(7, s, d), h])],
  ["B8", [clip(8, 2, L.B8)]],
  ["B9a", [clip(9, 25.25 - L.B9a, L.B9a)]],   // ends on the click (25.25 in the clip)
  ["B9b", [clip(9, 25.25, L.B9b)]],           // MATCH frame is 25.40 in the clip = B9b start + 0.15
  ["B10", [clip(10, 2, L.B10)]],
  ["B11", [[path.join(V2, "stills/S12.png"), 0, L.B11]]],
];
const T = {}; let acc = 0; for (const [n] of beats) { T[n] = acc; acc += L[n]; }
const TOTAL = acc, MATCH_T = T.B9b + 0.15;


const FONT = `<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">`;
const BASE = `*{box-sizing:border-box}body{margin:0;font-family:Inter,system-ui,sans-serif;-webkit-font-smoothing:antialiased}`;
const pill = (text, css, extra = "") => `${FONT}<style>${BASE}html,body{background:transparent}
  div{position:absolute;bottom:8px;${css};padding:8px 20px;border-radius:10px;background:${INK};color:${FG};font-size:24px;font-weight:600;white-space:nowrap;${extra}}</style><div>${text}</div>`;
const cap = (t) => pill(t, "right:40px", `font-size:22px;font-weight:400;color:${MUTED}`);
const OVER = {
  // B2b (31-45 s) is the Radox mainnet card: no testnet pill over it
  label: [pill("Stellar testnet · test keys", "left:40px", `border:2px solid ${LIME}`), 0, T.B2b],
  label2: [pill("Stellar testnet · test keys", "left:40px", `border:2px solid ${LIME}`), T.B3, TOTAL],
  prior: [pill("Prior work · Radox", "left:40px"), T.B2b, T.B3],
  lower: [pill("Narration: AI voice generated from Pedro's voice", "left:50%;transform:translateX(-50%)"), 0, 8],
  wto: [cap("Source: WTO, trade finance"), T.B2 + 2, T.B2b],
  b7: [cap("Live on Stellar testnet · open rail API"), T.B7, T.B8],
  b8: [cap("Stellar testnet transaction, public explorer"), T.B8, T.B9a],
};
const card = (last) => `${FONT}<style>${BASE}body{background:${INK};color:${FG};width:1920px;height:1080px;display:grid;place-content:center;text-align:center;gap:34px;padding:0 120px}</style>
  <div style="font-size:60px;font-weight:700;letter-spacing:-.02em;color:${LIME}">Radox · tokenized real-world assets on Stellar</div>
  <div style="font-size:30px;color:${MUTED};line-height:1.45">token_sale, yield_distributor, maturity_settlement · Stellar mainnet since June–July 2026 · <span style="color:${LIME}">github.com/pwsaragossy/radox</span> (contracts only)</div>
  <div style="font-size:38px;margin-top:30px;opacity:${last ? 1 : 0}">New: <b style="color:${LIME}">Radox Rail</b> · built at HackMeridian · Stellar testnet</div>`;

(async () => {
  const b = await chromium.launch({ executablePath: "/Users/pedrosaragossy/Library/Caches/ms-playwright/chromium_headless_shell-1228/chrome-headless-shell-mac-arm64/chrome-headless-shell" });
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
  const segs = beats.flatMap(([, s]) => s);
  const args = ["-v", "error", "-y"];
  for (const [f, ss, d, hold] of segs) {
    if (f.endsWith(".png")) args.push("-loop", "1", "-framerate", "30", "-t", String(d + 0.2), "-i", f);
    else args.push("-ss", String(ss), "-t", hold ? "0.1" : String(d + 0.2), "-i", f);
  }
  const ovk = Object.keys(OVER);
  for (const o of ovk) args.push("-loop", "1", "-framerate", "30", "-t", String(TOTAL), "-i", path.join(WK, o + ".png"));
  let g = segs.map(([, , d], i) => `[${i}:v]tpad=stop_mode=clone:stop_duration=5,trim=end_frame=${Math.round(d * 30)},setpts=PTS-STARTPTS,fps=30,scale=1806:1016,pad=1920:1080:57:0:color=0x0E0F11,setsar=1,format=yuv420p[s${i}];`).join("");
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
  const starts = beats.map(([n]) => (n === "B9b" ? MATCH_T + 0.3 : T[n] + 0.4));
  beats.forEach(([n]) => a.push("-i", path.join(dir, wav[n] + ".wav")));
  const af = beats.map((_, i) => `[${i + 1}:a]aresample=48000,aformat=channel_layouts=mono,adelay=${Math.round(starts[i] * 1000)}:all=1[a${i}];`).join("")
    + beats.map((_, i) => `[a${i}]`).join("") + `amix=inputs=${beats.length}:normalize=0:duration=longest,loudnorm=I=-16:TP=-1.5:LRA=7,apad=whole_dur=${TOTAL}[aout]`;
  const out = path.join(V2, "rail-demo-v2.mp4");
  execFileSync(FF, [...a, "-filter_complex", af, "-map", "0:v", "-map", "[aout]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "1", "-t", String(TOTAL), "-movflags", "+faststart", out]);
  console.log("TOTAL", TOTAL, "beats", JSON.stringify(T), "final", out, "starts", starts.join(" "));
})().catch((e) => { console.error(e); process.exit(1); });
