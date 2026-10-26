"""Build deck/yc/radox-custody-rail-yc.pdf: minimalist deck, YC design rules ([[yc-pitch-deck-design-rules-kevin-bd35]]).

Run: python3 deck/yc/build.py [--png]   (needs Google Chrome; --png also needs pdftoppm)
Opens with three lost-cargo cases, then the cover. One idea per slide, the headline is the line a judge repeats. Radox Signal tokens only (LANDING-V2-BRIEF.md "Design").
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
# Lucide icons 0.553.0 (ISC licence), SVG markup copied from lucide-react: one per actor and one per column heading.
ICONS = {
    "warehouse": '<path d="M18 21V10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1v11"/><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V8a2 2 0 0 1 1.132-1.803l7.95-3.974a2 2 0 0 1 1.837 0l7.948 3.974A2 2 0 0 1 22 8z"/><path d="M6 13h12"/><path d="M6 17h12"/>',
    "anchor": '<path d="M12 22V8"/><path d="M5 12H2a10 10 0 0 0 20 0h-3"/><circle cx="12" cy="5" r="3"/>',
    "truck": '<path d="M14 18V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v11a1 1 0 0 0 1 1h2"/><path d="M15 18H9"/><path d="M19 18h2a1 1 0 0 0 1-1v-3.65a1 1 0 0 0-.22-.624l-3.48-4.35A1 1 0 0 0 17.52 8H14"/><circle cx="17" cy="18" r="2"/><circle cx="7" cy="18" r="2"/>',
    "stamp": '<path d="M14 13V8.5C14 7 15 7 15 5a3 3 0 0 0-6 0c0 2 1 2 1 3.5V13"/><path d="M20 15.5a2.5 2.5 0 0 0-2.5-2.5h-11A2.5 2.5 0 0 0 4 15.5V17a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1z"/><path d="M5 22h14"/>',
    "building-2": '<path d="M10 12h4"/><path d="M10 8h4"/><path d="M14 21v-3a2 2 0 0 0-4 0v3"/><path d="M6 10H4a2 2 0 0 0-2 2v7a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-2"/><path d="M6 21V5a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v16"/>',
    "pen-line": '<path d="M13 21h8"/><path d="M21.174 6.812a1 1 0 0 0-3.986-3.987L3.842 16.174a2 2 0 0 0-.5.83l-1.321 4.352a.5.5 0 0 0 .623.622l4.353-1.32a2 2 0 0 0 .83-.497z"/>',
    "search-check": '<path d="m8 11 2 2 4-4"/><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>',
    "landmark": '<path d="M10 18v-7"/><path d="M11.12 2.198a2 2 0 0 1 1.76.006l7.866 3.847c.476.233.31.949-.22.949H3.474c-.53 0-.695-.716-.22-.949z"/><path d="M14 18v-7"/><path d="M18 18v-7"/><path d="M3 22h18"/><path d="M6 18v-7"/>',
    "handshake": '<path d="m11 17 2 2a1 1 0 1 0 3-3"/><path d="m14 14 2.5 2.5a1 1 0 1 0 3-3l-3.88-3.88a3 3 0 0 0-4.24 0l-.88.88a1 1 0 1 1-3-3l2.81-2.81a5.79 5.79 0 0 1 7.06-.87l.47.28a2 2 0 0 0 1.42.25L21 4"/><path d="m21 3 1 11h-2"/><path d="M3 3 2 14l6.5 6.5a1 1 0 1 0 3-3"/><path d="M3 4h8"/>',
    "package": '<path d="M11 21.73a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73z"/><path d="M12 22V12"/><polyline points="3.29 7 12 12 20.71 7"/><path d="m7.5 4.27 9 5.15"/>',
    "link": '<path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/>',
    "arrow-right-left": '<path d="m16 3 4 4-4 4"/><path d="M20 7H4"/><path d="m8 21-4-4 4-4"/><path d="M4 17h16"/>',
    "shield-x": '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m14.5 9.5-5 5"/><path d="m9.5 9.5 5 5"/>',
    "circle-check": '<circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/>',
    "ship": '<path d="M12 10.189V14"/><path d="M12 2v3"/><path d="M19 13V7a2 2 0 0 0-2-2H7a2 2 0 0 0-2 2v6"/><path d="M19.38 20A11.6 11.6 0 0 0 21 14l-8.188-3.639a2 2 0 0 0-1.624 0L3 14a11.6 11.6 0 0 0 2.81 7.76"/><path d="M2 21c.6.5 1.2 1 2.5 1 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1s1.2 1 2.5 1c2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1"/>',
    "repeat": '<path d="m17 2 4 4-4 4"/><path d="M3 11v-1a4 4 0 0 1 4-4h14"/><path d="m7 22-4-4 4-4"/><path d="M21 13v1a4 4 0 0 1-4 4H3"/>',
    "banknote": '<rect width="20" height="12" x="2" y="6" rx="2"/><circle cx="12" cy="12" r="2"/><path d="M6 12h.01M18 12h.01"/>',
    "calendar-sync": '<path d="M11 10v4h4"/><path d="m11 14 1.535-1.605a5 5 0 0 1 8 1.5"/><path d="M16 2v4"/><path d="m21 18-1.535 1.605a5 5 0 0 1-8-1.5"/><path d="M21 22v-4h-4"/><path d="M21 8.5V6a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h4.3"/><path d="M3 10h4"/><path d="M8 2v4"/>',
    "receipt": '<path d="M4 2v20l2-1 2 1 2-1 2 1 2-1 2 1 2-1 2 1V2l-2 1-2-1-2 1-2-1-2 1-2-1-2 1Z"/><path d="M16 8h-6a2 2 0 1 0 0 4h4a2 2 0 1 1 0 4H8"/><path d="M12 17.5v-11"/>',
    "eye": '<path d="M2.062 12.348a1 1 0 0 1 0-.696 10.75 10.75 0 0 1 19.876 0 1 1 0 0 1 0 .696 10.75 10.75 0 0 1-19.876 0"/><circle cx="12" cy="12" r="3"/>',
    "rocket": '<path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"/><path d="m12 15-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/><path d="M9 12H4s.55-3.03 2-4c1.62-1.08 5 0 5 0"/><path d="M12 15v5s3.03-.55 4-2c1.08-1.62 0-5 0-5"/>',
    "plane": '<path d="M17.8 19.2 16 11l3.5-3.5C21 6 21.5 4 21 3c-1-.5-3 0-4.5 1.5L13 8 4.8 6.2c-.5-.1-.9.1-1.1.5l-.3.5c-.2.5-.1 1 .3 1.3L9 12l-2 3H4l-1 1 3 2 2 3 1-1v-3l3-2 3.5 5.3c.3.4.8.5 1.3.3l.5-.2c.4-.3.6-.7.5-1.2z"/>',
    "network": '<rect x="16" y="16" width="6" height="6" rx="1"/><rect x="2" y="16" width="6" height="6" rx="1"/><rect x="9" y="2" width="6" height="6" rx="1"/><path d="M5 16v-3a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v3"/><path d="M12 12V8"/>',
}
ACTOR = {"Warehouse": "warehouse", "Port": "anchor", "Carrier": "truck", "Customs": "stamp", "Buyer": "building-2"}


def icon(name, size=48, color="#C8CBD0"):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.6" '
            f'stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</svg>')


def ic(name, lime=False):
    """Column-heading icon: same stroke as the actor icons, lime only where the column is already lime."""
    return f'<div class="ic">{icon(name, 60, "#C6F24E" if lime else "#C8CBD0")}</div>'


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
.grow { flex:1; display:flex; flex-direction:column; justify-content:center; padding-top:32px; }
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
.three.big b { font-size:48px; margin-bottom:20px; } .three.big p { font-size:36px; }
/* columns, stats */
.cols { display:grid; grid-template-columns:1fr 1fr; gap:80px; }
.col h2 { font-size:30px; font-weight:600; letter-spacing:.14em; text-transform:uppercase; color:var(--muted); margin-bottom:24px; }
.col p { font-size:52px; font-weight:600; line-height:1.3; }
.cols.tight .col p { font-size:44px; }
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
.ic { margin-bottom:24px; line-height:0; }
/* opening cases: one lost shipment per slide, the number first */
.case .big { font-size:200px; font-weight:700; letter-spacing:-.04em; line-height:1; color:var(--lime); margin-bottom:48px; }
.case h1 { font-size:76px; max-width:1560px; }
.case .lead { font-size:44px; color:var(--fg); margin-top:48px; }
.ph { width:240px; height:240px; border-radius:50%; object-fit:cover; border:2px solid var(--border-h); margin-bottom:32px; display:block; }
"""


def route(problem):
    cells = []
    for i, name in enumerate(ROUTE):
        cells.append(f'<div class="node">{icon(ACTOR[name])}<span>{name}</span></div>')
        if i < len(ROUTE) - 1:
            cells.append('<div class="gap">?</div>' if problem else '<div class="link"><span>handover</span></div>')
    return f'<div class="route">{"".join(cells)}</div>'


SLIDES = [
    # 1-3 opening cases (owner's order 2026-10-26): lost cargo, then who held it. Sources: [[three-lost-cargo-cases-for-the-cfc4]].
    """<div class="kicker">October 2026 · Guarulhos airport, São Paulo</div>
    <div class="grow case"><div class="big">R$2.5M</div>
      <h1>Two pallets of RTX 5090s arrived at the airport. Inside, they vanished.</h1>
      <p class="lead">Nobody has shown who last held them.</p></div>
    <div class="src">Canaltech, 19 Oct 2026, from the importer's account (Oderço). Cause unknown; theft not confirmed.</div>""",
    """<div class="kicker">April 2023 · Toronto Pearson airport</div>
    <div class="grow case"><div class="big">C$20M</div>
      <h1>Gold left an airline cargo warehouse 40 minutes after it arrived, on a fake waybill.</h1>
      <p class="lead">Brink's sued the airline. The court capped what the airline owed at about C$18,500.</p></div>
    <div class="src">CP24: 11 Oct 2023; court ruling Jan 2025 (Montreal Convention limit, value not declared); settled Aug 2026, amount undisclosed. Fake waybill: Peel police, April 2024.</div>""",
    """<div class="kicker">Court ruling, September 2025 · UAE to India</div>
    <div class="grow case"><div class="big">49.9 t</div>
      <h1>A copper shipment vanished on the way from the UAE to India.</h1>
      <p class="lead">One transporter said its leg had ended. The other said nothing proved the copper was loaded. A court had to decide.</p></div>
    <div class="src">Khaleej Times, 27 Sep 2025. Dubai courts held all defendants jointly liable.</div>""",
    # 4 cover
    """<div class="grow">
      <div class="kicker">HackMeridian 2026 · Scale track</div>
      <h1 style="font-size:150px;letter-spacing:-.035em">Radox Custody Rail</h1>
      <p class="lead" style="font-size:60px;margin-top:36px;color:var(--fg)">SWIFT for goods in transit, <span class="lime">on Stellar</span></p>
      <p class="lead" style="font-size:36px">Every handover signed by both companies, checkable by anyone.</p>
    </div>
    <div class="src">Running on Stellar testnet.</div>""",
    # 5 problem
    f"""<div class="kicker">Problem</div>
    <h1>The owner of the goods is partly blind the whole way.</h1>
    <div class="grow">{route(True)}
      <p class="lead" style="margin-top:64px">Each company keeps its own record. When cargo goes missing, no one can show who held it last.</p>
      <p class="lead" style="font-size:32px;margin-top:40px">Why now: ICC set digital standards for all 36 key trade documents (2024); about US$4B of real-world assets is tokenized on Stellar (SDF, Sep 2026). The custody record is missing.</p>
    </div>""",
    # 6 solution
    f"""<div class="kicker">Solution</div>
    <h1>One shared record. Both companies sign every handover.</h1>
    <div class="grow">{route(False)}
      <div class="three">
        <div><b>Both sign</b><p>The company giving the goods and the one receiving them both sign.</p></div>
        <div><b>Nobody rewrites</b><p>Each step is chained to the one before, so no one can rewrite history.</p></div>
        <div><b>Anyone checks</b><p>The owner, a buyer, insurer or lender checks the whole history against one public 32-byte value.</p></div>
      </div>
    </div>""",
    # 7 target users
    f"""<div class="kicker">Target users</div>
    <h1>The companies that hand over goods, and the ones that own or pay on them.</h1>
    <div class="grow"><div class="cols">
      <div class="col">{ic("pen-line")}<h2>They sign</h2><p>Warehouses, ports, carriers, customs, buyers</p></div>
      <div class="col">{ic("search-check", True)}<h2>They check</h2><p class="lime">Owners, buyers, insurers, lenders</p></div>
    </div>
    <p class="lead" style="margin-top:72px">First corridor: US–Brazil. Later, any Stellar issuer of a tokenized good, through the open spec.</p></div>""",
    # 8 value proposition
    f"""<div class="kicker">Value proposition</div>
    <h1>Every handover becomes proof the owner and lenders can check.</h1>
    <div class="grow"><div class="three big" style="margin-top:0">
        <div>{ic("landmark", True)}<b class="lime">Owners see the proof</b><p>Owners, lenders and insurers will see which company last signed for the goods before paying.</p></div>
        <div>{ic("handshake")}<b>Companies prove their leg</b><p>Your handover carries the receiver's signature, so you can show you passed the goods.</p></div>
        <div>{ic("link")}<b>Cargo token, linked record</b><p>Each cargo token links to one shipment record of signed handovers.</p></div>
    </div></div>
    <div class="src">Proof on Stellar testnet.</div>""",
    # 9 proof
    f"""<div class="kicker">Proof</div>
    <h1>Live on Stellar testnet. Check every handover yourself.</h1>
    <div class="grow"><div class="stats" style="grid-template-columns:repeat(3,1fr)">
      <div class="stat">{ic("arrow-right-left")}<div class="n">7</div><div class="l">transactions: one shipment from open to delivery and burn</div></div>
      <div class="stat">{ic("shield-x")}<div class="n">9</div><div class="l">refusal cases, each rejected in simulation (wrong signer, out of route)</div></div>
      <div class="stat">{ic("circle-check", True)}<div class="n lime">MATCH</div><div class="l">anyone recomputes the head from Horizon</div></div>
    </div>
    <p class="lead" style="margin-top:56px;font-size:34px">Second shipment: two teammates signed handovers on their own computers.</p>
    <p class="lead" style="margin-top:20px;font-size:34px">Local mainnet-state dry run, nothing sent: 15 transactions applied, 9 refusals rejected, 13.72 XLM gross simulated fees.</p></div>
    <div class="src"><a href="https://stellar.expert/explorer/testnet/contract/{CONTRACT}" style="text-decoration:none"><span class="mono">custody_registry {CONTRACT} · testnet · stellar.expert</span></a></div>""",
    # 10 market
    f"""<div class="kicker">Market opportunity</div>
    <h1>45 million ocean bills of lading a year. Each one a chain of handovers.</h1>
    <div class="grow"><div class="nums">
      <div class="num">{ic("ship")}<div class="n">45M</div><div class="l">ocean bills of lading issued a year</div><div class="s">DCSA, Feb 2023</div></div>
      <div class="num">{ic("repeat", True)}<div class="n lime">~180M</div><div class="l">custody handovers a year, if every bill of lading had our 4 signed handovers</div><div class="s">Illustration, not a forecast</div></div>
      <div class="num">{ic("banknote")}<div class="n">US$2.5T</div><div class="l">global trade finance gap</div><div class="s">ADB, Dec 2025</div></div>
    </div></div>
    <div class="src">Illustration: 45M × 4 handovers; the 4 is our design assumption.</div>""",
    # 11 business model
    f"""<div class="kicker">Business model</div>
    <h1>Companies on the route subscribe, and pay per shipment.</h1>
    <div class="grow"><div class="cols tight" style="grid-template-columns:repeat(3,1fr);gap:64px">
      <div class="col">{ic("calendar-sync")}<h2>Subscription</h2><p>per connected company</p></div>
      <div class="col">{ic("receipt", True)}<h2>Fee</h2><p class="lime">per shipment on the rail</p></div>
      <div class="col">{ic("eye")}<h2>Open record</h2><p>checking needs no signature and no account</p></div>
    </div>
    <p class="lead" style="margin-top:44px">Every handover has two signers, so each shipment brings in the next company on the route.</p></div>
    <div class="src">Same shape as Swift's published fees: entry, annual, per-message usage (swift.com, accessed 25 Oct 2026). Radox is not affiliated with Swift.</div>""",
    # 12 go-to-market and vision
    f"""<div class="kicker">Go-to-market and vision</div>
    <h1>One corridor first. Then every route.</h1>
    <div class="grow"><div class="steps">
      <div class="step">{ic("rocket")}<div class="k">First</div><p>Apply to SCF Build: fund and build everything the operation needs.</p></div>
      <div class="step">{ic("plane")}<div class="k">Next</div><p>The Rio–Miami pilot, which we aim to present at the G20 in the US in December.</p></div>
      <div class="step">{ic("network", True)}<div class="k">Then</div><p class="lime">More ports and chambers of commerce already in conversation. More rails.</p></div>
    </div></div>
    <div class="src">Our design target: US–Brazil goods trade, about US$94.2 billion in 2025 (US Census Bureau, exports plus imports).</div>""",
    # 13 team
    f"""<div class="kicker">Team</div>
    <div class="grow"><div class="team">
      <div><img class="ph" src="img/pedro.jpg" alt=""><b>Pedro Wakigawa Saragossy</b><p>Founder. Built the Radox platform before the event.</p></div>
      <div><img class="ph" src="img/leo.jpg" alt=""><b>Leo Schlanger</b><p>Developer. Reviewed the contract's auth and signing logic. Signed testnet handovers.</p></div>
      <div><img class="ph" src="img/vhendala.jpg" alt=""><b>Vhendala</b><p>Supervision and product review. Signed testnet handovers.</p></div>
    </div>
    <p class="lead" style="margin-top:80px;color:var(--fg)">github.com/pwsaragossy/rio-miami-rail · <span class="lime">rio-miami-rail.vercel.app</span></p></div>
    <div class="src">Radox is prior work. A Claude Code agent wrote the contract; Leo reviewed it (AI_USAGE.md).</div>""",
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
