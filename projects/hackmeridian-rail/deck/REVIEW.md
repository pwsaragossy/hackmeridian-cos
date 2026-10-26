# Deck review: Radox Custody Rail (v7)

Deck: deck/radox-custody-rail.pdf (10 slides, 742096 bytes), built by deck/build_deck.py on DECK-TEMPLATE.pptx.
Judge: `python deck/check_deck.py proofs/lifecycle.json` exits 0 on v7 (2026-10-25). A stripped copy (users claim, no Claude Code, short name) now fails with 4 failures.

## Verdict
Independent reviewer (fresh-context subagent, reviewer card) on v3: approve with changes. No on-chain claim false; all 7 lifecycle hashes and the attestation re-checked on Horizon testnet, successful=true.

## What changed after the review (v4)
- Narrative (Pedro via central, 2026-10-25; RADOX_CANON "Scope of the standard"): Rio–Miami is the pilot corridor; the goal is a SWIFT-like custody standard for tokenized goods on rails, built to integrate with chambers of commerce, ports and airports. Cover subtitle, problem slide, new vision slide 9 and the closing line on slide 10. Future tense, nobody named as a partner.
- Finding 1 (prior work): slide 8 now lists the closed backend, the architecture notes (20 Oct), the explainer video, our agent tooling (from 22 Oct) and "first repo commit 25 Oct 09:00 UTC" (gh: 2026-10-25T09:00:17Z).
- Finding 4 (checker): check_deck.py now requires the full name, Claude Code, AI_USAGE.md, AI voice, prior work, the explainer video, "No users or revenue yet", "none agreed yet", test key, "not built", "24 unit tests"; bans "our users", "revenue is growing", "integrated with".
- Finding 5: AI attribution names the page, docs and deck too.
- Finding 6: "Buyer" became "Recipient" on slide 2 (slide 7 keeps the user role "Exporter · Buyer").
- Finding 7: "its 3 Soroban contracts … public since 2026-08-19"; backend called closed.
- Finding 9: Pipeline added to the neighbours line.
- Slide 10: the photo goes in automatically when deck/screens/team.jpg exists.

## Still open (not fixable in the deck)
- Team photo from Vhendala: dashed placeholder until deck/screens/team.jpg exists, then rebuild.
- The repo github.com/pwsaragossy/rio-miami-rail is private; the link on slides 1, 4, 10 gives judges a 404 until it goes public at submission (owner's OK).
- ZIS/Paulo stay unnamed; if Paulo's written OK arrives, switch BRIDGE in build_deck.py and drop the ZIS/Paulo regex in check_deck.py.
- Testnet reset on 2026-12-16 [[stellar-testnet-resets-wipe-contracts-and-dfe4]]: the QR and MATCH stop working after it.
- Not changed, by choice: slide 5 "7 transactions" counts the lifecycle only (attestation disclosed; setup transactions not counted); slide 4 screenshot text is below 18 pt but the same hashes are on slide 5 at 18 pt.
- `pitch` (two timed rehearsals) is still open in TRACK.md; the deck follows PITCH.md.

## Sources
[[deck-and-video-rules-for-async-8b70]] [[stellar-and-solana-hackathon-winners-no-31ca]] [[wording-the-rio-miami-deck-readme-ef38]] [[zis-in-public-material-radox-is-bc05]] [[no-sep-and-no-stellar-project-aa39]] [[adb-trade-finance-gap-survey-dec-d033]] [[hackmeridian-rubric-7-criteria-weights-scored-50e2]] [[python-pptx-shadow-inherit-false-still-499c]]

## Second round (v5 to v6, same day)
- Marketing specialist on the v4 vision copy (S/marketing-v4.md): applied "our pilot corridor", "on Stellar", "to integrate with" (no "built to"), NOW "No standard, users or revenue yet", ask widened to "one port, airport or logistics operator", slide 2 "rarely one shared record across borders" (IATA ONE Record exists for air cargo, [[iata-one-record-is-a-live-e27f]]), slide 10 "Our goal: …".
- Independent reviewer on v5: approve with changes. Applied in v6:
  - Slide 7 now follows canon (Radox-operated rail, public format): "Radox operates the rail and the API"; the financial institution is the CLIENT that pays to use it. Slide 9 says "public" standard, not "open".
  - "(none started)" became "(none confirmed)" (canon: nobody named until it confirms in writing; does not assert that no conversation exists).
  - USD leg moved to FUTURE; slide 6 scopes the neighbours to "on Stellar".
  - check_deck.py now bans partnership, working with, already use, adopted, in talks, agreed with, integrated into, and requires "none confirmed" and "The goal is". All 6 of the reviewer's mutants now fail (they all passed or 5 of 6 passed before).
- Left open: DEMO-SCRIPT.md 2:30 "with chambers of commerce, ports and airports" reads as a present partnership (owner of that file: rail session; on the board). A judge may ask about IATA ONE Record: answer in Q&A, no slide claim until its spec is read.

## Third round (v7: core value on slide 7, three-machine proof on slide 5)
- Pedro via central: the core value ("o valor está todo aí") is integrate once with a public standard on a Radox-operated rail, like SWIFT, instead of N bilateral integrations; split what is open from what Radox operates.
- Slide 7 rebuilt: title "Integrate once, reach every party that joins"; diagram (example, 5 parties: 10 pair-by-pair links vs 5 links to one Radox rail; 5·4/2 = 10); OPEN · ANYONE (record format, roles and events = the custody_registry contract, Apache-2.0; verify any shipment, no login) vs RADOX OPERATES · CLIENT PAYS (onboarding, issuance controls, operation; the API and backend closed, not self-hostable; paid by the financial institution, not priced). Footer: adoption still takes a key, own signatures and one connection to the rail; Radox never the issuer; regulation with the client and counsel.
- Marketing specialist (S/marketing-s7.md, [[slide-7-hub-and-spoke-claim-ba2f]]) and independent reviewer (S/review-s7.md): approve with changes; applied all fixes (unsourced "today pairs connect" sentence removed, hub named "ONE RADOX RAIL", "closed" scoped to the API and backend so it does not contradict the Apache-2.0 contract, "one connection to the rail", title conditioned by "that joins"). The reviewer read the contract source: record = Shipment struct; events Opened, Handover, Attested, Delivered, StatusChanged; roles admin, operator, sources.
- Slide 5: three-machine run added as "two team members authorised handovers on their own computers, with their own testnet keys". Horizon (checked here and by the reviewer): 861544e4, 9214980e, 850da342, 849c268d successful, ledgers 5384199-202; leo key in handovers 1-2, vhendala in 2-3. "Most held by one harness" is true (4 of 6 actors). Where the signing happened rests on the proof file, not on chain.
- Open: proofs/three-machine.json is only on branch three-machine; the slide names the branch. Merge to main before the repo goes public (a push: Pedro's OK, rail session).

---

# Appendix A: reviewer output (v3), verbatim

Role: reviewer
Reviewing: Radox Custody Rail deck v3 (10 slides, deck/radox-custody-rail.pdf/.pptx), outside the team
Verdict: approve with changes (3 must-fix before it leaves; none is a false on-chain fact)
Reason: Every number and hash I re-checked is true. The weak points are disclosure completeness, one unfinished placeholder, a private repo link, and a judge script that cannot catch the failures that disqualify.

Question/conclusion: can v3 go to judges without overclaim, undisclosed prior work or missing AI attribution? Conclusion: no overclaim found; prior-work and AI disclosure are incomplete against the rules.

## Fourth round (v8: problem section in numbers, 2026-10-25 ~17:30 UTC)

Two problem slides were added before any result, and the product and workflow slides were merged into slide 5, so the deck stays at 10 slides. Every number is a row of PROBLEM-NUMBERS.md, which another session's reviewer verified. The deck session re-opened NTC, ICC, DCSA and the TT Club PDF itself.
- Slide 2: 45M ocean bills of lading a year (DCSA, Feb 2023, 2021 data); ~11% issued electronically (DCSA, as of 2025, with the Jan 2025 5.7% shown); 22% of recorded cargo thefts in 2025 involved insiders (TT Club & BSI, Apr 2026).
- Slide 3: R$900M est. direct loss from 8,570 cargo robberies in Brazil, 2025 (NTC&Logística, 28 Mar 2026); US$85M HSBC loss on forged documents (Hin Leong, GTR, 18 Nov 2024); US$2.5T trade finance gap, market size only (ADB, Dec 2025).

Independent reviewer verdict: approve with changes. All of the changes were applied:
- the 45M and the 11% are no longer tied together;
- "thefts" became "robberies" (the source says "roubo");
- "Banks get fooled" became "A bank got fooled";
- the closing line no longer implies the build solves part of the problem;
- the ADB figure is labelled market size only;
- the TT Club figure is labelled "recorded".

check_deck.py exits 0. "{{" placeholders and "traction" are banned.

Open:
- None of these numbers measures the handover itself; the 22% insider figure is the closest. This limit is honest and no slide claims more.
- PITCH.md slide row 3 still cites the ADB 2022 figure (Sept 2023). That file belongs to the pitch work.
- The reviewer's full report is in its note [[problem-slides-review-2026-10-25-2478]].

Round 4b (same day): the spoken script PITCH-FINAL.md was moved to the same wording. An independent reviewer approved it with changes, all applied: each DCSA figure keeps its year, the TT Club figure names its year and source, and the script is 388 words.

## Fifth round (v11: problem, standard, rail, proof; owner reframe 2026-10-25)

Owner's request, relayed by chief-of-staff: start with the problem, then the SWIFT-like standard, then the double signature. The real solution is an end-to-end rail across many companies, and the double signature is only the rule of each link.

v10 is kept at the session scratchpad for comparison.

check_deck.py has a new story-order rule. The slide pills must run PROBLEM, STANDARD, RAIL, TESTNET, and no headline of 36 pt or more before the rail slide may mention signing. v10 failed it with 4 failures; v11 passes with 0.

Independent reviewer verdict: approve with changes. The rubric, estimated by the reviewer and not a judge, scored v10 at 67 and v11 at 71.5, about 73 with the fixes. All the fixes against overclaiming were applied:
- the cover says "could share";
- slide 6 is titled "The lifecycle ran on testnet";
- the three-machine line reads "own registry ... still test keys"; the branch three-machine exists on GitHub;
- the rule bullet reads "both sides (delivery: recipient and holder)";
- the slide 5 pill reads "DESIGN, LIFECYCLE BUILT" and its subtitle says "would follow ... today it runs across five test keys";
- slide 7 is titled "all signers, one call";
- the slide 2 hypothesis says "not yet tested with a customer";
- the 9 refused calls are labelled "e.g. wrong signer".

Slide 4 uses the rail session's wording, so the deck, the video and the README match: "a shared, SWIFT-like custody standard that companies along a supply chain, from origin to destination, could use. Neither the standard nor the rail exists yet." The ask was not changed, because the video quotes it word for word.

Claims row added: "2 signatures" on Recipient → Delivered comes from REVIEW-contract.md item 7 (deliver needs the final custodian and the holder; lib.rs 356-360).

PITCH-FINAL.md was rewritten in the v11 order. The marketing specialist drafted it, and the wording was aligned to the rail session. It is 387 words by wc -w, and two timed reads are still needed.

Open:
- slide 2 keeps the unnamed bridge line, which [[zis-in-public-material-radox-is-bc05]] allows without Paulo's OK;
- User Value stays capped near 7 until a customer exists.

Round 5b (Leo's technical pass): a 32-byte head verifies history and cannot rebuild it. The deck now says history is replayed from Horizon and checked against the head (verify-head.mjs reads Horizon, line 53). The three-machine line now cites proofs/three-machine.json, and the shipment key is sha256(container | origin). 'rebuild' is banned in check_deck, and a mutant containing it fails.

### v11 rubric per criterion (reviewer, round 5)
The scores are the reviewer's own estimates, not a judge's. Weights are from [[hackmeridian-rubric-7-criteria-weights-scored-50e2]]. The "Reason" column is the reviewer's evidence. The "To reach 10" column is this session's reading and was not in the reviewer's output.

| Criterion (weight) | v10 | v11 | Reason (reviewer) | To reach 10 |
|---|---|---|---|---|
| Ecosystem Alignment (20) | 7 | 8 | The standard slide and the "many companies, one ledger" framing are new; the Stellar neighbours stay. | One named ecosystem partner (anchor, wallet or SEP issuer) that commits to read or write the rail, with written OK to name it. |
| User Value and Problem (20) | 6 | 7 | The problem now leads and the rail fits the supply chain; the hypothesis is still untested. | A real shipper, forwarder or bank confirms the pain in writing or runs one shipment. Capped near 7 until a customer exists. |
| Technical Execution (15) | 8 | 7 (~8 with the restored line) | The atomic dual-sign visual and the "fails" line were dropped. Fix 4 restored the substance as "both sides sign one Stellar transaction ... or the call fails". | Handovers signed by independent organisations' keys, plus the head check run by an outsider from the public page. |
| Innovation (15) | 6 | 6 | "Found none in directories searched" stays; the standard is only a proposal. | A published draft spec of the standard (schema and auth rules) that someone else implements against. |
| Hackathon Progress (10) | 8 | 8 | Same 7 transactions and 24 tests. The overclaim in the slide 6 title was fixed ("The lifecycle ran on testnet"). | The second shipment from separate machines shown live on the public page, with the fresh run reproducible from the README. |
| Market and Ecosystem (10) | 5 | 6 | "Integrate once": 10 links vs 5; still no customer. | A sized first segment for the pilot corridor and a price, from a source, with one paying or committed user. |
| Product Design and UX (10) | 7 | 8 | The skim story is clearer; slides 4 and 5 are denser. | Slides 4 and 5 carry less text; the public shipment page is linked from the deck and works on a phone. |

Weighted: v10 = 67, v11 = 71.5. The reviewer expected about 73 with fixes 1-7, mostly from Technical going back to 8. All seven fixes were applied (see above).

## Sixth round (v12: market, model, multi-company proof; 2026-10-25 ~19:45 UTC)
Slide 9 became "One rail, every corridor" (pill MARKET · MODEL · THE ASK). It holds the market figures from MARKET-NUMBERS.md section 4, labelled "figures, not ours"; the model, a subscription per connected institution plus a fee per shipment that borrows the shape of Swift's published fees (section 5), with no prices and "Not affiliated with Swift"; Now/Next; and the locked ask. The deck stays at 10 slides. Slide 4's "Paid by the financial institution; not priced" now names the same model. The old vision items (payment leg, USD leg) were removed under central's "no money flow on any slide" rule. Slide 4 still keeps "No port, airport or chamber link: none confirmed".
Independent reviewer: approve with changes, all applied. Footnotes 2, 4 and 6 got back their year and access date, and the Swift line lists entry, annual and per-message fees. Market and Ecosystem moved from 6 to 7 (the reviewer's own estimate). It stays capped by no prices, no go-to-market and no pilot.
Slide 6 adds: "two test companies' chains on one registry, sharing stops, each dual-signed (proofs/multi-chain.json)". All 10 transactions show successful on Horizon testnet (19:19–19:20 UTC, checked by this session). Pushed afterwards: GitHub main 7dd63f7 has the file (run commit ef0ca00).
check_deck: exit 0, 10 slides, PDF 751,941 bytes.

## Findings (ranked)
1. [major, FACT] Slide 8 prior-work list is incomplete against the disqualifier ("Undisclosed prior work is a disqualification", PORTAL-PASTE.md:47). Missing: (a) the explainer video and the Rio-Miami initiative that slide 2's bridge cites ("our explainer video") - pre-event work shown as context; (b) the chief-of-staff plugin (public repo, first commit 2026-10-22, SUBMISSION.md:55 says "declared as prior work"; it ran the team's work); (c) the 2026-10-20 architecture panel (wording note rule 9); (d) the sentence "no contract code before Sun 09:00" (rule 9). Git supports it: rio-miami-rail first commit is 2026-10-25T09:00:17Z (placeholder page); contract commit 11:29Z. Slide shows only "Planning files, 24-25 Oct". Fix with no new fact: add those items and "first commit 25 Oct 09:00 UTC".
2. [major, FACT] Slide 10 shows a dashed "Team photo" placeholder in a final deck; card says photo is Vhendala's, due Sun 09:00. Replace or remove the box before sending.
3. [major, FACT] Slide 10 and slide 1/4 link github.com/pwsaragossy/rio-miami-rail; `gh repo view` says PRIVATE today. Rules require a public repo; judges would hit a 404. Gate: flip public before the PDF is uploaded (owner's call; already on the card).
4. [major, FACT] check_deck.py can pass a bad deck. I mutated a copy (removed AI attribution, prior-work heading and "AI coding agents"; replaced "No users or revenue yet" with "Our users love it and revenue is growing"; "24 contract" -> "240"; Pedro's name -> "Pedro"): exit 0, failures=0. It tests only: slide count, PDF size and mtime, runs under 18 pt (and skips runs with no explicit size), a banned-word list, 8-hex tokens and the contract ID. It does not require AI attribution, prior-work text, the full name, or any number besides hashes; it never calls Horizon; it cannot read images (slide 4's screenshot text is about 12-16 pt: row labels ~16, ledger/hash ~14 - under the 18 pt rule, and the "Verify head" button is clipped at the crop edge). Treat exit 0 as "no banned words and hashes real", not "deck is safe". My own pass by hand supplies the rest.
5. [minor, FACT] AI attribution (slides 8, 10): meets the rule for code and narration. Gaps: it says "Code, tests and scripts" but AI_USAGE.md lists the shipment page as AI-made and "not reviewed line by line by a human"; the deck itself (text, build script, layout) and the docs were AI-made too and are not named. SUBMISSION.md's own draft says "contract, tests, harness, verify script, shipment page and docs". Say "code, tests, scripts, the shipment page, docs and this deck". "No AI-generated images" is true (screenshots, QR codes, shapes).
6. [minor, FACT] Buyer vs Recipient: slide 2 and 7 say "Buyer"; slides 4-5 and the contract say "Recipient" then "Holder". A judge cannot tell if the buyer is the last custodian or the token holder. Use "Recipient" on slide 2, or "Recipient (buyer side)". Keep rejecting "Buyer" on slide 5: the live page says Recipient.
7. [minor, FACT] Slide 8 "Radox platform and 3 Soroban contracts ... (public repo...)": the parenthesis can read as "platform is public". Only the contracts are public; backend closed (said elsewhere on the slide). Write "3 Soroban contracts public; platform backend closed".
8. [minor, FACT] Slide 5 "7 testnet transactions" counts the lifecycle only. On chain there are also 13 setup steps (12 with hashes), the deploy, and the attestation (disclosed in small print). Not false; but "7 ... All successful" next to "9 refused" invites "what about the rest". The footnote handles the attestation; add "plus setup" or leave.
9. [minor, SUSPICION] Slide 6 names Kutana and Trustless Work as nearest; the library note [[no-sep-and-no-stellar-project-aa39]] says Pipeline (SCF #43, trade finance) is "the closest substitute a judge may name". Omitting it while saying "we found none" is hedged correctly, but a judge naming Pipeline reads it as a miss. Add Pipeline to the neighbours line.
10. [minor, FACT] Slide 2 bridge ("our explainer video about a Rio-Miami trade-corridor initiative") names no one, so the ZIS rule holds (no "ZIS", no "Paulo" on any slide; check_deck greps for both). But "initiative" unverifiable by a judge and can read as an affiliation; it is the owner's board line 34, so keep, and list it as prior work (finding 1).
11. [note] Live page and testnet: Stellar testnet resets about quarterly (next 2026-12-16, [[wording-the-rio-miami-deck-readme-ef38]] rule 14). The QR and "MATCH" die then. Say "snapshot in repo" if judging runs past that.

## Premises tested (hands-on)
- On-chain: all 7 lifecycle hashes plus the attestation exist on Horizon testnet with successful=true; ledgers 5381140/42/43/45/46/47/48 (attest 44). Slide 4 ledger numbers match. Hash prefixes on slide 5 match proofs/lifecycle.json.
- 9 refused calls: lifecycle.json failures has 9 entries, all "simulation" - slide says "(simulated)". Good.
- 24 unit tests: 24 `#[test]` in test.rs; VERIFY-LEO line 20 "24 passed".
- Names/roles: commits by pwsaragossy and leo-schlanger only; Leo "custody_registry, harness, proofs" matches; Vhendala has no commits and the slide says QA/review. Full name "Pedro Wakigawa Saragossy" is the board decision. OK.
- ADB: adb.org page says "remains at $2.5 trillion, as in 2023"; slide's caption says it is not evidence of the custody problem. OK.
- Claims guard words: slides contain no title/bill-of-lading/legal claims; "In production it would sit beside the carrier's bill of lading; not integrated" is the guard's own text. No "none exists". No users/partners/pilot claim: "none agreed yet", "No customer has confirmed", "not yet submitted", "not done", "not built" all present. No legal analysis done (STATE §6).
- App claims: app.js header says read-only, RPC+Horizon, Verify head recomputes like verify-head.mjs. OK.

## Strongest contrary case
The deck is honest to a fault: slides 2 and 9 admit no customer, no pilot, no revenue, and slide 5 says the actors are one harness. A judge scoring User Value (20) and Market (10) may mark it low. That is the cost of a safe deck, and correct: the alternative risks the disqualifier.

## Rubric (weights from [[hackmeridian-rubric-7-criteria-weights-scored-50e2]])
Strong: Technical Execution 15, Ecosystem 20 (slide 6 + proofs), Product Design 10. Weak: User Value 20 (assumption only), Market 10 (one slide, "not priced"). Hackathon Progress 10 is fixable. Single highest-value change with no new facts: complete slide 8 (finding 1 plus "first commit 25 Oct 09:00 UTC; AI named for page and deck"). It also removes the only disqualification path.

## Rejections in merge-log: judged
- Keep "Pedro Wakigawa Saragossy": right, newer owner decision beats the wording note.
- Keep full bridge sentence: right (board line 34). Keep on slide 2: right. But its source (explainer video) must be disclosed as prior work.
- Keep "Recipient" on slide 5: right (page's own label); but reconcile slide 2.
- Own addition (attestation disclosed): right and honest.

## Readability
Template labels 12-14 pt (header, footer, "NEXT" bar) are exempt in check_deck and do not carry claims. Real content: all text runs 18 pt or more except the slide 4 screenshot (see finding 4, not essential: the same hashes are 18 pt on slide 5). Slide 9 body text 24 pt, fine.

## Pre-mortem
Top failure story: a judge opens the QR/GitHub link and gets 404 (repo private), or notices the placeholder box, and reads the rest as unfinished; or an AI-assisted pre-judge reads "explainer video" on slide 2, finds nothing about it in prior work, and flags undisclosed prior work. Fix: findings 1-3.

## Owner's manual work
Make repo public (one click, owner's OK). Insert team photo (Vhendala). Re-export PDF after edits and re-run check_deck. Feasible before Mon 08:00.

## Never-skip checklist
- [x] Library cited: [[wording-the-rio-miami-deck-readme-ef38]], [[no-sep-and-no-stellar-project-aa39]], [[hackmeridian-rubric-7-criteria-weights-scored-50e2]], [[zis-in-public-material-radox-is-bc05]], [[adb-trade-finance-gap-survey-dec-d033]]. No new library note saved: the one reusable lesson (a checker that never tests required disclosures will pass a mutated deck) is recorded here; not saved with library.sh.
- [x] Specialists' Never-skip items: researcher and marketing outputs read; marketing's name change rejected correctly; designer fixes applied (shadow, crop, rail).
- [x] Three premises tested (on-chain truth, disclosure vs rules, checker strength) plus hands-on counts.
- [x] Key citations opened (ADB page, Horizon, repo, AI_USAGE.md, notes).
- [x] Numbers recomputed (7+1 txs, 9, 24, ledgers).
- [x] Contrary case written. [x] Contradictions found (Buyer/Recipient, prior-work vs bridge).
- [x] Owner's manual work listed. [x] Pre-mortem run.
- [~] Specialists' `## Versions`: researcher gave two versions with "no outside judge beyond the sources"; marketing and designer versions not checked line by line.
- [x] Severity and evidence on every finding.

## Not checked
Video and README (not in scope); stellar.expert (rate-limited); deployed page lacks commits be4bcb9/9cf9301 (board says not deployed); whether Kutana/Trustless Work descriptions are current (library only).

## Questions for the owner
1. Flip rio-miami-rail public before upload? 2. Photo ready or remove the box? 3. List the explainer video and chief-of-staff as prior work on slide 8?

## Versions
v1: lens "rules as the judge reads them", judge = RULES/PORTAL-PASTE disqualifier text; verdict: 4 disclosure gaps found. v2: lens "can the script be fooled", judge = mutated deck run through check_deck.py; verdict: exit 0 on a bad deck, so script is not a safety proof. v3: lens "goal behind the goal", judge = live repo and Horizon; verdict: repo private, placeholder visible, on-chain claims true.

---

# Appendix B: claims and sources (v3; v4 changes above)

## Claims on the slides and their sources

Files are in projects/hackmeridian-rail/ unless stated; proofs/ is in pwsaragossy/rio-miami-rail.

| # | Slide | Claim | Source | Checked |
|---|---|---|---|---|
| 1 | 1, 4, 5 | Testnet, test keys, not real custodians | proofs/lifecycle.json `network: testnet`; PITCH.md Claims guard (Demo) | file |
| 2 | 1 | First corridor Rio–Miami; title "Radox Custody Rail" | board, owner decision 2026-10-25 ~11:15 WET | board |
| 3 | 2 | "changes hands several times" (not "4+") | SUBMISSION.md fallback; no source for a number | rule |
| 4 | 2 | Paper or one operator's own system; financier cannot see: stated as hypothesis, no customer confirmed | IDEA.md (assumption); wording note rule 10 | rule |
| 5 | 2 | US$2.5T global trade finance gap, ADB Dec 2025, context only | adb.org/publications/adb-global-trade-finance-gap-survey, re-opened 2026-10-25 13:25 UTC: "remains at $2.5 trillion, as in 2023", Dec 2025 | live |
| 6 | 2 | Bridge sentence (unnamed initiative) | board line 34, unnamed version; [[zis-in-public-material-radox-is-bc05]] | board |
| 7 | 3 | Both custodians authorise one invocation; missing signature fails | developers.stellar.org authorization#authorizing-multiple-addresses (Raven 2026-10-25 13:22 UTC); proofs failures `wrong_signer Auth InvalidAction` | live + file |
| 8 | 3, 6 | Token stays with holder in transit; burned by existing `redeem` after Delivered; policy not enforced by registry; needs holder signature | PITCH.md slide 2; wording note rule 1; proofs `redeem_precondition`, `holder_balance_after_redeem: "0"` | file |
| 9 | 3 | Custody record keyed to container; beside the bill of lading, not integrated | PITCH.md Claims guard custody wording (verbatim) | rule |
| 10 | 4 | Page shows every handover, signer roles and tx hash; Verify head recomputes and compares: MATCH from 7 transactions | rio-miami-rail.vercel.app, clicked 2026-10-25 ~13:27 UTC: "MATCH recomputed 2d74fe…195414 from 7 transactions; on-chain head 2d74fe…195414"; app.js lines 4-8, 192-204 | live |
| 11 | 4 | Reads Stellar RPC and Horizon directly; read-only | app.js header comment and constants (RPC, HORIZON) | code |
| 12 | 5 | 7 transactions, all successful; the 7 short hashes | proofs/lifecycle.json lifecycle; Horizon `successful: true` for 635c99ac and 864fd164 re-checked 2026-10-25 13:23 UTC; check.py 7/7 | live + file |
| 13 | 5 | Route labels (Warehouse → Port … Recipient → Holder) | live page handover list, 2026-10-25 | live |
| 14 | 5 | 9 invalid calls refused (simulated) | proofs failures, 9 entries `hash_or_sim: simulation`; VERIFY-LEO.md d | file |
| 15 | 5 | 24 contract unit tests pass | VERIFY-LEO.md line 20 (`24 passed; 0 failed`) | file |
| 16 | 5 | Contract ID CCBJVXMJ…H4LII | proofs `custody_registry` | file (check_deck.py) |
| 17 | 5 | Every actor is a test key held by one harness (proofs `actors`: 11 test keys) | PITCH.md Claims guard (Demo) | rule |
| 18 | 6 | RPC keeps events about 7 days | developers.stellar.org/docs/build/guides/events (Raven 2026-10-25): "7 day retention window" | live |
| 19 | 6 | Kutana and Trustless Work release escrow on trade milestones; none records a dual-signed physical handover; no SEP covers it (directories searched 24-25 Oct) | [[no-sep-and-no-stellar-project-aa39]] | library |
| 20 | 6, 10 | Apache-2.0 | [[apache-2-0-for-rio-miami-9905]]; LICENCES.md | library |
| 21 | 7 | SWIFT-style public format; fee from the operating financial institution, not priced; Radox is the rail, never the issuer; regulation with client and counsel | PITCH.md slide 7 and Copy rules | rule |
| 22 | 8, 10 | 3 Soroban contracts on Stellar mainnet, public repo created 2026-08-19 | PITCH.md Claims guard (verbatim); wording note rule 3 | rule |
| 23 | 8 | transfer_agent new testnet instance from existing wasm; planning files 24-25 Oct | wording note rule 9; STATE.md §3 | rule |
| 24 | 8, 9 | Radox API reads the registry, same head; closed backend; testnet | API-PROOF.md (radox-internal 7ececba0, curl head 2d74fec0…5414); board 13:45 UTC full backend boot | file |
| 25 | 8, 10 | Code, tests and scripts written with AI coding agents (Claude Code); per-file record AI_USAGE.md; narration AI voice from Pedro's voice; no AI images in the deck | SUBMISSION.md AI tooling note (owner: "name everything"); board ~13:20 UTC; deck images are page screenshots, QR codes and shapes | rule + file |
| 26 | 9 | No users or revenue; pilot none agreed; SCF not submitted; audit not done; USD leg not built | PITCH.md Claims guard; wording note rules 4-6 | rule |
| 27 | 9 | The ask (introductions, engineer review) | Scale intake "also wanted at the event", STATE.md §2 | file |
| 28 | 10 | Pedro Wakigawa Saragossy founder and captain; Leo Schlanger developer; Vhendala QA and product review; Leo and Vhendala joined for the hackathon | board (full name, 2026-10-25); wording note rule 7 | rule |

## Seventh round (v13, founder voice, 2026-10-25)

Owner rule in force: "NÃO É PRA LOWBALL NOSSO PROJETO, VENDA APENAS A PARTE BOA". Hedges are now defects (check_deck HEDGES); the false-claim line holds: no partner named, no signed deal, no users or revenue, no testnet called mainnet ([[founder-voice-in-public-text-sell-d820]]).

v13 changes: slide 2 legacy-ports line (World Bank via IAPH, IMO FAL.5/Circ.54); slide 4 "Radox is in conversations with ports, airports and chambers of commerce", "Radox will operate"; slide 7 any Stellar asset, US$4B (SDF, 1 Sep 2026), open API for issuers; slide 9 market, Swift-shaped model, roadmap. Spoken pitch rewritten (394 words, limit 396).

Independent reviewer (REVIEW-V13.md): approve with changes; all six fixes applied (no "their" before legacy systems; "Radox API custody route"; "Swift's billing rules"; shorter context line; "DCSA, Feb 2023"; "RADOX WILL OPERATE"). Every number re-opened at its source except R$900M, US$85M, US$2.5T and the slide 9 trade figures (checked in earlier rounds).

Judge: check_deck exit 0 (10 slides, 759,297 bytes). Mutants on a scratch copy, all exit 1: "Two ports have signed with Radox", "A bank signed a letter of intent with Radox", "The Port of Santos signed on to the rail", "The lifecycle ran on mainnet", "Radox has paying clients in three ports", "The rail is live on mainnet", "none signed" (hedge).

| Criterion | Weight | v13 score |
|---|---|---|
| Ecosystem | 20 | 9 |
| User Value | 20 | 8 |
| Technical Execution | 15 | 9 |
| Innovation | 15 | 8 |
| Progress | 10 | 9 |
| Market | 10 | 8 |
| UX (slides only) | 10 | 8 |
| Total | 100 | 84.5 |

User Value stays at 8: 9 needs one first-hand user fact (a port or chamber that spoke with Radox, quotable without a name), which only the owner can give. Owner questions on the card: "in conversations" true for each type; that user fact.

### Round 7 delta (owner answers via central)
Slide 4, pitch and COPY-V13 §4 now say "Radox has openings with ports and airports, and chambers of commerce in Brazil and Miami are opening doors" (owner wording; no chamber, ZIS or Paulo named). Reviewer delta (REVIEW-V13-DELTA.md): approve, no must-fix. check_deck exit 0; mutant "chambers ... have joined the rail" exits 1; pitch 395 words. User Value 8 to 8.5; total 85.5/100 (reviewer estimate).

### Round 7 delta 2 (20:09 UTC, owner answers via chief of staff)
Direct conversations are with chambers of commerce; ports and airports come through the corridor initiative ("a zis fechando, nós fechamos"; "se adotar a zis, nós somos consequência"). Slide 4, pitch and COPY-V13 §4 now read: "Radox is part of the Rio–Miami trade-corridor initiative and its technology rail: every port, airport and chamber that joins it joins the rail, through one adapter to the Radox API. Radox is in conversations with chambers of commerce in Brazil and Miami." Initiative unnamed. This replaces delta 1 ("openings with ports and airports"), which overstated direct contact. Reviewer (REVIEW-V13-DELTA2.md): pass, its safer "part of ... and its technology rail" applied. check_deck exit 0; signed-ports mutant fails; pitch 394 words. User Value 8.5.

- Delta 3: "joins it joins the rail" became "joins it will join the rail" (rail-leo-brief request; reviewer reason in REVIEW-CORRIDOR-SENTENCE.md: no adapter exists today). Deck, pitch (395 words) and COPY-V13 §4 identical. check_deck exit 0.

## Eighth round (v14 cover, 2026-10-26)
Cover: submission title "Radox Custody Rail: SWIFT for goods in transit, on Stellar" and the owner-approved tagline; "First corridor: Rio–Miami". Slide 3: Hin Leong US$85M cut (dual signing does not stop forgery by a signer), WTO 80–90% of trade relies on trade finance, ADB US$2.5T gap unchanged from 2023; headline "Cargo goes missing. No shared record." Reviewer (REVIEW-V14-COVER.md): pass, both must-fixes applied; WTO and ADB passages re-opened. check_deck exit 0.
