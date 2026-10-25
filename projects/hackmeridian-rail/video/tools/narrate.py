# One wav per DEMO-SCRIPT row with the cloned profile (server running, see ../README.md).
# Usage: python3 narrate.py rows.json outdir; rows.json is [{"t": "0:00–0:20", "text": ...}] from the Narration column.
import json, sys, time, sqlite3, shutil, urllib.request, os
rows, out = json.load(open(sys.argv[1])), sys.argv[2]
D = os.path.expanduser("~/Movies/hackmeridian-rail-video/voicebox-data")
API, PROFILE = "http://127.0.0.1:17493", "316a059e-bbaa-4e3b-a392-f1606759ba8a"
# spoken forms only: identifiers read as words
SAY = {"custody_registry": "custody registry", "require_auth": "require auth", "verify-head": "verify head",
       "TEST4627832": "test four six two seven eight three two"}
# seeds that read back cleanest in a local transcription (DEMO-SCRIPT 5bc5ca6)
SEEDS = {1: 23, 2: 23}
os.makedirs(out, exist_ok=True)
for _ in range(120):
    try: urllib.request.urlopen(API + "/health", timeout=2); break
    except Exception: time.sleep(2)
for i, r in enumerate(rows):
    text = r["text"]
    for k, v in SAY.items(): text = text.replace(k, v)
    body = json.dumps({"profile_id": PROFILE, "text": text, "language": "en", "engine": "qwen", "model_size": "1.7B", "seed": SEEDS.get(i, 7)}).encode()
    gid = json.load(urllib.request.urlopen(urllib.request.Request(API + "/generate", body, {"Content-Type": "application/json"})))["id"]
    while True:
        st, path, dur, err = sqlite3.connect(D + "/voicebox.db").execute("select status,audio_path,duration,error from generations where id=?", (gid,)).fetchone()
        if st in ("completed", "failed"): break
        time.sleep(5)
    if st == "failed": sys.exit(f"{r['t']} failed: {err}")
    dst = f"{out}/{i+1:02d}-{r['t'][:4].replace(':','')}.wav"
    shutil.copy(os.path.join(D, path), dst)
    print(f"{r['t']}\t{dur:.2f}s\t{dst}", flush=True)
