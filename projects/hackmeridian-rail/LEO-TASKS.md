# For Leo's agent — everything still open for Leo (Sun 25 Oct, evening)

Internal: never copy into rio-miami-rail. Written by session-hackmeridian-rail on 2026-10-25 ~16:55 UTC.
This file replaces the "## Tasks" list on `board/Leo contract and testnet proofs.md`. Answer there, one dated
line per task (`- HH:MM UTC (leo-agent): …`, stamp from `date -u +%H:%M`), with the evidence. Never message
Pedro; a question goes on the card with `status: waiting-owner`. A line without evidence counts as not done.

What changed since your last line: branch `three-machine` is merged into `main` and pushed (origin/main
2c043a9, repo still **private**). Start with `git -C <your clone> fetch && git checkout main && git pull`.
The branch `three-machine` is no longer needed; review `main` only.

## 1. Read the README as an SDF judge — by Sun 21:00 UTC

On `main` 2c043a9 or later, from a clean clone:
- Every contract ID and tx hash in README.md: open `https://horizon-testnet.stellar.org/transactions/<hash>`
  (must be `successful: true`) and check the contract it calls is the one the README says.
- Every command in README.md: run it as written (build, `cargo test`, `npm ci`, both `verify-head` lines,
  `handover-signers`). Expected: tests 24/24, verify-head `MATCH` for 31b4cff7… and, with
  `PROOF_FILE=proofs/three-machine.json`, for 8f32b176….
- Every relative link in README.md resolves to a file in the repo.
- Read it once as a judge: what is unclear, what is claimed without proof.
Card line: "README read: N hashes ok, N commands ok, links ok; notes: …" (or the exact failure).
Do not edit README.md; Pedro's session owns it and applies your notes.

## 2. Pre-public scrub of rio-miami-rail — by Sun 23:00 UTC

The repo goes public only after this passes and Pedro gives a separate OK. On `main`, tree **and** history
(`git log -p --all`):
- Secrets: `grep -rnE "S[A-Z2-7]{55}"`, `.env`, private keys, tokens. Must be empty.
- Personal paths: `/Users/`, `/home/`, `C:\`, `Desktop/hackaton-meridian`. Must be empty.
- Names: no partner or client names (no ZIS, no Paulo, no chamber, port or airport by name); team names only
  as name and role. No content from the private Radox backend (`radox-internal`, internal file names, private URLs).
- Note any hit with file, line and commit. Do not rewrite history yourself: put it on the card, Pedro's
  session decides the fix.
Card line: "scrub main <hash>: empty = pass" or the list of hits.

## 3. Your `scripts/remote-sign.mjs` — decide by Sun 21:00 UTC

The three-machine shipment ran with `scripts/remote-auth.mjs` (prepare / sign / submit, refuses wrong
address, contract, function or sub-calls). Your `remote-sign.mjs` does the same job and has no proof run.
Two tools for one job confuse a judge. Your call, as its author:
- remove it (commit on `main`: delete the file and its row 20 in AI_USAGE.md), or
- keep it and say on the card in one line why, so the README can mention it.
Card line: the decision and the commit hash.

## Not yours (so you do not duplicate it)

The README, FORM-ANSWERS, Challenges text (your 12:55 lines are already used), AI_USAGE rows for files
Pedro's sessions wrote, the page, the video, the deck and the submission.
