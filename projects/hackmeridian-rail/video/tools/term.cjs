// Replays real command output (captured to t1..t3.txt) as a terminal clip at 1920x1080.
const { chromium } = require(process.env.PW);
const fs = require("fs"), path = require("path");
const { execFileSync } = require("child_process");
const [OUT, W] = process.argv.slice(2);
const rd = (f) => fs.readFileSync(path.join(W, f), "utf8").replace(/\nrc=0\n?$/, "\n");
const short = (s) => s.replace(/head ([0-9a-f]{64})/g, (_, h) => `head ${h.slice(0, 8)}…${h.slice(-4)}`);
const CLIPS = [
  { name: "02-terminal-list", len: 20, steps: [[`jq -r '.lifecycle[] | "\\(.step)  \\(.hash[0:8])"' proofs/lifecycle.json`, rd("t1.txt")]] },
  { name: "05-terminal-verify", len: 25, steps: [["node scripts/verify-head.mjs 31b4cff7…5e37", short(rd("t2.txt"))], ["echo $?", "0\n"]] },
  { name: "06b-terminal-balance", len: 17, steps: [["stellar contract invoke --id CBCWTIT5…Q22Z --network testnet --source-account alice --send=no -- balance --id GBPFJMZ7…IGDJ", rd("t3.txt")]] },
];
const HTML = `<body style="margin:0;background:#0E0F11;color:#E7E8EA;font:30px/1.45 'JetBrains Mono',Menlo,monospace;padding:56px 64px;box-sizing:border-box;height:1080px;overflow:hidden">
<pre id="t" style="margin:0;white-space:pre-wrap;word-break:break-all;font:inherit"></pre></body>`;
(async () => {
  const b = await chromium.launch();
  for (const c of CLIPS) {
    const raw = path.join(OUT, "raw", c.name); fs.mkdirSync(raw, { recursive: true });
    const ctx = await b.newContext({ viewport: { width: 1920, height: 1080 }, recordVideo: { dir: raw, size: { width: 1920, height: 1080 } } });
    const p = await ctx.newPage(); const t0 = Date.now();
    await p.setContent(HTML);
    const start = (Date.now() - t0) / 1000;
    await p.evaluate(async (steps) => {
      const t = document.getElementById("t"), sleep = (ms) => new Promise((r) => setTimeout(r, ms));
      const prompt = () => { const s = document.createElement("span"); s.style.color = "#C6F24E"; s.textContent = "rail % "; t.append(s); };
      for (const [cmd, out] of steps) {
        prompt(); await sleep(800);
        for (const ch of cmd) { t.append(ch); await sleep(cmd.length > 80 ? 18 : 35); }
        await sleep(700); t.append("\n"); await sleep(600);
        for (const line of out.split("\n").filter(Boolean)) { t.append(line + "\n"); await sleep(120); }
        await sleep(1200);
      }
      prompt();
    }, c.steps);
    const used = (Date.now() - t0) / 1000 - start;
    await p.waitForTimeout(Math.max(0, (c.len - used) * 1000) + 500);
    const video = await p.video().path(); await ctx.close();
    execFileSync("/opt/homebrew/bin/ffmpeg", ["-v", "error", "-y", "-ss", String(start), "-i", video, "-t", String(c.len), "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-r", "30", path.join(OUT, c.name + ".mp4")]);
    console.log(c.name, c.len, "typed+output", used.toFixed(1) + "s");
  }
  await b.close();
})().catch((e) => { console.error(e); process.exit(1); });
