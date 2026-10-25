"""Build deck/radox-custody-rail.pptx from the organizers' DECK-TEMPLATE.pptx.

Run: python deck/build_deck.py   (needs python-pptx and Pillow), then
     soffice --headless --convert-to pdf --outdir deck deck/radox-custody-rail.pptx
Copy rules: PITCH.md Claims guard and [[wording-the-rio-miami-deck-readme-ef38]].
Every fact on a slide has its source in deck/REVIEW.md (claims table).
"""
import copy
import io
import os

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
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
text(s, 1.0, 5.95, 12.5, 0.5, ["A dual-signed custody record on Stellar  ·  First corridor: Rio–Miami"],
     size=24, color=SEC_D)
s.shapes.add_picture(SHOT("qr-page-dark.png"), Inches(15.75), Inches(1.75), Inches(2.6), Inches(2.6))
text(s, 14.3, 4.5, 5.5, 0.9, ["Scan: the live shipment", [("rio-miami-rail.vercel.app", {"font": MONO, "color": LIME, "size": 18})]],
     size=20, color=TEXT_D, align=PP_ALIGN.CENTER, after=2)
hline(s, 14.0, 6.15, 5.0, LIME_C, 0.03)
for i in range(6):
    dot(s, 14.0 + i * 1.0, 6.15, 0.26 if i in (0, 5) else 0.16, LIME)
text(s, 13.87, 6.42, 2.0, 0.4, ["RIO"], size=18, font=MONO, bold=True, color=SEC_D)
text(s, 17.13, 6.42, 2.0, 0.4, ["MIAMI"], size=18, font=MONO, bold=True, color=SEC_D, align=PP_ALIGN.RIGHT)

# ---------- 2. Problem (template: PMF) ----------
s = content_slide(2, "PMF · THE PROBLEM", "Who holds the cargo right now?", "NEXT ▸ THE SOLUTION")
text(s, 1.0, 3.55, 11.2, 1.2, ["Between seller and buyer, a shipment changes hands several times."], size=30, color=INK)
stops = ["Warehouse", "Port", "Carrier", "Customs", "Buyer"]
x0, x1, ly = 1.9, 11.4, 5.35
hline(s, x0, ly, x1 - x0, LIME_C, 0.03)
for i, name in enumerate(stops):
    cx = x0 + i * (x1 - x0) / 4
    dot(s, cx, ly, 0.34, LIME_C)
    text(s, cx - 1.2, ly + 0.32, 2.4, 0.5, [name], size=22, bold=True, align=PP_ALIGN.CENTER)
text(s, 1.0, 6.4, 11.2, 1.0, ["Handovers are mostly paper, or sit inside one operator's own system."], size=26, color=SEC_C)
text(s, 1.0, 7.6, 11.2, 1.2, [[("Our hypothesis: ", {"bold": True, "color": LIME_C}),
                                ("a financier cannot see who holds the goods before paying. No customer has confirmed it yet; we are testing it with mentors.", {})]],
     size=24, color=INK)
text(s, 13.2, 3.55, 5.8, 1.1, ["US$2.5T"], size=64, font=TITLE, bold=True, color=INK, spacing=0.95)
text(s, 13.2, 4.6, 5.8, 2.6, ["Global trade finance gap.",
                               [("ADB Global Trade Finance Gap Survey, Dec 2025. It sizes the financing gap; it is not evidence of the custody problem.", {"size": 18, "color": SEC_C, "bold": False})]],
     size=24, bold=True, after=10)
text(s, 1.0, 8.75, 18.0, 0.9, [BRIDGE], size=18, color=SEC_C)

# ---------- 3. Solution ----------
s = content_slide(3, "THE SOLUTION", "Both custodians sign, or nothing changes", "NEXT ▸ THE PRODUCT")
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

# ---------- 4. Product ----------
s = content_slide(4, "THE PRODUCT · LIVE ON TESTNET", "Anyone can check the chain. No login.", "NEXT ▸ TECHNICAL WORKFLOW", dark=True)
s.shapes.add_picture(SHOT("page-handovers-rows.png"), Inches(1.0), Inches(3.45), width=Inches(8.9))
box(s, 1.0, 3.45, 8.9, 8.9 * 950 / 1400, line=LINE_D)
tx = 10.6
text(s, tx, 3.45, 8.4, 2.2, [[("Verify head", {"bold": True, "color": LIME}),
                              (" recomputes the hash chain in the browser and compares it with the head stored in the contract.", {})]],
     size=26, color=TEXT_D)
text(s, tx, 5.75, 6.0, 1.2, ["MATCH"], size=80, font=MONO, bold=True, color=LIME, spacing=0.9)
text(s, tx, 6.95, 5.6, 1.6, ["Clicked live on 25 Oct 2026.", "Read-only: Stellar RPC and Horizon, no wallet."],
     size=20, color=SEC_D, after=6)
s.shapes.add_picture(SHOT("qr-page-dark.png"), Inches(16.8), Inches(6.2), Inches(2.2), Inches(2.2))
text(s, 14.0, 8.6, 5.0, 0.4, ["rio-miami-rail.vercel.app"], size=18, font=MONO, color=LIME, align=PP_ALIGN.RIGHT)

# ---------- 5. Technical workflow ----------
s = content_slide(5, "TECHNICAL WORKFLOW", "7 testnet transactions. All successful.", "NEXT ▸ WHY STELLAR", dark=True)
w, y = 18.0 / 7, 3.6
hline(s, 1.0 + w / 2, y + 0.15, 18.0 - w, LIME_C, 0.03)
for i, (step, who, h) in enumerate(HASHES):
    x = 1.0 + i * w
    edge = i in (0, 6)
    dot(s, x + w / 2, y + 0.15, 0.4 if edge else 0.26, LIME)
    text(s, x + 0.05, y + 0.5, w - 0.1, 1.0, [[(step, {"bold": True, "size": 24})], [(who, {"size": 18, "color": SEC_D})]],
         color=TEXT_D, align=PP_ALIGN.CENTER, after=2)
    text(s, x + 0.05, y + 1.5, w - 0.1, 0.4, [h], size=18, font=MONO, color=SLATE_D, align=PP_ALIGN.CENTER)
for i, (num, label) in enumerate([("7", "successful testnet transactions"), ("9", "invalid calls refused (simulated)"),
                                  ("24", "contract unit tests pass"), ("MATCH", "verify-head rebuilds the chain")]):
    x = 1.0 + i * 4.6
    text(s, x, 5.85, 4.4, 1.1, [num], size=72, font=TITLE, bold=True, color=LIME, spacing=0.9)
    text(s, x, 7.0, 4.3, 0.8, [label], size=22, color=TEXT_D)
text(s, 1.0, 8.05, 18.0, 1.6, [
    [("custody_registry  ", {"color": SEC_D}), (CONTRACT, {"color": TEXT_D})],
    [("Plus one event attestation by a source custodian (33379211), also on chain. Full hashes: the repo's proofs/lifecycle.json.", {"color": SEC_D, "font": BODY})],
    [("Every actor is a test key held by one harness: this proves the mechanism, not independent custodians.", {"color": TEXT_D, "font": BODY, "bold": True})]],
    size=18, font=MONO, after=6)

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
    [("Nearest neighbours we found ", {"bold": True}), ("(LumenLoop, SCF, Scout; searched 24–25 Oct 2026): ", {"color": SEC_C}),
     ("Kutana and Trustless Work release escrow on trade milestones. We found none that records a custody handover signed by two custodians, and no SEP for it.", {})],
    [("Open source, Apache-2.0: ", {"bold": True, "color": LIME_C}), ("a custody primitive other Stellar real-world-asset issuers can reuse.", {})]],
    size=21, after=6)

# ---------- 7. Users and business model ----------
s = content_slide(7, "USERS · BUSINESS MODEL", "Custodians sign. Financiers check.", "NEXT ▸ BUILT THIS WEEKEND")
users = [("CUSTODIANS", "Warehouse, port, carrier, customs: sign each handover."),
         ("EXPORTER · BUYER", "See where the goods are and who holds them."),
         ("FINANCIER", "Checks the custody chain before paying."),
         ("OPERATOR", "A financial institution, the client, would run the rail for its trade flows.")]
for i, (k, v) in enumerate(users):
    y = 3.6 + i * 1.5
    hline(s, 1.0, y - 0.14, 9.6, LINE_C, 0.02)
    text(s, 1.0, y, 3.3, 0.5, [k], size=18, font=MONO, bold=True, color=LIME_C)
    text(s, 4.3, y - 0.04, 6.3, 1.2, [v], size=24)
box(s, 11.4, 3.45, 7.6, 5.7, fill=CARD, line=LINE_C, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, 11.85, 3.75, 6.8, 5.5, [
    [("MODEL · THE OPERATOR PAYS", {"font": MONO, "size": 18, "bold": True, "color": LIME_C})],
    [("SWIFT-style: the record format is public; Radox runs the rail and the API.", {"bold": True})],
    "Revenue: a fee from the financial institution that operates the rail. Not priced yet.",
    [("Radox is the rail, never the issuer. Regulation and licences stay with the client and its local counsel.", {"color": SEC_C, "size": 22})]],
    size=26, after=18)

# ---------- 8. Hackathon progress ----------
s = content_slide(8, "HACKATHON PROGRESS", "Built this weekend, on disclosed prior work", "NEXT ▸ WHAT COMES NEXT")
cols = [(1.0, "PRIOR WORK · BEFORE SUN 25 OCT 09:00", SEC_C, [
            "Radox platform and 3 Soroban contracts on Stellar mainnet (public repo, created 2026-08-19)",
            "transfer_agent and its redeem (new testnet instance from the existing wasm)",
            "Planning files, 24–25 Oct"]),
        (10.3, "BUILT AT HACKMERIDIAN", LIME_C, [
            "custody_registry contract, 24 unit tests",
            "Lifecycle harness: 7 testnet transactions, 9 refused calls",
            "verify-head script and the public shipment page",
            "Radox API reads the registry: same head (closed backend, testnet)"])]
for x, head, hc, items in cols:
    text(s, x, 3.5, 8.7, 0.5, [head], size=18, font=MONO, bold=True, color=hc)
    hline(s, x, 4.08, 8.7, hc, 0.03)
    text(s, x, 4.3, 8.7, 3.8, [[("— ", {"color": hc}), (t, {})] for t in items], size=24, after=14)
box(s, 1.0, 8.0, 18.0, 1.45, fill=CARD, line=LINE_C, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, 1.35, 8.12, 17.3, 1.2, [[("AI attribution  ", {"font": MONO, "bold": True, "color": LIME_C, "size": 18}),
                                ("Code, tests and scripts were written with AI coding agents (Claude Code); the team decided scope and what ships. Per-file record in AI_USAGE.md. The video narration is an AI voice generated from Pedro's voice.", {})]],
     size=20, anchor=MSO_ANCHOR.MIDDLE)

# ---------- 9. Next steps and ask ----------
s = content_slide(9, "NEXT · THE ASK", "Next: one pilot shipment, not yet agreed", "NEXT ▸ THE TEAM")
phases = [("NOW", "Testnet this weekend: contract, 7 transactions, public page, API read."),
          ("NEXT", "Full testnet test matrix. A first pilot shipment with one producer (none agreed yet)."),
          ("PLANNED", "SCF Build application (not yet submitted). Security audit before mainnet (not done)."),
          ("FUTURE", "Mainnet. A USD on-ramp leg (not built).")]
hline(s, 1.2, 3.75, 13.8, LIME_C, 0.03)
for i, (k, v) in enumerate(phases):
    x = 1.0 + i * 4.6
    dot(s, x + 0.2, 3.75, 0.34 if i == 0 else 0.26, LIME_C)
    text(s, x, 4.1, 4.3, 0.5, [k], size=20, font=MONO, bold=True, color=LIME_C)
    text(s, x, 4.6, 4.3, 2.2, [v], size=24)
text(s, 1.0, 6.85, 18.0, 0.6, [[("No users or revenue yet. ", {"bold": True}), ("First users come from one pilot shipment in the Rio–Miami corridor.", {"color": SEC_C})]], size=24)
box(s, 1.0, 7.6, 18.0, 1.55, fill=LIME, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, 1.45, 7.65, 17.1, 1.45, [[("Our ask  ", {"font": MONO, "size": 20, "bold": True}),
                                  ("Introductions to one financial institution and one logistics operator for a first pilot shipment, and a Stellar engineer's review of the design.", {"bold": True})]],
     size=26, anchor=MSO_ANCHOR.MIDDLE)

# ---------- 10. Team ----------
s = content_slide(10, "THE TEAM", "Why us: a founder already on Stellar mainnet", "FINAL STOP")
team = [("Pedro Wakigawa Saragossy", "Founder, captain. Built Radox: 3 Soroban contracts on Stellar mainnet."),
        ("Leo Schlanger", "Developer: custody_registry, the testnet harness and the proofs."),
        ("Vhendala", "QA and product review: reads every deliverable as a judge would.")]
for i, (name, role) in enumerate(team):
    y = 3.45 + i * 1.5
    text(s, 1.0, y, 10.8, 1.3, [[(name, {"bold": True, "size": 30, "font": TITLE})], [(role, {})]], size=21, color=INK, after=4)
text(s, 1.0, 7.65, 10.6, 0.5, ["Leo and Vhendala joined for the hackathon."], size=20, color=SEC_C)
box(s, 12.4, 3.5, 6.6, 4.5, line=SEC_C, shape=MSO_SHAPE.ROUNDED_RECTANGLE, dash=True)
text(s, 12.4, 3.5, 6.6, 4.5, ["Team photo"], size=22, color=SEC_C, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
hline(s, 1.0, 8.3, 18.0, LINE_C, 0.02)
text(s, 1.0, 8.45, 18.0, 1.2, [
    [("Live page  ", {"bold": True, "color": LIME_C}), ("rio-miami-rail.vercel.app", {}), ("     Code  ", {"bold": True, "color": LIME_C}),
     ("github.com/pwsaragossy/rio-miami-rail (Apache-2.0)", {})],
    [("AI  ", {"bold": True, "color": LIME_C}), ("Code written with AI coding agents (Claude Code). Narration: an AI voice from Pedro's voice. No AI-generated images in this deck.", {"font": BODY})]],
    size=18, font=MONO, after=6)

# drop the template's five original slides
ids = prs.slides._sldIdLst
for sld in list(ids)[:5]:
    prs.part.drop_rel(sld.rId)
    ids.remove(sld)
prs.save(OUT)
print("saved", OUT, len(prs.slides), "slides")
