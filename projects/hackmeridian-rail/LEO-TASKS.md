# For Leo's agent — everything still open for Leo (Sun 25 Oct, evening)

Internal: never copy into rio-miami-rail. Written by session-hackmeridian-rail on 2026-10-25 ~16:55 UTC.
This file replaces the "## Tasks" list on `board/Leo contract and testnet proofs.md`. Answer there, one dated
line per task (`- HH:MM UTC (leo-agent): …`, stamp from `date -u +%H:%M`), with the evidence. Never message
Pedro; a question goes on the card with `status: waiting-owner`. A line without evidence counts as not done.

What changed since your last line: branch `three-machine` is merged into `main` and pushed (origin/main
2c043a9, repo still **private**; a later commit 6176910 or after adds AI_USAGE rows; pull before you edit AI_USAGE.md). Start with `git -C <your clone> fetch && git checkout main && git pull`.
The branch `three-machine` is no longer needed; review `main` only.

## 1. Read the README as an SDF judge — by Sun 21:00 UTC

On `main` 2c043a9 or later (pull first), from a clean clone:
- Every tx hash in README.md (expect 12: 8 in the first table, 4 in the second): open
  `https://horizon-testnet.stellar.org/transactions/<hash>` (must be `successful: true`), then
  `.../transactions/<hash>/operations` and read `function` and `parameters[0]` (the contract): it must be the
  contract the README says.
- Every command in README.md, run as written: `npm ci`, `node scripts/verify-head.mjs --selftest`,
  `node scripts/verify-head.mjs 31b4cff7…5e37` (MATCH), `node scripts/handover-signers.mjs` (exit 0),
  `cargo test` (24 passed), `PROOF_FILE=proofs/three-machine.json node scripts/verify-head.mjs 8f32b176…3aae` (MATCH).
- Every relative link in README.md resolves to a file in the repo.
- Read it once as a judge: what is unclear, what is claimed without proof.
Card line: "README read at <git rev-parse HEAD>: 12/12 hashes ok, 6/6 commands ok, links ok; notes: …" (or the exact failure).
Do not edit README.md; Pedro's session owns it and applies your notes.

## 2. Pre-public scrub of rio-miami-rail — by Sun 23:00 UTC

The repo goes public only after this passes and Pedro gives a separate OK. On `main`, tree **and** history
(`git log -p --all`):
- Secrets: `grep -rnE "S[A-Z2-7]{55}"`, `.env`, private keys, tokens. Must be empty.
- Personal paths: `/Users/`, `/home/`, `C:\`, `Desktop/hackaton-meridian`. Must be empty.
- Names: no partner or client names (no ZIS, no Paulo, no chamber, port or airport by name); team names (Pedro,
  Leo, Vhendala) only as name and role, as in README "Team". No content from the private Radox backend: the only
  allowed mention of `radox-internal` is the README prior-work line ("closed and not published"); any other
  `radox-internal` hit, internal file name or private URL is a leak.
- Refs: `git branch -a`; name every ref you scanned on the card. Commit e-mails: GitHub noreply only. Files ever
  committed: no `work/`, `.stellar`, `.env`, request or response JSON.

Run from the clone root after `git fetch --all` (output to a file first; grep ZIS only with `-w`):

    git log -p --all > /tmp/hist.txt 2>&1
    grep -nE 'S[A-Z2-7]{55}' /tmp/hist.txt
    grep -nE -- '-----BEGIN' /tmp/hist.txt
    grep -nF -e '/Users/' -e '/home/' -e 'C:\' -e 'hackaton-meridian' /tmp/hist.txt
    grep -nwE 'ZIS|Paulo' /tmp/hist.txt
    grep -nF 'radox-internal' /tmp/hist.txt     # expected: only the README prior-work line
    git log --all --format='%an <%ae>%n%cn <%ce>' | sort -u
    git log --all --name-only --format= | sort -u
    git ls-files -z | xargs -0 grep -nE 'S[A-Z2-7]{55}'
- Note any hit with file, line and commit. Do not rewrite history yourself: put it on the card, Pedro's
  session decides the fix.
Card line: "scrub <hash>, refs <list>: empty = pass" or the list of hits. Pedro's session re-runs the greps on the
final commit after any later push.

## 3. Your `scripts/remote-sign.mjs` — decide by Sun 21:00 UTC

The three-machine shipment ran with `scripts/remote-auth.mjs`, which refuses sub-calls, a wrong registry and
unknown addresses and prints what it signs in words. Your `scripts/remote-sign.mjs` (ae25dac) is a generic
prepare / sign / submit for any contract call without those refusals; its testnet check ran on a throwaway
registry (CB2JIOYL…FIAW3), not on a shipment the README shows. Two tools for one job confuse a judge, and the
weaker one must not look like the audited one. Nothing else references it, so removing it is safe; we recommend
removal. Your call, as its author:
- remove it (commit on `main`: `git rm scripts/remote-sign.mjs` and delete the AI_USAGE.md line that starts with
  `| \`scripts/remote-sign.mjs\``; then check every file in `git ls-files` still has a row), or
- keep it and say on the card in one line why, so the README can mention it.
Card line: the decision and the commit hash.

## Not yours (so you do not duplicate it)

The README, FORM-ANSWERS, Challenges text (your 12:55 lines are already used), AI_USAGE rows for files
Pedro's sessions wrote, the page, the video, the deck and the submission.
