Role: reviewer
Reviewing: STUDY-MAINNET.md (engineer + security) and STUDY-WIN.md (researcher + product), both written 2026-10-25 23:55 UTC
Written: 2026-10-26 00:00–00:15 UTC, read-only (this file is the only write; no commits)

| Study | Verdict | Reason |
|---|---|---|
| STUDY-MAINNET.md | **approve with changes** | Every hard number I re-ran matches: fees, TTLs, retention, the SDK TTL behaviour, the RPC provider list, Horizon, Audit Bank timeline and co-pay, SCF #46 date. It misses one eligibility condition of the Audit Bank, and that condition sits on the critical path. |
| STUDY-WIN.md | **approve with changes** | The gates, the Claims-guard breach on landing-v3, the deck gaps and the 20/20/17 benchmark all reproduce. The headline score arithmetic is wrong. The video kill time contradicts the upload deadline. Tonight's list leaves out two README errors that an SDF engineer would see. |

Neither study has a critical finding. Neither is a substitute for a licensed auditor or lawyer: mainnet custody of tokens that stand for cargo needs both (STUDY-MAINNET G1, B1).

## Findings (ranked by severity)

### STUDY-MAINNET.md

1. **[major] The Audit Bank also restricts eligibility by project type, and the study does not mention it.** B1 and the critical path ("SCF award → Audit Bank readiness → audit") assume that an SCF award is enough. The official FAQ, read again 2026-10-26 00:10 UTC, says the eligible projects are "Projects funded through the Stellar Community Fund involving financial protocols", plus "high-dependency data services, or high-traction dApps". A custody registry that never calls the token is not obviously a "financial protocol". Evidence: [FACT] stellar.org/grants-and-funding/soroban-audit-bank FAQ. Confidence: high (quoted). **Fix:** in B1 and in risk row "Audit not obtainable", add: "Eligibility also requires the category financial protocol / high-dependency data service / high-traction dApp. Scope the audit as registry + transfer_agent + redeem gate, which is the financial path, and confirm the fit with SCF before relying on it." Raise the likelihood in that risk row from 3 to 4. Add owner question Q10: "Does the Audit Bank accept the rail as a financial protocol? Ask at SCF office hours."
2. **[minor] The "7.0 days" retention belongs to one provider, not to mainnet.** D2 says "RPC keeps 7.0 days (measured)". I re-measured `mainnet.sorobanrpc.com` `getHealth` → `ledgerRetentionWindow` 120960 (00:01 UTC). That is the operator's configuration; the providers page lists archive RPCs (Lightsail, Ankr) with longer history. **Fix:** "the public RPC we used keeps 7.0 days; archive RPC providers keep more".
3. **[minor] A8's wording on archival timing is muddled.** "A shipment idle near the end of its life will archive about a month later" is unclear. With `extend_ttl(120_960, 518_400)` and a 120-day starting TTL, a write does nothing until fewer than 7 days remain. It then extends to 30 days. An idle shipment therefore archives 120 days after `open`. The recommendation (mainnet-sized thresholds) is right. **Fix:** "a new entry lives 120 days; writes extend it only when under 7 days remain, and only to 30 days; an idle shipment archives at day 120."
4. **[minor] SCF tranches are listed incompletely.** The awards page lists "Initial Award Distribution (on approval)", then Tranche #1 MVP, #2 Testnet and #3 "Live on Mainnet". The cost table lists three tranches. **Fix:** add the initial distribution.
5. **[minor] "transfer_agent is not deployed on mainnet" has one source.** It rests only on the header comment of `mainnet-rehearsal.mjs`. That fits the claims note, which lists only three Radox mainnet contracts ([[claims-hackmeridian-material-may-and-may-3e4f]]), but no chain query was made. **Fix:** tag it "per script header and public Radox README; not queried on chain".
6. **[minor, cross-study] Phase 0 lists the A9 README correction as still to do, but STUDY-WIN has no action for it.** See STUDY-WIN finding 3.
7. **[note] A10 brute force holds.** 26³·10⁶ ≈ 1.76·10¹⁰ is an upper bound: ISO 6346 owner codes are registered prefixes, so the real space is smaller. The README publishes the key format and a worked example (`TEST4627832|BRRIO`, README:230). The finding stands, and it is correctly tagged [INFERENCE].

### STUDY-WIN.md

1. **[major] The video kill time contradicts the upload deadline.** Item 1 says "2.5 h build" and "Latest start 03:00 UTC". 03:00 + 2.5 h = 05:30. Open question 1 says "Latest 04:00 UTC" for the upload. R1 says the fallback must be ready "by 05:00". Pedro would act on 03:00 and miss both. Evidence: quoted lines in STUDY-WIN §3 item 1, §4 R1 and question 1. **Fix:** "Latest start 01:30 UTC for a 04:00 upload. If not started by 01:30, cut the R1 fallback from the existing DEMO-SCRIPT clips and have it uploaded by 05:00." Change the kill criterion in the product checklist the same way.
2. **[major] The headline projection is miscomputed and the range does not follow from its own rule.** The study's inputs give 8·20 + 7·20 + 9·15 + 7.5·15 + 9·10 + 7·10 + 8·10 = **787.5, i.e. 78.75**. The study instead shows "~77" (answer), "~77.5" (table) and "~78" (formula line). It also says "a range of ±1 per criterion gives 72–80". ±1 on every criterion is ±10 weighted, so the range is **68.75–88.75**. The "Now" figure of 67.5 recomputes correctly. Confidence: high (recomputed). The ranked actions do not depend on the total. Leo and Pedro will quote it, though, and a judge would catch it. **Fix:** "~79 after fixes (my judgment; ±1 on each criterion gives 69–89)" in all three places. Also give the Points column a unit: on a 10-weight criterion, 1 criterion point = 1 weighted point; on a 20-weight criterion, 1 criterion point = 2 weighted points.
3. **[major] Two README errors that go public at 06:00 are missing from tonight's actions.** (a) README:305 says "the contract code's TTL is the deployer's to extend". soroban-sdk 29.0.1 `storage.rs` (doc of `Instance::extend_ttl`) says "Extend the TTL of the contract instance and code … done for both the contract code and contract instance". The contract calls it in `bump_instance` (lib.rs:195-199). I confirmed this in the local crate source; it is the same finding as STUDY-MAINNET A9. (b) README:283 says the Audit Bank "prioritises projects in the Stellar Community Fund". The official page contains no "prioritise" wording; its eligibility FAQ restricts the Audit Bank to SCF-funded projects (see STUDY-MAINNET finding 1). The judge named in the brief is an SDF engineer, and an AI pre-judge reads the README. Fixing both takes about 5 minutes. **Fix:** add to item 6 or 7, owner Leo:
   - README:305: "Writes to the instance also extend the contract code's TTL (soroban-sdk `instance().extend_ttl`); an idle contract needs a keeper."
   - README:283: "The SDF Audit Bank is open to SCF-funded projects; we plan to apply to SCF Build first."
4. **[minor] The close time is stated as a fact, but the sources conflict.** The header says "portal closes 12:00 WET". [[hackmeridian-2026-rules-and-submission-requirement-5868]] records Pedro saying the editing window closes Mon 10:00 Lisbon. PORTAL-SEEN.md line 5 says the deadline is 12:00 WET and that editing is allowed until close. R9 lists this conflict, but the header and the "What would change" bullet treat 12:00 as settled. **Fix:** in the header, "closes 10:00 or 12:00 WET (sources conflict; item 10 settles it)". The 08:00 plan is unaffected.
5. **[minor, Claims guard] Item 11 could put a person's name in public text.** It says "quote them only with their OK". The claims note allows only "design reviewed by <role> at HackMeridian on <date>", and names only with written approval of the wording ([[claims-hackmeridian-material-may-and-may-3e4f]]). **Fix:** "record the role only (for example 'a Stellar engineer at HackMeridian, 26 Oct'); no name unless the person approves the exact wording in writing."
6. **[minor] Prior-work disclosure: the gap is real, but check the field's length.** I confirmed that FORM-ANSWERS' Prior work field (1,416 characters now) and README "Prior work" (README:168-176) do not mention the Radox design tokens or the voice sample's source video. Board line 124 (20:53 UTC) shows the page's tokens were checked against `radox-internal frontend/src/index.css`. The portal rule "Undisclosed prior work is a disqualification" (PORTAL-PASTE:47) and the field text "any code, designs, or assets that existed before the event" (PORTAL-SEEN:7) are quoted correctly. The field's character limit is unknown. **Fix:** run item 8 after item 10 confirms the limit; the shortest addition is "Page colours and type are Radox's existing design tokens; the narration voice was cloned from an earlier Pedro video."
7. **[minor] The deck evidence is slightly misstated, but the conclusion holds.** The study says the PDF holds "the 4 template images repeated on every slide". PyMuPDF finds **22 image objects, the same set on all 10 pages**. So there is no per-slide product image, as the study concludes. Slide 10 contains "Team photo" and slide 8 contains "24 unit" (both confirmed). **Fix:** say "22 image objects, identical on every page (template); no product screenshot".
8. **[minor] Item 3's done-when grep is too broad.** `grep -i "santos|hamburg|COFFEE"` also matches the cargo label `content: "Coffee"` at page/index.html:102. That label is not a Claims breach. **Fix:** grep for `santos|hamburg|COFFEE-0042|Port of` only, or decide to drop the coffee label on purpose.
9. **[note] The benchmark reproduces exactly, and the event label is slightly off.** I re-ran Scout `getHackathon` on the 7 events at 00:03 UTC: video 3+3+3+3+3+3+2 = **20**, GitHub **20**, demo 3+3+3+2+2+2+2 = **17** of 21. The event the study calls "Build Better" is slug `build-on-stellar` (ended 2025-03-31). The source is single (DoraHacks-derived) and the study labels it so. The reference class is online Stellar Hacks, not an in-person Scale pitch; the study already draws only "minimum, not differentiator" from it, which is the right limit.
10. **[note] Owner-accepted claims-guard risk, not raised again.** FORM-ANSWERS:68 and README:312 say "Radox is in conversations with chambers of commerce in Brazil and Miami". The sentence names no one, so it passes the guard, but it is an activity claim a judge cannot check. R8 covers the adjacent sentence and the owner accepted it at 20:12.

## Claims-guard check of every public text the studies recommend
| Text | Result |
|---|---|
| WIN item 3: "Rio → Miami test shipment", custodian as a role ("Port terminal"), real API shape | passes |
| WIN item 6: rename H1, verify block, list of scripts | passes |
| WIN item 7: "local fork … nothing was sent to mainnet" | passes |
| WIN item 8: prior-work sentence | passes (Radox is the team's own company) |
| WIN item 9: `proofs/radox-api.json` scrubbed of internal names | passes, if the scrub grep is run |
| WIN item 11: quote an engineer | **fix needed** (finding 5) |
| MAINNET A9 README correction | passes |
No recommended text names a partner, port, airport or chamber, or claims users or revenue. landing-v3 as it stands breaks the guard ("Port of Santos", "Santos → Hamburg" at page/index.html:199, 249, 250), so item 3 must land before the merge and before the screen recording.

## Premises tested (confirmed at source)
| Claim | How I checked | Result |
|---|---|---|
| 0.1333597 XLM per shipment on the fork | `git show origin/landing-v3:proofs/mainnet-rehearsal.json`, per-step fee table | **Confirmed.** Steps 16, 17, 18, 19, 20, 21, 22 sum to 0.1333597. Operator (8 tx) 0.2500726 − second `open` 0.1167129 = 0.1333597. One-time total 13.4727617 confirmed. Exporter's 13.4748967 covers its 7 tx (upload, deploy, add_source, freeze, unfreeze, pause, resume). "Charged" equals the balance decrease, i.e. net of refund. USD 0.0223 at 0.167267 confirmed. The fork is a simulator (soroban-sim, base fee only), as the study says. |
| Same wasm as testnet | script line `WASM_HASH` vs DEPLOYMENTS.md:8 | Confirmed: 8230ed93…1342 in both |
| Mainnet persistent entries start at 120 days | `stellar network settings` on mainnet, 00:01 UTC | Confirmed: `min_persistent_ttl` 2073600 (= 120 d at 5 s), `max_entry_ttl` 3110400 (= 180 d), `ledger_max_tx_count` 2000, close target 5000 ms |
| RPC retention 7.0 days; protocol 29 | `getHealth`, `getVersionInfo`, 00:01 UTC | Confirmed: 120960 ledgers, protocol 29, RPC 29.0.0 (scope: one provider, finding MAINNET 2) |
| soroban-sdk 29.0.1 instance bump extends code | `~/.cargo/registry/.../soroban-sdk-29.0.1/src/storage.rs` | Confirmed verbatim; lib.rs:195-199 calls it on every write |
| SDF hosts no mainnet RPC | developers.stellar.org/docs/data/apis/rpc/providers (WebFetch 00:08 UTC) | Confirmed: SDF rows are Futurenet and Testnet only; 16 providers list mainnet. The page has no explicit sentence saying "SDF does not host mainnet". |
| SDF Horizon one year, "nearing end-of-life" | developers.stellar.org/docs/data | Confirmed verbatim: "The SDF-hosted Horizon keeps one year of history and is nearing end-of-life in favor of RPC." |
| Audit Bank 11–20 weeks, 5% refundable, SCF-gated, STRIDE, partner list | stellar.org Audit Bank page, two reads | Confirmed: match ~2 weeks, schedule 3–6 weeks, audit 2–8 weeks, 5% refundable if critical/high/medium findings are fixed within 20 business days. 2 + 3–6 + 2–8 weeks + 4 weeks = 11–20. Eligibility also needs the project category (finding MAINNET 1). |
| SCF #46 closes 2026-11-08; Build award up to $150K | communityfund.stellar.org/awards | Confirmed |
| Repo private; production page up | logged-out curl, 00:00 UTC | Confirmed: repo 404, production page 200 |
| landing-v3 breach and fake API card | `git show origin/landing-v3:page/index.html` | Confirmed: lines 199, 246, 248–250 |
| A file copy drops README lines; a merge does not | `git diff 3daa78c origin/main -- README.md` (+73), `git merge-tree` | Confirmed: the merge is clean; landing-v3 does not touch README |
| NOTICE lacks three.js, GSAP and Lucide | `git show origin/landing-v3:NOTICE` | Confirmed |
| Other branches carry no port names or secrets (my addition, since every branch becomes public) | `git grep` on landing-v2, three-machine, globe | Clean of port names and secret patterns. `globe` mentions `radox-internal` in 3 files; its deletion is already planned. |
| Benchmark 20/20/17 of 21 | Scout `getHackathon` ×7, 00:03 UTC | Confirmed exactly |
| Deck gaps | PyMuPDF on `deck/radox-custody-rail.pdf` | Confirmed (finding WIN 7) |
| Prior-work gaps | FORM-ANSWERS:107-110, README:168-176, board line 124, PORTAL-PASTE:47, PORTAL-SEEN:7 | Confirmed |

## Strongest contrary cases
- WIN: REVIEW-V13 scored 84.5, and "Now" may be underscored, since judges of an in-person Scale track may weigh the existing mainnet product more heavily. Even if that is true, the action order does not change: gates first, then the Claims fix, then the merge. The study answers this case.
- MAINNET: "skip the Audit Bank and pay for an audit, or run a testnet-only pilot". The study covers the self-paid path (an inferred $15k–$60k, low confidence). With MAINNET finding 1 it becomes a live branch, not a fallback.

## Pre-mortem
- WIN: at 03:00 the video has not started, because 03:00 is the written latest start. The build finishes at 05:30, after the 04:00 upload target, and no fallback cut was prepared in parallel. Pedro then submits at 08:00 with a rushed upload or none, and the required video field fails. Missing check: a 01:30 kill time and a fallback built in parallel (WIN finding 1).
- MAINNET: in three months the team holds an SCF award, but the Audit Bank declines the registry as "not a financial protocol". Phase 2 has no money and the pilot slips by a quarter. Missing check: confirm the category fit before the SCF #46 application (MAINNET finding 1).

## Never-skip checklist
- Library [[id]]s: each cited note was opened for existence and status. All are active and none is stale; the review_by dates of soroban-versions and claims are 2026-11-25. New notes saved: **none**, because this run was limited to one file. Candidates to save: the Audit Bank eligibility category; the soroban-sdk instance+code TTL fact.
- Specialist checklists: done (below).
- Premises tested: 15 (table above).
- Citations that carry the conclusions: opened (table above).
- Key numbers recomputed from the inputs: fees, TTLs, audit weeks, score totals, benchmark counts.
- Contrary case: written. Contradictions searched: across the two studies, and against README, FORM-ANSWERS, deck, board and library (WIN findings 3 and 4, MAINNET finding 6).
- Owner's manual work: listed in both studies. It is feasible apart from the video timing (WIN finding 1).
- Pre-mortem: written.
- Versions: MAINNET has v1→v2, judged against the stated judge using sources. WIN has only v1 and says so ("No independent reviewer ran"); this review is that pass.

## Specialist's checklist audit
- MAINNET, engineer and security: the items are present as claimed. Library saving is marked "not done", which is correct. The multisig medium-threshold point is "documented, not tested", which is correct.
- WIN, researcher: "single-source labelled" is present. "Disconfirming searched" is present. "Library saved" is absent (declared). "Every source dated" is present; the Meridian 2025 blog is undated but is used only for names.
- WIN, product: "behavioural evidence" is absent, declared as the User Value cap. "Accessibility" is absent, deferred to review-4. Both absences are honest.

## Not checked
- The portal itself, which needs Pedro's login.
- The rendered landing-v3 page (I read its source only).
- `cargo test`, `cargo audit` and `npm audit` were not run.
- Whether a GPU actually brute-forces a key in minutes (no hashcat run).
- The SCF Audit Bank rules document linked from the FAQ.
- `team.jpg` and the rejected 20:47 video cut.
- The per-criterion scores themselves: they are judgment, and I can test only their arithmetic.

## Questions for the owner (for the card)
1. Pedro: is the close 10:00 or 12:00 WET? Read it off the portal before 07:00 (WIN finding 4).
2. Leo: may the two README fixes (lines 283 and 305) go in before the repo goes public at 06:00 (WIN finding 3)?
3. Pedro: before SCF #46 (closes 2026-11-08), ask SCF whether the rail counts as a "financial protocol" for the Audit Bank (MAINNET finding 1).

## Library
cited: [[claims-hackmeridian-material-may-and-may-3e4f]] [[hackmeridian-2026-rules-and-submission-requirement-5868]] [[stellar-and-solana-hackathon-winners-no-31ca]] [[horizon-public-history-one-year-and-983a]]
saved: none (run limited to one output file)
