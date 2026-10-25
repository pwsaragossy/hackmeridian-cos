# Review-2 — independent review of stage 2 (Scope and build)

Date: 2026-10-25, 12:53–13:00 UTC.
Reviewer: independent reviewer subagent (role card reviewer), briefed by session-hackmeridian-rail; specialists whose work is reviewed: engineer (licences, secrets, VERIFY-LEO), designer (LOOK), product (SCOPE).
Code reviewed: fresh clone of github.com/pwsaragossy/rio-miami-rail at HEAD 262ab1727abbd99f3e96aa321c95f06d42d33a17 (16 commits, cloned 12:53:49 UTC). Live page: https://rio-miami-rail.vercel.app.

Question: is the stage 2 gate true ("scope is frozen, the thinnest end-to-end path runs, and nothing in the build breaks the rules"), and does each item's evidence prove its own wording?
Conclusion: the path runs on live testnet and the scope holds. The licences evidence is stale against HEAD. No stage 2 file checked prior-work disclosure. The page's offline fallback depends on a CDN.

**Verdict: approve with changes.** There are no critical findings. Fix M1 before `licences` counts as closed. Fix M2 before the repo goes public. Fix M3 before `demo-offline` (stage 3).

## What I re-ran (evidence)

- `python3 check.py` at 12:56 UTC: 7 SUCCESS, exit 0.
- `node scripts/verify-head.mjs 31b4cff7…5e37` on the clone at 12:55 UTC: recomputed = on-chain = `2d74fec0…95414`, MATCH, exit 0.
- `get(key)` by simulation (read only, no transaction sent) on CCBJVXMJ…H4LII: status `Delivered`, seq 4, route of 5, holder GBPFJMZ7…, custodian GAG5WGRM… (Recipient).
- Live page, logged out (curl): index.html, app.js, snapshot.json, llms.txt, robots.txt and sitemap.xml all return 200 and are byte-identical to HEAD `page/`. `/.env` and `/proofs/lifecycle.json` return 404.
- Live page in a browser: "LIVE FROM STELLAR TESTNET". The text matches SKELETON.md. "Verify head" shows "MATCH recomputed 2d74fe…195414 from 7 transactions; on-chain head 2d74fe…195414". Inter loaded, background rgb(14,15,17).
- `page/snapshot.json`.proof is byte-equal to `proofs/lifecycle.json`.
- LOOK contrast ratios recomputed: 15.64, 8.02, 14.8, 8.87, 17.73, 6.98, 5.31, 6.94, 1.28. All match LOOK.md and the library note. The page `:root` colours equal the LOOK.md table exactly. The name "Radox Custody Rail" is the `<title>`, the page eyebrow and the llms.txt heading.

## Findings, by severity

### M1 (major): LICENCES.md does not cover HEAD, and it omits the page's third-party assets
- Evidence: LICENCES.md was made at 179bb9c and says "npm: none in the repo … no package.json or package-lock.json". But `package.json` and `package-lock.json` arrived in 3ba0d68 (11:57 UTC) and are in HEAD. The lock holds 41 packages: MIT 38, Apache-2.0 2 (`@stellar/stellar-sdk` 17.3.0, `@stellar/js-xdr`), BSD-3-Clause 1 (`smol-toml`). The page also loads two runtime assets that are not listed: the `@stellar/stellar-sdk@17.3.0` browser bundle from cdn.jsdelivr.net (index.html, SRI-pinned) and the Inter font from fonts.googleapis.com. The item's wording names "dependencies, datasets and third-party assets".
- Facts only, no analysis (owner rule): neither the Cargo list nor the npm list contains a GPL, LGPL, AGPL, MPL, EPL or other copyleft string. The repo ships lockfiles and no third-party source.
- Fix: re-run the listing on the current HEAD and stamp it. Add the npm table and the two CDN assets with the licence string their publisher states. Then keep `licences` closed with that file.

### M2 (major): nothing a judge can open today discloses prior work, and the 7th target transaction runs prior work
- Evidence: the repo has no README (`git ls-files`). The public page says "Redeemed: token burned". llms.txt says "Final delivery burns the token … Built at HackMeridian 2026". The redeem transaction 864fd1… calls CAYD3EFT…SJWH, an instance of the pre-event Radox `transfer_agent` wasm `3870748b…`, whose source is closed (VERIFY-LEO b; `scripts/lifecycle.mjs:23`). The only disclosure in the build is the code comment `// prior work, deployed as-is` (lifecycle.mjs:23). The rule (PORTAL-PASTE.md line 47, RULES.md) says "Undisclosed prior work is a disqualification". No stage 2 evidence file checks the gate's "nothing in the build breaks the rules" for disclosure.
- Not a finding: I compared every `.rs` line over 40 characters in the public pwsaragossy/radox repo with `custody_registry/src`. Only 6 lines are shared, all SDK boilerplate (`env.mock_auths(...)`, `#[derive(...)]`, storage set lines). All 16 commits are dated 2026-10-25 09:00:17Z to 12:41:03Z, after the 09:00 start. Commit dates are author-set, so they are consistent with the rule, not proof.
- Fix: add one line now to the page and llms.txt: the burn runs through Radox's pre-event `transfer_agent`, deployed from its existing wasm; the new work is `custody_registry`, the harness, verify-head and this page. Write the README "Prior work" section before the repo goes public (KICKOFF Sun 20:30). The pitch's "seven signed transactions" must say that 6 hit the new registry and 1 hits prior work.

### M3 (major, stage 3 risk): the snapshot fallback cannot render without jsDelivr
- Evidence (from the code, not run): `page/app.js:9` binds `const S = window.StellarSdk`. `history()` calls `S.xdr.ScVal.fromXDR` (app.js:94) even when it reads from the snapshot. If the CDN script fails to load, `load()` throws and `app.js:210` shows only "Could not load the shipment … Reload the page in a minute." The card line "Snapshot fallback … tested with RPC and Horizon blocked" is true only while the CDN is reachable. Stage 3 `demo-offline` requires "without internet or live third-party services".
- Fix: serve the SRI-pinned bundle from `page/` (it is Apache-2.0; add it to M1's list). Inter already falls back to `system-ui`. Then re-test with the network fully off.

### m1 (minor): SKELETON.md does not say which page data is live
- Evidence: these are live: the state rows and the head (`get` by simulation) and each history row's parameters (Horizon). But the list of transactions to fetch comes from `snapshot.json` (app.js:87): the page cannot find a handover outside that list, although "Verify head" would then show MISMATCH. The actor role names and the container label also come from the snapshot. The "Redeemed: token burned" row is not read from chain at all (app.js:136-143 renders only a link). In snapshot mode, "Verify head" compares saved data with a saved head, so its MATCH is circular. It is labelled "saved head".
- Fix: add one sentence to SKELETON.md. Read the holder's token balance live (VERIFY-LEO c did it by simulation), or label the redeem row "from the proof".

### m2 (minor): the scope text promises "assurance" per handover, and the page does not show it
- Evidence: IDEA.md scope item 3 says "each handover with both signers, assurance, tx links". The page uses `a[4]` (assurance) only inside `recompute` and shows no assurance value. "Both signed" is supported by the contract: `from.require_auth()` and `to.require_auth()` (lib.rs:303-304), and `final_custodian` plus `holder` for deliver (lib.rs:370-371).
- Fix: show "assurance N" in each handover row, or drop the word from the scope text.

### m3 (minor): the secrets evidence scans only for Stellar S-keys; I closed the gap
- Evidence: SECRETS-SCAN.md and VERIFY-LEO g grep only `S[A-Z2-7]{55}`. VERIFY-LEO admits this. I added a further check. I took every 64-hex string in the tree (268) and in the history (269) and treated each as an ed25519 seed. None gives a project account (the 11 actors; admin and operator are among them): 0 hits. Other results: no `/Users/`, brain or private path; the commit e-mails are GitHub noreply; the partner-name scan (plus G20 and Guava) is 0 on HEAD and in history; `.env`, `.stellar/`, `*.key` and `*.pem` are git-ignored; keys come from env (`EXPORTER_SECRET`, `OPERATOR_SECRET`) or are generated per run. The "demo" half of the item (video, deck) does not exist yet.
- Fix: add this check to SECRETS-SCAN.md. Re-run the scan on the video and the deck at stage 3/4 (already planned for Sun 22:00).

### m4 (minor): AI attribution files contradict each other
- Evidence: the card line of 11:25 UTC says "AI_USAGE.md in the repo keeps the generic wording: the exception is for the form field only". The repo's AI_USAGE.md names "Claude Opus 5.5 (`claude-opus-5-5`)" and `claude-sonnet-5-5`, and STATE §5.4 expects the model names there. Inside AI_USAGE.md, the header says Opus 5.5 was used "including its review subagents", but the page row says those subagents ran Sonnet. That one is already on Leo's card. The "Human review: Leo" cells are unconfirmed (tracked on the card). Every path in `git ls-files` is covered.
- Fix: correct the stale 11:25 card line to match what the repo does now. If the generic-wording rule was still meant for the repo, that is a `waiting-owner` line for central, not an edit.

### m5 (minor): llms.txt has text that turns false
- Evidence: llms.txt:19 says "Code repository … (private until submission)". It is judge-facing and becomes false when the repo goes public.
- Fix: edit it in the same push that makes the repo public.

### m6 (minor): LOOK is a deck spec, not yet a consistent style
- Evidence: the deck does not exist yet. The page uses Inter. The deck keeps Inter Tight, Instrument Sans and JetBrains Mono (LOOK.md). The page's eyebrow, source label and transaction meta are 14–15 px, which is small on a projector. The `button:focus-visible` ring is the text colour, not lime (LOOK says lime; on a lime button, the text colour is the right choice).
- Fix: review-3 renders the page and the deck side by side at 1280×720 and decides the fonts.

### m7 (minor): the live page takes seconds to fill
- Evidence: in one browser load, the page still showed "Loading…" after about 2 s and was complete before 10 s. app.js fetches 8 transactions × 2 Horizon calls one after another (app.js:56-61, 87-90). "Verify head" stays disabled until then.
- Fix: run the fetches in parallel (`Promise.all`), or start the demo recording after the load ends.

## Premises tested
- Scope holds: the repo contains only must-haves 1–3. Pause, freeze and sources sit inside must-have 1 (the contract). The conditional API connection is not in this repo. It has a time box ("Sun 20:30–21:00 hard stop", board `Sessions build and submission.md`). The handover ran before the 18:00 line, so the 4th stays conditional, not cut.
- The target is still met on live testnet (check.py above). check.py still does not prove that each transaction calls our registry. VERIFY-LEO b proved it by hand. The proposed check is already in STATE §5.5.
- The library notes say what LOOK and the licence work claim. In [[apache-2-0-for-rio-miami-9905]], "transitive … not checked" is now answered for Cargo only, not npm (M1).

## Pre-mortem
Mon 13:30. A Stellar engineer on the panel opens the redeem link, sees a contract with no source, and finds no "Prior work" section in the README. Or the offline demo shows only "Could not load the shipment". M2 and M3 close both cases.

## Not checked
- The page with RPC and Horizon blocked, and with the CDN blocked: not run. M3 comes from the code.
- The 9 failure branches, one by one (VERIFY-LEO d also did not re-run them).
- Whether the review subagents for the page ran `claude-sonnet-5-5` (an AI_USAGE.md claim).
- Vercel project settings and env vars. Only the 6 served files and two 404 paths were checked.
- The deck, the video and the README: none exist yet.
- The portal rules page (login). Prior-work wording is judged against PORTAL-PASTE.md only.

## Sources
[[radox-custody-rail-look-signal-adapted-d030]] [[apache-2-0-for-rio-miami-9905]] [[transfer-agent-testnet-interface-2026-10-3378]]
