"""Outside judge for the deck: exits 0 only when every rule below holds; prints each failure.

Run: python deck/check_deck.py [path/to/lifecycle.json]
(default: proofs/lifecycle.json read from pwsaragossy/rio-miami-rail with gh)
Rules: SUBMISSION.md (PDF <= 20 MiB, max 10 slides), LOOK.md (nothing to read under 18 pt),
PITCH.md Claims guard (banned words), proofs/lifecycle.json (every hash and the contract ID on the slides are real).
"""
import base64
import json
import os
import re
import subprocess
import sys

from pptx import Presentation
from pptx.util import Pt

HERE = os.path.dirname(os.path.abspath(__file__))
PPTX = os.path.join(HERE, "radox-custody-rail.pptx")
PDF = os.path.join(HERE, "radox-custody-rail.pdf")

# Claims guard (PITCH.md) and the ZIS rule ([[zis-in-public-material-radox-is-bc05]]); case-insensitive.
BANNED = [r"\btitle to\b", r"document of title", r"digital bill of lading", r"replaces? the bill of lading",
          r"proof of ownership", r"legally recognised", r"\bUCC\b", r"\bMLETR\b", r"\bcustomers\b(?! has)",
          r"\binvestors?\b", r"\btraction\b", r"live pilot", r"\bendorse", r"\bbacked by\b", r"\bpartner(s)?\b",
          r"\bZIS\b", r"\bPaulo\b", r"none exists", r"\bmainnet-ready\b", r"\bsponsor"]
TEMPLATE_SMALL = {"107", "108", "109", "122", "84", "85", "99", "100", "101"}  # template's decorative 12-14 pt labels


def lifecycle(argv):
    if len(argv) > 1:
        return json.load(open(argv[1]))
    out = subprocess.run(["gh", "api", "repos/pwsaragossy/rio-miami-rail/contents/proofs/lifecycle.json",
                          "--jq", ".content"], capture_output=True, text=True, check=True).stdout
    return json.loads(base64.b64decode(out))


def main():
    fails = []
    prs = Presentation(PPTX)
    n = len(prs.slides)
    if n > 10:
        fails.append(f"{n} slides, max 10")
    if not os.path.exists(PDF):
        fails.append("PDF missing")
    elif os.path.getsize(PDF) > 20 * 1024 * 1024:
        fails.append(f"PDF {os.path.getsize(PDF)} bytes > 20 MiB")
    if os.path.exists(PDF) and os.path.getmtime(PDF) < os.path.getmtime(PPTX):
        fails.append("PDF older than PPTX: re-export")

    texts = []
    for i, s in enumerate(prs.slides, 1):
        for sh in s.shapes:
            if not sh.has_text_frame:
                continue
            key = sh.name.split(";")[1] if ";" in sh.name else ""
            for p in sh.text_frame.paragraphs:
                for r in p.runs:
                    if not r.text.strip():
                        continue
                    texts.append((i, r.text))
                    if key not in TEMPLATE_SMALL and r.font.size is not None and r.font.size < Pt(18):
                        fails.append(f"slide {i}: {r.font.size.pt:.0f} pt < 18: {r.text[:40]!r}")
    full = "\n".join(t for _, t in texts)
    for pat in BANNED:
        for i, t in texts:
            if re.search(pat, t, re.I):
                fails.append(f"slide {i}: banned /{pat}/ in {t[:60]!r}")

    lc = lifecycle(sys.argv)
    real = [x["hash"] for x in lc["lifecycle"]]
    if len(real) != 7:
        fails.append(f"lifecycle has {len(real)} txs, expected 7")
    for h in real:
        if h[:8] not in full:
            fails.append(f"hash {h[:8]} from proofs not on any slide")
    for h in set(re.findall(r"\b[0-9a-f]{8}\b", full)):
        if not any(r.startswith(h) for r in real + [x["hash"] for x in lc.get("attest", [])]) and h not in lc.get("custody_registry", "").lower():
            fails.append(f"8-hex token {h} on a slide is not a lifecycle hash")
    contract = lc["custody_registry"] if isinstance(lc["custody_registry"], str) else lc["custody_registry"].get("id", "")
    if contract and contract not in full:
        fails.append(f"contract {contract} not on the slides")

    for f in fails:
        print("FAIL", f)
    print(f"slides={n} pdf_bytes={os.path.getsize(PDF) if os.path.exists(PDF) else 0} failures={len(fails)}")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
