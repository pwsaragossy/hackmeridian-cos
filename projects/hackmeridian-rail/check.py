"""Target check: the 7 lifecycle transactions are SUCCESS on the public testnet RPC.

Reads proofs/lifecycle.json from github.com/pwsaragossy/rio-miami-rail (main) through `gh`,
then asks testnet Horizon for each hash. Exit 0 when all 7 steps succeeded; last line = the count.
Expected file shape: {"lifecycle": [{"step": "open", "hash": "<64 hex>"}, ...]}
with the steps open, handover x4, deliver, redeem, in that order.
"""
import json
import re
import subprocess
import sys
import urllib.request

HORIZON = "https://horizon-testnet.stellar.org"
STEPS = ["open", "handover", "handover", "handover", "handover", "deliver", "redeem"]


def done(n, msg=""):
    if msg:
        print(msg)
    print(n)
    sys.exit(0 if n == len(STEPS) else 1)


def tx_status(h):
    # Horizon keeps the full testnet history; the RPC only keeps a short window.
    req = urllib.request.Request(f"{HORIZON}/transactions/{h}", headers={"User-Agent": "hackmeridian-check"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return "SUCCESS" if json.load(r).get("successful") else "FAILED"
    except urllib.error.HTTPError as e:
        return "NOT_FOUND" if e.code == 404 else f"HTTP_{e.code}"


try:
    raw = subprocess.run(
        ["gh", "api", "repos/pwsaragossy/rio-miami-rail/contents/proofs/lifecycle.json",
         "-H", "Accept: application/vnd.github.raw"],
        capture_output=True, text=True, timeout=30, check=True).stdout
    rows = json.loads(raw)["lifecycle"]
except Exception as e:  # no file yet, no gh, bad JSON: the target is not met
    done(0, f"proofs/lifecycle.json not readable: {e}")

if [r.get("step") for r in rows] != STEPS:
    done(0, f"steps are {[r.get('step') for r in rows]}, expected {STEPS}")

ok = 0
for r in rows:
    h = str(r.get("hash", ""))
    if not re.fullmatch(r"[0-9a-f]{64}", h):
        print(f"{r['step']}: bad hash {h!r}")
        continue
    s = tx_status(h)
    print(f"{r['step']}: {h[:12]}… {s}")
    ok += s == "SUCCESS"
done(ok)
