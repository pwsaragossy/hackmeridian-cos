> **Reviewer corrections (REVIEW-STUDIES.md, approve with changes), applied by leo-agent:** (1) the video must START by 01:30 UTC, not 03:00 (2.5 h build → upload by 04:00), with a fallback cut prepared in parallel; (2) the projection from this file's own values is 78.75/100 after the fixes, and ±1 per criterion gives 69–89, not 72–80; the action order does not change; (3) two README fixes before the repo goes public are DONE in rio-miami-rail 78a1060 (code TTL is extended by the instance bump; Audit Bank needs SCF funding in an eligible category); (4) item 11: quote the engineer by role only, unless they approve their name in writing.

---
role: researcher + product (gap ranking)
written: 2026-10-25 23:55 UTC
question: "What is still missing for this project to win the hackathon?"
decision: what the team does in the ~8 h before Pedro submits (target Mon 26 Oct 08:00 UTC; portal closes 12:00 WET = UTC; Pedro's own target 10:00)
judge: HackMeridian Scale panel, 7 criteria scored 1–10, weights 20/20/15/15/10/10/10 [[hackmeridian-rubric-7-criteria-weights-scored-50e2]]
status: read-only study; nothing was edited, committed or pushed in any repo
---

# What is still missing to win HackMeridian 2026 (Scale)

Role: researcher (with the product card for the gap ranking)

**Answer (confidence medium):** the engineering is at a level that can win. The **package** cannot win in its current state. Two required items are missing: the **video** (the 20:47 cut was rejected, so no upload exists) and a **public repo** (`github.com/pwsaragossy/rio-miami-rail` returns 404 logged-out at 23:50 UTC). Either one makes the entry incomplete. Behind those two gates the score is capped by three things. The landing page that will become the video (landing-v3) tells a **Santos → Hamburg** story with a **"Port of Santos"** custodian, which contradicts "First corridor: Rio–Miami" and breaks the Claims guard. The deck has **no product image** and still has a **team-photo placeholder**. User Value has no behavioural evidence.

Projected weighted score on the 1–10 rubric:
- **~67/100** if the two gates are closed as things stand.
- **~77/100 (range 72–80)** after the top fixes below.
- The self-score in IDEA.md was 72, given as a ceiling. REVIEW-V13 gave 84.5, but it judged only the slides.

**Decision threshold used.** If an item moves at least +1 weighted point per hour, or it closes a disqualification gate, it is done before 08:00. Anything else is cut.

---

## 1. Score per criterion: what a judge sees now, and what caps it

Evidence was read on 2026-10-25 between 23:30 and 23:55 UTC:
- deck `deck/radox-custody-rail.pdf` (10 slides, 0.72 MiB, built 20:11);
- README at `origin/main` f76e649;
- landing page at `origin/landing-v3` b42c521;
- production page https://rio-miami-rail.vercel.app (200 logged-out, with llms.txt, robots.txt and sitemap.xml);
- FORM-ANSWERS.md and the board cards.

The "Now" column assumes the repo goes public and some video is attached; without those two, the entry is incomplete. "After" assumes the top 10 gap items in section 3 are done.

| # | Criterion (weight) | IDEA.md self-score (1–5 → %) | Now (1–10) | Evidence a judge sees | What caps it | After fixes |
|---|---|---|---|---|---|---|
| 1 | Ecosystem Alignment (20). Scale is judged here on milestone vs intake, SCF eligibility, production readiness and ecosystem impact [[hackmeridian-rubric-7-criteria-weights-scored-50e2]] | 4 → 80% | **7** | Every intake promise is met on testnet: dual-signed handover, attest, ownership kept, burn [[hackmeridian-scale-intake-as-submitted-the-7fb5]]. The record is token-agnostic and published as an open spec (CUSTODY-SPEC.md, Apache-2.0). README has a "Production path" (SDF Audit Bank, SCF Build) and the US$4B Stellar RWA figure. | The intake's "connected to our API" exists only as "a local development run" of a closed backend, so no judge can reproduce it. Production readiness is testnet only, with no audit and an admin key that cannot be rotated. No live Stellar project is composed (no anchor, wallet or passkey). The promised Stellar-engineer design review has no result recorded. The mainnet-fork rehearsal (40d3c26) sits only on landing-v3 and is not in main or the README. | 8 |
| 2 | User Value & Problem (20) | 3 → 60% | **6** | Sourced pain: 45M bills of lading, ~11% electronic, 22% insider thefts, the R$900M Brazil robbery estimate, US$85M HSBC/Hin Leong, the US$2.5T trade-finance gap. The landing page has a "bank checks who holds the cargo before it pays" beat. | Behavioural evidence of the problem is zero: no interview, pilot or quote (IDEA.md calls it an assumption). "Radox is in conversations with chambers of commerce" cannot be checked by a judge. The beachhead user (financier/buyer) gets no screen of their own. The live page is a shipment log, not a financier's answer. | 7 |
| 3 | Technical Execution (15) | 4 → 80% | **8** | 7 SUCCESS testnet transactions plus 9 simulated refusals. 26 tests (24 unit + 2 seeded property tests). `verify-head` gives MATCH in the CLI and in the browser. The second shipment was signed on teammates' own machines and a multi-company registry ran (proofs/). A threat model table is in the README. A fresh run on Windows passed. | Burn and token admin are closed prior work (`transfer_agent`), and the burn is gated off-chain. No one-command judge check exists yet (Leo's `npm run verify` proposal is not built). The README spends about 4,850 words before any image. | 9 |
| 4 | Innovation (15) | 4 → 80% | **7** | A handover signed by both custodians in one Soroban call, plus a hash-chained `head` and assurance levels. No SEP and no directory project does this [[no-sep-and-no-stellar-project-aa39]], [[physical-goods-rwas-on-stellar-matrixdock-05ea]]. | The primitives are known: multi-party `require_auth` and a hash chain. Novelty rests on a directory search; Kutana (SCF #45) and Trustless Work look adjacent to a judge. The "many supply chains, one rail" idea is the real differentiator, but it appears only as one deck line and one landing scene. | 7–8 |
| 5 | Hackathon Progress (10) | 4 → 80% | **8** | Prior and new work are split clearly in the README, deck slide 8 and the form. First commit 09:00:17. Large output in about 15 h. | Several items are not shown: the Radox design tokens used on the page (see risk R5), the mainnet rehearsal, multi-chain.mjs and CUSTODY-SPEC are missing from the README's "Built at HackMeridian" list. The private-branch API work cannot be inspected. | 9 |
| 6 | Market & Ecosystem Potential (10) | 3 → 60% | **6** | The corridor is sized (US$94.2B US–Brazil, US$6.1B Florida→Brazil). The SWIFT-shaped model is checked against swift.com. The ask is clear. | No pilot, no LOI and no price point. The SWIFT analogy is a goal, not traction. Market has no moment in the video ([[deck-and-video-rules-for-async-8b70]]). | 7 |
| 7 | Product Design & UX (10) | 3 → 60% | **5** | The production page is legible and has Verify MATCH. Landing-v3 (3D globe, scroll scenes, ≤120 words) exists on a branch. | Landing-v3 is not in production. Its story is Santos → Hamburg, with a fake API card (`COFFEE-0042` would return 400 E_CUSTODY_KEY). The deck carries **no product screenshot**: the only images in the PDF are the 4 template images, repeated on every slide. Slide 10 still has a dashed "Team photo" box (deck/REVIEW.md item 2, still open). There is no video. | 8 |
| | **Weighted total** | **72** (ceiling, IDEA.md) | **67.5** | | | **~77.5** |

[INFERENCE] How the totals are computed. Now: 7·20 + 6·20 + 8·15 + 7·15 + 8·10 + 6·10 + 5·10 = 675, i.e. 67.5. After: 8·20 + 7·20 + 9·15 + 7.5·15 + 9·10 + 7·10 + 8·10 = 787, i.e. ~78. A range of ±1 per criterion gives 72–80. These are my judgments, not an outside judge. REVIEW-V13 scored 84.5, but its own note says UX was judged on slides only; I disagree on User Value (8 there, 6 here) because it has no first-hand user.

---

## 2. Competitive benchmark: what comparable winners and funded peers showed

Sources: Raven Scout `getHackathon` / `searchHackathonBuilds` and LumenLoop `get_project`, observed 2026-10-25 23:50–23:52 UTC (community-aggregated sources, DoraHacks-derived). Also the Stellar blog "The Blueprint at Meridian 2025" (undated page; event Sept 2025), read by WebFetch 2026-10-25.

**Pattern across Stellar hackathon winners [FACT, Scout, observed 2026-10-25 23:51 UTC].** I took the top-3 winners of 7 recent Stellar Hacks / Build Better events (Real-World ZK, Agents, ZK Gaming, KALE×Reflector, PaltaLabs, Blend, Build Better; 2025-03 to 2026-07; 21 winners in all):
- **20/21 had a video link**;
- **20/21 had a GitHub link**;
- **17/21 had a live demo URL**.

[INFERENCE] A public repo, a video and a live URL are the minimum that winners clear, not a differentiator. Today we have one of the three (the live URL).

| Comparable (event / programme, date) | What it is | What they showed that we do not (yet) | Source |
|---|---|---|---|
| HackMeridian 2025 winners: The Simple Fund, 4Bridge, Stellar Forge (Open Innovation); Lance, Star Lends, Panorama Block (Composability) | Six finalists pitched on stage; Composability winners built on live protocols (Blend, Soroswap, DeFindex, Kale, Reflector) | The page gives no detail per project, only that the Composability track rewarded plugging into **live ecosystem protocols**. We plug into none. | stellar.org/blog/foundation-news/the-blueprint-at-meridian-2025 (undated); Scout `hackmeridian-2025` (winners-only coverage) |
| Cards402.com, Stellar Hacks: Agents, 1st place (ended 2026-04-13, 249 submissions) | Agent wallets with spend management and "instant real Visa card issuance" | A **real-world output a judge can trigger** (a card is issued), plus repo, demo and video. We show testnet custody only, with no real-world action. | Scout `stellar-agents-x402-stripe-mpp` |
| Wraith / AnchorShield, Stellar Hacks: Real-World ZK, 1st and 2nd place (ended 2026-07-03, 319 submissions) | ZK privacy; ZK proof of KYC and sanctions clearance for anchors | **Load-bearing use of a new Stellar host feature** (ZK, Protocol 25+) plus a compliance story tied to anchors. We use mature Soroban auth only. | Scout `stellar-hacks-zk` |
| Kutana (SCF #45, US$58,200) | B2B trade escrow in USDC on Stellar, released on attested trade events, with embedded insurance and on-chain KYB | A **money flow tied to trade milestones** and insurance partners: the financier's reason to pay. Our rail has no payment leg, by owner decision. | LumenLoop `kutana`, observed 2026-10-25 23:51 UTC |
| Pipeline (SCF #43) | Commodity trade-finance yield, BitGo custody, KYC/AML, 3-of-5 risk council | An **institutional custody partner and governance structure** named in public. | LumenLoop `pipeline`. Source conflict: awarded_total US$84,000 (observed 23:51 UTC) vs US$140,000 in [[no-sep-and-no-stellar-project-aa39]]. Neither figure is used in our public text. |
| Trustless Work (SCF #31 and #41, US$118,000) | Escrow-as-a-service API on Soroban, with a "Trade & B2B" use case | A **developer API others integrate today**. Our API is closed, read-only and runs locally. | LumenLoop `trustless-work` |
| DeFarm (SCF #40, US$90,000), Brazil | Agricultural traceability circuits with selective disclosure | **Multi-organisation data sharing with privacy** (producers, certifiers, government), which judges may see as a substitute for "many supply chains, one rail". | LumenLoop `defarm` |

Organiser guidance [FACT, [[stellar-and-solana-hackathon-winners-no-31ca]], [[deck-and-video-rules-for-async-8b70]]]:
- Stellar Hacks wants "an honest work in progress over a polished mystery" and wants the technology load-bearing.
- Colosseum (an interested party) says the video decides shortlisting: problem and user in the first 20 s, product early, on-chain integration on its own beat.
- The portal states that **AI-assisted pre-judging** reads the submission ([FACT] PORTAL-SEEN.md, Pedro's paste 2026-10-25). [INFERENCE] So the README and llms.txt are read by a machine first. A short "verify in 60 seconds" block at the top of the README is worth more than the length that is already there.

Disconfirming evidence I searched for: Scout found no prize-winning hackathon build matching "logistics", "escrow", "traceability" or "invoice" (winnersOnly, observed 23:50 UTC). This is a whitespace signal, not proof of absence. [INFERENCE] It cuts both ways: no RWA-logistics build is on record as having won a Stellar hackathon, so the panel has no template to reward us against, and the pitch has to make the problem legible on its own.

---

## 3. Gap list, ranked by points per hour (~8 h left; Pedro submits 08:00 UTC)

Points are weighted rubric points (out of 100); "Gate" means the entry is incomplete without the item. Owners: **Pedro**, **Leo**, **Vhendala**, or a named **session**. 🔒 marks an item blocked on Pedro.

| Rank | Item | Owner | Est. time | Points | Exact action | Done when |
|---|---|---|---|---|---|---|
| 1 | **Video exists and is linked** 🔒 (upload) | rail-page-host session builds it; **Pedro** uploads | 2.5 h build + 15 min upload | Gate; +3 UX, and +1–2 on Tech and User Value through the "show it working" beats | Screen-record the **fixed** landing-v3 (item 3 first) with `?film=1`. Then cut the 7 transaction hashes, the explorer handover and the `verify-head` MATCH from the existing clips. Narration in the cloned voice from a new 2:30–3:30 script. Problem and user in the first 20 s; the lower third "Narration: AI voice generated from Pedro's voice". Upload to Pedro's YouTube as public or unlisted. | URL opens logged-out in a private window; length 2:00–4:00; URL pasted in README (2 `{{fill}}`s), FORM-ANSWERS and deck slide 10. Latest start 03:00 UTC. |
| 2 | **Repo public** 🔒 | Pedro (one click); central first deletes the remote `globe` branch | 10 min | Gate (required public repo) | `gh repo edit pwsaragossy/rio-miami-rail --visibility public` after Leo's scrub; the delta scrub at b42c521 is clean except item 3. | `curl -s -o /dev/null -w '%{http_code}' https://github.com/pwsaragossy/rio-miami-rail` returns 200 logged-out, and the README renders. |
| 3 | **Landing-v3 claims and accuracy fix** | page owner (Pedro's session; Vhendala reviews) | 30 min | Avoids a Claims-guard breach; +1 UX; story consistency across all artefacts | In `page/index.html` (v3): replace "coffee leaves Santos for Hamburg" with a Rio → Miami test shipment. Replace `currentCustodian: Port of Santos` with a role ("Port terminal") or the real test-key role. Replace the `COFFEE-0042` / `In transit` / `signed handovers` card with the **real** `GET /api/custody/shipments/<64-hex key>` shape: status `Delivered`, `seq`, route as roles. Add three.js, GSAP and Lucide to `NOTICE` (Leo's 23:43 line). | `grep -i -E "santos\|hamburg\|COFFEE"` returns 0 on page/; the card fields match the README "Closed interfaces" schema; NOTICE lists every file in page/vendor/. |
| 4 | **Merge landing-v3 into main and deploy to production** | rail session | 30 min | +1–2 UX (the judge-facing URL becomes the 3D story) | Use `git merge origin/landing-v3` into main. Do **not** copy files over: landing-v3 is based on 3daa78c, and a file copy drops f76e649's "Closed interfaces" README section (the diff shows −73 README lines). Run the 17 page cases, then `vercel --prod`. | Logged-out production shows v3 with Verify MATCH for both shipments; llms.txt, robots.txt and sitemap.xml return 200; README on main still has "### Closed interfaces this repo uses". |
| 5 | **Deck: real product images, team photo, links** | rail-pitch-deck session; Vhendala supplies `deck/screens/team.jpg` | 45 min | +1 UX, +0.5 Progress | On slide 6 add `screens/shot-page-delivered.png` (or a v3 frame); on slide 5 the explorer handover shot. Put the team photo in, or remove the dashed box. Put the video URL and repo URL on slide 10. Re-run `check_deck.py`. | The PDF has at least 2 non-template images, no "Team photo" placeholder, and is ≤20 MiB; check_deck passes. |
| 6 | **README: 60-second judge path at the top, plus consistency** | rail session (Leo for the verify command) | 45 min | +1 Tech, +0.5 UX, and it helps AI pre-judging | Under the title add a screenshot or GIF and a 4-line "Verify in 60 s" block: live page → Verify head; `npm ci && node scripts/verify-head.mjs <key>`; the explorer link to the first handover; `node scripts/handover-signers.mjs`. If Leo's `npm run verify` (scripts/verify-all.mjs) is ready by 03:00, use it. Rename the H1 "Rio-Miami Rail" to "Radox Custody Rail" (the title everywhere else). Add multi-chain.mjs, CUSTODY-SPEC.md, the threat model and (after the merge) mainnet-rehearsal.mjs to "Built at HackMeridian". | The README's first screen shows the image and the verify block; H1 equals the portal title; every script in `scripts/` appears in "Built at HackMeridian". |
| 7 | **Mainnet-fork rehearsal, worded safely** | Leo | 20 min | +0.5–1 Ecosystem (production readiness) | After the merge, add one README "Production path" line: "Rehearsed the same wasm on a **local fork** of mainnet (soroban-sim); nothing was sent to mainnet; proofs/mainnet-rehearsal.json". Put the same words on deck slide 9 under "Next". | The words "local fork" and "nothing was sent to mainnet" appear next to every mention; nowhere says "deployed on mainnet" about custody_registry. |
| 8 | **Prior-work disclosure completed** | rail session; Pedro pastes | 10 min | Removes a disqualifier risk (R5) | Add to the form's Prior work field and the README: "The page uses Radox's existing design tokens (colours, type) from the Radox app; the explainer video and the voice sample used for the narration clone existed before the event." Deck slide 8 already lists the explainer video. | Form, README and deck list the same prior items. |
| 9 | **Radox API evidence a judge can read** | Leo, or the rail session with API-PROOF.md | 20 min | +0.5 Ecosystem/Progress (the intake's API milestone) | Commit `proofs/radox-api.json`: request, timestamp and response from the 2026-10-25 local run, with head `2d74fec0…5414`, scrubbed of internal names. Link it from the README Architecture section. | The file exists on main and its head equals the `verify-head` output; the scrub grep returns 0. |
| 10 | **Portal dry-run with real lengths** 🔒 | Pedro | 15 min | Protects everything above (paste failures, the Markdown table) | Paste FORM-ANSWERS into the form without submitting and check the char limits of the optional fields. Confirm when editing closes (10:00 or 12:00). | PORTAL-SEEN.md records the limits and close time seen. |
| 11 | Stellar-engineer design review 🔒 (venue, Monday morning) | Pedro | 15 min | +0–1 Ecosystem (an intake success line) | Ask one SDF or Stellar engineer at ONE16 the 3 questions in the engineer brief; quote them only with their OK. | A line on the card with the person's OK, or "not obtained". The README stays silent if it is not obtained. |
| 12 | Pitch "rehearsals" (two timed plays of the final video) | Vhendala | 10 min | 0 judge points (track gate only) | Two logged plays in PITCH-REHEARSALS.md. | Two lines with start, end and length. |
| — | Paulo letter 🔒 | Pedro | — | ≤ +1 (context only, per STATE §6) | Do not wait for it. If it arrives signed before 08:00, quote only its text. | — |

**Cut, under the points-per-hour threshold:** a payment or USD leg (owner said no, 19:18 UTC); a mainnet deploy (owner said no, 14:29 UTC); a new contract feature; a financier dashboard. [INFERENCE] The financier view would lift User Value by about 1 but costs over 3 h, so it is shown only as the landing "Ask. Get the answer." beat.

**Critical path [INFERENCE]:**
- **00:00–00:30** item 3 (page fix).
- **00:30–01:00** item 4 (merge and deploy).
- **01:00–03:30** item 1 (video). Items 5, 6, 7, 8 and 9 run in parallel in other sessions.
- **03:30–04:00** Pedro uploads.
- **05:45** delete `globe`; repo public.
- **06:00** review-4 with logged-out link checks.
- **08:00** Pedro submits.

The buffer to the 10:00 internal close is 2 h.

---

## 4. Risks that could disqualify or cost points

| # | Risk | Severity | Evidence | Control |
|---|---|---|---|---|
| R1 | No video at submission | **Disqualifying** (required field) | STATE 20:57 UTC says the cut was rejected and nothing was uploaded; FORM-ANSWERS line 86 is still a placeholder | Item 1. Fallback by 05:00: upload the best existing cut of the old DEMO-SCRIPT clips (180 s, clips in `~/Movies/hackmeridian-rail-video/`) rather than nothing, and replace it before close if the portal allows edits. |
| R2 | Repo still private, or links that need a login | **Disqualifying** / zero on Tech | The repo returned 404 logged-out at 23:50 UTC. Vercel **preview** URLs need a login (board lines 19:12, 20:48, 21:31). | Item 2. Submit only `rio-miami-rail.vercel.app` (production), never a preview URL. Open every link in a private window at review-4. |
| R3 | Claims-guard breach on the page: a real port named as custodian; a corridor (Santos → Hamburg) that contradicts "Rio–Miami" | High (misrepresentation, terms §05 [[claims-hackmeridian-material-may-and-may-3e4f]]; an inconsistency judges notice) | landing-v3 b42c521 `page/index.html` lines 199, 246–250 | Item 3, before merge and before the video records it. |
| R4 | Mismatches across artefacts | Medium (credibility) | README H1 "Rio-Miami Rail" vs title "Radox Custody Rail"; deck "24 unit tests" vs README/form "26 tests (24 unit + 2 property)"; Vhendala is "supervision and product review" (README) vs "QA and product review" (deck); the deck (20:11) predates v3 and the mainnet rehearsal; the video will show v3 | Item 6 plus one consistency grep at review-4: title, test count, team roles, corridor, tx hashes. |
| R5 | Incomplete prior-work disclosure ("any code, designs, or assets that existed before the event", PORTAL-SEEN.md) | High (undisclosed prior work disqualifies, PORTAL-PASTE) | The page uses Radox's design tokens taken from the closed `radox-internal` `frontend/src/index.css` (board 20:53 UTC). The voice clone was built from Pedro's earlier video. Neither is in the form's Prior work field. | Item 8. |
| R6 | "Mainnet" misread | Medium | proofs/mainnet-rehearsal.json and "13.73 XLM in fees" (commit 40d3c26) were run on a local fork | Item 7 wording. |
| R7 | AI attribution gaps | Medium (the AI line is required) | The form names the models, Voicebox and the plugin; AI_USAGE.md gained a row on v3. The landing-v3 vendored files and any v3-specific AI work must be in AI_USAGE.md after the merge. | Re-run the AI_USAGE row check at review-4 (every file in page/ has a row). |
| R8 | An unverifiable membership claim ("Radox is part of the Rio–Miami trade-corridor initiative and its technology rail") | Low–medium, accepted by the owner 20:12 UTC | README Future, deck slide 4, form | Not raised again per the owner. Noted only: a judge may discount it, since it carries no name. No partner, port, airport or chamber name may be added anywhere. |
| R9 | The submit window closes early (10:00 vs 12:00) | Medium | [[hackmeridian-2026-rules-and-submission-requirement-5868]] vs PORTAL-SEEN.md | Submit at 08:00 as planned; item 10 confirms the close time. |
| R10 | Presence rule (in person only) | Low, unconfirmed | [[hackmeridian-is-in-person-only-on-d6b2]] | Unchanged; Pedro is at the venue. |
| R11 | The history names `radox-internal` (commit 67c2b13) once the repo is public | Low, accepted by the owner 19:17 UTC | STATE §3 | No action. |

---

## 5. How we win (thesis)

[INFERENCE] We win by being the only entry where a judge can watch goods change hands, see that both companies had to sign, and check the record themselves in under a minute without trusting us. The landing film carries the claim visually: one corridor, Rio–Miami, end to end. The video shows the real testnet transactions and a MATCH. The README's first screen lets an AI pre-judge or a human reproduce the MATCH with one command.

That converts our real strength into points on the two 20-weight criteria. The strength is Technical Execution and Progress: 7 transactions, 26 tests, own-key and multi-company proofs, a threat model, an open spec. The two criteria are Ecosystem (an open, token-agnostic Stellar primitive with a stated mainnet path) and User Value (the "bank checks who holds the cargo before paying" moment).

What loses is a package that is incomplete or inconsistent: no video, a private repo, a Santos→Hamburg page with a named port, or a deck with no product in it. Those are cheap to fix tonight and costly to leave. Nothing in this plan adds a partner name, a user claim or a revenue claim.

---

## What would change the conclusion
- A signed Paulo letter, or an engineer's quotable review, moves User Value or Ecosystem by about +1 each, which is about +2–4 weighted. That is not enough to change the plan order.
- If the portal accepts edits after submission until 12:00 (PORTAL-SEEN says so), a placeholder-video early submit becomes a valid safety net. The owner decided at 18:26 not to submit early, so this stays a note.
- If organisers reject a Scale repo without the closed backend, cut the API claims to "design" (STATE §6).

## Never-skip checklist (researcher)
- [x] Library claims cite their [[id]]. **New findings were not saved with library.sh**, because the caller limited output to one file. To save next session: the winner-artefact pattern (20/20/17 of 21) and the Pipeline SCF amount conflict.
- [x] Decision and threshold written before searching (header, and "Decision threshold used").
- [x] Decision-driving numbers: the winner-artefact count is single-source (Scout, DoraHacks-derived), labelled. Rubric weights come from two sources ([[hackmeridian-rubric-7-criteria-weights-scored-50e2]]).
- [x] Every source is dated; the Meridian 2025 blog page is undated (event date given) and supports only the winner names.
- [x] Disconfirming evidence searched (no logistics, escrow, traceability or invoice winners; my score is below REVIEW-V13's and I say why).
- [ ] Market-size ranges: not applicable (no sizing in this study; market figures were reused from reviewed notes).
- [x] Definitions consistent (scale 1–10, weighted to 100).
- [x] "Not found" scoped to Scout winnersOnly and LumenLoop.
- [x] Interested parties marked (Colosseum organiser guidance; DoraHacks-derived data).
- [x] Library searched first (13 notes read).

## Never-skip checklist (product)
- [x] Library claims cited; new findings not saved (see above).
- [x] Target user in behavioural terms: a financier or buyer paying against goods in transit (IDEA.md). Access path: the deck ask (one financial institution).
- [ ] Behavioural evidence of the problem: **none exists**. This is the User Value cap, stated in section 1.
- [x] Existing alternative: bill of lading plus carrier tracking plus surveyor (IDEA.md). Its cost is not sourced.
- [x] Scope out: payment leg, mainnet deploy, new contract features, financier dashboard (section 3, "Cut").
- [x] Empty, loading and error states: the page already has a "Snapshot, not live" fallback and a loading line (v3 `#source`). The video fallback is in R1.
- [x] Effort estimates: unvalidated, mine; each owner confirms.
- [x] Success metric: weighted score 67.5 → about 77.5 by 08:00. Kill criterion: if the video has not started by 03:00, use the R1 fallback.
- [ ] Accessibility: not re-checked here (DESIGN-REVIEW-V3 has a contrast and keyboard table); review-4 must run it on the merged v3.
- [x] Riskiest assumption named (custodians would co-sign). It cannot be tested before 08:00; the cheapest test is one mentor question at the venue.

## Not checked
- The portal itself (needs Pedro's login).
- The current landing-v3 preview, rendered: I read the source only.
- The content of the rejected 20:47 video cut.
- Whether `team.jpg` exists on Vhendala's machine.
- Detail pages of HackMeridian 2025 winners: the coverage is winners-only.

## Open questions for the owner (card)
1. Who builds the video from v3 tonight, and by when does Pedro upload? Latest 04:00 UTC.
2. Should the Prior work field add "Radox design tokens; the voice sample's source video"? (R5)
3. Should v3's example corridor be Rio → Miami? It is needed for consistency with the title, deck and README.

## Library
cited: [[hackmeridian-rubric-7-criteria-weights-scored-50e2]] [[claims-hackmeridian-material-may-and-may-3e4f]] [[no-sep-and-no-stellar-project-aa39]] [[product-framing-rio-miami-is-the-34f9]] [[stellar-and-solana-hackathon-winners-no-31ca]] [[hackmeridian-2026-rules-and-submission-requirement-5868]] [[hackmeridian-scale-intake-as-submitted-the-7fb5]] [[hackmeridian-thematic-tracks-stellar-unlocked-or-158c]] [[physical-goods-rwas-on-stellar-matrixdock-05ea]] [[zis-in-public-material-radox-is-bc05]] [[deck-and-video-rules-for-async-8b70]] [[no-text-says-a-hackmeridian-scale-7074]] [[hackmeridian-is-in-person-only-on-d6b2]]
saved: none (caller allowed one output file only)

## Versions
- v1, 2026-10-25 23:55 UTC: first full pass. Outside judges run: Scout and LumenLoop live data; logged-out curl of the production page and repo; git refs of rio-miami-rail (local refs equal `ls-remote`). No independent reviewer ran on this study; review-4 should attack section 1's scores.

### Researcher never-skip (verbatim list)
- [ ] Every claim taken from the library cites its [[id]]; every new finding was saved with library.sh new, and similar notes were retired, merged or marked coexists.
- [ ] Decision and threshold written down before searching.
- [ ] Every decision-driving number has two independent sources or is labeled single-source.
- [ ] Every source carries a publication date; nothing undated supports a conclusion.
- [ ] Disconfirming evidence was searched for and the result reported (even "none found, searched X, Y").
- [ ] Market-size inputs are ranged (low/base/high) and the most sensitive input is named.
- [ ] Definitions are consistent across sources (users vs paying users, revenue vs bookings, region, year, currency).
- [ ] "Not found" is reported as "not found in <where I looked>", never as "does not exist".
- [ ] Vendor-produced and advocacy statistics are marked as interested parties.
- [ ] Library searched first; new reusable findings saved.

### Product never-skip (verbatim list)
- [ ] Every claim taken from the library cites its [[id]]; every new finding was saved with library.sh new, and similar notes were retired, merged or marked coexists.
- [ ] The target user is named in behavioral terms, and a count or access path to them exists.
- [ ] The problem has at least one evidence type that is behavior (not just stated opinion).
- [ ] The existing alternative, including "do nothing", is described with its cost.
- [ ] Scope states what is explicitly out.
- [ ] Empty, loading, error and first-use states are specified, not only the happy path.
- [ ] Effort is estimated by someone who will build it, or marked "unvalidated estimate".
- [ ] Success metric has a baseline, a target and a date; a kill criterion is written.
- [ ] Accessibility basics checked: contrast, keyboard or touch target size, text alternatives, not color alone.
- [ ] Riskiest assumption identified with the cheapest test for it.
