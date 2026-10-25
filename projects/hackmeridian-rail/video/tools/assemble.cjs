// Lays the clips out row by row of DEMO-SCRIPT.md (3:00, 5400 frames at 30 fps), burns the overlays the script asks for
// and puts the narration under it. Usage: node assemble.cjs <outdir> <rio-miami-rail clone>
// The picture is scaled to 94% so the overlays sit in their own 64 px strip at the bottom and never cover content.
// Overlays: bottom label for the whole video; lower third 0:00-0:08; source line 0:08-0:20 (read from the 0:00 row of
// DEMO-SCRIPT.md, so a script change carries over); captions on 03c (held still) and on the README row.
const { chromium } = require(process.env.PW);
const fs = require("fs");
const path = require("path");
const { execFileSync } = require("child_process");

const OUT = process.argv[2];
const REPO = process.argv[3];
const FF = "/opt/homebrew/bin/ffmpeg";
const W = path.join(OUT, "assemble");
fs.mkdirSync(W, { recursive: true });

const script = fs.readFileSync(path.join(__dirname, "../../DEMO-SCRIPT.md"), "utf8");
const row0 = script.split("\n").find((l) => l.startsWith("| 0:00"));
const source = /source line[^"]*"([^"]+)"/.exec(row0)?.[1];
if (!source) throw new Error("no source line in the 0:00 row of DEMO-SCRIPT.md");
const commit = execFileSync("git", ["-C", REPO, "rev-parse", "--short", "origin/main"]).toString().trim();
fs.writeFileSync(path.join(W, "README.md"), execFileSync("git", ["-C", REPO, "show", "origin/main:README.md"]));
const readmeHtml = execFileSync("gh", ["api", "-X", "POST", "markdown", "-F", `text=@${path.join(W, "README.md")}`,
  "-f", "mode=gfm", "-f", "context=pwsaragossy/rio-miami-rail"]).toString();

const FONT = `<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">`;
const BASE = `*{box-sizing:border-box}body{margin:0;font-family:Inter,system-ui,sans-serif;-webkit-font-smoothing:antialiased}`;
const pill = (text, css) => `${FONT}<style>${BASE}html,body{background:transparent}
  div{position:absolute;bottom:8px;${css};padding:8px 20px;border-radius:10px;background:#0E0F11;color:#E7E8EA;font-size:24px;font-weight:600;white-space:nowrap}</style><div>${text}</div>`;
const OVER = {
  label: pill("Stellar testnet · test keys", "left:40px;border:2px solid #C6F24E"),
  lower: pill("Narration: AI voice generated from Pedro's voice", "left:50%;transform:translateX(-50%)"),
  source: pill(source, "left:50%;transform:translateX(-50%);font-weight:400;color:#A3A8B0"),
  cap03c: pill("Public page, captured 2026-10-25 17:14 UTC", "right:40px;font-size:22px;font-weight:400;color:#A3A8B0"),
  cap08: pill("Public page, recorded 2026-10-25 17:21 UTC", "right:40px;font-size:22px;font-weight:400;color:#A3A8B0"),
  cap08b: pill("Radox backend (private), local test run · recorded output, replayed · 2026-10-25 13:23 UTC", "right:40px;font-size:22px;font-weight:400;color:#A3A8B0"),
  capreadme: pill(`README.md, rio-miami-rail ${commit}, rendered by GitHub (repo private until submission)`, "right:40px;font-size:22px;font-weight:400;color:#A3A8B0"),
};
const TITLE = `${FONT}<style>${BASE}body{background:#0E0F11;color:#E7E8EA;height:1080px;display:flex;flex-direction:column;justify-content:center;padding:0 200px}
  h1{margin:0 0 90px;font-size:120px;font-weight:700;letter-spacing:-.03em}
  .c{display:flex;align-items:center;gap:40px;font-size:34px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:#A3A8B0}
  .l{flex:1;height:4px;background:#C6F24E;display:flex;justify-content:space-evenly;align-items:center}
  .l i{width:26px;height:26px;border-radius:50%;background:#C6F24E}</style>
  <h1>Radox Custody Rail</h1><div class="c"><span>Rio de Janeiro</span><span class="l"><i></i><i></i><i></i><i></i></span><span>Miami</span></div>`;
const README = `<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/github-markdown-css@5.8.1/github-markdown-dark.css">
  <style>body{margin:0;background:#0d1117}.markdown-body{max-width:1012px;margin:0 auto;padding:48px 32px}</style>
  <article class="markdown-body">${readmeHtml}</article>`;

(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  const shot = async (html, name, transparent) => {
    await p.setContent(html, { waitUntil: "networkidle" });
    await p.evaluate(() => document.fonts.ready);
    await p.screenshot({ path: path.join(W, name + ".png"), omitBackground: !!transparent });
  };
  await shot(TITLE, "title");
  for (const [k, v] of Object.entries(OVER)) await shot(v, k, true);
  // README row: the three sections the script names, 5 s each, at 125% zoom like the explorer clips
  await p.setContent(README, { waitUntil: "networkidle" });
  await p.evaluate(() => { document.documentElement.style.zoom = "1.25"; });
  for (const [i, h] of ["Prior work", "Built at HackMeridian", "AI usage"].entries()) {
    const ok = await p.evaluate((h) => {
      const el = [...document.querySelectorAll("h2")].find((e) => e.textContent.trim() === h);
      if (!el) return false;
      el.scrollIntoView({ block: "start" }); scrollBy(0, -24); return true;
    }, h);
    if (!ok) throw new Error(`README has no "${h}" section`);
    await p.screenshot({ path: path.join(W, `readme${i + 1}.png`) });
  }
  await b.close();

  const M = (f) => path.join(OUT, f);
  // [input, start frame, frames]; images are looped stills
  const segs = [
    [path.join(W, "title.png"), 0, 600],                                   // 0:00-0:20
    [M("02-terminal-list.mp4"), 0, 600],                                   // 0:20-0:40
    [M("03-explorer-handover.mp4"), 0, 270],                               // 0:40-1:05: call outlined from 5 s
    [M("03b-terminal-signers.mp4"), 149, 150],                             // last 5 s: every line printed
    [M("03c-page-shipment-2.mp4"), 0, 330],                                // 0:54-1:05, under "In a second shipment, two teammates..."
    [M("04-explorer-cuts.mp4"), 0, 600],                                   // 1:05-1:25
    [M("05-terminal-verify.mp4"), 0, 750],                                 // 1:25-1:50
    [M("06-explorer-redeem.mp4"), 0, 240],                                 // 1:50-2:15
    [M("06b-terminal-balance.mp4"), 0, 510],
    [path.join(W, "readme1.png"), 0, 150],                                 // 2:15-2:30
    [path.join(W, "readme2.png"), 0, 150],
    [path.join(W, "readme3.png"), 0, 150],
    [M("08-page-live.mp4"), 0, 240],                                       // 2:30-3:00
    [M("08b-terminal-radox-api.mp4"), 90, 120],                            // 2:38-2:42, the last 4 s: response and highlight
    [M("08-page-live.mp4"), 440, 540],                                     // back to the page at 2:42 (08 at 14.7 s): MATCH from 2:43.4, before "Verify head: match" at 2:43.6
  ];
  const at = (i) => segs.slice(0, i).reduce((s, x) => s + x[2], 0) / 30;   // segment start in seconds
  const args = ["-v", "error", "-y"];
  for (const [f] of segs) args.push(...(f.endsWith(".png") ? ["-loop", "1", "-framerate", "30", "-t", "21", "-i", f] : ["-i", f]));
  const ov = ["label", "lower", "source", "cap03c", "cap08", "cap08b", "capreadme"];
  for (const o of ov) args.push("-loop", "1", "-framerate", "30", "-t", "180", "-i", path.join(W, o + ".png"));
  args.push("-i", M("narration-full-3m00.wav"));
  let g = segs.map(([, s, n], i) =>
    `[${i}:v]trim=start_frame=${s},setpts=PTS-STARTPTS,tpad=stop_mode=clone:stop=${n},trim=end_frame=${n},setpts=PTS-STARTPTS,fps=30,scale=1806:1016,pad=1920:1080:57:0:color=0x0E0F11,setsar=1,format=yuv420p[s${i}];`).join("");
  g += segs.map((_, i) => `[s${i}]`).join("") + `concat=n=${segs.length}:v=1:a=0[v0];`;
  const when = { label: [0, 180], lower: [0, 8], source: [8, 20], cap03c: [at(4), at(5)], cap08: [at(12), 180], cap08b: [at(13), at(14)], capreadme: [at(9), at(12)] };
  ov.forEach((o, k) => {
    const [a, z] = when[o];
    g += `[v${k}][${segs.length + k}:v]overlay=0:0:enable='between(t,${a.toFixed(3)},${(z - 0.001).toFixed(3)})'[v${k + 1}];`;
  });
  g = g.replace(/;$/, "");
  const out = path.join(OUT, "rail-demo-3m00.mp4");
  args.push("-filter_complex", g, "-map", `[v${ov.length}]`, "-map", `${segs.length + ov.length}:a`, "-t", "180",
    "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-r", "30", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out);
  execFileSync(FF, args);
  console.log(`${out}\tsource line "${source}"\tREADME ${commit}\t03c ${at(4).toFixed(2)}-${at(5).toFixed(2)} s\tREADME ${at(9)}-${at(12)} s`);
})().catch((e) => { console.error(e); process.exit(1); });
