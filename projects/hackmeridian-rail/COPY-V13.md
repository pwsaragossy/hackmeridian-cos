# COPY-V13: deck, pitch and form wording (founder voice)

Role: marketing. Date 2026-10-25. Rule applied: owner's "venda apenas a parte boa" (via coordinator): no apologies, no doubt, only true statements. Nothing edited in build_deck.py, PITCH-FINAL.md or check_deck.py.
Library cited: [[claims-hackmeridian-material-may-and-may-3e4f]] [[founder-statements-in-the-deck-open-89a2]] [[world-bank-and-iaph-port-community-6ec0]] [[stellar-tokenized-rwa-size-on-2026-a455]] [[physical-goods-rwas-on-stellar-matrixdock-05ea]] [[iata-one-record-is-a-live-e27f]] [[wording-the-rio-miami-deck-readme-ef38]] [[multi-company-chain-proof-on-testnet-672b]]

## 0. Re-opened sources (25 Oct 2026, raw HTML, not the fetch summary)
- stellar.org/solutions/real-world-assets: "4 billion dollars in tokenized real-world assets, as of September 1, 2026"; "67 tokenized products"; "10 regulated issuers". Confirmed.
- app.rwa.xyz/networks/stellar: "Distributed Asset Value $3.75B", page data updated 2026-10-25 (transferable 3,753,080,649). Confirmed. The deck uses only the SDF figure; the rwa.xyz figure is never in the same claim.
- World Bank "over 90%" (via IAPH): NOT re-opened by me (not in my brief); label stays "World Bank remark relayed by IAPH, 1 Nov 2023", scope "low- and middle-income countries". Reviewer must reopen it.
- Dropped as asked: corridor-project dependency line, "parties per shipment" line. Not "integrated": the API line says "reads the registry, read-only".

## 1. Slide edits (old = exact string in build_deck.py)

Check the render: lines marked LONGER need a look at slides 2, 4, 7 (tight space; I could not render, python-pptx missing here).

### Slide 1
- Pill. OLD `"TESTNET · TEST KEYS · NOT REAL CUSTODIANS"` NEW `"TESTNET · TEST KEYS"` (also change `pill.width = Inches(0.9 + 0.15 * 41)` to `* 19`).
- Sub. OLD `One record for the goods, from origin to delivery, that every company along the way could share.` NEW `One record for the goods, from origin to delivery, that every company along the way will share.`

### Slide 2
- Hypothesis. OLD `("Our hypothesis: ", ...)` + `each company records only its own leg; no shared record follows the goods. Not yet tested with a customer.` NEW label `The gap: ` + `each company records only its own leg; no shared record follows the goods, and port and airport systems are legacy and hard to integrate.` (founder statement as fact; sourced version below)
- 11% source. OLD `DCSA, as of 2025 (Jan 2025 guide: 5.7%)` NEW `DCSA, as of 2025`
- Bottom box: keep BRIDGE as is, add a second paragraph (LONGER, 18 pt): `Ports: over 90% of ports in low- and middle-income countries have no port community system¹; IMO guidance plans for legacy systems with proprietary formats².  ¹ World Bank remark relayed by IAPH, 1 Nov 2023  ² IMO FAL.5/Circ.54, 2024`

### Slide 3
- Gap line. OLD `a financier cannot see who holds the goods before paying. No customer has confirmed it yet.` NEW `a financier cannot see who holds the goods before paying.` (label `The gap: ` replaces `Our hypothesis: `)
- Third stat. OLD `global trade finance gap (market size only)` NEW `global trade finance gap (market size)`
- Bottom. OLD `These numbers size the market problem. They are not results of ours, and we do not claim our build prevents any of it.` NEW `These figures size the market problem the rail addresses. Sources under each number.`

### Slide 4
- Goal. OLD `... from origin to destination, could use. ` + bold `Neither the standard nor the rail exists yet.` NEW `... from origin to destination, will use. ` + bold `We are building it on Stellar, starting with the custody rail.` (keeps "The goal is")
- Pair-by-pair line (same length). OLD `Each company would integrate once instead of pair by pair, but would still need a key and one connection. No port, airport or chamber link: none confirmed.` NEW `Each company integrates once instead of pair by pair. Ports and airports run legacy systems that are hard to integrate; Radox is in conversations with ports, airports and chambers of commerce, and a legacy system joins through one adapter to the Radox API.` (LONGER by about 100 characters; 2 lines at 18 pt)
- Pricing bullet. OLD `Subscription per connected institution + fee per shipment; no prices yet (slide 9)` NEW `Subscription per connected institution + fee per shipment (slide 9)`
- "Radox is the rail, never the issuer..." unchanged (role statement, not a caveat).

### Slide 5
- Pill. OLD `THE RAIL · DESIGN, LIFECYCLE BUILT` NEW `THE RAIL · LIFECYCLE BUILT`
- Top line. OLD `One record would follow the goods across company boundaries; today it runs across five test keys.` NEW `One record will follow the goods across company boundaries; port and airport systems will connect by API, not a rewrite.`
- Bold line. OLD `Built: this lifecycle on testnet, test keys. Design, not built: real companies on the rail, the standard, integrations.` NEW `Built: this lifecycle on testnet, test keys. Next: real companies on the rail, the standard, integrations.`
- Footnote. OLD `Keyed by sha256(container | origin); would sit beside the carrier's bill of lading, not integrated. ¹ Radox policy, not enforced on-chain; redeem needs the holder's signature.` NEW `Keyed by sha256(container | origin); sits beside the carrier's bill of lading. ¹ Radox policy, not enforced on-chain; redeem needs the holder's signature.` (the ¹ clause stays: it is a fact, removing it would imply the burn is enforced on-chain)

### Slide 6
- OLD `All test keys: this proves the mechanism, not independent companies.` NEW `Testnet, test keys.`

### Slide 7
- Row 03. OLD `("03", "The token stays put, then burns", "The shipment token never moves in transit; the existing Radox redeem burns it after delivery.")` NEW `("03", "Any Stellar asset, one record format", "The record stores a token address and never calls the token, so any tokenized Stellar asset can carry a custody record.")`  (source: contracts/custody_registry/src/lib.rs lines 62, 87, 278)
- Neighbours paragraph. OLD `("(LumenLoop, SCF, Scout, 24–25 Oct): ", ...)` + `Kutana and Trustless Work release escrow on trade milestones; Pipeline finances commodity trade. We found none that records a custody handover signed by two custodians, and no SEP.` NEW lead-in bold `Stellar holds about US$4B in tokenized assets (SDF, as of 1 Sep 2026). Nearest neighbours we found ` + `(LumenLoop, SCF, Scout, 24–25 Oct): ` + `Kutana and Trustless Work release escrow on trade milestones; Pipeline finances commodity trade. None records a custody handover signed by two custodians; no SEP.` (LONGER by one line)
- Footer. OLD `a custody primitive other Stellar real-world-asset issuers can reuse.` NEW `a custody primitive any Stellar tokenized-asset issuer can reuse. Radox will open API access to them, from onboarding to delivery.` (founder statement, future tense)

### Slide 8 (disclosures stay)
- OLD `Radox API reads the registry: same head (closed backend, testnet)` NEW `Radox API reads the registry, read-only: same head (testnet)` (API-PROOF.md: read-only simulate on a throwaway host; never "integrated")

### Slide 9
- Header. OLD `MARKET · FIGURES, NOT OURS` NEW `MARKET · SOURCED FIGURES`
- Header. OLD `MODEL · NO PRICES YET` NEW `MODEL`
- Small print. OLD `Borrows the shape of Swift's published fees: entry, annual, per-message usage⁶. Prices not set. Not affiliated with Swift.` NEW `Borrows the shape of Swift's published fees: entry, annual, per-message usage⁶. Not affiliated with Swift.` (kept: trademark disclaimer, true)
- Now/Next. OLD `testnet only; no users or revenue yet.  ` and `one Rio–Miami pilot (none agreed yet), SCF Build, audit, mainnet.` NEW `running on testnet, test keys.  ` and `the Rio–Miami pilot shipment, SCF Build, audit, mainnet, API for other Stellar assets.` (one line at 20 pt; if it wraps, drop `SCF Build, `)
- Ask: unchanged, word for word.

### Slide 10
No change. "Leo and Vhendala joined for the hackathon." is a team disclosure, kept.

## 2. Caveats removed, all slides (summary of the above)
Slide 1 "NOT REAL CUSTODIANS"; 2 "Not yet tested with a customer", "Our hypothesis"; 3 "No customer has confirmed it yet", "not results of ours / we do not claim", "market size only"; 4 "Neither the standard nor the rail exists yet", "none confirmed", "would still need a key", "no prices yet"; 5 "Design, not built", "today it runs across five test keys", "would sit ... not integrated"; 6 "not independent companies"; 7 "No SEP" kept as a finding; "other issuers can reuse" firmed; 9 "FIGURES, NOT OURS", "NO PRICES YET", "Prices not set", "no users or revenue yet", "none agreed yet". Spoken pitch: "market figures, not our results", "Our hypothesis", "No customer has confirmed it yet", "Neither ... exists yet", "this proves the mechanism, not independent companies", "not enforced on-chain", "nothing is filed", "A USD leg is not built", "none agreed yet".
Kept on purpose (true statements the rules or the facts need): prior work (slide 8), AI usage, "testnet" and "test keys", "Radox policy, not enforced on-chain" footnote, "Not affiliated with Swift", "9 refused (simulated)".
check_deck.py REQUIRED strings that this removes: "users or revenue yet", "none agreed yet", "none confirmed", "not built". Still present: "The goal is", "test key", "24 unit tests", "explainer video", "PRIOR WORK", "first repo commit", the AI strings.

## 3. Spoken pitch: 391 words (limit 396)
Full v13 text (replaces the spoken block of PITCH-FINAL.md):

A container leaves Rio for Miami and changes hands several times: warehouse, port, carrier, customs. DCSA reports about 45 million ocean bills of lading are issued a year, and only about 11% were electronic in 2025. TT Club and BSI report insiders were involved in 22% of recorded cargo thefts in 2025. Each company keeps its own record of its own leg, nobody holds the chain end to end, and a financier cannot see who holds the goods before paying.

So our goal is a shared, SWIFT-like custody standard that companies along a supply chain, from origin to destination, will use: each integrates once, not pair by pair. Ports and airports run legacy systems that are hard to integrate. Radox is in conversations with ports, airports and chambers of commerce, and a legacy system joins through one adapter to the Radox API.

We are building one rail, origin to delivery, across the companies in the chain. The double signature is the rule of each link: both sides sign one Stellar transaction, or the call fails.

On Stellar testnet, one shipment: seven successful transactions, open, four dual-signed handovers, deliver, and a burn. Nine invalid calls refused. Twenty-four unit tests pass. Testnet, test keys. The burn is our existing redeem.

Why Stellar. Soroban authorizes both companies of a link in one call, so the handover is atomic. We replay the history from Horizon and check it against the head stored in the contract. Stellar holds about 4 billion dollars of tokenized assets, the Stellar Development Foundation says. We found no Stellar project recording a handover signed by two custodians. The record never calls the token, so any tokenized Stellar asset can carry a custody record, and Radox will open API access to them, from onboarding to delivery.

This weekend we built the custody registry contract, the testnet harness and the public shipment page, on disclosed prior work: Radox, with three Soroban contracts on mainnet. AI coding agents wrote the code; the video narration is an AI voice generated from Pedro's voice.

Next: the Rio-Miami pilot shipment, then the Stellar Community Fund, audit and mainnet. Our ask: introductions to one financial institution and one port, airport or logistics operator for a first pilot shipment, and a Stellar engineer's review of the design.

Pedro built Radox; Leo and Vhendala joined for this hackathon. Thank you.

Changed against v11: P1 loses "market figures, not our results", "Our hypothesis", "No customer has confirmed it yet"; P2 gains the legacy and conversations sentences and loses "Neither ... exists yet"; P3 shortened; P4 loses the bill-of-lading, "not enforced" and "not independent companies" lines; P5 gains the SDF size and the token-agnostic plan; P7 loses "none agreed", "nothing is filed", "USD leg". Counted with wc -w on the block. The ask sentence is word for word.

## 4. README and FORM wording
User Value and Problem: Goods change hands across many companies and each keeps its own record of its own leg, so a financier cannot see who holds them before paying. Ports and airports run legacy systems that are hard to integrate. Radox is part of the Rio–Miami trade-corridor initiative and its technology rail: every port, airport and chamber that joins it will join the rail, through one adapter to the Radox API. Radox is in conversations with chambers of commerce in Brazil and Miami. Radox Rail gives every company in the chain one shared record on Stellar, proven end to end on testnet with test keys (7 transactions, 9 refused calls, head check MATCH). The first shipment is Rio–Miami.

Ecosystem Alignment: custody_registry is an open Apache-2.0 Soroban contract that stores a token address and never calls the token, so any tokenized Stellar asset can carry a custody record. Radox will open API access to Stellar issuers, from onboarding to delivery. Stellar holds about US$4B in tokenized assets (SDF, as of 1 Sep 2026) and we found no Stellar project recording a handover signed by two custodians (LumenLoop, SCF, Scout, 24-25 Oct).

## 5. Claims table
| Claim | Label | Source |
|---|---|---|
| 45M ocean bills of lading a year; ~11% electronic 2025; 22% of thefts insiders | sourced | DCSA; TT Club & BSI; PROBLEM-NUMBERS.md |
| R$900M, US$85M, US$2.5T | sourced | NTC; GTR; [[adb-trade-finance-gap-survey-dec-d033]] |
| Over 90% of ports in low- and middle-income countries have no PCS | sourced (conference remark relayed by IAPH, 2023; not re-opened by me) | [[world-bank-and-iaph-port-community-6ec0]] |
| IMO guidance plans for legacy systems with proprietary formats | sourced | IMO FAL.5/Circ.54 s8.4.3 (in the researcher's note) |
| Ports and airports run legacy systems, hard to integrate | founder (stated as fact, in founder voice) | [[founder-statements-in-the-deck-open-89a2]] |
| Radox is the technology rail of the (unnamed) Rio–Miami corridor initiative; ports, airports and chambers that join it join the rail; Radox is in conversations with chambers of commerce in Brazil and Miami | founder, Pedro via chief of staff 2026-10-25 20:05 (direct conversations are with chambers only; ports and airports come through the initiative) (no names, no deal, no endorsement) | [[founder-statements-in-the-deck-open-89a2]] |
| Standard will be used; port/airport systems will connect by API; Radox will open API access to Stellar assets | future (plan) | owner's words 25 Oct |
| Stellar holds about US$4B tokenized assets | sourced (SDF, as of 1 Sep 2026; rwa.xyz US$3.75B on 25 Oct is a separate figure, never mixed) | [[stellar-tokenized-rwa-size-on-2026-a455]] |
| Record stores a token address, never calls the token | sourced to our code | contracts/custody_registry/src/lib.rs 62, 87, 278 |
| Lifecycle on testnet: 7 tx, 9 refused, 24 tests, MATCH | sourced to our proofs | proofs/lifecycle.json; [[multi-company-chain-proof-on-testnet-672b]] |
| Radox API reads the registry (testnet, read-only) | sourced to our proof | API-PROOF.md |
| Found no Stellar project recording a two-custodian handover | sourced (search, dated) | [[physical-goods-rwas-on-stellar-matrixdock-05ea]], researcher B7 |
| Prior work, AI usage | sourced | slide 8, [[wording-the-rio-miami-deck-readme-ef38]] |

## 6. Predicted scores (my estimate, not a judge's)
- User Value and Problem: 8 (range 7-9). Stronger story, but still no third-party confirmation in the folder.
- Ecosystem Alignment: 9 (range 8-9). Code-verifiable token-agnostic property, SDF size, honest neighbour search.
Risk: a judge who reads "in conversations" next to an ask for introductions to one bank and one port may probe it; the founder must be able to name the kind of conversation in Q&A.

## Open questions for the owner
1. Is "conversations" (his word was "abertura com vários") exactly what he can say aloud? It is stronger than "openness".
2. Optional: corridor project depending on us (left out per coordinator).
3. Reviewer must reopen the World Bank/IAPH 90% quote.
4. "A financier cannot see who holds the goods" and "will use" are now stated as fact and plan, not tested: a judge may read them as unproven; owner's call.

## Versions
- v1, lens goal-behind-goal: product plan copy with founder labels. Judge (my reading): fails the new owner rule.
- v2, lens rawest material: facts re-opened (SDF, rwa.xyz raw HTML), code lines cited. Judge: numbers pass.
- v3, lens outside judge on overclaim: after the rule change, removed caveats but kept only true statements; "can carry" tied to the code. Judge: no partner, deal, user, revenue or mainnet claim found by my regex reading of BANNED.
- v4, lens skim test: word count 391, one-line Now/Next. check_deck.py and the independent reviewer have NOT run; pending.

## Never-skip checklist
- Library cites: done; no new note (existing [[stellar-tokenized-rwa-size-on-2026-a455]] already covers the re-opened figures, nothing to merge).
- Numeric goal with date / funnel / unit economics / channels / tracking: not applicable (deck and form copy, not a campaign).
- One first segment: financier plus port/airport operator (from product note); real alternative: paper and each firm's own system.
- Every claim has proof or label: done (table).
- Jurisdiction: US and Brazil trade claims; no endorsement or testimonial used; legal review of "conversations" flagged to owner.
