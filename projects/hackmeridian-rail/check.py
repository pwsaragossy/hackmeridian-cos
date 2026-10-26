"""Target check: what a judge can open and run, logged out, from the submission. Last line = gates passed.

Exit 0 only when all gates pass. The old check counted only the 7 testnet transactions, so it
stayed green while the API, the docs, the video and the public repo were missing (owner, 26 Oct:
"o mapa está mentindo, ele diz que não falta nada, mas falta sim").
  lifecycle  the 7 lifecycle transactions are SUCCESS on testnet Horizon, 7 distinct hashes
  repo       github.com/pwsaragossy/rio-miami-rail is PUBLIC
  site       the demo site answers 200
  api        GET /api/shipments/<shipment 1 key> answers 200 JSON with a status (read live on testnet)
  docs       /docs answers 200 and shows the parameters and a request-access link
  form       FORM-ANSWERS.md has no {{placeholder}} left (video link and deck upload included)
  deck       the deck named in the form exists and is under 20 MiB
"""
import json
import os
import re
import subprocess
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
HORIZON = "https://horizon-testnet.stellar.org"
SITE = "https://rio-miami-rail.vercel.app"
SHIPMENT_1 = "31b4cff785831659b4ecb8fd3e7382f9760a12ef45ef7eb30f45b3b6911a5e37"
STEPS = ["open", "handover", "handover", "handover", "handover", "deliver", "redeem"]


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "hackmeridian-check"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status, r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception as e:
        return 0, str(e)


def lifecycle():
    raw = subprocess.run(
        ["gh", "api", "repos/pwsaragossy/rio-miami-rail/contents/proofs/lifecycle.json",
         "-H", "Accept: application/vnd.github.raw"],
        capture_output=True, text=True, timeout=30, check=True).stdout
    rows = json.loads(raw)["lifecycle"]
    hashes = [str(r.get("hash", "")) for r in rows]
    if [r.get("step") for r in rows] != STEPS or len(set(hashes)) != len(STEPS):
        return False, "steps or hashes are not the 7 expected"  # one tx copied 7 times must not pass
    ok = 0
    for h in hashes:
        code, body = get(f"{HORIZON}/transactions/{h}") if re.fullmatch(r"[0-9a-f]{64}", h) else (0, "")
        ok += code == 200 and json.loads(body).get("successful") is True
    return ok == len(STEPS), f"{ok}/7 SUCCESS"


def repo():
    v = subprocess.run(["gh", "repo", "view", "pwsaragossy/rio-miami-rail", "--json", "visibility", "-q", ".visibility"],
                       capture_output=True, text=True, timeout=30).stdout.strip()
    return v == "PUBLIC", v or "unknown"


def site():
    code, _ = get(SITE + "/")
    return code == 200, f"HTTP {code}"


def api():
    code, body = get(f"{SITE}/api/shipments/{SHIPMENT_1}")
    try:
        d = json.loads(body)
        status = (d.get("data") or d).get("status")
    except Exception:
        status = None
    return code == 200 and bool(status), f"HTTP {code}, status {status}"


def docs():
    code, body = get(SITE + "/docs")
    low = body.lower()
    params, access = "parameter" in low, "request access" in low
    return code == 200 and params and access, f"HTTP {code}, parameters {params}, request access {access}"


def form_text():
    with open(os.path.join(HERE, "FORM-ANSWERS.md")) as f:
        return f.read()


def form():
    left = re.findall(r"\{\{[^}]*\}\}", form_text())
    return not left, f"{len(left)} placeholder(s) left: " + "; ".join(x[:60] for x in left) if left else "none left"


def deck():
    m = re.search(r"(deck/[\w./-]+\.(?:pdf|pptx|ppt))", form_text())
    if not m:
        return False, "no deck path in the form"
    p = os.path.join(HERE, m.group(1))
    if not os.path.exists(p):
        return False, f"{m.group(1)} missing"
    size = os.path.getsize(p)
    return size < 20 * 1024 * 1024, f"{m.group(1)} {size} bytes"


GATES = [lifecycle, repo, site, api, docs, form, deck]
passed = 0
for fn in GATES:
    try:
        ok, why = fn()
    except Exception as e:  # no gh, no network, no file: the gate is not met
        ok, why = False, f"error: {e}"
    print(f"{'PASS' if ok else 'FAIL'} {fn.__name__}: {why}")
    passed += ok
print(passed)
sys.exit(0 if passed == len(GATES) else 1)
