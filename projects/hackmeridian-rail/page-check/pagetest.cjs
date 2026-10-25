// Usage: PW=... node pagetest2.cjs <base url> [allowHost]
// Both shipments, live and offline (RPC and Horizon blocked), at 375 and 1280 px, plus a switch mid-load.
const { chromium } = require(process.env.PW);
const BASE = process.argv[2];
const state = () => ({
  pressed: [...document.querySelectorAll("#switch button")].map((b) => b.getAttribute("aria-pressed")),
  about: document.getElementById("about").textContent.slice(0, 40),
  src: document.getElementById("source").textContent,
  state: [...document.getElementById("state").children].map((r) => r.innerText.replace(/\n/g, ": ")),
  res: document.getElementById("result").textContent,
  rows: [...document.getElementById("history").children].map((l) => l.innerText.replace(/\n/g, " | ")),
  overflow: document.documentElement.scrollWidth > innerWidth,
  hash: location.hash,
});
(async () => {
  const b = await chromium.launch();
  let fail = 0;
  const cases = [];
  for (const width of [375, 1280]) for (const mode of ["live", "offline"]) for (const how of ["link", "switch"]) cases.push({ width, mode, how });
  cases.push({ width: 375, mode: "live", how: "race" });
  for (const c of cases) {
    const ctx = await b.newContext({ viewport: { width: c.width, height: 900 } });
    if (c.mode === "offline") await ctx.route(/(horizon|soroban)-testnet\.stellar\.org/, (r) => r.abort());
    const p = await ctx.newPage(); const errs = [];
    p.on("console", (m) => m.type() === "error" && errs.push(m.text()));
    p.on("pageerror", (e) => errs.push("pageerror " + e.message));
    const out = [];
    for (const s of [0, 1]) {
      const t0 = Date.now();
      if (c.how === "link") await p.goto(BASE + (s ? "#shipment-2" : ""));
      else if (c.how === "switch") { if (s === 0) await p.goto(BASE); else { await p.waitForFunction(() => !verify.disabled, null, { timeout: 30000 }); await p.click('#switch button[data-s="1"]'); } }
      else { if (s === 1) continue; await p.goto(BASE); await p.waitForTimeout(150); await p.click('#switch button[data-s="1"]'); await p.waitForTimeout(50); await p.click('#switch button[data-s="0"]'); await p.waitForTimeout(50); await p.click('#switch button[data-s="1"]'); }
      await p.waitForFunction(() => !verify.disabled, null, { timeout: 40000 });
      const ms = Date.now() - t0;
      await p.click("#verify");
      await p.waitForFunction(() => /MATCH|Could not/.test(result.textContent), null, { timeout: 20000 });
      const r = await p.evaluate(state);
      const want = c.how === "race" ? 1 : s;
      const ok = r.res.startsWith("MATCH") && !r.overflow && r.pressed[want] === "true" && r.state[0].includes(want ? "TEST6109555" : "TEST4627832")
        && (c.mode === "live" ? r.src === "Live from Stellar testnet" : r.src.startsWith("Snapshot"));
      if (!ok) fail++;
      out.push({ s: want, ms, ok, ...r });
    }
    const bad = errs.filter((e) => !/net::ERR_FAILED|Failed to load resource/.test(e));
    if (bad.length) fail++;
    console.log(JSON.stringify({ ...c, errors: bad, out }, null, 1));
    await ctx.close();
  }
  await b.close();
  console.log(fail ? `FAIL ${fail}` : "ALL PASS");
  process.exit(fail ? 1 : 0);
})().catch((e) => { console.error(e); process.exit(1); });
