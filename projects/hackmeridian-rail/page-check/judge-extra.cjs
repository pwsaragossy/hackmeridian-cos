// The globe page's extra checks. Usage: PW=<playwright-core> node judge-extra.cjs <base url> <page dir>
// 1 reduced motion: static and complete; 2 no request outside the page and Stellar testnet; 3 added JS + data <= 200 KB gzip;
// 4 throttled 4G (150 ms RTT, 1.6 Mbps): text paints by 2.5 s and the globe is drawn by 4 s. Last line: failures.
const { chromium } = require(process.env.PW);
const fs = require("fs"); const zlib = require("zlib"); const path = require("path");
const [BASE, DIR] = process.argv.slice(2);
const ALLOW = [new URL(BASE).host, "soroban-testnet.stellar.org", "horizon-testnet.stellar.org"];
const IDLE = /^Done\. One shared record followed the test shipment/;
let fail = 0; const say = (ok, msg) => { if (!ok) fail++; console.log(ok ? "PASS" : "FAIL", msg); };
const painted = () => { const c = document.getElementById("globe"); const d = c.getContext("2d").getImageData(0, 0, c.width, c.height).data;
  let n = 0; for (let i = 3; i < d.length; i += 400) if (d[i]) n++; return n; };

(async () => {
  // 3: size of what this work added (files new to the page, gzip -9)
  const added = ["globe.js", "chains.js", "multichain.json", "vendor/d3-array.min.js", "vendor/d3-geo.min.js", "vendor/land-110m.geo.json"];
  const kb = added.reduce((n, f) => n + zlib.gzipSync(fs.readFileSync(path.join(DIR, f)), { level: 9 }).length, 0) / 1024;
  say(kb <= 200, `added JS + data ${kb.toFixed(1)} KB gzip (${added.join(", ")})`);

  const b = await chromium.launch();
  for (const width of [375, 1280]) for (const s of [0, 1]) {
    // 1: reduced motion
    const ctx = await b.newContext({ viewport: { width, height: 900 }, reducedMotion: "reduce" });
    const p = await ctx.newPage(); const outside = [];
    p.on("request", (r) => { const h = new URL(r.url()).host; if (!ALLOW.includes(h)) outside.push(r.url()); });
    await p.goto(BASE + (s ? "#shipment-2" : ""));
    await p.waitForFunction(() => !document.getElementById("verify").disabled, null, { timeout: 40000 });
    await p.waitForTimeout(800);
    const st = await p.evaluate(() => ({ cap: caption.textContent, steps: steps.children.length, done: steps.querySelectorAll("li.done").length,
      a: document.getElementById("globe").toDataURL() }));
    await p.waitForTimeout(1200);
    const still = (await p.evaluate(() => document.getElementById("globe").toDataURL())) === st.a;
    const px = await p.evaluate(painted);
    say(IDLE.test(st.cap) && st.steps > 0 && st.done === st.steps && still && px > 50,
      `reduced motion ${width}px shipment ${s + 1}: ${st.done}/${st.steps} steps lit, final caption, canvas still ${still}, drawn ${px}`);
    await p.click("#verify");
    await p.waitForFunction(() => /MATCH|Could not/.test(result.textContent), null, { timeout: 20000 });
    say((await p.textContent("#result")).startsWith("MATCH"), `reduced motion ${width}px shipment ${s + 1}: Verify head MATCH`);
    // 2: nothing fetched from a CDN or any other host
    say(!outside.length, `no outside requests ${width}px shipment ${s + 1}${outside.length ? ": " + outside.join(" ") : ""}`);
    await ctx.close();
  }
  // full motion: the story plays and ends lit
  { const p = await b.newPage({ viewport: { width: 375, height: 812 } });
    // v2: the story is driven by scroll, so scroll to the last step
    await p.goto(BASE); await p.waitForFunction(() => steps.children.length > 0, null, { timeout: 40000 });
    await p.evaluate(() => steps.lastElementChild.scrollIntoView({ block: "center" }));
    await p.waitForFunction(() => /^Done\./.test(caption.textContent), null, { timeout: 10000 });
    const done = await p.evaluate(() => [steps.querySelectorAll("li.done").length, steps.children.length]);
    say(done[0] === done[1], `motion 375px: story ends with ${done[0]}/${done[1]} steps lit`); await p.close(); }
  // 4: throttled 4G, cold cache
  { const ctx = await b.newContext({ viewport: { width: 375, height: 812 } }); const p = await ctx.newPage();
    const cdp = await ctx.newCDPSession(p);
    await cdp.send("Network.enable"); await cdp.send("Network.setCacheDisabled", { cacheDisabled: true });
    await cdp.send("Network.emulateNetworkConditions", { offline: false, latency: 150, downloadThroughput: 1.6e6 / 8, uploadThroughput: 750e3 / 8 });
    const t0 = Date.now(); await p.goto(BASE, { waitUntil: "commit" });
    await p.waitForFunction(() => performance.getEntriesByName("first-contentful-paint").length, null, { timeout: 30000 });
    const fcp = await p.evaluate(() => performance.getEntriesByName("first-contentful-paint")[0].startTime);
    const h1 = await p.evaluate(() => !!document.querySelector("h1")?.textContent);
    await p.waitForFunction(painted, null, { timeout: 30000, polling: 100 }); const globe = Date.now() - t0;
    say(fcp <= 2500 && h1, `4G: first contentful paint ${Math.round(fcp)} ms with the headline`);
    say(globe <= 4000, `4G: globe drawn ${globe} ms after navigation`);
    await ctx.close(); }
  await b.close();
  console.log(fail ? `FAIL ${fail}` : "ALL PASS");
  console.log(fail);
  process.exit(fail ? 1 : 0);
})().catch((e) => { console.error(e); process.exit(1); });
