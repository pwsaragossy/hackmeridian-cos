// Records the browser clips of DEMO-SCRIPT.md at 1920x1080. Usage: node record.cjs <outdir> [clip...]
const { chromium } = require(process.env.PW);
const fs = require("fs");
const path = require("path");
const { execFileSync } = require("child_process");

const OUT = process.argv[2];
const ONLY = process.argv.slice(3);
const EXP = "https://stellar.expert/explorer/testnet/tx/";
const PAGE = "https://rio-miami-rail.vercel.app";
const TX = {
  h1: "635c99ac73cb13416e6b52f29ac9a067fbc615e01b8de962eb36245db3f0bd38",
  attest: "333792115c7a93abdbf4a45dc217b4bb332c69d14f95095d7d0dffc9d0068905",
  deliver: "919def8c0b3f29ae650f5f1ea6d632e49efd4a9442381c84c83d858ad2144e37",
  h2: "56a0f006e337",
  h3: "ac268a49e00d",
  h4: "5199d4fb6b28",
  redeem: "864fd1644d30bf708a59f94ca5b0fc303a50deccfd96099bd32dfb67e215644d",
};
const full = JSON.parse(fs.readFileSync(path.join(__dirname, "hashes.json")));

// lime cursor dot, since headless video has none
const CURSOR = `addEventListener('DOMContentLoaded', () => {
  const d = document.createElement('div');
  d.style.cssText = 'position:fixed;left:-50px;top:-50px;width:28px;height:28px;margin:-14px 0 0 -14px;border-radius:50%;background:#C6F24E;border:3px solid #0E0F11;z-index:2147483647;pointer-events:none;transition:transform .15s';
  document.body.append(d);
  addEventListener('mousemove', (e) => { d.style.left = e.clientX + 'px'; d.style.top = e.clientY + 'px'; });
  addEventListener('mousedown', () => d.style.transform = 'scale(.7)');
  addEventListener('mouseup', () => d.style.transform = '');
});`;

const wait = (p, ms) => p.waitForTimeout(ms);
const zoom = (p, z) => p.evaluate((z) => { document.documentElement.style.zoom = z; }, z);

async function explorer(p, hash, z = "1.875") {
  for (let i = 0; ; i++) {
    await p.goto(EXP + hash, { waitUntil: "networkidle", timeout: 60000 });
    try { await p.getByText("Successful").first().waitFor({ timeout: 30000 }); break; }
    catch (e) { if (i === 5) throw e; await p.waitForTimeout(5000); }                                      // the explorer sometimes renders empty; reload
  }
  await zoom(p, z);
  await p.evaluate(() => document.fonts.ready);
}

// outline the contract call line and centre it
const markCall = (p) => p.evaluate(() => {
  const els = [...document.querySelectorAll("body *")].filter((e) => /invoked contract/.test(e.innerText || ""));
  const el = els[els.length - 1];
  el.style.outline = "4px solid #C6F24E";
  el.style.outlineOffset = "6px";
  // bottom of the frame, so the Signatures box (operator only) stays out of shot
  el.scrollIntoView({ block: "end" });
  scrollBy({ top: -90, behavior: "instant" });
});

async function verify(p) {
  await p.waitForFunction(() => !document.getElementById("verify").disabled, null, { timeout: 30000 });
}

const CLIPS = {
  // 0:40-1:05, 25 s
  "03-explorer-handover": { len: 25, run: async (p, ready) => {
    await explorer(p, TX.h1); ready();
    await wait(p, 5000);
    await markCall(p);
    await wait(p, 20500);
  } },
  // 0:40-1:05, replaces the 03c terminal clip at the same 119 frames: shipment 2 on the page, keys per handover and MATCH.
  // A held still of the live page: the frame does not move, and a still cannot be trimmed before the framing.
  "03c-page-shipment-2": { still: true, frames: 119, run: async (p, ready, png) => {
    await p.goto(PAGE + "/#shipment-2", { waitUntil: "networkidle" });
    await verify(p);
    const src = await p.textContent("#source");
    if (!src.startsWith("Live from Stellar testnet")) throw new Error(`source says "${src}"`);
    await p.click("#verify");
    await p.getByText("MATCH", { exact: true }).waitFor({ timeout: 10000 });
    await zoom(p, "1.5");
    await p.evaluate(() => {
      document.querySelector("body > div:last-child[style*='pointer-events']")?.remove();   // no cursor dot: nothing is clicked on screen
      document.getElementById("result").scrollIntoView({ block: "end" });
      scrollBy({ top: 15, behavior: "instant" });
    });
    await p.evaluate(() => document.fonts.ready);
    await wait(p, 500);
    await p.screenshot({ path: png });
    return p.textContent("#result");
  } },
  // 1:05-1:25, 20 s: attest 8, deliver 8, three handovers 1.33 each (joined after recording)
  "04a-attest": { len: 8, part: true, run: async (p, ready) => { await explorer(p, TX.attest); ready(); await markCall(p); await wait(p, 8500); } },
  "04b-deliver": { len: 8, part: true, run: async (p, ready) => { await explorer(p, TX.deliver); ready(); await markCall(p); await wait(p, 8500); } },
  "04c-h2": { len: 1.333, part: true, run: async (p, ready) => { await explorer(p, full.h2); ready(); await wait(p, 2000); } },
  "04d-h3": { len: 1.333, part: true, run: async (p, ready) => { await explorer(p, full.h3); ready(); await wait(p, 2000); } },
  "04e-h4": { len: 1.334, part: true, run: async (p, ready) => { await explorer(p, full.h4); ready(); await wait(p, 2000); } },
  // 1:50-1:58, 8 s
  "06-explorer-redeem": { len: 8, run: async (p, ready) => {
    await explorer(p, TX.redeem); ready();
    await markCall(p);
    await wait(p, 8500);
  } },
  // 2:30-3:00, 30 s; 08b-terminal-radox-api covers 8-15 s (2:38-2:45); click at 17 s (2:47), hold MATCH to the end
  "08-page-live": { len: 30, run: (p, ready) => pageTake(p, ready, "Live from Stellar testnet") },
  // same take with RPC and Horizon blocked
  "09-page-snapshot": { len: 30, block: true, run: (p, ready) => pageTake(p, ready, "Snapshot, not live") },
};

async function pageTake(p, ready, expect) {
  await p.goto(PAGE, { waitUntil: "networkidle" });
  await verify(p);
  const src = await p.textContent("#source");
  if (!src.startsWith(expect)) throw new Error(`source says "${src}", expected "${expect}"`);
  await zoom(p, "2.25");
  await p.evaluate(() => document.fonts.ready);
  await p.mouse.move(1500, 300);
  ready();
  await wait(p, 5000);                                                      // label, source, h1
  await p.evaluate(() => document.getElementById("source").scrollIntoView({ block: "start", behavior: "smooth" }));
  await wait(p, 3000);                                                      // container, status, handovers (to 8 s)
  await p.evaluate(() => document.querySelector("h2").scrollIntoView({ block: "start", behavior: "smooth" }));
  await wait(p, 3500);                                                      // under the 08b overlay
  await p.evaluate(() => document.getElementById("verify").scrollIntoView({ block: "center", behavior: "smooth" }));
  await wait(p, 3500);                                                      // Verify head in view at 15 s
  const b = await p.locator("#verify").boundingBox();
  await p.mouse.move(b.x + b.width / 2, b.y + b.height / 2, { steps: 25 });
  await wait(p, 1000);
  await p.mouse.click(b.x + b.width / 2, b.y + b.height / 2);
  await p.getByText("MATCH", { exact: true }).waitFor({ timeout: 10000 });
  await p.evaluate(() => document.getElementById("result").scrollIntoView({ block: "center", behavior: "smooth" }));
  await wait(p, 14500);
  return p.textContent("#result");
}

(async () => {
  const b = await chromium.launch();
  const log = [];
  for (const [name, c] of Object.entries(CLIPS)) {
    if (ONLY.length && !ONLY.includes(name)) continue;
    const raw = path.join(OUT, "raw", name);
    fs.mkdirSync(raw, { recursive: true });
    const ctx = await b.newContext({ viewport: { width: 1920, height: 1080 }, recordVideo: { dir: raw, size: { width: 1920, height: 1080 } } });
    await ctx.addInitScript(CURSOR);
    if (c.block) await ctx.route(/(horizon|soroban)-testnet\.stellar\.org/, (r) => r.abort());
    const t0 = Date.now();
    let start = 0;
    const p = await ctx.newPage();
    const png = path.join(raw, `${name}.png`);
    const res = await c.run(p, () => { start = (Date.now() - t0) / 1000; }, png);
    const video = await p.video().path();
    await ctx.close();
    const out = path.join(c.part ? path.join(OUT, "raw") : OUT, `${name}.mp4`);
    const input = c.still ? ["-loop", "1", "-framerate", "30", "-i", png, "-frames:v", String(c.frames)] : ["-ss", String(start), "-i", video, "-t", String(c.len)];
    execFileSync("/opt/homebrew/bin/ffmpeg", ["-v", "error", "-y", ...input, "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-r", "30", out]);
    log.push(`${name}\t${c.still ? c.frames + " frames, still" : c.len + "s"}\tstart ${start.toFixed(2)}s${res ? "\t" + res.trim() : ""}`);
    console.log(log[log.length - 1]);
  }
  await b.close();
  if (!ONLY.length || ONLY.some((n) => n.startsWith("04"))) {
    const parts = Object.keys(CLIPS).filter((n) => n.startsWith("04")).map((n) => `file '${path.join(OUT, "raw", n + ".mp4")}'`);
    fs.writeFileSync(path.join(OUT, "raw", "04.txt"), parts.join("\n"));
    execFileSync("/opt/homebrew/bin/ffmpeg", ["-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", path.join(OUT, "raw", "04.txt"), "-c", "copy", path.join(OUT, "04-explorer-cuts.mp4")]);
  }
})().catch((e) => { console.error(e); process.exit(1); });
