Role: reviewer
Reviewing: deck v13 "Radox Custody Rail" (10 slides, deck/radox-custody-rail.pptx + PDF), spoken pitch v13 (PITCH-FINAL.md), and the outputs PRODUCT-VALUE-ECOSYSTEM.md (product), COPY-V13.md (marketing), RESEARCH-VALUE-ECOSYSTEM.md (researcher). Date 2026-10-25. No project file was edited.
Verdict: approve with changes
Reason: every number re-opens at its source and check_deck exits 0, but two sentences read as more than the owner said or the proof shows, check_deck lets four false-claim shapes through, and slide 2 has a render collision.

Question: can v13 reach 9+ on User Value and Ecosystem under the owner rule, with every sentence surviving diligence? Conclusion: Ecosystem yes (9); User Value is 8, 9 only with a first-hand user fact the deck cannot truthfully invent.

## Findings (ranked by severity)

1. [major] Slide 4 and pitch: "their legacy systems will join through one adapter to the Radox API". "Their" attaches the future to the ports, airports and chambers named in the previous clause, so a judge reads a commitment by those parties. Owner's words ("abertura com vários") support openness, not that their systems will join. [FACT] (slide 4 bottom text; pitch paragraph 2). Fix: delete "their". Slide: "Each company integrates once instead of pair by pair. Radox is in conversations with ports, airports and chambers of commerce; legacy systems will join through one adapter to the Radox API." Pitch: "...chambers of commerce, and legacy systems will join through one adapter to the Radox API." (pitch becomes 394 words). Confidence high.

2. [major] check_deck guard gaps. Mutants run on a scratch copy (/private/tmp/claude-501/.../scratchpad/rev-mut/): "Two ports have signed with Radox" FAILS (good); "live on mainnet / real keys" FAILS (good). But "A bank signed a letter of intent with Radox", "The Port of Santos signed on to the rail", "The lifecycle ran on mainnet" and "Radox has paying clients in three ports" all EXIT 0. The judge asked for a signed-partner mutant to fail: it does only in the "ports have signed" shape. [FACT] (rev-mut/*/, exit codes). Fix (add to check_deck, none hits the current deck, tested against its text): `\b(?:ran|runs|running|live|deployed|settled|operat\w+)\b[^.;]{0,40}\bmainnet`; `\b(?:port|bank|airport|chamber|carrier)\b[^.;]{0,40}\b(?:signed|agreed|committed|joined)\b`; `\b(?:signed|agreed|committed)\s+(?:a|an|the)?\s*(?:letter|loi|mou|contract|agreement|deal|pilot)`; `\b(?:paying|our|first|signed)\s+clients?\b`. Do not use bare "paying": slide 3 says "before paying". Also the "testnet" requirement only checks the word exists somewhere. Confidence high (reproduced).

3. [major] Slide 8: "Radox API reads the registry, read-only: same head (testnet)". API-PROOF.md says the full Radox backend did NOT boot (dev database behind by migrations); the real route module `custodyRoutes.js` was mounted in a throwaway express host, real testnet RPC, and the `app.js` mount "was not exercised in a full boot". A judge who opens API-PROOF.md will see this. The sentence is true of the route, not of the running API. [FACT] (API-PROOF.md "How it was served"). Fix: "Radox API custody route reads the registry, read-only: same head (testnet)". Same wording in spoken pitch if it appears (it does not today). Confidence high.

4. [minor] Slide 9: "Borrows the shape of Swift's published fees: entry, annual, per-message usage". The Swift billing-rules page I opened publishes the structure (entry fees, annual charges, network usage charges) and the invoicing rules, with no amounts anywhere on it. "Published fees" invites "show me the price list". Fix: "Borrows the shape of Swift's billing rules: entry, annual, per-message usage. Not affiliated with Swift." Footnote 6 already says "billing rules". [FACT] (browser read of the page, 25 Oct). Confidence high.

5. [minor] Slide 2 render: the last line of the "Context:" paragraph ("is its custody layer.") sits on the divider rule; slide 7 last line ("onboarding to delivery.") touches the footer text. [FACT] (s-02.png, s-07.png). Fix: slide 2 shorten to "Context: our explainer video on a Rio–Miami trade-corridor initiative; this project is its custody layer." (one line, no banned token; it keeps the unnamed bridge). Slide 7: drop "end to end" from "Radox will open API access to them, end to end." only if the line still wraps to three lines at 18 pt; otherwise move the box up 0.15 in.

6. [minor] "Radox is in conversations with ports, airports and chambers of commerce" vs the owner's words ("tem abertura com vários" ports and airports; chambers "abrindo a porta"). "Abertura" = access or receptiveness; "in conversations" says a dialogue took place. It is a fair rendering only if the owner has actually spoken with at least one of each type. It does not read as a signed partnership: no names, no "agreed/partner/signed", and the ask on the same deck is for introductions to one institution and one port, which is consistent with no deal. check_deck's own rule allows it. If the owner cannot say "yes, I spoke with each type", the literal true line is: "Radox has openings with ports and airports, and chambers of commerce are opening doors." [SUSPICION] on the factual match (his claim, not checkable by me); [FACT] on the not-signed reading. Goes to the owner as a question.

7. [minor] Slide 4 column headed "RADOX OPERATES · CLIENT PAYS" with "Onboarding, issuance controls, operation of the rail" in present tense. Everything runs on testnet and the deck correctly claims no clients, so a present-tense "operates / client pays" next to it can be read as existing clients. Fix (roadmap with confidence, still true): "RADOX WILL OPERATE · CLIENT PAYS" and "— Onboarding, issuance controls, operation of the rail" unchanged. check_deck unaffected.

8. [minor] Slide 2 "45M ocean bills of lading issued a year / DCSA, Feb 2023 (2021 data)". The DCSA press release (15 Feb 2023) gives "around 45 million" with no data year; "2021 data" belongs to the 1.2% figure beside it in PROBLEM-NUMBERS.md. Fix: "DCSA, Feb 2023". [FACT] (release text as fetched; PROBLEM-NUMBERS.md row 1).

9. [note] Slide 7 "Nearest neighbours": the researcher's own list (RESEARCH B7, no-sep note) has AgTrail (SCF #38, end-to-end supply chain tracking) and DeFarm as closer in spirit than Pipeline. "None records a handover signed by two custodians" is scoped to the three named, and the pitch scopes it ("We found no Stellar project..."). Defensible, but a judge may name AgTrail. Optional: add "AgTrail tracks supply chains with IoT and QR" before "None records".

10. [note] Specialist process: the researcher's Versions say "no outside judge ran"; marketing's v3/v4 judge is "my regex reading". Under the reviewer card these verdicts are opinion, not outside judges. This review supplies the run (check_deck) and the mutants; I did not rerun product's rubric predictions.

11. [note] SDF figure vs rwa.xyz: deck says "about US$4B (SDF, as of 1 Sep 2026)"; rwa.xyz showed US$3.75B on 25 Oct. Never mixed in one claim, labelled by date and source. Fine; be ready for the question.

## Source re-opening (task item 1)

| Claim | Opened | Passage | Matches | Date |
|---|---|---|---|---|
| World Bank via IAPH, over 90% | yes, sustainableworldports.org/?p=10830 | "Over 90 percent of the ports in low- and middle-income countries have not yet implemented these PCS platforms." Speaker Sebastien Dessus, World Bank, IAPH 2023 World Ports Conference | Yes. The deck's "have no port community system" = "not yet implemented"; label "remark relayed by IAPH" is exact (a spoken remark, not the report) | 1 Nov 2023 |
| IMO FAL.5/Circ.54 | yes, PDF downloaded, text extracted | 8.4.3 Legacy System Integration: "When legacy systems with proprietary data formats and interfaces exist, at the early stages of the PCS introduction, some data format/interface conversion services should be considered." | Yes. Deck: "IMO guidance plans for legacy systems with proprietary formats" is a fair short form | 25 Apr 2024 (circular), 34 pages |
| SDF US$4B | yes, stellar.org/solutions/real-world-assets | "4 billion dollars in tokenized real-world assets, as of September 1, 2026" | Yes (deck drops "real-world"; says "tokenized assets"; harmless) | as of 1 Sep 2026 |
| Swift billing shape | yes, built-in browser (WebFetch got 403) | "Entry fees are invoiced after receipt of the Swift Undertaking." "Annual charges (including Swift BIC costs, network connection costs, software maintenance, documentation subscriptions) ... invoiced in January of each year." "network usage part (message transmission traffic)" | Shape yes; "published fees" no (finding 4); no amounts on the page | undated, FX table to Sep 2026 |
| DCSA 45M | yes, DCSA release | "Ocean carriers issue around 45 million bills of lading a year." | Yes; no data year (finding 8) | 15 Feb 2023 |
| DCSA ~11% | yes, dcsa.org soft-barriers article | "As of 2025, around 11% of bills of lading are issued electronically." | Yes; page undated | as of 2025 |
| TT Club/BSI 22% | yes, BSI press release | "more than a fifth (22%) of global cargo theft incidents involved the cooperation of insiders." 2025 Cargo Theft Report | Yes. Deck "of recorded cargo thefts in 2025 involved insiders" fine | 21 Apr 2026 |

Not re-opened by me (earlier rounds only): R$900M (NTC), US$85M (GTR), US$2.5T (ADB), US$94.2B, US$6.1B, US$26.26T, ~80% by sea. Say so; do not treat as verified by this review.

## Sentence-by-sentence against the owner rule

- Hedges: none left that the check lists; check_deck HEDGES pass. Remaining qualifiers are precision, not lowballing, and should stay: "(simulated)" on the 9 refused calls (they are simulations in lifecycle.json: `hash_or_sim: simulation`), "Radox policy, not enforced on-chain" on the burn, "Not affiliated with Swift", testnet / test keys.
- Partner or deal implied: only finding 1 (and 7 mildly). "Radox is in conversations" alone: no. Slide 10 team is the team, not partners.
- Testnet labels: slide 1 pill, 5 "built on testnet, test keys", 6 "Testnet, test keys", 8 "(testnet)", 9 "Now running on testnet, test keys", 10 not needed. Mainnet appears only for the three prior Radox contracts (slides 8, 10) and as a "Next" item (9). No testnet-as-mainnet claim found.
- Proofs: lifecycle.json network testnet; contract CCBJVXMJ...H4LII on slide 6 matches; 7 hashes match slide 6 and `hash[:8]`; 9 failures; final head 2d74fec0...5414; three-machine.json: "leo and vhendala signed their entries on their own computers" supports "handovers signed from separate computers" (named team, not third parties); multi-chain.json has two opens, two delivers, handovers for two shipments, supports "two test companies' chains on one registry" (the "sharing stops" detail I did not decode). 24 unit tests: README line 79 (README also counts 2 property tests; deck says "24 unit tests", true). First repo commit d10cb84 at 2026-10-25 09:00:17 UTC: slide 8 true.
- Required disclosures present: prior work (3 contracts on mainnet, public since 2026-08-19, slide 8), AI attribution (slides 8, 10), testnet. Ask on slide 9 unchanged and not reviewed for change.
- Banned third parties: no ZIS, Paulo, mentors, partners in the deck text (check_deck passes). The unnamed "trade-corridor initiative" in the Context line is a third party described but not named; allowed by the ZIS note, stays as the owner's bridge.

## check_deck and mutants (task item 3)

- `check_deck.py lifecycle.json` in the project folder: `slides=10 pdf_bytes=759395 failures=0`, exit 0.
- Mutants (copies of pptx, pdf and check_deck in rev-mut/, pdf touched newer; real deck untouched):

| Mutant | Edit | Result |
|---|---|---|
| signed_ports | slide 4 sentence -> "Two ports have signed with Radox" | exit 1 "reads as a signed partner" (required fail: yes) |
| mainnet_live | slide 1 pill -> "LIVE ON MAINNET · REAL KEYS" | exit 1 banned live-on-mainnet |
| signed_bank | "A bank signed a letter of intent with Radox" | exit 0 (escape) |
| santos_signed | "The Port of Santos signed on to the rail" | exit 0 (escape) |
| mainnet_run | slide 6 title -> "The lifecycle ran on mainnet" | exit 0 (escape) |
| customers | "Radox has paying clients in three ports" | exit 0 (escape) |

The two required mutants fail in their cheapest shapes; the escapes are finding 2.

## Scores for v13 (CRITERIA.md; weights 20/20/15/15/10/10/10, sum 100; scale 1–10)

| Criterion | Weight | Score | Product |
|---|---|---|---|
| Ecosystem Alignment | 20 | 9 | 180 |
| User Value and Problem | 20 | 8 | 160 |
| Technical Execution | 15 | 9 | 135 |
| Innovation | 15 | 8 | 120 |
| Hackathon Progress | 10 | 9 | 90 |
| Market and Ecosystem Potential | 10 | 8 | 80 |
| Product Design and UX | 10 | 8 | 80 |

Total 845 / 100 weight = 84.5 of 100 (8.45 on the 10 scale). I recomputed the weights from CRITERIA.md; they sum to 100. UX is provisional: I judged the 10 slides, not the public shipment page. The rubric scale conflict (1–5 vs 1–10) in CRITERIA.md is unresolved; ratios hold either way.

Reasons: Ecosystem 9 because the token-agnostic property is in code, the SDF size is sourced, the neighbour search is dated, Apache-2.0 and the API route are stated; no adopter exists, which is the only gap to 10. User Value 8: real, sourced pain (45M, 11%, 22%, US$85M, legacy systems with IMO text); no first-hand user.

Exact change toward 9 on User Value (no false statement needed): slide 2, replace the one-line "The gap:" with two lines that name who feels it and what it costs, using only sourced facts: "The gap: each company records only its own leg, and no shared record follows the goods. A financier pays before it can see who holds them; HSBC lost US$85M on oil trades that never happened (slide 3)." Then make findings 1 and 5 so slide 2 does not overflow. This moves the pain from "market sizing" to "named buyer behaviour", worth about half a point at best. The other half point needs one real user fact, which only the owner can supply (his question 4 in PRODUCT: a one-line written "we spoke" from one port or chamber). I do not claim 9 on User Value without it. For Ecosystem to stay at 9: apply findings 1, 3 and 4 (they are the diligence-fail points a judge would find in the repo).

## Pitch recount (task item 5)

Words counted by `wc -w` on the v13 text (paragraph "A container leaves Rio..." through "...Thank you."): 395. Limit 396, passes by 1. After finding 1 (delete "their"): 394. At 2.2 words a second this is 179 seconds; rehearsal timing by Pedro still pending, as the file says. Spoken facts check: DCSA 45M and 11%, TT Club/BSI 22% in 2025, SDF 4B ("the Stellar Development Foundation says"), seven transactions, nine refused, 24 tests, Radox with three Soroban contracts on mainnet: all agree with sources and proofs. "AI coding agents wrote the code" is consistent with the disclosure.

## Premises tested

| Premise | Evidence | Result |
|---|---|---|
| Every cited number re-opens | 7 sources opened (table above) | holds; two wording fixes |
| Hash and contract facts on slides match proofs | lifecycle.json compared with check_deck (exit 0) and slide 6 | holds |
| "In conversations" is not read as a signed partner | slide text, regex, ask on slide 9 | holds, subject to owner confirming the conversations |
| Radox API reads the registry | API-PROOF.md | partly: route yes, full backend no (finding 3) |
| check_deck blocks false claims | 6 mutants | partly (finding 2) |
| Prior-work disclosure and first commit time | git log d10cb84 09:00:17Z | holds |

## Consider the opposite

Strongest contrary case: removing the hedges raised the overclaim surface. "Will use", "will join", "Radox operates / client pays" and "in conversations" are all adoption language with no adopter; the earlier hedged deck was less exposed in diligence, and a judge scoring User Value at 9 wants evidence, which the hedges at least labelled honestly. The output answers it only partly: the false-statement line holds (no partner, deal, user, revenue, mainnet), but findings 1, 3 and 7 are exactly where confidence outruns proof. After the fixes the deck states only what is proven (testnet, code, sources) or planned in the future tense, which is what the owner asked.

## Pre-mortem

Failure story: a judge asks in Q&A or opens the repo: "which ports?" and "is the Radox API running?". The founder cannot name one; API-PROOF.md says the backend did not boot; the deck said "Radox API reads the registry" and "their legacy systems will join". Trust in every sentence drops, including the true ones, and User Value falls to 6–7. Missing control: findings 1 and 3 fixed, plus one rehearsed true answer for "which ports" (the kind of conversation, not names).

## Never-skip checklist (reviewer card)

- Library cites, new finding saved with Compared: done ([[check-deck-evasions-signed-bank-or-3570]]; its Compared lines are coexists with two notes, each a valid separate subject).
- Specialist Never-skip lists checked item by item: done (below).
- At least three premises tested: done (six).
- Every citation that carries the conclusion opened: done, 7 of 7 (Swift via browser; IMO via the PDF itself).
- Key numbers recomputed: done (weights 20+20+15+15+10+10+10 = 100; total 845/100; pitch 395 words; 7 hashes and contract against the proof JSON).
- Strongest contrary case written: done.
- Contradictions with library and other specialists: done. Product said "none signed, none named, none confirmed" and "per the founder" labels (superseded by [[founder-voice-in-public-text-sell-d820]]); marketing removed them, consistent with the owner rule. Researcher said do not write "90% of ports" without the income-group limit; the deck complies.
- Every cited note opened; retire/merge judged: done. The owner-rule note says it supersedes the hedge parts of [[founder-statements-in-the-deck-open-89a2]]; that note carries a "Superseded in part" line. No retire needed. [[world-bank-and-iaph-port-community-6ec0]] is at confidence low but its quote is now confirmed at the primary page; raise it at its next edit (not done: not my note).
- Owner's manual work listed and feasible: done (questions below; each is one line).
- Pre-mortem with top failure story: done.
- Specialist Versions exist and verdicts come from an outside judge: absent for researcher (self-declared) and marketing (own regex reading); present with a rubric judge for product. This review adds the run. Last version reaches past the request without growing scope: marketing yes (form wording), product yes.
- Each finding has severity and evidence: done.

## Specialist's checklist audit

- Product card: target user, alternative, out-of-scope, riskiest assumption, accessibility: present. "Problem has behavior evidence" and "success metric" left unchecked by product itself and still open (honest). Product's UV prediction 8 and Ecosystem 9 match mine.
- Marketing card: numeric goal, funnel, unit economics, channels, tracking: declared not applicable (deck and form copy); I accept that. Every claim has proof or label: present (table, one gap: IAPH quote was not re-opened by marketing; I did). "Jurisdiction/endorsement": present.
- Researcher card: quotes with URL, date and interested party: present. Outside-judge versions: only claimed (self-declared). Not-found items stated: present.

## Not checked

- Whether the owner actually has the conversations described (his statement; not checkable).
- R$900M, US$85M, US$2.5T, US$94.2B, US$6.1B, US$26.26T and the UNCTAD ~80%: not re-opened this round.
- Public shipment page, the video, the README "Production path": not opened; UX score provisional.
- "Sharing stops" detail in multi-chain.json: not decoded.
- Ask on slide 9: locked, not reviewed for change; I made no proposal on it.
- This review is the same model with a different brief and gives no legal authority. The statements about conversations with ports and chambers, and any regulated-asset wording, are for the owner and counsel.

## Questions for the owner (to go on the project card)

1. Can you say aloud, in Q&A, that you have spoken with at least one port or airport and one chamber of commerce? If not, switch the slide 4 line to "Radox has openings with ports and airports, and chambers of commerce are opening doors."
2. Do you accept "RADOX WILL OPERATE · CLIENT PAYS" (finding 7)?
3. Will you add check_deck patterns of finding 2 (the project agent will do it on your yes)?
4. For User Value 9: can one port or chamber give a one-line written "yes, we spoke", with permission to say "one port"?

## Versions

- v1, lens "attack the premises" (open every source, run every proof): judge = the seven sources and the proof JSON. Verdict: numbers hold, two wording gaps (findings 4, 8), one proof overstatement (finding 3).
- v2, lens "outside judge on the guard" (mutants against check_deck): judge = exit codes of 6 mutants. Verdict: required two fail; four false-claim shapes escape (finding 2).
- v3, lens "hostile judge reading the owner's words": judge = owner's verbatim phrases against slide 4 and the pitch. Verdict: "in conversations" passes as not-signed; "their ... will join" fails (finding 1).
- v4, lens "who does this work and what is the next 0.5 point" (past the request, scope unchanged): judge = recomputed weights (845/100) and the criterion table. Verdict: Ecosystem 9 holds after findings 1, 3, 4; User Value stays 8 until one first-hand user fact exists (question 4).

## Library
cited: [[world-bank-and-iaph-port-community-6ec0]] [[stellar-tokenized-rwa-size-on-2026-a455]] [[no-sep-and-no-stellar-project-aa39]] [[founder-voice-in-public-text-sell-d820]] [[founder-statements-in-the-deck-open-89a2]] [[swift-fee-structure-on-swift-com-9ed6]] [[wording-the-rio-miami-deck-readme-ef38]] [[zis-in-public-material-radox-is-bc05]] [[multi-company-chain-proof-on-testnet-672b]]
saved: [[check-deck-evasions-signed-bank-or-3570]]
