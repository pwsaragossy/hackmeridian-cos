"""Build deck/yc/radox-custody-rail-yc.pdf: minimalist deck, YC design rules ([[yc-pitch-deck-design-rules-kevin-bd35]]).

Run: python3 deck/yc/build.py [--png]   (needs Google Chrome; --png also needs pdftoppm)
One idea per slide, the headline is the line a judge repeats. Radox Signal tokens only (LANDING-V2-BRIEF.md "Design").
Every number on a slide is traced in check.py (TRACE). Story and title follow FORM-ANSWERS.md.
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(HERE, "deck.html")
PDF = os.path.join(HERE, "radox-custody-rail-yc.pdf")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
CONTRACT = "CCBJVXMJYWPHTDJHDFPRGKPGXGEP24JOPJAMUS5C3BMZJTRTWR2H4LII"
ROUTE = ["Warehouse", "Port", "Carrier", "Customs", "Buyer"]

CSS = """
@page { size: 1920px 1080px; margin: 0; }
:root { --bg:#0E0F11; --fg:#E7E8EA; --card:#131517; --muted:#8A8F98; --soft:#C8CBD0; --faint:#7F848E;
        --border:#1F2329; --border-h:#303740; --lime:#C6F24E; }
* { box-sizing:border-box; margin:0; padding:0; }
html, body { background:var(--bg); }
body { font-family:'Inter', sans-serif; color:var(--fg); -webkit-font-smoothing:antialiased; }
section { width:1920px; height:1080px; padding:110px 128px 96px; position:relative; overflow:hidden;
          page-break-after:always; display:flex; flex-direction:column; background:var(--bg); }
.kicker { font-size:28px; font-weight:600; letter-spacing:.14em; text-transform:uppercase; color:var(--muted); margin-bottom:36px; }
h1 { font-size:84px; line-height:1.06; font-weight:700; letter-spacing:-.025em; max-width:1600px; }
.lead { font-size:40px; line-height:1.35; color:var(--soft); margin-top:40px; max-width:1500px; }
.src { position:absolute; left:128px; right:200px; bottom:56px; font-size:24px; color:var(--faint); line-height:1.4; }
.pg { position:absolute; right:128px; bottom:56px; font-size:24px; color:var(--faint); }
.lime { color:var(--lime); }
.grow { flex:1; display:flex; flex-direction:column; justify-content:center; }
/* route diagram */
.route { display:flex; align-items:center; margin-top:8px; }
.node { flex:0 0 230px; height:120px; border:2px solid var(--border-h); border-radius:10px; background:var(--card);
        display:flex; align-items:center; justify-content:center; font-size:34px; font-weight:600; }
.gap { flex:1; text-align:center; font-size:40px; color:var(--faint); }
.link { flex:1; position:relative; height:120px; }
.link::before { content:""; position:absolute; left:0; right:0; top:59px; height:3px; background:var(--lime); }
.link span { position:absolute; left:-20px; right:-20px; white-space:nowrap; top:76px; text-align:center; font-size:24px; color:var(--soft); }
.recs { display:flex; justify-content:space-between; margin-top:20px; }
.recs div { flex:0 0 230px; text-align:center; font-size:26px; color:var(--faint); }
.bar { margin-top:36px; border:2px solid var(--lime); border-radius:10px; padding:22px 32px; font-size:32px; color:var(--fg); }
.three { display:grid; grid-template-columns:repeat(3,1fr); gap:56px; margin-top:96px; }
.three b { display:block; font-size:40px; margin-bottom:12px; }
.three p { font-size:30px; line-height:1.4; color:var(--soft); }
/* columns, stats */
.cols { display:grid; grid-template-columns:1fr 1fr; gap:80px; }
.col h2 { font-size:30px; font-weight:600; letter-spacing:.14em; text-transform:uppercase; color:var(--muted); margin-bottom:24px; }
.col p { font-size:52px; font-weight:600; line-height:1.3; }
.stats { display:grid; grid-template-columns:repeat(4,1fr); gap:48px; }
.stat .n { font-size:120px; font-weight:700; letter-spacing:-.03em; line-height:1; }
.stat .l { font-size:30px; line-height:1.35; color:var(--soft); margin-top:20px; }
.mono { font-family:ui-monospace, Menlo, monospace; font-size:24px; color:var(--faint); }
.nums { display:grid; grid-template-columns:repeat(3,1fr); gap:64px; }
.num .n { font-size:110px; font-weight:700; letter-spacing:-.03em; line-height:1; }
.num .l { font-size:32px; line-height:1.35; color:var(--soft); margin-top:22px; }
.num .s { font-size:24px; color:var(--faint); margin-top:14px; }
.steps { display:grid; grid-template-columns:repeat(3,1fr); gap:56px; }
.step .k { font-size:30px; font-weight:600; letter-spacing:.14em; text-transform:uppercase; color:var(--muted); margin-bottom:18px; }
.step p { font-size:38px; line-height:1.35; font-weight:500; }
.team { display:grid; grid-template-columns:repeat(3,1fr); gap:64px; }
.team b { display:block; font-size:44px; margin-bottom:16px; }
.team p { font-size:30px; line-height:1.4; color:var(--soft); }
svg text { font-family:'Inter', sans-serif; }
"""


def route(problem):
    cells = []
    for i, name in enumerate(ROUTE):
        cells.append(f'<div class="node">{name}</div>')
        if i < len(ROUTE) - 1:
            cells.append('<div class="gap">?</div>' if problem else '<div class="link"><span>both sign</span></div>')
    return f'<div class="route">{"".join(cells)}</div>'


def mesh():
    """Five companies: pair by pair (10 links) vs one rail (5 connections)."""
    import math
    pts = [(200 + 150 * math.cos(math.radians(-90 + 72 * i)), 190 + 150 * math.sin(math.radians(-90 + 72 * i))) for i in range(5)]
    pair = "".join(f'<line x1="{a[0]:.0f}" y1="{a[1]:.0f}" x2="{b[0]:.0f}" y2="{b[1]:.0f}" stroke="#7F848E" stroke-width="3"/>'
                   for i, a in enumerate(pts) for b in pts[i + 1:])
    hub = "".join(f'<line x1="200" y1="190" x2="{p[0]:.0f}" y2="{p[1]:.0f}" stroke="#C6F24E" stroke-width="4"/>' for p in pts)
    dots = "".join(f'<circle cx="{p[0]:.0f}" cy="{p[1]:.0f}" r="22" fill="#131517" stroke="#E7E8EA" stroke-width="3"/>' for p in pts)
    left = f'<svg width="400" height="380">{pair}{dots}</svg>'
    right = (f'<svg width="400" height="380">{hub}{dots}<rect x="150" y="160" width="100" height="60" rx="8" fill="#C6F24E"/>'
             f'<text x="200" y="200" text-anchor="middle" font-size="26" font-weight="700" fill="#0E0F11">rail</text></svg>')
    return (f'<div class="cols" style="align-items:center">'
            f'<div class="col" style="display:flex;gap:40px;align-items:center">{left}<div><h2>Today</h2><p>10 links,<br>pair by pair</p></div></div>'
            f'<div class="col" style="display:flex;gap:40px;align-items:center">{right}<div><h2>On the rail</h2><p class="lime">5 connections,<br>one each</p></div></div></div>')


SLIDES = [
    # 1 cover
    """<div class="grow">
      <div class="kicker">HackMeridian 2026 · Scale track</div>
      <h1 style="font-size:150px;letter-spacing:-.035em">Radox Custody Rail</h1>
      <p class="lead" style="font-size:60px;margin-top:36px;color:var(--fg)">SWIFT for goods in transit, <span class="lime">on Stellar</span></p>
      <p class="lead" style="font-size:36px">Every handover signed by both companies, checkable by anyone.</p>
    </div>""",
    # 2 problem
    f"""<div class="kicker">Problem</div>
    <h1>One container, five companies, five separate records.</h1>
    <div class="grow">{route(True)}
      <div class="recs">{''.join('<div>own record</div>' for _ in ROUTE)}</div>
      <p class="lead" style="margin-top:64px">None of them can check what the others say about who held the goods.</p>
    </div>
    <div class="src">The money that rides on those records is large: 80–90% of world trade relies on trade finance (WTO).</div>""",
    # 3 solution
    f"""<div class="kicker">Solution</div>
    <h1>One shared record. Both companies sign every handover.</h1>
    <div class="grow">{route(False)}
      <div class="three">
        <div><b>Both sign</b><p>The company giving the goods and the one receiving them authorise the step.</p></div>
        <div><b>Nobody rewrites</b><p>Each step folds into a hash chain. One 32-byte head commits to the whole history.</p></div>
        <div><b>Anyone checks</b><p>A buyer, insurer or lender recomputes the head from public data.</p></div>
      </div>
    </div>""",
    # 4 target users
    """<div class="kicker">Target users</div>
    <h1>The companies that hand over goods, and the ones that pay on them.</h1>
    <div class="grow"><div class="cols">
      <div class="col"><h2>They sign</h2><p>Warehouses, ports, carriers, customs brokers, buyers</p></div>
      <div class="col"><h2>They check</h2><p class="lime">Buyers, insurers, lenders</p></div>
    </div>
    <p class="lead" style="margin-top:72px">And any Stellar issuer of a tokenized good, through the open spec.</p></div>""",
    # 5 value proposition
    f"""<div class="kicker">Value proposition</div>
    <h1>Each company connects once, not to every other company.</h1>
    <div class="grow">{mesh()}
    <p class="lead" style="margin-top:56px">A lender sees which company last signed for the goods before it pays.</p></div>""",
    # 6 proof
    f"""<div class="kicker">Proof</div>
    <h1>It runs on Stellar testnet today.</h1>
    <div class="grow"><div class="stats">
      <div class="stat"><div class="n">7</div><div class="l">transactions: one shipment from open to delivery and burn</div></div>
      <div class="stat"><div class="n">9</div><div class="l">refusal branches, each refused (wrong signer, out of route)</div></div>
      <div class="stat"><div class="n">26</div><div class="l">contract tests</div></div>
      <div class="stat"><div class="n lime">MATCH</div><div class="l">anyone recomputes the head from Horizon</div></div>
    </div>
    <p class="lead" style="margin-top:72px">Rehearsed on a local fork of Stellar mainnet: 15 transactions applied, 9 refusals refused, 13.72 XLM in fees.</p></div>
    <div class="src"><span class="mono">custody_registry {CONTRACT} · testnet</span></div>""",
    # 7 market
    """<div class="kicker">Market opportunity</div>
    <h1>The trade that runs on these records is enormous.</h1>
    <div class="grow"><div class="nums">
      <div class="num"><div class="n">45M</div><div class="l">ocean bills of lading issued a year</div><div class="s">DCSA, Feb 2023</div></div>
      <div class="num"><div class="n">US$2.5T</div><div class="l">global trade finance gap</div><div class="s">ADB, Dec 2025</div></div>
      <div class="num"><div class="n lime">US$4B</div><div class="l">tokenized real-world assets on Stellar</div><div class="s">SDF, as of 1 Sep 2026</div></div>
    </div></div>
    <div class="src">Market figures, not Radox volumes.</div>""",
    # 8 business model
    """<div class="kicker">Business model</div>
    <h1>The SWIFT model: pay to connect, pay per shipment.</h1>
    <div class="grow"><div class="cols">
      <div class="col"><h2>Subscription</h2><p>per connected company</p></div>
      <div class="col"><h2>Fee</h2><p class="lime">per shipment on the rail</p></div>
    </div></div>
    <div class="src">The shape follows Swift's published billing rules: entry fee, annual charges and usage fees (swift.com, accessed 25 Oct 2026). Radox is not affiliated with Swift.</div>""",
    # 9 go-to-market and vision
    """<div class="kicker">Go-to-market and vision</div>
    <h1>One corridor first. Then every route.</h1>
    <div class="grow"><div class="steps">
      <div class="step"><div class="k">Now</div><p>The rail on testnet and an open spec any Stellar issuer can implement (Apache-2.0).</p></div>
      <div class="step"><div class="k">Next</div><p>First live shipment on the US–Brazil corridor with a lender and a logistics operator. Mainnet after an audit.</p></div>
      <div class="step"><div class="k">Then</div><p class="lime">Every route. Each company joins once, through one adapter to the Radox API.</p></div>
    </div></div>
    <div class="src">US–Brazil goods trade was about US$94.2 billion in 2025 (US Census Bureau, exports plus imports).</div>""",
    # 10 team
    """<div class="kicker">Team</div>
    <h1>Built by people who already ship on Stellar.</h1>
    <div class="grow"><div class="team">
      <div><b>Pedro Wakigawa Saragossy</b><p>Founder. Built Radox: 3 Soroban contracts on Stellar mainnet.</p></div>
      <div><b>Leo Schlanger</b><p>Developer: the custody_registry contract, the testnet harness and the proofs.</p></div>
      <div><b>Vhendala</b><p>QA and product review: reads every deliverable as a judge would.</p></div>
    </div>
    <p class="lead" style="margin-top:80px;color:var(--fg)">github.com/pwsaragossy/rio-miami-rail · <span class="lime">rio-miami-rail.vercel.app</span></p></div>
    <div class="src">Built at HackMeridian on the Radox platform (prior work, listed in the repo). Code, docs and this deck were made with AI coding agents (Claude Code); AI_USAGE.md lists every file.</div>""",
]


def build():
    body = "".join(f'<section data-slide="{i}">{s}<div class="pg">{i}</div></section>' for i, s in enumerate(SLIDES, 1))
    html = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Radox Custody Rail</title>'
            f'<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=block">'
            f'<style>{CSS}</style></head><body>{body}</body></html>')
    open(HTML, "w").write(html)
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=8000",
                    f"--print-to-pdf={PDF}", "file://" + HTML], check=True, capture_output=True)
    print(f"{PDF} {os.path.getsize(PDF)} bytes, {len(SLIDES)} slides")
    if "--png" in sys.argv:
        subprocess.run(["pdftoppm", "-png", "-r", "50", PDF, os.path.join(HERE, "png", "slide")], check=True)


if __name__ == "__main__":
    os.makedirs(os.path.join(HERE, "png"), exist_ok=True)
    build()
