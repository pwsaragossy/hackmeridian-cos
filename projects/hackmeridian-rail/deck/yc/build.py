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
# Lucide icons 0.553.0 (ISC licence), path data copied from lucide-react: they name each actor, nothing else gets an icon.
ICONS = {
    "Warehouse": ['M18 21V10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1v11', 'M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V8a2 2 0 0 1 1.132-1.803l7.95-3.974a2 2 0 0 1 1.837 0l7.948 3.974A2 2 0 0 1 22 8z', 'M6 13h12', 'M6 17h12'],
    "Port": ['M12 22V8', 'M5 12H2a10 10 0 0 0 20 0h-3', 'C12 5 3'],
    "Carrier": ['M14 18V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v11a1 1 0 0 0 1 1h2', 'M15 18H9', 'M19 18h2a1 1 0 0 0 1-1v-3.65a1 1 0 0 0-.22-.624l-3.48-4.35A1 1 0 0 0 17.52 8H14', 'C17 18 2', 'C7 18 2'],
    "Customs": ['M14 13V8.5C14 7 15 7 15 5a3 3 0 0 0-6 0c0 2 1 2 1 3.5V13', 'M20 15.5a2.5 2.5 0 0 0-2.5-2.5h-11A2.5 2.5 0 0 0 4 15.5V17a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1z', 'M5 22h14'],
    "Buyer": ['M10 12h4', 'M10 8h4', 'M14 21v-3a2 2 0 0 0-4 0v3', 'M6 10H4a2 2 0 0 0-2 2v7a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-2', 'M6 21V5a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v16'],
}


def icon(name):
    parts = "".join(f'<circle cx="{e.split()[0][1:]}" cy="{e.split()[1]}" r="{e.split()[2]}"/>' if e[0] == "C" else f'<path d="{e}"/>'
                    for e in ICONS[name])
    return (f'<svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#C8CBD0" stroke-width="1.6" '
            f'stroke-linecap="round" stroke-linejoin="round">{parts}</svg>')

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
.node { flex:0 0 230px; height:170px; border:2px solid var(--border-h); border-radius:10px; background:var(--card);
        display:flex; flex-direction:column; gap:14px; align-items:center; justify-content:center; font-size:32px; font-weight:600; }
.gap { flex:1; text-align:center; font-size:40px; color:var(--faint); }
.link { flex:1; position:relative; height:170px; }
.link::before { content:""; position:absolute; left:0; right:0; top:84px; height:3px; background:var(--lime); }
.link span { position:absolute; left:-20px; right:-20px; white-space:nowrap; top:106px; text-align:center; font-size:24px; color:var(--soft); }
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
        cells.append(f'<div class="node">{icon(name)}<span>{name}</span></div>')
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
      <p class="lead" style="font-size:36px">Every handover signed by both companies, checkable by anyone. Running on Stellar testnet.</p>
    </div>""",
    # 2 problem
    f"""<div class="kicker">Problem</div>
    <h1>One container, five parties, five separate records.</h1>
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
      <div class="col"><h2>They sign</h2><p>Warehouses, ports, carriers, customs, buyers</p></div>
      <div class="col"><h2>They check</h2><p class="lime">Buyers, insurers, lenders</p></div>
    </div>
    <p class="lead" style="margin-top:72px">And any Stellar issuer of a tokenized good, through the open spec.</p></div>""",
    # 5 value proposition
    f"""<div class="kicker">Value proposition</div>
    <h1>Each company connects once, not to every other company.</h1>
    <div class="grow">{mesh()}
    <p class="lead" style="margin-top:56px">A lender will read which company last signed for the goods, straight from the contract, before it pays.</p></div>""",
    # 6 proof
    f"""<div class="kicker">Proof</div>
    <h1>It runs on Stellar testnet today.</h1>
    <div class="grow"><div class="stats">
      <div class="stat"><div class="n">7</div><div class="l">transactions: one shipment from open to delivery and burn</div></div>
      <div class="stat"><div class="n">9</div><div class="l">refusal cases, each rejected in simulation (wrong signer, out of route)</div></div>
      <div class="stat"><div class="n">26</div><div class="l">contract tests</div></div>
      <div class="stat"><div class="n lime">MATCH</div><div class="l">anyone recomputes the head from Horizon</div></div>
    </div>
    <p class="lead" style="margin-top:72px">Dry run on a local copy of mainnet state, nothing sent to mainnet: 15 transactions applied, 9 refusals rejected, 13.72 XLM simulated fees.</p></div>
    <div class="src"><span class="mono">custody_registry {CONTRACT} · testnet</span></div>""",
    # 7 market
    """<div class="kicker">Market opportunity</div>
    <h1>The market around the rail: bills of lading, a financing gap, tokenized assets.</h1>
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
      <div class="step"><div class="k">Now</div><p>The rail on testnet. An open spec any Stellar issuer can implement.</p></div>
      <div class="step"><div class="k">Next</div><p>First live shipment on the US–Brazil corridor. Mainnet after an audit.</p></div>
      <div class="step"><div class="k">Then</div><p class="lime">Every route. Each company joins once, through one adapter.</p></div>
    </div></div>
    <div class="src">US–Brazil goods trade was about US$94.2 billion in 2025 (US Census Bureau, exports plus imports).</div>""",
    # 10 team
    """<div class="kicker">Team</div>
    <h1>Built by people who already ship on Stellar.</h1>
    <div class="grow"><div class="team">
      <div><b>Pedro Wakigawa Saragossy</b><p>Founder. Built Radox before the event: 3 Soroban contracts on Stellar mainnet (prior work).</p></div>
      <div><b>Leo Schlanger</b><p>Developer: reviewed the contract, the signing logic and the proofs.</p></div>
      <div><b>Vhendala</b><p>Supervision and product review.</p></div>
    </div>
    <p class="lead" style="margin-top:80px;color:var(--fg)">github.com/pwsaragossy/rio-miami-rail · <span class="lime">rio-miami-rail.vercel.app</span></p></div>
    <div class="src">Prior work is listed in the repo. Made with AI coding agents (Claude Code); see AI_USAGE.md.</div>""",
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
