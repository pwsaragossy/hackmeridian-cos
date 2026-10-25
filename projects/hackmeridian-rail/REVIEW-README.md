Reviewer: independent reviewer subagent (role card reviewer), briefed by session-hackmeridian-rail; work reviewed: engineer (README)

Date: Sun Oct 25 14:33:33 UTC 2026 (start of review; checks ran 14:33-14:50 UTC)
Target: ~/code/rio-miami-rail/README.md at local commit c014c85 (not pushed). Checked in a fresh clone at c014c85.

## Verdict: APPROVE WITH CHANGES

Count: 2 critical, 3 major, 6 minor. No false number, hash or capability claim found. The two criticals are gates (unfinished placeholders, repo still private), not wrong facts.

## What I verified myself (all matched the README)

- All 8 tx hashes (Horizon testnet): successful true, ledgers 5381140, 42, 43, 44, 45, 46, 47, 48 exactly as in the table. First tx created_at 2026-10-25T11:54:47Z.
- Redeem tx 864fd164... invokes CAYD3EFT...XSJWH (decoded the contract address from the operation); holder balance after redeem in proofs is "0".
- Three contract IDs exist on testnet (`stellar contract info interface` returns a spec for each). The wasm fetched from CCBJVXMJ...H4LII hashes to 8230ed93...1342, equal to README and DEPLOYMENTS.md. Transfer agent wasm 3870748b...fc6bff1 is the constant in scripts/lifecycle.mjs line 23.
- Quick verify in a fresh clone (Node 26.12.0, `npm ci` exit 0, 0 vulnerabilities): `--selftest` prints 3 ok lines; `verify-head.mjs <key>` prints exactly the 6 lines pasted in the README, recomputed = on-chain = 2d74fec0...5414, MATCH. `--offline` works (MATCH). `handover-signers.mjs` exit 0, "both signed" on 4 handovers and the delivery. `jq` lifecycle listing gives 7 hashes equal to the table.
- `cargo test`: 24 passed (rustc 1.97.1, stellar CLI 28.1.0, as in the table).
- Contract source: `handover` calls `from.require_auth()` and `to.require_auth()` (lib.rs 303-304); `deliver` requires final custodian and holder (370-371); `open` requires the operator (251); `attest` requires an allow-listed source (UnknownSource); `deliver` refuses until seq equals the last route index (NotFinal); assurance 1..3 (BadAssurance). Key is sha256(container|origin) (lifecycle.mjs line 51; TEST4627832|BRRIO gives 31b4cff7...5e37 in proofs). The harness reads the registry status before `redeem` (lifecycle.mjs 176-178).
- Nine refused cases are in proofs/lifecycle.json, as stated.
- Prior work: `gh api repos/pwsaragossy/radox`: created and pushed 2026-08-19, visibility public, no licence file (README says "All rights reserved"); tree has contracts token_sale, yield_distributor, maturity_settlement; README of that repo marks all three mainnet. This repo's README says "different licence": true (Apache-2.0 vs all rights reserved).
- Built at HackMeridian: first commit d10cb84 is 2026-10-25T09:00:17Z; last commit before the README is 54dc401 13:42:36Z; no commit before 09:00 UTC. The GitHub repo was created empty on 2026-10-24T22:49:19Z (matches SUBMISSION.md); `rio-miami-rail` is currently private.
- Radox API claim (line 108): API-PROOF.md has a "Full backend boot" section (throwaway Postgres and Redis), card line 13:23 UTC; head 2d74fec0...5414 equals verify-head. The README states honestly that judges cannot reproduce it.
- Licence counts: 215 crates in Cargo.lock, 41 npm packages (38 MIT, 2 Apache-2.0, 1 BSD-3-Clause): match.
- Scrub over the tree (git grep, README, DEPLOYMENTS, NOTICE, page, scripts, proofs): no "Claude", "Anthropic", "ZIS", e-mail, /Users path, secret seed (S...56) or private key block outside AI_USAGE.md. README names no partner, client, chamber, port or airport (only the generic words in the Future sentence). Future section is future tense, intent only, and ends "No such standard, adoption or partnership exists today", equal to the approved text. No claim of real custodians (line 29 says test accounts), mainnet (line 153 says none), audit, SCF eligibility, partnership.

## Findings

### Critical

C1. Unfilled placeholders, README lines 7 and 27: `Video: {{fill: video URL}}` and `Video walkthrough: {{fill: video URL}}.` A judge sees template text; the portal also needs the video.
Evidence: grep shows 2 occurrences. SUBMISSION.md says the video is a required submission item.
Replacement: put the YouTube/Vimeo URL in both places once the upload exists. If the README must go public first, replace both with `Video: link in the submission form.` and `Video walkthrough: see the submission form.`, and fix before 08:00 Mon. Never push the repo public with `{{fill` in it (add `grep -n '{{' README.md` to the pre-push scrub).

C2. Quick verify cannot run for a stranger today, line 36: `git clone https://github.com/pwsaragossy/rio-miami-rail` returns not found because the repo is private (`gh api` private: true). Judges need it public (SUBMISSION.md safe rule: public before 10:00 Mon 26 Oct; the rules require it).
Evidence: `gh api repos/pwsaragossy/rio-miami-rail --jq .private` gives true.
Replacement: no text change; gate for the owner: make the repo public after the scrub, then run the clone line logged out (`git clone` without credentials) and re-run the five Quick verify commands from that clone. The README also says in line 29 and 143 things about files that only exist after push; re-check after.

### Major

M1. Prior work omits the pre-event design and planning, lines 129-134. The claims guard ([[wording-the-rio-miami-deck-readme-ef38]] item 9) says to list the 2026-10-20 architecture panel and the planning files dated 24-25 Oct, and to state that no contract code was written before Sun 09:00. The portal rule says undisclosed prior work is a disqualification; SUBMISSION.md plans the same. The "Built at HackMeridian" section says "from d10cb84" but not that the repo was created empty on 2026-10-24 22:49 UTC.
Replacement (add as a fifth bullet under Prior work): `- Design and planning before the event: an architecture review of the custody idea on 2026-10-20 (design notes only, no code) and planning documents dated 2026-10-24 and 2026-10-25 (kick-off, task brief, pitch outline). The GitHub repository was created empty on 2026-10-24 22:49 UTC so the team could be invited. No contract code was written before 2026-10-25 09:00 UTC; the first commit is at 09:00:17.`

M2. Line 149 says AI_USAGE.md "lists every path". It does not: `README.md` and `scripts/handover-signers.mjs` (both in `git ls-files`) have no row (`grep -c README AI_USAGE.md` is 0). A judge comparing the two files finds a gap in the attribution that the rules require.
Replacement: add two rows to AI_USAGE.md: `| README.md | AI coding agent | Leo / Pedro: <who actually read it> |` and `| scripts/handover-signers.mjs | AI coding agent | <who read it, or "Not reviewed line by line by a human"> |` (do not write a reviewer name that did not read it). Then line 149 stays true.

M3. README and AI_USAGE.md versus the owner's rule "no Claude or Anthropic name". README is clean. AI_USAGE.md (public in the repo) names "Claude Opus 5.5 (`claude-opus-5-5`) in Claude Code", "`claude-sonnet-5-5`" (header and last row). That is not a contradiction between the two files (README names no model; both say AI coding agents wrote it, same reviewers), but it conflicts with the global rule and with the hackathon text ("note where AI meaningfully generated code"; the claims guard item 8 says "name which tool and model"). One of the two rules must give.
Replacement: owner decision, put on the card. If model names stay (attribution), no change. If the rule wins, in AI_USAGE.md replace the header line with: `AI coding agents, with their review subagents, wrote the files marked "AI coding agent".` and replace the two `claude-...` mentions in the page row with `an AI model`. I recommend asking Pedro once; either way keep README and AI_USAGE.md consistent.

### Minor

m1. Line 138: `The repo has 21 commits ... to 54dc401 (13:42:36)`. At c014c85 the repo has 23 commits and the README commits are at 14:32-14:33. The sentence is true of the range it names but a judge counting finds 23.
Replacement: `The repo has 23 commits, all dated 2026-10-25 UTC, from `d10cb84` (09:00:17) to this README (14:33); 21 of them are the code, page and proofs below.` (recount just before push: `git rev-list --count HEAD`).

m2. Line 134 and 131: token_sale on mainnet. The public radox README says the deployed `token_sale` is v7 and the published source is v8 ("The other two match what is deployed"). README line 131 says "Their source is public" without that difference.
Replacement for line 131: `- Three Soroban contracts (`token_sale`, `yield_distributor`, `maturity_settlement`) run on Stellar mainnet (June-July 2026). Their source is public, contracts only, at <https://github.com/pwsaragossy/radox> since 2026-08-19; the published `token_sale` is a newer version (v8) than the one deployed (v7), the other two match.`

m3. Demo honesty, line 29. The claims guard item 13 asks to say the six actors are test keys held by one harness, so the run proves the mechanism, not independent custodians. Line 29 says test accounts, not real companies, but not that one script holds all keys.
Replacement: `Everything on testnet runs with generated test keys held by one harness script. The custodians are test accounts, not real companies, and the cargo ID `TEST4627832` is invented. The run proves the mechanism (each handover needs both signatures), not independent custodians.`

m4. Team, line 170: `Vhendala, supervision and product review` matches PITCH-FINAL.md but the claims note says "QA and review", and the guard says to state that Leo and Vhendala joined for the hackathon. Not wrong, but nobody should read "supervision" as an employer role.
Replacement: `- Vhendala, product review (joined for the hackathon)` and `- Leo Schlanger, developer (joined for the hackathon)`. Confirm with Pedro (title wording is the owner's).

m5. Problem, line 11: "Each party keeps its own record" and "changes hands many times" are unsourced assertions; the claims guard calls the problem a hypothesis (item 10: "mostly paper or inside one carrier's own system", source needed).
Replacement: `In our working assumption, a container that crosses a border changes hands many times ... and each party keeps its own record.` (keep "assumption"; do not add numbers without a source).

m6. Line 23: "Admin controls (freeze, pause, source list) exist for lost or seized cargo." True for freeze (source comment: lost or seized cargo, court order, sanction); pause and source list are not for that. Replacement: `Admin controls exist: freeze (for lost or seized cargo), pause, and an allow-list of data sources.`

## Rule and requirement checks

- HackMeridian README requirements (SUBMISSION.md lines 10-13, 27-28): summary yes (line 3), problem yes, setup and environment yes, installation yes (npm ci), env vars yes, demo instructions yes (Live demo and Quick verify), architecture with contract IDs, assets, APIs yes, tx hashes yes, prior work yes (see M1), AI attribution yes (see M2, M3), built-at-event yes. Missing: working video URL (C1), public repo (C2). Not stated: when the live page was last confirmed (https://rio-miami-rail.vercel.app returned HTTP 200 at review time; its HTML title is "Radox Custody Rail", not "Rio-Miami Rail"; if intended as Radox-branded, one line of explanation avoids a judge asking whether the page is prior Radox work).
- Burn wording: README line 21 says the contract does not enforce the burn and the harness checks first; this matches the claims guard (not "the contract burns").
- Not copied: I did not diff this repo against the public radox contracts byte by byte; the licence difference, commit times and file list give no sign of copying.

## Not checked

- Mainnet instance IDs of the three Radox contracts on chain (the README gives none; the claims note says only yield_distributor was matched earlier).
- Radox gating claim (line 155, "physical-asset offers stay blocked outside testnet") against radox-internal origin/main: my grep found no flag and I did not read the code path; SUBMISSION.md says to re-check before publishing.
- Line 159 testnet reset date 2026-12-16: taken from the library note (read from the Stellar networks page on 2026-10-25), not re-opened.
- The video, the deck and the form answers; the live page behaviour in a browser (Verify head, Snapshot label); the seven handover signatures against the explorer; the "nine refused calls" were not re-run (they need testnet transactions/simulations; I sent no transaction).
