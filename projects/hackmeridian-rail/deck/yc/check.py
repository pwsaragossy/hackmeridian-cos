"""Outside judge for deck/yc: exits 0 only when every rule holds; prints each failure, then the slide count.

Run: python3 deck/yc/check.py
Rules: PDF exists, newer than build.py, <= 20 MiB, 10 slides (SUBMISSION.md); every number on a slide is in TRACE and
appears in its source file; no banned names or claims (PITCH.md Claims guard, owner limits 2026-10-26);
at most MAX_WORDS words per slide (YC: one idea per slide, [[yc-pitch-deck-design-rules-kevin-bd35]]);
every required topic (RULES.md Scale requirement 5) has its slide.
"""
import html as htmllib
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.dirname(os.path.dirname(HERE))
HOME = os.path.expanduser("~")
PDF = os.path.join(HERE, "radox-custody-rail-yc.pdf")
HTML = os.path.join(HERE, "deck.html")
MAX_WORDS = 70

# number as printed on a slide -> (file that verified it, text that must be in that file)
NOTES = os.path.join(HOME, "hackmeridian", "knowledge", "notes")
RAIL = os.path.join(HOME, "code", "rio-miami-rail")
TRACE = {
    "2026": (os.path.join(PROJ, "RULES.md"), "2026"),  # event name and source dates
    "80–90%": (os.path.join(PROJ, "MARKET-NUMBERS.md"), "80 to 90 per cent of world trade relies on trade finance"),
    "32-byte": (os.path.join(PROJ, "FORM-ANSWERS.md"), "32-byte"),
    "10": (None, "pair-by-pair links among 5 companies: 5*4/2, computed in check"),
    "5": (None, "five companies on the route: ROUTE in build.py"),
    "7": (os.path.join(RAIL, "proofs", "lifecycle.json"), None),  # counted below
    "9": (os.path.join(RAIL, "proofs", "mainnet-rehearsal.json"), None),
    "26": (os.path.join(RAIL, "contracts", "custody_registry", "src"), None),
    "15": (os.path.join(RAIL, "proofs", "mainnet-rehearsal.json"), None),
    "13.72": (os.path.join(RAIL, "proofs", "mainnet-rehearsal.json"), "13.72"),
    "45M": (os.path.join(PROJ, "MARKET-NUMBERS.md"), "around 45 million bills of lading a year"),
    "Feb 2023": (os.path.join(PROJ, "MARKET-NUMBERS.md"), "15 Feb 2023"),
    "US$2.5T": (os.path.join(NOTES, "adb-trade-finance-gap-survey-dec-d033.md"), "$2.5 trillion"),
    "Dec 2025": (os.path.join(NOTES, "adb-trade-finance-gap-survey-dec-d033.md"), "December 2025"),
    "US$4B": (os.path.join(NOTES, "stellar-tokenized-rwa-size-on-2026-a455.md"), "4 billion dollars in tokenized real-world assets"),
    "1 Sep 2026": (os.path.join(NOTES, "stellar-tokenized-rwa-size-on-2026-a455.md"), "as of September 1, 2026"),
    "25 Oct 2026": (os.path.join(PROJ, "MARKET-NUMBERS.md"), "2026-10-25 at 19:20 UTC"),
    "US$94.2 billion": (os.path.join(PROJ, "MARKET-NUMBERS.md"), "about US$94.2 billion in 2025"),
    "20": (None, "G20: owner statement in chat, 2026-10-26 (pilot to be presented at the G20 in the US in December)"),
    "Sep 2026": (os.path.join(NOTES, "stellar-tokenized-rwa-size-on-2026-a455.md"), "as of September 1, 2026"),
    "36": (os.path.join(PROJ, "PROBLEM-NUMBERS.md"), "covering all 36 key trade documents"),
    "2024": (os.path.join(PROJ, "PROBLEM-NUMBERS.md"), "24 Apr 2024"),
    "5.7%": (os.path.join(PROJ, "PROBLEM-NUMBERS.md"), "5,7% in January 2025"),
    "January 2025": (os.path.join(PROJ, "PROBLEM-NUMBERS.md"), "5,7% in January 2025"),
    "1.2%": (os.path.join(PROJ, "PROBLEM-NUMBERS.md"), "In 2021, only 1.2%"),
    "11%": (os.path.join(PROJ, "PROBLEM-NUMBERS.md"), "around 11% of bills of lading are issued electronically"),
    "2021": (os.path.join(PROJ, "PROBLEM-NUMBERS.md"), "In 2021, only 1.2%"),
    "45": (os.path.join(PROJ, "MARKET-NUMBERS.md"), "around 45 million bills of lading a year"),
    "180M": (os.path.join(PROJ, "MARKET-NUMBERS.md"), "about 180 million custody handovers a year"),
    "~180M": (os.path.join(PROJ, "MARKET-NUMBERS.md"), "about 180 million custody handovers a year"),
    "4": (os.path.join(PROJ, "MARKET-NUMBERS.md"), "4 dual-signed handovers in our testnet demo"),
    "2023": (os.path.join(PROJ, "MARKET-NUMBERS.md"), "15 Feb 2023"),
    "2025": (os.path.join(PROJ, "MARKET-NUMBERS.md"), "in 2025"),
    "3": (os.path.join(PROJ, "FORM-ANSWERS.md"), "three mainnet contracts"),
    "2.0": (os.path.join(RAIL, "LICENSE"), "Apache License"),  # Apache-2.0
}
NUM = re.compile(r"US\$[\d.,]+\s?(?:billion|[TBM])?|\d+(?:[.,]\d+)?(?:–\d+)?%?(?:-byte|M)?(?: (?:Feb|Dec|Sep|Oct) \d{4})?")
DATES = [r"(?:\d{1,2} )?(?:Feb|Dec|Sep|Oct) \d{4}"]

# Claims guard + owner limits for this deck (brief 2026-10-26).
BANNED = [r"\bpartner", r"\bZIS\b", r"\bPaulo\b", r"PortMiami", r"\bairport", r"Hin Leong", r"\bcustomers?\b",
          r"\busers have\b", r"\brevenue\b", r"\btraction\b", r"(live|deployed|running|launched) on (Stellar )?mainnet",
          r"mainnet-ready", r"publicly hosted", r"api\.radox", r"\bendorse", r"\bbacked by\b", r"\bin talks\b", r"\bsponsor",
          r"(port|bank|airport|chamber).{0,40}(signed|agreed|committed|joined)", r"(?<!nothing sent to )\b(ran|runs) on (Stellar )?mainnet", r"\bcustoms brokers?\b", r"title to", r"document of title", r"bill of lading replace", r"\bLeo-agent\b", r"\{\{", r"\bdemo\b"]
REQUIRED = {"Problem": "problem", "Solution": "solution", "Target users": "target users", "Value proposition": "value proposition",
            "Team": "team", "vision": "future vision", "Business model": "business model", "Market opportunity": "market opportunity",
            "Go-to-market": "go-to-market", "testnet": "network named", "Claude Code": "AI disclosure", "prior work": "prior work disclosure",
            "not affiliated with Swift": "Swift disclaimer"}


def slides():
    raw = open(HTML).read()
    out = []
    for sec in re.findall(r"<section[^>]*>(.*?)</section>", raw, re.S):
        sec = re.sub(r"<svg.*?</svg>", lambda m: " ".join(re.findall(r">([^<>]+)</text>", m.group(0))), sec, flags=re.S)
        text = htmllib.unescape(re.sub(r"<[^>]+>", " ", sec))
        out.append(re.sub(r"\s+", " ", text).strip())
    return out


def proof_counts():
    import json
    life = json.load(open(os.path.join(RAIL, "proofs", "lifecycle.json")))
    reh = json.load(open(os.path.join(RAIL, "proofs", "mainnet-rehearsal.json")))
    hashes = set(re.findall(r"\b[0-9a-f]{64}\b", json.dumps(life["lifecycle"])))
    src = os.path.join(RAIL, "contracts", "custody_registry", "src")
    tests = sum(open(os.path.join(src, f)).read().count("#[test]")
                for f in os.listdir(src) if f.endswith(".rs"))
    return {"7": len(hashes), "15": len(reh["steps"]), "9": len(reh["failures"]), "26": tests,
            "9-life": len(life["failures"])}


def main():
    fails = []
    if not os.path.exists(PDF):
        sys.exit("PDF missing: run python3 deck/yc/build.py")
    size = os.path.getsize(PDF)
    if size > 20 * 1024 * 1024:
        fails.append(f"PDF {size} bytes > 20 MiB")
    if os.path.getmtime(PDF) < os.path.getmtime(os.path.join(HERE, "build.py")):
        fails.append("PDF older than build.py: rebuild")
    pages = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", PDF], capture_output=True, text=True).stdout).group(1))
    sl = slides()
    if pages != len(sl) or pages > 10:
        fails.append(f"PDF {pages} pages, HTML {len(sl)} slides, max 10")

    counts = proof_counts()
    expect = {"7": 7, "15": 15, "9": 9, "26": 26}
    for k, v in expect.items():
        if counts[k] != v:
            fails.append(f"proof count {k}: source says {counts[k]}")
    if counts["9-life"] != 9:
        fails.append(f"lifecycle refusals: source says {counts['9-life']}")
    for key, (path, needle) in TRACE.items():
        if path and needle and needle not in open(path).read():
            fails.append(f"trace {key!r}: {needle!r} not found in {path}")

    full = "\n".join(sl)
    for i, t in enumerate(sl, 1):
        words = len(re.findall(r"[A-Za-z0-9$%–.\-]+", re.sub(r"\b[A-Z0-9]{56}\b", "", t)))
        if words > MAX_WORDS:
            fails.append(f"slide {i}: {words} words > {MAX_WORDS}")
        clean = re.sub(r"\b[A-Z0-9]{56}\b", "", t)  # contract ID
        clean = clean.replace("custody_registry", "").replace("Apache-2.0", "Apache-2.0 2.0").replace("CUSTODY-SPEC.md", "")
        for m in NUM.finditer(clean):
            tok = m.group(0).strip()
            if re.fullmatch(r"\d{1,2}", tok) and clean.rstrip().endswith(tok) and tok == str(i):
                continue  # page number
            if tok not in TRACE and not any(re.fullmatch(d, tok) for d in DATES if tok in TRACE):
                if tok == str(i):
                    continue
                fails.append(f"slide {i}: untraced number {tok!r}")
        for pat in BANNED:
            if re.search(pat, t, re.I):
                fails.append(f"slide {i}: banned /{pat}/")
        print(f"slide {i}: {words} words")
    for needle, topic in REQUIRED.items():
        if needle.lower() not in full.lower():
            fails.append(f"missing: {topic} ({needle!r})")
    if "Radox Custody Rail" not in sl[0] or "SWIFT for goods in transit, on Stellar" not in sl[0].replace("transit, on", "transit, on"):
        fails.append("cover does not carry the form title")

    for f in fails:
        print("FAIL", f)
    print(f"{'OK' if not fails else 'FAILED'}: {pages} slides, {size} bytes, {len(fails)} failures")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
