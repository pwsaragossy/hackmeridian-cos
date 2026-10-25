Reviewer: independent reviewer subagent (role card reviewer), briefed by session-hackmeridian-rail; work reviewed: LEO-TASKS.md and AI_USAGE rows (c3086e1)

Time: Sun Oct 25 16:53 UTC 2026

# Verdict: APPROVE WITH CHANGES

The repo can go public Sun night with no leak. My own scrub of tree and full history found nothing that must be fixed (hits below). LEO-TASKS.md can be run by Leo's agent after 5 fixes; as written, task 2 contradicts the repo (README names radox-internal on purpose) and task 3 overstates what remote-sign.mjs is. AI_USAGE c3086e1: 1 row overclaims, the `proofs/` row is now wrong, and `remote-sign.mjs` row 20 is true but not what the task says.

## My scrub (rio-miami-rail, HEAD c3086e1 local + `git log -p --all`, 36 commits, refs: main, origin/main, origin/three-machine; no tags)

| Check | Result |
|---|---|
| `S[A-Z2-7]{55}` tree and history | 0 hits |
| `-----BEGIN` | 0 hits |
| `/Users/`, `/home/`, `C:\`, `Desktop/hackaton` | 0 hits |
| `ZIS` and `Paulo` as words | 0 hits |
| `radox-internal` | 1 hit, tree: README.md:145 "The Radox backend, `radox-internal`, is closed and not published ..." (and the same line in the history of README.md). Intentional disclosure, keep it |
| Commit metadata | only 2 identities, both GitHub noreply (`148293189+pwsaragossy@...`, 10 commits by `37229572+leo-schlanger@...`); no personal e-mail anywhere in the diff text either |
| File names ever committed (`git log --all --name-only`) | nothing outside the current `git ls-files`: no `work/`, `.stellar`, `.env`, `request-*.json`, `response-*.json`, no deleted files |
| Hosts in history | github.com, horizon-testnet, soroban-testnet, stellar.expert, rio-miami-rail.vercel.app, npm, Google Fonts, jsdelivr: no private URLs, no Vercel project or team IDs (`prj_`, `team_`) |
| Names | README.md:133-135,182-184 and `proofs/` mention Pedro, Leo, Vhendala by name and role only. No partner, port, airport or chamber name |
| `.gitignore` | has `.env`, `.env.*`, `.stellar/`, `*.pem`, `*.key`, `/work/`, `node_modules/`, `target/` |

Things that are not hits but matter on Sunday night:
- **The remote branch `origin/three-machine` goes public with the repo.** It is merged, so nothing extra, but it is a second ref. Delete it after the scrub (Pedro's session, a push-side action).
- **c3086e1 is local only.** `git log origin/main..main` shows it. Leo's clone at 2c043a9 does not have those 3 AI_USAGE rows. If Leo edits AI_USAGE.md (task 3) before Pedro pushes c3086e1, there will be a rebase conflict on the same table.
- README line 129 and `proofs/three-machine.json` contain public keys of Leo and Vhendala (G...). Fine, they are testnet and already disclosed.

## A) LEO-TASKS.md

### A1. Task 2 contradicts the repo (blocking for the agent)
Text: "No content from the private Radox backend (`radox-internal`, internal file names, private URLs)" under "Must be empty" style rules. A literal grep for `radox-internal` hits README.md:145, which is the required prior-work disclosure. The agent will either report a false leak or delete the sentence.

Replace the "Names" bullet with:
```
- Names: no partner or client names (no ZIS, no Paulo, no chamber, port or airport by name); team names (Pedro, Leo, Vhendala) only as name and role, as in README "Team". No content from the private Radox backend: the only allowed mention of `radox-internal` is README.md line 145 ("closed and not published"); any other `radox-internal` hit, internal file name or private URL is a leak.
```

### A2. Task 2 gives patterns, not commands (a grep with `C:\` breaks in `grep -E`)
Add this block (WSL, bash) after the bullets:
```
Run from the clone root, after `git fetch --all`. Write output to a file first:
  git log -p --all > /tmp/hist.txt 2>&1
  grep -nE 'S[A-Z2-7]{55}' /tmp/hist.txt
  grep -nE -- '-----BEGIN' /tmp/hist.txt
  grep -nF -e '/Users/' -e '/home/' -e 'C:\' -e 'hackaton-meridian' /tmp/hist.txt
  grep -nwE 'ZIS|Paulo' /tmp/hist.txt
  grep -nF 'radox-internal' /tmp/hist.txt          # expected: only README.md line 145 (and its history)
  git log --all --format='%an <%ae>%n%cn <%ce>' | sort -u   # expected: only the two github noreply addresses
  git log --all --name-only --format= | sort -u            # expected: only paths in `git ls-files`, nothing like work/, .stellar, .env, request-*.json, response-*.json
  git ls-files -z | xargs -0 grep -nE 'S[A-Z2-7]{55}'      # tree
```
(Do not grep `ZIS` without `-w`: it matches "registry", "authorisation" and similar words.)

### A3. Task 2 does not name two classes this repo can leak
Add one bullet: "Refs: `git branch -a`; tell the card every ref you scanned (main, origin/three-machine). Metadata: author and committer e-mails must be GitHub noreply only. Files: `git log --all --name-only --format= | sort -u` must show no `work/`, `.stellar`, `.env`, request or response JSON from the three-machine run (those live in the private workspace, not in this repo)." I checked these three classes myself and they are clean today; the bullet makes the pass repeatable on the final commit.

### A4. Task 1 steps that are missing
- "Open `https://horizon-testnet.stellar.org/transactions/<hash>` ... and check the contract it calls": the transaction page does not show the contract. Add: "contract and function: open `.../transactions/<hash>/operations` and read `function` and `parameters[0]` (the contract), or open the `stellar.expert` link in the README."
- The command list says "both `verify-head` lines" and "`handover-signers`". Name them: README.md lines 37-39 (`npm ci`, `--selftest`, `verify-head.mjs 31b4cff7...5e37`), line 60 (`node scripts/handover-signers.mjs`, exit 0), line 77 (`cargo test`), line 138 (`PROOF_FILE=proofs/three-machine.json node scripts/verify-head.mjs 8f32b176...3aae`). Then Leo's agent cannot miss one.
- "from a clean clone ... `main` 2c043a9 or later": fine, but say `git rev-parse HEAD` goes in the card line (the template does not ask for it).
- The README has 8 transactions in the first table (7 lifecycle + attest) plus 4 in the second table: the card template "N hashes ok" should say 12, otherwise the agent invents its own N. Add "(expect 12: 8 + 4)".

### A5. Task 3 claims, checked against the script and AI_USAGE row 20
| Claim in LEO-TASKS | Check | Result |
|---|---|---|
| "`remote-auth.mjs` (prepare / sign / submit, refuses wrong address, contract, function or sub-calls)" | remote-auth.mjs:149 registry, :160 address, :163 sub-calls, :167 contract, header lists prepare/sign/submit | True (function: refused via the `handover`/`deliver` shape match at :170; not read to the end) |
| "Your `remote-sign.mjs` does the same job" | remote-sign.mjs:73-91 | **Overstated.** Same shape (prepare/sign/submit) but a generic tool for any contract call. Its `sign` only checks that the entry's root call is the request's contract and function (:83-85); it does not refuse sub-invocations (`authorizeEntry` signs the whole tree), has no `--registry` or `--known` check, prints `req.args` from the request file rather than decoding the signed entry. Not "the same job" for a judge reading a safety claim |
| "its testnet check ran on a throwaway registry (CB2JIOYL...FIAW3), not on a shipment the README shows" | AI_USAGE.md row 20 and Leo's own 14:46 card line | True |
| "delete the file and its row 20 in AI_USAGE.md" | row 20 is file line 20 today and stays line 20 after c3086e1 | True but fragile; name the row by its text |
| Nothing else references the script | `grep remote-sign` in README, page, proofs: 0 hits; only AI_USAGE.md:20 and ae25dac in history | True: deleting is safe |

Replace the first two sentences of task 3 with:
```
The three-machine shipment ran with `scripts/remote-auth.mjs`, which refuses sub-calls, wrong registry and unknown addresses and prints what it signs in words. Your `scripts/remote-sign.mjs` (ae25dac) is a generic prepare / sign / submit for any contract call without those refusals; its testnet check ran on a throwaway registry (CB2JIOYL...FIAW3), not on a shipment the README shows. Two tools for one job confuse a judge, and the weaker one must not look like the audited one.
```
and the first option with:
```
- remove it (commit on `main`: `git rm scripts/remote-sign.mjs` and delete the AI_USAGE.md line that starts with `| \`scripts/remote-sign.mjs\``; run `git ls-files` and check every remaining file still has a row), or
```
Recommendation for Pedro's session if Leo asks: remove. Keeping it needs a README sentence and a sub-call refusal it does not have.

### A6. Deadlines against the card
Sun 21:00 UTC (README read, remote-sign decision) and Sun 23:00 UTC (scrub) match `board/Leo contract and testnet proofs.md` "## Tasks". Consistent. Two things on the card are stale and will confuse the agent: the 14:41 line "finish by 23:30 UTC" (three-machine, done at 16:10) and the 14:45-era line about THREE-MACHINES.md. Not blocking. One real gap: the scrub (23:00) must be run on the final commit; if Pedro's session pushes c3086e1 or any README edit after Leo's pass, the pass is void. Add to task 2: "State the commit you scanned; Pedro's session re-runs the 5 greps on the final commit after any later push."

### A7. Other
- Header says "main 2c043a9", but the local main is c3086e1. Say "2c043a9 or later (c3086e1 adds 3 AI_USAGE rows and is pushed after the scrub)", or push before Leo starts (that is a push, Pedro's call).
- "Do not edit README.md" and "Do not rewrite history": fine and clear.
- The file says "Never message Pedro": consistent with the project CLAUDE.md.

## B) AI_USAGE.md, c3086e1

| Row | "Human review" cell | Verdict |
|---|---|---|
| `remote-auth.mjs`, `handover-signers.mjs` | "Not reviewed line by line by a human. Checked by the same agent: refuses a wrong address, contract, function, unknown counterparty, sub-invocations and mainnet; each signed response re-checked by a separate script (invocation bytes, nonce, ed25519 signature); handover-signers output matches the auth entries on Horizon" | True for address, contract, sub-calls, unknown counterparty (code lines above); the card 16:10 line records the separate re-check. "mainnet" I did not find in remote-auth.mjs (grep `mainnet` 0 hits; `NET` is fixed to testnet in lib/stellar.mjs:10, so it cannot reach mainnet, but it does not "refuse" it). Replace "and mainnet" with "; the network is fixed to testnet". "Tested by the same agent" is not "checked on testnet by a reviewer": fine as written |
| `proofs/three-machine.json` | "4 hashes checked successful on Horizon and verify-head MATCH by an AI agent and an independent reviewer agent" | True (REVIEW-THREE-MACHINE.md, 16:14: four hashes successful, verify-head MATCH on 8f32b176). Not inflated. The reviewer also said "key never left that computer" needs rewording; the cell here does not claim it |
| `README.md` | "each hash, ID and command checked by an independent reviewer agent" | **Slightly inflated.** REVIEW-README.md checked an earlier commit (c014c85, not in the current history); six README commits followed (three-machine section 4f90bb1, 64e980b, cbe26a4, mentor sentence edits). REVIEW-THREE-MACHINE.md (16:14) covers the three-machine section only. Replace with: "each hash, ID and command checked by independent reviewer agents (the main text at an earlier commit, the three-machine section on 2026-10-25 16:14); later wording edits not re-checked" |

### The `proofs/` row is now inconsistent
Row 21: "generated by `scripts/lifecycle.mjs` on testnet | 7 lifecycle hashes checked ...". But `proofs/` also holds `three-machine.json` and 4 extra `tx/*.json` (861544e4..., 9214980e..., 850da342..., 849c268d..., plus 34860ed8... open) that `remote-auth.mjs` produced; `three-machine.json` has its own row. Replace the row with:
```
| `proofs/lifecycle.json`, `proofs/tx/` (the 8 files of the first shipment) | generated by `scripts/lifecycle.mjs` on testnet; each `tx/` file is a copy of the Horizon record | 7 lifecycle hashes checked successful on Horizon by an AI agent (`check.py`, independent verify run); anyone can repeat it with the hashes |
```
and change the `proofs/three-machine.json` row's path cell to `proofs/three-machine.json`, `proofs/tx/` (the 5 files of the second shipment). I counted 13 files in `proofs/tx/` (8 + 5); the exact split should be re-checked by whoever edits it with `grep -l` on the hashes.

### Coverage of `git ls-files`
Every one of the 65 tracked files is covered by a path or folder row: Cargo.*, contracts/, snapshots, .gitignore, NOTICE, AI_USAGE.md, LICENSE, DEPLOYMENTS.md, package*.json, scripts/*.mjs (lib/stellar.mjs, lifecycle, verify-head, remote-sign, remote-auth, handover-signers, page-snapshot), proofs/, page/ (stellar-sdk.min.js, robots.txt, sitemap.xml, llms.txt are under the `page/` row), README.md. Gaps in wording only:
- `page/stellar-sdk.min.js` is a vendored third-party bundle (NOTICE names it) but the `page/` row says "AI coding agent". Add "except `page/stellar-sdk.min.js`, vendored js-stellar-sdk 17.3.0, unmodified (see NOTICE)".
- `scripts/page-snapshot.mjs` is listed in the `page/` row only, fine.

## What I did not check
- Whether Leo, in his WSL clone, has `jq`, `gh` and the same Node version; task 1 assumes Node, npm and cargo are there (README lists them).
- remote-auth.mjs lines 175-281 (submit) and the "mainnet" claim beyond a grep.
- Horizon status of the 12 hashes (the 16:14 reviewer did the three-machine four; I did not repeat any).
- Binary and minified blobs for secrets beyond the regexes above (`page/stellar-sdk.min.js` matched nothing).
- Remote GitHub state (no network calls): whether origin/main really is 2c043a9, and whether the repo is still private.
