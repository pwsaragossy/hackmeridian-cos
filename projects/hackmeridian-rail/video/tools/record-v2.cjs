// Records the screen clips of the video plan v2 (VIDEO-PLAN.md) at 1920x1080, 30 fps.
// Usage: PW=<playwright-core dir> node record-v2.cjs <outroot> [clip...]   (MOCK=1 fakes the /docs sandbox API: rehearsal, no opens used)
// Clips: b1 b2 b3 b4 b5 b6 b9 b10 b8 b7 end   (b1..b6 = landing scenes 0..5, b9 = scene 6 live, b10 = scene 7)
// Output: <outroot>/clips/*.mp4, <outroot>/stills/S*.png, <outroot>/raw/ (webm takes). Media stays outside ~/hackmeridian.
// Landing runs at a 1536x864 viewport (page zoom 125%: body text 26 px, labels 16 px in the 1080 frame), device scale 1.25,
// so stills are sharp 1920x1080 and the video (frames are CSS-pixel sized) is scaled up 1.25x with lanczos.
const { chromium } = require(process.env.PW);
const fs = require("fs");
const path = require("path");
const { execFileSync } = require("child_process");

const OUT = process.argv[2];
const ONLY = process.argv.slice(3);
const FF = "/opt/homebrew/bin/ffmpeg";
const PAGE = "https://rio-miami-rail.vercel.app";
const EXP = "https://stellar.expert/explorer/testnet/tx/";
const TX8 = "9214980ea8f3923ca0e036a803517dba2b3d1c1a12d8e5cbb481f31625eb7c0c";
const MOCK = !!process.env.MOCK;
const GL = process.env.GL === "sw"
  ? ["--use-gl=angle", "--use-angle=swiftshader", "--enable-unsafe-swiftshader", "--ignore-gpu-blocklist"]
  : ["--use-angle=metal", "--ignore-gpu-blocklist", "--enable-gpu"];
for (const d of ["clips", "stills", "raw"]) fs.mkdirSync(path.join(OUT, d), { recursive: true });

const CURSOR = `addEventListener('DOMContentLoaded', () => {
  const d = document.createElement('div');
  d.id = '__cur'; d.style.cssText = 'position:fixed;left:-50px;top:-50px;width:28px;height:28px;margin:-14px 0 0 -14px;border-radius:50%;background:#C6F24E;border:3px solid #0E0F11;z-index:2147483647;pointer-events:none;transition:transform .15s';
  document.body.append(d);
  addEventListener('mousemove', (e) => { d.style.left = e.clientX + 'px'; d.style.top = e.clientY + 'px'; });
  addEventListener('mousedown', () => d.style.transform = 'scale(.7)');
  addEventListener('mouseup', () => d.style.transform = '');
});`;
// scene 7: hide ONLY the paragraph that names ZIS, Cisbra and Camacol (first <p> under the h2); headline, aside and chips stay
const HIDE7 = `section[data-ch="7"] h2 + p { display: none !important; }`;

const wait = (p, ms) => p.waitForTimeout(ms);
const zoom = (p, z) => p.evaluate((z) => { document.documentElement.style.zoom = z; }, z);
async function slowMove(p, from, to, ms) {            // cursor glide, ~40 ms per step
  const n = Math.max(2, Math.round(ms / 40));
  for (let i = 1; i <= n; i++) {
    const t = i / n, e = t * t * (3 - 2 * t);
    await p.mouse.move(from[0] + (to[0] - from[0]) * e, from[1] + (to[1] - from[1]) * e);
    await wait(p, ms / n);
  }
}
const smoothScroll = (p, y, ms) => p.evaluate(([y, ms]) => new Promise((res) => {   // eased scroll, ms long
  const y0 = scrollY, t0 = performance.now();
  const step = (now) => { const t = Math.min(1, (now - t0) / ms), e = t * t * (3 - 2 * t); scrollTo({ top: y0 + (y - y0) * e, behavior: "instant" }); t < 1 ? requestAnimationFrame(step) : res(); };
  requestAnimationFrame(step);
}), [y, ms]);

// run one clip: fn(p, h) calls h.ready() when the clip starts and h.end() when it ends
async function take(b, name, o, fn) {
  const raw = path.join(OUT, "raw", name);
  fs.rmSync(raw, { recursive: true, force: true }); fs.mkdirSync(raw, { recursive: true });
  const ctx = await b.newContext({ viewport: { width: o.vw, height: o.vh }, deviceScaleFactor: o.dsf || 1, recordVideo: { dir: raw, size: { width: o.vw, height: o.vh } } });
  await ctx.addInitScript(CURSOR);
  const p = await ctx.newPage();
  const t0 = Date.now(), now = () => (Date.now() - t0) / 1000;
  const h = { t: {}, now, log: [], ready() { h.t.start = now(); }, end() { h.t.end = now(); },
    async still(n) { await p.screenshot({ path: path.join(OUT, "stills", n + ".png") }); h.log.push(`${n} at ${now().toFixed(1)}s`); } };
  let res;
  try { res = await fn(p, h, ctx); } finally { /* keep going to save the video */ }
  const video = await p.video().path();
  await ctx.close();
  const out = path.join(OUT, "clips", `${name}.mp4`);
  if (!o.noEncode) {
    encode(video, h.t.start, h.t.end - h.t.start, o.vw === 1920 ? null : "scale=1920:1080:flags=lanczos", out);
    const dur = execFileSync("/opt/homebrew/bin/ffprobe", ["-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", out]).toString().trim();
    console.log(`${name}\t${(h.t.end - h.t.start).toFixed(2)} s planned\t${(+dur).toFixed(2)} s file\t${h.log.join("; ")}`);
  }
  return { h, video, res, t0 };
}
function encode(video, ss, len, vf, out) {
  execFileSync(FF, ["-v", "error", "-y", "-ss", String(ss), "-i", video, "-t", String(len), ...(vf ? ["-vf", vf] : []), "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "17", "-preset", "slow", "-r", "30", "-an", out]);
}

// ---------- landing ----------
const LAND = { vw: 1536, vh: 864, dsf: 1.25 };
const LAND15 = { vw: 1280, vh: 720, dsf: 1.5 };                            // the API cards (B6, B9): page zoom 150%, card text 21 px
async function openLanding(p, n) {
  await p.goto(PAGE, { waitUntil: "networkidle" });
  await p.addStyleTag({ content: HIDE7 });
  await p.evaluate(() => document.fonts.ready);
  await p.evaluate(() => { document.documentElement.style.scrollBehavior = "auto"; });
  await wait(p, 1200);                                                      // globe dots and fonts settled
  if (n > 0) await p.evaluate((n) => document.querySelectorAll(".ch")[n].scrollIntoView({ behavior: "instant", block: "start" }), n);
}
const until = (p, h, sec) => wait(p, Math.max(0, (sec - (h.now() - h.t.start)) * 1000));
const noZis = (p) => p.evaluate(() => /ZIS|Cisbra|Camacol/.test(document.body.innerText));

// scene n, beat seconds, pad 2 s each end; still taken mid-beat
const SCENE = { b1: [0, 19, "S01"], b2: [1, 12, "S02"], b3: [2, 12, "S03"], b4: [3, 13, "S04"], b5: [4, 10, "S05"], b10: [7, 16, "S11"] };
function sceneClip(name) {
  const [n, beat, still] = SCENE[name];
  return (b) => take(b, name, LAND, async (p, h) => {
    await openLanding(p, n);
    h.ready();
    await until(p, h, 2 + beat / 2);
    await h.still(still);
    if (await noZis(p)) throw new Error("ZIS/Cisbra/Camacol text is visible");
    await until(p, h, 4 + beat);
    h.end();
  });
}

// B6, scene 5: slow taps, stop before the 4th handover completes (that would show the simulated GET COFFEE-0042 card)
const b6 = (b) => take(b, "b6", LAND15, async (p, h) => {
  await openLanding(p, 5);
  const A = await p.locator("#d-a").boundingBox(), B = await p.locator("#d-b").boundingBox();
  let pos = [A.x + A.width + 160, A.y - 160];
  await p.mouse.move(...pos);
  h.ready();
  await wait(p, 2200);
  const at = (bb) => [bb.x + bb.width * 0.86, bb.y + bb.height / 2];
  for (let i = 0; i < 7; i++) {                                              // a b a b a b a: three handovers done, the fourth half signed
    const bb = await p.locator(i % 2 ? "#d-b" : "#d-a").boundingBox();
    await slowMove(p, pos, at(bb), 800); pos = at(bb);
    await p.mouse.down(); await wait(p, 90); await p.mouse.up();
    if (i === 3) await h.still("S06");
    await wait(p, 900);
  }
  if (await p.locator("#d-read").isVisible()) throw new Error("simulated GET card is visible");
  await until(p, h, 18);
  h.end();
});

// B9, scene 6, read live. hold top 9 s (7 + pad), scroll the signers list 10 s, cursor to the button 5 s, click, hold MATCH 15 s
const b9 = (b) => take(b, "b9", LAND15, async (p, h) => {
  await p.goto(PAGE, { waitUntil: "networkidle" });
  await p.waitForFunction(() => !document.getElementById("verify").disabled, null, { timeout: 40000 });
  const src = (await p.textContent("#source")).trim();
  h.log.push(`source "${src}"`);
  if (!src.startsWith("Live from Stellar testnet")) throw new Error(`not live: ${src}`);
  await p.addStyleTag({ content: HIDE7 });
  await p.evaluate(() => { document.documentElement.style.scrollBehavior = "auto"; document.querySelectorAll(".ch")[6].scrollIntoView({ behavior: "instant", block: "start" }); });
  await wait(p, 800);
  await p.mouse.move(1180, 200);
  h.ready();
  await wait(p, 6000);
  await h.still("S09");
  await wait(p, 3000);                                                       // 9 s: top of the card
  // scroll through the list: card top to the button
  const geo = await p.evaluate(() => {
    const hi = document.getElementById("history").getBoundingClientRect(), v = document.getElementById("verify").getBoundingClientRect();
    return { histTop: hi.top + scrollY, histBottom: hi.bottom + scrollY, vTop: v.top + scrollY, vBottom: v.bottom + scrollY, y: scrollY, vh: innerHeight };
  });
  h.log.push(JSON.stringify(geo));
  const yEnd = Math.max(geo.y, Math.min(geo.vBottom + 150 - geo.vh, geo.histBottom - 150));
  await smoothScroll(p, geo.y + (yEnd - geo.y) * 0.5, 5000);
  await smoothScroll(p, yEnd, 5000);                                         // 19 s
  const vb = await p.locator("#verify").boundingBox();
  const target = [vb.x + vb.width / 2, vb.y + vb.height / 2];
  await slowMove(p, [1180, 200], target, 5000);                              // 24 s
  const click = h.now() - h.t.start;
  await p.mouse.down(); await wait(p, 100); await p.mouse.up();
  fs.writeFileSync(path.join(OUT, "clips", "b9-click.txt"), `click at ${click.toFixed(2)} s from the start of clips/b9.mp4 (B9a beat starts at 2.0 s, so ${(click - 2).toFixed(2)} s into the beat)\n`);
  await p.getByText("MATCH", { exact: true }).waitFor({ timeout: 20000 });
  const m = h.now() - h.t.start;
  h.log.push(`click ${click.toFixed(2)} s, MATCH seen ${m.toFixed(2)} s`);
  await wait(p, 800);
  await smoothScroll(p, (await p.evaluate(() => scrollY)) + 150, 1200);       // MATCH row clear of the bottom edge
  await wait(p, 500);
  await h.still("S10");
  await wait(p, 13500);
  h.end();
  fs.appendFileSync(path.join(OUT, "clips", "b9-click.txt"), `MATCH on screen at ${m.toFixed(2)} s; clip ends ${(h.t.end - h.t.start).toFixed(2)} s; result: ${(await p.textContent("#result")).trim()}\n`);
});

// ---------- explorer, B8 ----------
const b8 = (b) => take(b, "b8", { vw: 1920, vh: 1080 }, async (p, h) => {
  for (let i = 0; ; i++) {
    await p.goto(EXP + TX8, { waitUntil: "networkidle", timeout: 60000 });
    try { await p.getByText("Successful").first().waitFor({ timeout: 30000 }); break; } catch (e) { if (i === 5) throw e; await wait(p, 5000); }
  }
  await zoom(p, "1.875");
  await p.evaluate(() => document.fonts.ready);
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 600);
  h.ready();
  await wait(p, 4000);
  await h.still("S08");
  await wait(p, 1000);
  await p.evaluate(() => {                                                  // outline the call and put it at the bottom, Signatures box out of shot
    const els = [...document.querySelectorAll("body *")].filter((e) => /invoked contract/.test(e.innerText || ""));
    const el = els[els.length - 1];
    el.style.outline = "4px solid #C6F24E"; el.style.outlineOffset = "6px";
    el.scrollIntoView({ block: "end" }); scrollBy({ top: -90, behavior: "instant" });
  });
  await wait(p, 8000);
  const txt = await p.evaluate(() => document.body.innerText);
  h.log.push(`GDWN…TPPW ${/GDWN\S*TPPW/.test(txt)}, GAUK…CEFR ${/GAUK\S*CEFR/.test(txt)}`);
  h.end();
});

// ---------- B7: /docs "Try the API", live ----------
function mockApi(ctx) {
  let seq = 0, status = "Open";
  const hash = () => [...Array(64)].map(() => "0123456789abcdef"[Math.random() * 16 | 0]).join("");
  const KEY = "ab".repeat(32), REG = "C" + "A".repeat(55);
  return ctx.route(/\/api\/sandbox\//, async (r) => {
    await new Promise((s) => setTimeout(s, 1500));
    const u = r.request().url(), body = r.request().postData();
    const ship = () => ({ key: KEY, registry: REG, status, seq });
    let j, code = 200;
    if (u.endsWith("/shipments")) { seq = 0; status = "Open"; const h = hash(); j = { call: "open", shipment: ship(), tx: { hash: h, explorer: EXP + h } }; }
    else if (u.endsWith("/handover") && body) { code = 409; j = { error: { code: "E_WRONG_CUSTODIAN", message: "The company handing over is not the one holding the shipment.", refused_by: "custody_registry" } }; }
    else if (u.endsWith("/handover")) { seq++; const h = hash(); j = { call: "handover", shipment: ship(), tx: { hash: h, explorer: EXP + h } }; }
    else { status = "Delivered"; const h = hash(); j = { call: "deliver", shipment: ship(), tx: { hash: h, explorer: EXP + h } }; }
    await r.fulfill({ status: code, contentType: "application/json", body: JSON.stringify(j) });
  });
}

const b7 = (b) => take(b, "b7", { vw: 1920, vh: 1080, noEncode: true }, async (p, h, ctx) => {
  const hashes = [], seen = [];
  if (MOCK) await mockApi(ctx);
  p.on("response", async (r) => {
    if (!/\/api\/(sandbox|shipments)/.test(r.url()) || r.request().method() === "OPTIONS") return;
    try { const j = await r.json(); seen.push(`${h.now().toFixed(1)}s ${r.request().method()} ${new URL(r.url()).pathname.replace(/[0-9a-f]{64}/, "<key>")} ${r.status()}${j.error ? " " + j.error.code : ""}${j.tx?.hash ? " tx " + j.tx.hash : ""}`); if (j.tx?.hash) hashes.push(`${j.call}\t${j.tx.hash}`); } catch {}
  });
  await p.goto(PAGE + "/docs", { waitUntil: "networkidle" });
  await zoom(p, "1.5");
  await p.evaluate(() => document.fonts.ready);
  await p.evaluate(() => { document.querySelector("#try").scrollIntoView({ block: "start" }); scrollBy({ top: -125, behavior: "instant" }); });
  await wait(p, 500);
  const click = async (sel) => { const bb = await p.locator(sel).boundingBox(); const to = [bb.x + bb.width / 2, bb.y + bb.height / 2]; await slowMove(p, cur, to, 600); cur = to; await p.mouse.down(); await wait(p, 80); await p.mouse.up(); };
  let cur = [1500, 700];
  await p.mouse.move(...cur);
  const done = (ms = 60000) => p.waitForFunction(() => document.querySelector("#t-tx a, #t-tx strong") && !document.querySelector("#t-tx .wait"), null, { timeout: ms });
  const TR = { open: 0, link: 0, popup: 0, popupEnd: 0 };
  h.ready();
  await wait(p, 2000);
  TR.open = h.now() - h.t.start;
  await click("#b-open");
  await p.waitForFunction(() => document.querySelector("#t-tx a"), null, { timeout: 60000 });
  await wait(p, 2500);
  await h.still("S07");
  // the explorer link opens a second tab: it has its own video, joined in after the take
  const bb = await p.locator("#t-tx a").boundingBox(), to = [bb.x + bb.width / 2, bb.y + bb.height / 2];
  await slowMove(p, cur, to, 700); cur = to;
  const href = await p.locator("#t-tx a").getAttribute("href");
  h.log.push(`link ${href}`);
  const popupP = ctx.waitForEvent("page", { timeout: 8000 }).catch(() => null);
  TR.link = h.now() - h.t.start;
  await p.mouse.down(); await wait(p, 80); await p.mouse.up();
  let pop = await popupP;
  if (!pop) { h.log.push("popup did not open from the click: opened the same link in a new tab"); pop = await ctx.newPage(); await pop.goto(href).catch(() => {}); }
  const popStart = h.now();
  await pop.setViewportSize({ width: 1920, height: 1080 });
  for (let i = 0; i < 6; i++) {
    try { await pop.getByText("Successful").first().waitFor({ timeout: 25000 }); break; }
    catch { await pop.reload({ waitUntil: "networkidle" }).catch(() => {}); }
  }
  await zoom(pop, "1.875"); await pop.evaluate(() => document.fonts.ready);
  const popShown = h.now();
  await wait(pop, 4500);
  const popHash = pop.url().split("/").pop();
  TR.popup = popShown - popStart; TR.popupEnd = TR.popup + 4.5;
  const popVideoP = pop.video().path();
  await pop.close();
  await p.bringToFront();
  const popBack = h.now();
  await wait(p, 800);
  const step = async (sel, hold) => { await click(sel); await done(); await wait(p, hold); };
  await step("#b-hand", 2500);
  await click("#b-wrong"); await done(); await wait(p, 4500);              // 409 E_WRONG_CUSTODIAN
  const wrongSeen = await p.textContent("#t-status");
  for (let i = 0; i < 3; i++) await step("#b-hand", 1800);
  await step("#b-deliver", 3500);
  await wait(p, 1500);
  h.end();
  const popVideo = await popVideoP;
  fs.writeFileSync(path.join(OUT, "clips", "b7-hashes.txt"), `# B7 take, ${new Date().toISOString()}${MOCK ? " (MOCK, not real)" : ""}\n${hashes.join("\n")}\n# explorer tab showed tx ${popHash}\n# api log\n${seen.join("\n")}\n`);
  h.log.push(`wrong-company status "${wrongSeen.trim()}"`, `hashes ${hashes.length}`);
  return { TR, popVideo, popStart, popShown, popBack, popEndAbs: popBack };
});

// join: docs up to the link click, the explorer tab 4.5 s, docs from the return. B7 raw docs video is trimmed at the same offsets
async function joinB7(r) {
  const { h, video, res } = r, st = h.t.start;
  const pad = 0.4, seg = (src, ss, len, f) => { const o = path.join(OUT, "raw", `b7-seg-${f}.mp4`); encode(src, ss, len, null, o); return o; };
  const a = seg(video, st, res.TR.link + pad, "a");                                    // docs: start .. link click (+0.4 s)
  const e = seg(res.popVideo, res.popShown - res.popStart, 4.5, "e");                    // explorer tab, summary visible
  const c = seg(video, res.popBack + 0.0, h.t.end - res.popBack, "c");                   // docs after returning
  const list = path.join(OUT, "raw", "b7.txt");
  fs.writeFileSync(list, [a, e, c].map((f) => `file '${f}'`).join("\n"));
  const out = path.join(OUT, "clips", "b7.mp4");
  execFileSync(FF, ["-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", list, "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "17", "-r", "30", out]);
  const dur = execFileSync("/opt/homebrew/bin/ffprobe", ["-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", out]).toString().trim();
  console.log(`b7\t${(+dur).toFixed(2)} s file (docs ${(res.TR.link + pad).toFixed(1)} s + explorer 4.5 s + docs ${(h.t.end - res.popBack).toFixed(1)} s)\t${h.log.join("; ")}`);
}

// ---------- B11 end card (still only; the edit builds the clip) ----------
const end = async (b) => {
  const ctx = await b.newContext({ viewport: { width: 1920, height: 1080 } });
  const p = await ctx.newPage();
  await p.setContent(`<body style="margin:0;background:#0E0F11;color:#E8E9EB;font-family:Inter,system-ui,sans-serif;width:1920px;height:1080px;display:grid;place-content:center;text-align:center;gap:34px">
  <div style="font-size:60px;font-weight:700;letter-spacing:-.02em;color:#C6F24E">Built at HackMeridian</div>
  <div style="font-size:38px;line-height:1.4">custody_registry contract, 26 tests, verification scripts, this page</div>
  <div style="font-size:30px;color:#A8ABB0;margin-top:20px">Prior work: Radox platform, transfer_agent contract</div>
  <div style="font-size:32px;margin-top:30px">Open source, Apache-2.0 · <span style="color:#C6F24E">github.com/pwsaragossy/rio-miami-rail</span> · rio-miami-rail.vercel.app</div></body>`);
  await p.screenshot({ path: path.join(OUT, "stills", "S12.png") });
  await ctx.close();
  console.log("end\tS12.png");
};

const JOBS = { b1: sceneClip("b1"), b2: sceneClip("b2"), b3: sceneClip("b3"), b4: sceneClip("b4"), b5: sceneClip("b5"), b6, b10: sceneClip("b10"), b9, b8,
  b7: async (b) => joinB7(await b7(b)), end };
(async () => {
  const b = await chromium.launch({ args: GL });
  for (const [name, job] of Object.entries(JOBS)) {
    if (ONLY.length ? !ONLY.includes(name) : name === "b7") continue;      // b7 uses real opens: only when asked by name
    try { await job(b); } catch (e) { console.error(name, "FAILED", e.message); }
  }
  await b.close();
})();
