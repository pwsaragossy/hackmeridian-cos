Reviewer: independent reviewer subagent (role card reviewer), briefed by session-hackmeridian-rail; work reviewed: FORM-ANSWERS new sections and README 55f43e2

Time: Sun 2026-10-25 17:19 UTC (`date -u`)

## Verdict: APPROVE WITH CHANGES (0 blockers; 3 majors; 4 minors). Nothing found that disqualifies, no inflated claim in the Description.

## Checked and true
- 7 hashes: all `successful: true` on horizon-testnet (ledgers 5381140, 142, 143, 145, 146, 147, 148). Each Description row matches the README table order (open, warehouse->port, port->carrier, carrier->customs, customs->recipient, deliver, redeem) and the full hash in each link matches the abbreviation. Registry `CCBJVXMJ...H4LII` matches README line 99 and DEPLOYMENTS.md. Links point to stellar.expert, not Horizon; the same hashes, fine.
- "Nine refusal branches": `proofs/lifecycle.json` `failures` has 9 entries. "24 unit tests": `cargo test` 24 passed, 0 failed (run 17:18 UTC).
- Character counts (python, section bodies): title 72, tagline 25, Description 3076, Challenges 1306, Tech stack 145 (12 items, counted), Prior work 1096, AI note 835, Problem 396, What's next 810. All match the table.
- Challenges 1-4 vs Leo's 12:55 text: same meaning. Only the parenthetical evidence was dropped: "(testnet tx c6d06f2f...)" in 1, "(9b66e00, 24/24)" in 3, and the note "proof is only in Leo's session log" in 4. No meaning change.
- Names: no mentor, ZIS, Paulo, chamber, port or airport by name (line 89 says "chambers of commerce, ports and airports" generically). radox-internal is not named in the form (README names it); acceptable, the form says "the closed backend".
- Tech stack items all used (Cargo.lock soroban-sdk 29.0.1, CLI 28.1.0, `rpc.Server` and Horizon in scripts/lib/stellar.mjs, @stellar/stellar-sdk 17.3.0, token is a SAC, page at rio-miami-rail.vercel.app returns 200). "Vercel" is fair as the page host.
- AI note: Opus 5.5 and "Sonnet 5.5 review subagents" are both stated in AI_USAGE.md (page row: `claude-sonnet-5-5`), and this review ran as Sonnet 5.5. True.
- README 55f43e2: accurate. `remote-auth.mjs` exists, 24 tests, proofs/ holds both proof files, the stale "between d10cb84 and 54dc401" range is gone. Local only: `main` is ahead of origin by 1, so the public README does not yet say it.
- Live state now: page 200; `github.com/pwsaragossy/rio-miami-rail` is 404 (private, as planned); `pwsaragossy/radox` 200.

## Findings

### M1 (major). Challenge 5 has no evidence on disk and the check is not in the repo
The only trace of "CAP-71 address-bound payload" is one board line (Vhendala card, 16:00). I found no "preimage" in `~/code/rio-miami-rail/scripts` or in any project file. The "independent check" that "first rejected valid ones" is not in the public repo, so a judge cannot see the fix, and no record of the first rejection exists. I could not verify the protocol statement (the Raven `execute` tool was not loaded for me), so it is unverified, not false. Replace item 5 with only what is on disk, or get the session that wrote the check to name the file and the failed run:
> 5. For the second shipment, our check of the teammates' signed entries first rejected valid signatures. Protocol 29 address-bound credentials are signed over a different payload than the legacy ones; we changed the check to use that payload, and a wrong key is still rejected.
If neither the file nor the run can be shown, drop item 5; four items are enough.

### M2 (major). AI note omits tools and assets
Missing from "Tools", all found on disk:
- the deck: `deck/build_deck.py` uses python-pptx and was written by an agent, so deck.pptx/PDF is AI-generated work; the note says nothing about it;
- video capture: `video/tools/record.cjs` uses Playwright/Chromium; `narrate.py` drives Voicebox; the runtime is mlx-audio (LICENCES.md line 304);
- Raven (the Stellar docs/ecosystem MCP gateway) used by sessions (unverified for which sessions; the Stellar-lookup rule requires it).
Also: the Voicebox narration is described in the present tense, but KICKOFF/board put its generation at Mon 00:00-03:00. If it is not yet made at paste time, the note must say "will be". The video, deck and README must carry the same line (board rule, Mon 06:00).
Suggested text, replacing the sentence "Voicebox 0.5.0 ... voice.":
> Voicebox 0.5.0 (Qwen3-TTS 1.7B via mlx-audio), run locally on Pedro's Mac, for the video narration: an AI voice cloned from Pedro's own recording, labelled as AI-generated in the video; Playwright for the screen recordings; python-pptx scripts, written by Claude Code, for the deck.
And add to "What they did": "the deck and its build script were also written by Claude Code." Also make AI_USAGE.md/README cover the deck and the narration (neither file lists them today; the rule is attribution for generated assets).
Models of other sessions (central, page host, Vhendala's and Leo's agents, any Haiku or other model) are UNVERIFIABLE by me: AI_USAGE says Opus 5.5 is "the only model in Leo's session logs"; nothing covers the other sessions. Ask Pedro's session to confirm from its logs, or word it "mainly Claude Opus 5.5".

### M3 (major). Prior work disclosure omits two facts the README states or the rules reward
1. README says the published `token_sale` is v8 while the deployed one is v7. The form says "run on mainnet ... their source is public" with no caveat; a judge diffing the repo against mainnet will see it. Add: "(the published token_sale is a newer version, v8, than the deployed v7; the other two match)".
2. The Radox API endpoint was written during the event (radox-internal branch `hackmeridian`, API-PROOF.md, 13:17 UTC) but sits in a closed repo. The text says only "added on a private branch". State the date, so it is not read as hidden prior work:
> A read-only Radox API endpoint that reads this registry was written during the event, on a private branch of the closed Radox backend (2026-10-25); it is not part of this repo and its source is not published.
Also add the README's "That repo carries its own, different licence." (16 chars saved elsewhere is not needed; limit is unseen). Pre-event documents, the chief-of-staff plugin and the repo creation time are present and match the README. The count stays below 1500.

### m1 (minor). "Nine refusal branches are recorded with their error codes"
One of the nine (`wrong_signer`) is `Error(Auth, InvalidAction)`, not a numeric contract code, and all nine ran as simulations (DEPLOYMENTS/README say so). Replace:
> Nine refusal branches, run by simulation, are recorded with their error results in `proofs/lifecycle.json`.

### m2 (minor). Description: "by their account" appears twice (Description and Technical fragment). Fine and consistent with README. No change; keep identical wording in all places.

### m3 (minor). Challenges item 4: Leo noted the evidence exists only in his session log. The sentence is true by Leo's account but not checkable. Add "by Leo's account" is not needed if you accept it; otherwise append: "(the public repo starts after this fix)".

### m4 (minor). Table: "Repository link ... public after Leo's scrub and Pedro's OK" and the live check shows 404 now; the table status is correct. Remember that the README at 55f43e2 is not pushed (ahead 1).

## Unverifiable by me
- Challenge 5's protocol claim (CAP-71 payload) and the first rejection.
- Models used by sessions other than Leo's and this review.
- That a human reviewed what AI_USAGE says Leo reviewed (Leo confirmed per card line 14:05; taken from the card).
- Mainnet status of the three Radox contracts and the v7/v8 statement (taken from README).

## Not checked
- Judges' portal limits (title/tagline/others "unseen"); Markdown rendering of the Description table.
- Contract source semantics beyond tests and proofs (no line-by-line read of lib.rs); verify-head was not re-run; the three-machine hashes were not re-queried on Horizon.
- Problem solved, Technical fragment and What's next beyond name/count scans.
- Deck, video, PORTAL-PASTE and the other files.
