"""Build deck/radox-custody-rail.pptx from the organizers' DECK-TEMPLATE.pptx.

Run: python deck/build_deck.py   (needs python-pptx and Pillow), then
     soffice --headless --convert-to pdf --outdir deck deck/radox-custody-rail.pptx
Copy rules: PITCH.md Claims guard and [[wording-the-rio-miami-deck-readme-ef38]].
Every fact on a slide has its source in deck/REVIEW.md (claims table).
"""
import copy
import io
import math
import os

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_CONNECTOR, MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Emu, Inches, Pt

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "DECK-TEMPLATE.pptx")
OUT = os.path.join(ROOT, "deck", "radox-custody-rail.pptx")
SHOT = lambda name: os.path.join(ROOT, "deck", "screens", name)

# Switch only on Paulo's written OK ([[zis-in-public-material-radox-is-bc05]]); then paste his approved wording.
BRIDGE = ("Context: our explainer video about a Rio–Miami trade-corridor initiative poses one possibility: a unique "
          "digital record for every shipment that both sides can check. This project is a custody layer for that record.")

# LOOK.md (Signal adapted)
INK, PAPER, CARD, LINE_C = "0E0F11", "F7F6F2", "FFFFFF", "DFDDD6"
TEXT_D, SEC_D, LINE_D, PANEL_D = "E7E8EA", "A3A8B0", "2A2F36", "131517"
SEC_C, LIME, LIME_C, SLATE_D, SLATE_C = "4D5560", "C6F24E", "556F00", "9FB2CC", "3F5675"
TITLE, BODY, MONO = "Inter Tight", "Instrument Sans", "JetBrains Mono"

HASHES = [  # proofs/lifecycle.json, rio-miami-rail
    ("open", "operator", "2b3d51f0"),
    ("handover 1", "Warehouse → Port", "635c99ac"),
    ("handover 2", "Port → Carrier", "56a0f006"),
    ("handover 3", "Carrier → Customs", "ac268a49"),
    ("handover 4", "Customs → Recipient", "5199d4fb"),
    ("deliver", "Recipient → Holder", "919def8c"),
    ("burn", "existing redeem", "864fd164"),
]
CONTRACT = "CCBJVXMJYWPHTDJHDFPRGKPGXGEP24JOPJAMUS5C3BMZJTRTWR2H4LII"
N = 10

prs = Presentation(TEMPLATE)
COVER, CONTENT = prs.slides[0], prs.slides[1]
BLANK = prs.slide_layouts[0]


def rgb(h):
    return RGBColor.from_string(h)


def sid(shape):
    return shape.name.split(";")[1]


def clone(proto, keep, dark):
    """New slide with the template's fixed parts (bars, labels, footer, logo) copied from proto."""
    s = prs.slides.add_slide(BLANK)
    bg = copy.deepcopy(proto._element.cSld.bg)
    s._element.cSld.insert(0, bg)
    s.background.fill.solid()
    s.background.fill.fore_color.rgb = rgb(INK if dark else PAPER)
    for sh in proto.shapes:
        if sid(sh) not in keep:
            continue
        if sh.shape_type == 13:  # picture: re-add from its blob
            blob = sh.image.blob
            if dark and proto is CONTENT:  # dark logo on a dark slide: use the cover's light logo
                blob = next(x for x in COVER.shapes if sid(x) == "91").image.blob
            s.shapes.add_picture(io.BytesIO(blob), sh.left, sh.top, sh.width, sh.height)
        else:
            s.shapes._spTree.append(copy.deepcopy(sh._element))
    return s


def find(s, key):
    for sh in s.shapes:
        if ";" in sh.name and sid(sh) == key:
            return sh


def set_run_text(sh, text, color=None):
    r = sh.text_frame.paragraphs[0].runs[0]
    r.text = text
    if color:
        r.font.color.rgb = rgb(color)


def text(s, x, y, w, h, paras, size=26, color=INK, font=BODY, bold=False, align=PP_ALIGN.LEFT,
         anchor=MSO_ANCHOR.TOP, spacing=1.12, after=6):
    """paras: list of paragraphs; a paragraph is a str or a list of (text, overrides) runs."""
    tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = anchor
    for i, p in enumerate(paras):
        para = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        para.alignment = align
        para.line_spacing = spacing
        para.space_after = Pt(after)
        for run_text, o in ([(p, {})] if isinstance(p, str) else p):
            r = para.add_run()
            r.text = run_text
            f = r.font
            f.name = o.get("font", font)
            f.size = Pt(o.get("size", size))
            f.bold = o.get("bold", bold)
            f.color.rgb = rgb(o.get("color", color))
    return tb


def box(s, x, y, w, h, fill=None, line=None, shape=MSO_SHAPE.RECTANGLE, weight=1.0, dash=False):
    b = s.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    if shape == MSO_SHAPE.ROUNDED_RECTANGLE:
        b.adjustments[0] = min(0.12, 0.16 / min(w, h))
    if fill:
        b.fill.solid()
        b.fill.fore_color.rgb = rgb(fill)
    else:
        b.fill.background()
    if line:
        b.line.color.rgb = rgb(line)
        b.line.width = Pt(weight)
        if dash:
            b.line.dash_style = 4  # dash
    else:
        b.line.fill.background()
    b.shadow.inherit = False
    b._element.xpath(".//a:effectRef")[0].set("idx", "0")  # else LibreOffice draws the theme shadow
    return b


def dot(s, cx, cy, d, fill):
    return box(s, cx - d / 2, cy - d / 2, d, d, fill=fill, shape=MSO_SHAPE.OVAL)


def hline(s, x, y, w, color, t=0.025):
    return box(s, x, y - t / 2, w, t, fill=color)


def content_slide(n, pill, title, next_label, dark=False):
    keep = {"106", "107", "108", "109", "110", "121", "122", "123"}
    s = clone(CONTENT, keep, dark)
    set_run_text(find(s, "107"), f"PLATFORM {n:02d} / {N:02d}", LIME)
    set_run_text(find(s, "108"), "HACKMERIDIAN 2026 · LISBON")
    set_run_text(find(s, "109"), next_label, LIME if next_label != "FINAL STOP" else None)
    p = find(s, "110")
    set_run_text(p, pill, INK)
    p.text_frame.paragraphs[0].runs[0].font.size = Pt(18)
    p.fill.fore_color.rgb = rgb(LIME)
    p.width = Inches(0.9 + 0.15 * len(pill))
    if dark:
        find(s, "106").fill.fore_color.rgb = rgb(PANEL_D)
        find(s, "121").fill.fore_color.rgb = rgb(LINE_D)
        set_run_text(find(s, "122"), find(s, "122").text_frame.text, SEC_D)
    text(s, 1.0, 2.2, 18.0, 1.1, [title], size=58, font=TITLE, bold=True, color=TEXT_D if dark else INK,
         spacing=1.0)
    return s


# ---------- 1. Cover ----------
s = clone(COVER, {"84", "85", "86", "91", "92", "93", "94", "95", "96", "97", "98", "99", "100", "101"}, dark=True)
set_run_text(find(s, "85"), f"PLATFORM 01 / {N:02d}", LIME)
pill = find(s, "86")
set_run_text(pill, "TESTNET · TEST KEYS · NOT REAL CUSTODIANS", LIME)
pill.line.color.rgb = rgb(LIME)
pill.width = Inches(0.9 + 0.15 * 41)
pill.text_frame.paragraphs[0].runs[0].font.size = Pt(18)
set_run_text(find(s, "100"), "#HackMeridian26", LIME)
for k in ("95", "96", "97"):
    find(s, k).fill.fore_color.rgb = rgb(LIME)
text(s, 1.0, 2.55, 12.5, 1.5, ["Radox Custody Rail"], size=100, font=TITLE, bold=True, color=LIME, spacing=0.95)
text(s, 1.0, 4.15, 12.0, 1.6, ["Know who holds the goods: every handover signed by both custodians."],
     size=44, font=TITLE, bold=True, color=TEXT_D, spacing=1.0)
text(s, 1.0, 5.95, 12.5, 0.5, ["Toward a SWIFT-like custody standard on Stellar  ·  Pilot corridor: Rio–Miami"],
     size=24, color=SEC_D)
s.shapes.add_picture(SHOT("qr-page-dark.png"), Inches(15.75), Inches(1.75), Inches(2.6), Inches(2.6))
text(s, 14.3, 4.5, 5.5, 0.9, ["Scan: the live shipment", [("rio-miami-rail.vercel.app", {"font": MONO, "color": LIME, "size": 18})]],
     size=20, color=TEXT_D, align=PP_ALIGN.CENTER, after=2)
hline(s, 14.0, 6.15, 5.0, LIME_C, 0.03)
for i in range(6):
    dot(s, 14.0 + i * 1.0, 6.15, 0.26 if i in (0, 5) else 0.16, LIME)
text(s, 13.87, 6.42, 2.0, 0.4, ["RIO"], size=18, font=MONO, bold=True, color=SEC_D)
text(s, 17.13, 6.42, 2.0, 0.4, ["MIAMI"], size=18, font=MONO, bold=True, color=SEC_D, align=PP_ALIGN.RIGHT)

# ---------- 2-3. Problem, in numbers: only rows of PROBLEM-NUMBERS.md (verified 2026-10-25), wording kept ----------
# (big number, what it measures, source line). check_deck fails on any {{ placeholder.
P_HANDS = [("45M", "ocean bills of lading issued a year", "DCSA, Feb 2023 (2021 data)"),  # PROBLEM-NUMBERS.md row 1, [[dcsa-45-million-bills-of-lading-1af2]]
           ("~11%", "of bills of lading issued electronically, 2025", "DCSA, as of 2025 (Jan 2025 guide: 5.7%)"),  # row 2
           ("22%", "of recorded cargo thefts in 2025 involved insiders", "TT Club & BSI Cargo Theft Report, Apr 2026")]  # row 3, [[tt-club-bsi-2025-cargo-theft-12f4]]
P_COST = [("R$900M", "est. direct loss, 8,570 cargo robberies in Brazil, 2025", "NTC&Logística survey, 28 Mar 2026"),  # row 7
          ("US$85M", "HSBC's loss on forged documents for oil trades that never happened", "Hin Leong case, Global Trade Review, 18 Nov 2024"),  # row 5
          ("US$2.5T", "global trade finance gap (market size only)", "ADB survey of banks, Dec 2025")]  # [[adb-trade-finance-gap-survey-dec-d033]]


def stats(s, items, y, step=6.1, w=5.6):
    for i, (num, label, src) in enumerate(items):
        x = 1.0 + i * step
        hline(s, x, y, w, LIME_C, 0.03)
        text(s, x, y + 0.2, w, 1.2, [num], size=64, font=TITLE, bold=True, color=INK, spacing=0.95)
        text(s, x, y + 1.45, w, 1.0, [label], size=24, bold=True, color=INK)
        text(s, x, y + 2.45, w, 0.9, [src], size=18, color=SEC_C)


s = content_slide(2, "PMF · THE PROBLEM", "Who holds the cargo right now?", "NEXT ▸ WHAT IT COSTS")
stops = ["Warehouse", "Port", "Carrier", "Customs", "Recipient"]
x0, x1, ly = 1.6, 18.4, 3.75
hline(s, x0, ly, x1 - x0, LIME_C, 0.03)
for i, name in enumerate(stops):
    cx = x0 + i * (x1 - x0) / 4
    dot(s, cx, ly, 0.3, LIME_C)
    text(s, cx - 1.3, ly + 0.25, 2.6, 0.5, [name], size=22, bold=True, align=PP_ALIGN.CENTER)
stats(s, P_HANDS, 4.85)
text(s, 1.0, 8.6, 18.0, 0.9, [BRIDGE], size=18, color=SEC_C)

s = content_slide(3, "PMF · WHAT IT COSTS", "Cargo goes missing. A bank got fooled.", "NEXT ▸ THE SOLUTION")
text(s, 1.0, 3.4, 18.0, 0.9, [[("Our hypothesis: ", {"bold": True, "color": LIME_C}),
                               ("a financier cannot see who holds the goods before paying. No customer has confirmed it yet.", {})]], size=24)
stats(s, P_COST, 4.6)
text(s, 1.0, 8.2, 18.0, 0.9, ["These numbers size the market problem. They are not results of ours, and we do not claim our build prevents any of it."],
     size=20, color=SEC_C)

# ---------- 3. Solution ----------
s = content_slide(4, "THE SOLUTION", "Both custodians sign, or nothing changes", "NEXT ▸ LIVE ON TESTNET")
y = 3.6
for x, w, label, sub, fill, lc in [(1.0, 4.9, "Outgoing custodian", "signs", CARD, LINE_C),
                                   (6.55, 6.9, "One Stellar transaction", "custody_registry.handover", LIME, None),
                                   (14.1, 4.9, "Incoming custodian", "signs", CARD, LINE_C)]:
    box(s, x, y, w, 1.45, fill=fill, line=lc, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
    text(s, x, y + 0.2, w, 1.1, [[(label, {"bold": True, "size": 28})], [(sub, {"font": MONO, "size": 18, "color": INK if fill == LIME else SEC_C})]],
         align=PP_ALIGN.CENTER, after=2)
hline(s, 5.9, y + 0.72, 0.65, INK, 0.04)
hline(s, 13.45, y + 0.72, 0.65, INK, 0.04)
text(s, 1.0, 5.45, 18.0, 0.6, [[("Either signature missing → the call fails.", {"bold": True})]], size=30, align=PP_ALIGN.CENTER)
text(s, 1.0, 6.45, 18.0, 1.8, [
    [("— ", {"color": LIME_C}), ("Each handover moves custody and extends an on-chain hash chain, the ", {}), ("head", {"font": MONO}), (".", {})],
    [("— ", {"color": LIME_C}), ("The token stays with its holder in transit; only custody changes.", {})],
    [("— ", {"color": LIME_C}), ("After Delivered, the operator burns the token with the existing ", {}), ("redeem", {"font": MONO}), ("¹.", {})]],
    size=26, after=8)
text(s, 1.0, 8.65, 18.0, 1.0, [
    "A custody record keyed to the container number. In production it would sit beside the carrier's bill of lading; not integrated in this build.",
    "¹ Radox platform policy, not enforced on-chain by the registry; redeem still needs the holder's signature."],
    size=18, color=SEC_C, after=2)

# ---------- 5. Result: live on testnet (product page + technical workflow, merged to make room for the problem) ----------
s = content_slide(5, "THE PRODUCT · LIVE ON TESTNET", "7 testnet transactions. Anyone can check them.", "NEXT ▸ WHY STELLAR", dark=True)
s.shapes.add_picture(SHOT("page-handovers-rows.png"), Inches(1.0), Inches(3.4), width=Inches(7.4))
box(s, 1.0, 3.4, 7.4, 7.4 * 950 / 1400, line=LINE_D)
tx = 9.0
for i, (step, who, h) in enumerate(HASHES):
    y = 3.35 + i * 0.4
    text(s, tx, y, 10.0, 0.4, [[(h, {"color": LIME, "font": MONO}), (f"   {step} · {who}", {"color": TEXT_D})]], size=18)
for i, (num, label) in enumerate([("7", "successful"), ("9", "refused (simulated)"), ("24", "unit tests"), ("MATCH", "head check, 25 Oct")]):
    x = tx + i * 2.55
    text(s, x, 6.3, 2.5, 0.8, [num], size=44, font=TITLE, bold=True, color=LIME, spacing=0.9)
    text(s, x, 7.1, 2.45, 0.7, [label], size=18, color=TEXT_D)
text(s, tx, 7.55, 10.0, 1.6, [
    [("custody_registry ", {"color": SEC_D}), (CONTRACT, {"color": TEXT_D})],
    [("Plus attestation 33379211. Second run (branch three-machine): two team members authorised handovers on their own computers and testnet keys.", {"color": SEC_D, "font": BODY})],
    [("All test keys, mostly in one harness: it proves the mechanism, not independent custodians.", {"color": TEXT_D, "font": BODY, "bold": True})]],
    size=18, font=MONO, after=4)

# ---------- 6. Why Stellar ----------
s = content_slide(6, "ECOSYSTEM · WHY STELLAR", "Why Stellar: two signers, one call", "NEXT ▸ USERS AND MODEL")
rows = [("01", "Multi-party auth in one call", "Soroban authorises both custodians inside one contract invocation: the handover is atomic."),
        ("02", "Events plus an on-chain head", "RPC keeps contract events about 7 days. The head stored in the contract lets anyone rebuild the full history later."),
        ("03", "The token stays put, then burns", "The shipment token never moves in transit; the existing Radox redeem burns it after delivery.")]
for i, (n_, name, desc) in enumerate(rows):
    y = 3.55 + i * 1.5
    hline(s, 1.0, y - 0.12, 18.0, LINE_C, 0.02)
    text(s, 1.0, y + 0.08, 1.0, 0.6, [n_], size=24, font=MONO, bold=True, color=LIME_C)
    text(s, 2.0, y, 6.4, 1.2, [name], size=30, bold=True, font=TITLE)
    text(s, 8.6, y + 0.02, 10.4, 1.3, [desc], size=24, color=INK)
hline(s, 1.0, 7.93, 18.0, LINE_C, 0.02)
text(s, 1.0, 8.12, 18.0, 1.5, [
    [("Nearest neighbours we found on Stellar ", {"bold": True}), ("(LumenLoop, SCF, Scout, 24–25 Oct): ", {"color": SEC_C}),
     ("Kutana and Trustless Work release escrow on trade milestones; Pipeline finances commodity trade. We found none that records a custody handover signed by two custodians, and no SEP.", {})],
    [("Open source, Apache-2.0: ", {"bold": True, "color": LIME_C}), ("a custody primitive other Stellar real-world-asset issuers can reuse.", {})]],
    size=21, after=6)

# ---------- 7. Value: integrate once; open vs operated (canon: public standard on a Radox-operated rail) ----------
s = content_slide(7, "USERS · BUSINESS MODEL", "Integrate once, reach every party that joins", "NEXT ▸ BUILT THIS WEEKEND")
text(s, 1.0, 3.35, 18.0, 1.2, [[("With one public custody standard, a port, airport, carrier, chamber or financier would integrate once "
                                 "and reach every other party: adopt without a custom project.", {})]], size=24, color=INK)


def link(x1, y1, x2, y2, color, w=1.5):
    c = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    c.line.color.rgb = rgb(color)
    c.line.width = Pt(w)


R = 0.95
for cx, hub, head in ((2.8, False, "PAIR BY PAIR · 10 LINKS"), (6.65, True, "ONE RADOX RAIL · 5 LINKS")):
    cy = 5.95
    pts = [(cx + R * math.sin(2 * math.pi * k / 5), cy - R * math.cos(2 * math.pi * k / 5)) for k in range(5)]
    if hub:
        for x, y in pts:
            link(cx, cy, x, y, LIME_C, 2.0)
        dot(s, cx, cy, 0.42, LIME)
    else:
        for i in range(5):
            for j in range(i + 1, 5):
                link(*pts[i], *pts[j], SEC_C, 1.25)
    for x, y in pts:
        dot(s, x, y, 0.26, INK)
    text(s, cx - 1.8, 4.45, 3.6, 0.45, [head], size=18, font=MONO, bold=True, color=LIME_C if hub else SEC_C, align=PP_ALIGN.CENTER)
text(s, 1.0, 7.2, 7.8, 0.9, ["Example, 5 parties: 10 custom links, or 5 links to one standard."], size=20, color=SEC_C, align=PP_ALIGN.CENTER)
cols = [(9.3, "OPEN · ANYONE", LIME_C, ["Record format, roles and events: the custody_registry contract (Apache-2.0)", "Verify any shipment, no login (slide 5)"]),
        (14.35, "RADOX OPERATES · CLIENT PAYS", INK, ["Custodian onboarding, issuance controls, operation", "The API and backend: closed, not self-hostable", "Paid by the financial institution; not priced"])]
for x, head, hc, items in cols:
    text(s, x, 4.45, 4.8, 0.45, [head], size=18, font=MONO, bold=True, color=hc)
    hline(s, x, 4.98, 4.65, hc, 0.03)
    text(s, x, 5.15, 4.75, 3.0, [[("— ", {"color": hc}), (t_, {})] for t_ in items], size=21, after=8)
hline(s, 1.0, 8.3, 18.0, LINE_C, 0.02)
text(s, 1.0, 8.42, 18.0, 0.9, [
    "Adoption still takes work: a key per party, its own signatures, one connection to the rail (the Radox API).",
    [("Radox is the rail, never the issuer. Regulation and licences stay with the client and its local counsel.", {"color": SEC_C})]],
    size=18, after=2)

# ---------- 8. Hackathon progress ----------
s = content_slide(8, "HACKATHON PROGRESS", "Built this weekend, on disclosed prior work", "NEXT ▸ VISION AND ASK")
cols = [(1.0, "PRIOR WORK · BEFORE SUN 25 OCT 09:00", SEC_C, [
            "Radox platform (closed backend); its 3 Soroban contracts are on Stellar mainnet, public since 2026-08-19",
            "transfer_agent and its redeem (new testnet instance from the existing wasm)",
            "Architecture notes (20 Oct), planning files (24–25 Oct), the explainer video, our agent tooling (from 22 Oct)",
            "No contract code before then: first repo commit 25 Oct 09:00 UTC"]),
        (10.3, "BUILT AT HACKMERIDIAN", LIME_C, [
            "custody_registry contract, 24 unit tests",
            "Lifecycle harness: 7 testnet transactions, 9 refused calls",
            "verify-head script, the public shipment page, this deck",
            "Radox API reads the registry: same head (closed backend, testnet)"])]
for x, head, hc, items in cols:
    text(s, x, 3.5, 8.7, 0.5, [head], size=18, font=MONO, bold=True, color=hc)
    hline(s, x, 4.08, 8.7, hc, 0.03)
    text(s, x, 4.25, 8.7, 3.7, [[("— ", {"color": hc}), (t, {})] for t in items], size=21, after=8)
box(s, 1.0, 8.0, 18.0, 1.45, fill=CARD, line=LINE_C, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, 1.35, 8.12, 17.3, 1.2, [[("AI attribution  ", {"font": MONO, "bold": True, "color": LIME_C, "size": 18}),
                                ("Code, tests, scripts, the shipment page, docs and this deck were made with AI coding agents (Claude Code); the team decided scope and what ships. Per-file record in AI_USAGE.md. The video narration is an AI voice generated from Pedro's voice.", {})]],
     size=20, anchor=MSO_ANCHOR.MIDDLE)

# ---------- 9. Vision, next steps and ask ----------
s = content_slide(9, "VISION · NEXT · THE ASK", "Vision: one custody standard, every corridor", "NEXT ▸ THE TEAM")
text(s, 1.0, 3.4, 18.0, 1.3, [[("Rio–Miami is our pilot corridor. ", {"bold": True}),
                                ("The goal is a public, SWIFT-like custody standard on Stellar for tokenized goods in transit worldwide, "
                                 "to integrate with the systems of chambers of commerce, ports and airports.", {})]],
     size=26, color=INK)
phases = [("NOW", "Mechanism proven on testnet. No standard, users or revenue yet."),
          ("NEXT", "One Rio–Miami pilot shipment (none agreed yet). Full test matrix."),
          ("PLANNED", "SCF Build, then a security audit (neither done). Mainnet."),
          ("FUTURE", "More corridors; port, airport, chamber links (none confirmed); USD leg (not built).")]
hline(s, 1.2, 5.3, 13.8, LIME_C, 0.03)
for i, (k, v) in enumerate(phases):
    x = 1.0 + i * 4.6
    dot(s, x + 0.2, 5.3, 0.34 if i == 0 else 0.26, LIME_C)
    text(s, x, 5.55, 4.3, 0.5, [k], size=20, font=MONO, bold=True, color=LIME_C)
    text(s, x, 6.0, 4.3, 1.5, [v], size=22)
box(s, 1.0, 7.9, 18.0, 1.35, fill=LIME, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, 1.45, 7.9, 17.1, 1.35, [[("Our ask  ", {"font": MONO, "size": 20, "bold": True}),
                                  ("Introductions to one financial institution and one port, airport or logistics operator for a first pilot shipment, and a Stellar engineer's review of the design.", {"bold": True})]],
     size=24, anchor=MSO_ANCHOR.MIDDLE)

# ---------- 10. Team ----------
s = content_slide(10, "THE TEAM", "Why us: a founder already on Stellar mainnet", "FINAL STOP")
team = [("Pedro Wakigawa Saragossy", "Founder, captain. Built Radox: 3 Soroban contracts on Stellar mainnet."),
        ("Leo Schlanger", "Developer: custody_registry, the testnet harness and the proofs."),
        ("Vhendala", "QA and product review: reads every deliverable as a judge would.")]
for i, (name, role) in enumerate(team):
    y = 3.4 + i * 1.25
    text(s, 1.0, y, 10.8, 1.3, [[(name, {"bold": True, "size": 30, "font": TITLE})], [(role, {})]], size=21, color=INK, after=4)
text(s, 1.0, 7.15, 10.6, 0.5, ["Leo and Vhendala joined for the hackathon."], size=20, color=SEC_C)
if os.path.exists(SHOT("team.jpg")):  # drop the photo in deck/screens/team.jpg and rebuild
    s.shapes.add_picture(SHOT("team.jpg"), Inches(12.4), Inches(3.4), Inches(6.6), Inches(4.0))
else:
    box(s, 12.4, 3.4, 6.6, 4.0, line=SEC_C, shape=MSO_SHAPE.ROUNDED_RECTANGLE, dash=True)
    text(s, 12.4, 3.4, 6.6, 4.0, ["Team photo"], size=22, color=SEC_C, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
text(s, 1.0, 7.65, 18.0, 0.6, ["Rio–Miami first. Our goal: one custody standard for every corridor."], size=28, font=TITLE, bold=True, color=LIME_C)
hline(s, 1.0, 8.35, 18.0, LINE_C, 0.02)
text(s, 1.0, 8.45, 18.0, 1.2, [
    [("Live page  ", {"bold": True, "color": LIME_C}), ("rio-miami-rail.vercel.app", {}), ("     Code  ", {"bold": True, "color": LIME_C}),
     ("github.com/pwsaragossy/rio-miami-rail (Apache-2.0)", {})],
    [("AI  ", {"bold": True, "color": LIME_C}), ("Code, page, docs and deck made with AI coding agents (Claude Code). Narration: an AI voice from Pedro's voice. No AI-generated images in this deck.", {"font": BODY})]],
    size=18, font=MONO, after=6)

# drop the template's five original slides
ids = prs.slides._sldIdLst
for sld in list(ids)[:5]:
    prs.part.drop_rel(sld.rId)
    ids.remove(sld)
prs.save(OUT)
print("saved", OUT, len(prs.slides), "slides")
