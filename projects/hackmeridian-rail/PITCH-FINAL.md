# PITCH-FINAL: Radox Custody Rail deck (10 slides, v13) + spoken pitch

Built from PITCH.md (binding: Claims guard, Copy rules), DEMO-SCRIPT.md, SUBMISSION.md, VERIFY-LEO.md, `proofs/lifecycle.json` (rio-miami-rail, read with `gh api` 2026-10-25), template order from [[hackmeridian-2026-official-pitch-deck-template-d5c7]]. Wording rules: [[wording-the-rio-miami-deck-readme-ef38]], [[claims-hackmeridian-material-may-and-may-3e4f]]. ZIS: [[zis-in-public-material-radox-is-bc05]], no OK assumed, so ZIS and Paulo appear nowhere and the corridor is the "unnamed bridge".

Order (owner, 2026-10-25): problem → SWIFT-like standard → end-to-end rail → testnet proof; the double signature is only the rule of each link. check_deck.py enforces it. Slide text lives in deck/build_deck.py; this file holds the outline, the portal item and the spoken pitch.

Unnamed bridge (slide 7 only): "a Rio–Miami trade-corridor initiative". No ZIS, no person, no "part of", no "supported by".

Full hashes (testnet; explorer pattern `https://stellar.expert/explorer/testnet/tx/<hash>`):

| Step | Hash |
|---|---|
| open | 2b3d51f0cdf113d34a7c20dd373142c379926bd3bd24ca0a9cb6d4718e379902 |
| handover 1 | 635c99ac73cb13416e6b52f29ac9a067fbc615e01b8de962eb36245db3f0bd38 |
| handover 2 | 56a0f006e3373df34c96ae7b0f02c4b66753ccaca6ccc48fe5125bb65e7b7cc2 |
| handover 3 | ac268a49e00ddf4745c9026bf01e3c77e5c451a7e2396100ef590a36ecc3c4b2 |
| handover 4 | 5199d4fb6b2833662327deecbf5fcaf058a0d7a464f97974edd107f5de400b7a |
| deliver | 919def8c0b3f29ae650f5f1ea6d632e49efd4a9442381c84c83d858ad2144e37 |
| redeem (burn) | 864fd1644d30bf708a59f94ca5b0fc303a50deccfd96099bd32dfb67e215644d |

`custody_registry` testnet: CCBJVXMJYWPHTDJHDFPRGKPGXGEP24JOPJAMUS5C3BMZJTRTWR2H4LII. Final head: 2d74fec064a6796c34be93ede6241e0e067650dcfb2e058382f2f9cf83195414.

## Slides (v13, founder voice: owner 2026-10-25 "NÃO É PRA LOWBALL NOSSO PROJETO, VENDA APENAS A PARTE BOA"; no false claim, no partner named)

1. Cover: "Radox Custody Rail". One record for the goods, from origin to delivery, that every company along the way will share. Toward a SWIFT-like standard on Stellar; pilot corridor Rio–Miami. Pill: testnet, test keys.
2. Problem, "Who holds the whole chain?": the gap (each company records only its own leg); 45M ocean bills of lading a year (DCSA); ~11% electronic, 2025 (DCSA); 22% of cargo thefts with insiders (TT Club & BSI); ports run legacy systems: over 90% of ports in low- and middle-income countries have no port community system (World Bank remark relayed by IAPH, Nov 2023), IMO FAL.5/Circ.54 plans for legacy proprietary systems; unnamed bridge line.
3. What it costs: the gap (a financier cannot see who holds the goods before paying); R$900M, US$85M, US$2.5T (market size); "These figures size the market problem the rail addresses."
4. The proposal: the goal is a shared, SWIFT-like custody standard that companies along a supply chain will use; "We are building it on Stellar, starting with the custody rail." 10 vs 5 links; open vs Radox operates (per-institution subscription + fee per shipment). Radox has openings with ports and airports, and chambers of commerce in Brazil and Miami are opening doors; legacy systems will join through one adapter to the Radox API.
5. The rail: one record will follow the goods; port and airport systems will connect by API. Rule of every link, head hash chain, token stays with holder. Built: the lifecycle on testnet, test keys. Next: real companies, the standard, integrations.
6. The proof: 7 hashes, 7 successful, 9 refused (simulated), 24 unit tests, MATCH; separate computers (three-machine.json) and two test companies on one registry (multi-chain.json); testnet, test keys.
7. Why Stellar: multi-party auth; history from Horizon checked by the head; any Stellar asset (the record stores a token address and never calls the token); Stellar holds about US$4B in tokenized assets (SDF, 1 Sep 2026); neighbours, no SEP; Apache-2.0, Radox will open API access to Stellar issuers.
8. Built this weekend on disclosed prior work; Radox API custody route reads the registry, read-only (testnet); AI attribution.
9. "One rail, every corridor": sourced market figures; the model (subscription per connected institution + a fee per shipment, shape of Swift's billing rules, not affiliated); Now: running on testnet; Next: the Rio–Miami pilot shipment, SCF Build, audit, mainnet, API for other Stellar assets; the ask (locked).
10. Team: unchanged.

## Pitch item (portal)

The README and FORM wording for User Value and Ecosystem is in COPY-V13.md section 4, handed to the rail session.

## Spoken pitch (finalists, 3:00, v13)

Rehearsal: timed reads by Pedro needed twice.

Words (395, counted 2026-10-25; limit 396 for 3:00 at 2.2 words a second):

A container leaves Rio for Miami and changes hands several times: warehouse, port, carrier, customs. DCSA reports about 45 million ocean bills of lading are issued a year, and only about 11% were electronic in 2025. TT Club and BSI report insiders were involved in 22% of recorded cargo thefts in 2025. Each company keeps its own record of its own leg, nobody holds the chain end to end, and a financier cannot see who holds the goods before paying.

Our goal is a shared, SWIFT-like custody standard that companies along a supply chain, from origin to destination, will use: each integrates once, not pair by pair. Ports and airports run hard-to-integrate legacy systems. Radox has openings with ports and airports, and chambers of commerce in Brazil and Miami are opening doors; legacy systems will join through one adapter to the Radox API.

We are building one rail, origin to delivery, across the companies in the chain. The double signature is the rule of each link: both sides sign one Stellar transaction, or the call fails.

On Stellar testnet, one shipment: seven successful transactions, open, four dual-signed handovers, deliver, and a burn. Nine invalid calls refused. Twenty-four unit tests pass. Testnet, test keys. The burn is our existing redeem.

Why Stellar. Soroban authorizes both companies of a link in one call, so the handover is atomic. We replay the history from Horizon and check it against the head stored in the contract. Stellar holds about 4 billion dollars of tokenized assets, the Stellar Development Foundation says. We found no Stellar project recording a handover signed by two custodians. The record never calls the token, so any tokenized Stellar asset can carry a custody record, and Radox will open API access to them, end to end.

This weekend we built the custody registry contract, the testnet harness and the public shipment page, on disclosed prior work: Radox, with three Soroban contracts on mainnet. AI coding agents wrote the code; the video narration is an AI voice generated from Pedro's voice.

Next: the Rio-Miami pilot shipment, then the Stellar Community Fund, audit and mainnet. Our ask: introductions to one financial institution and one port, airport or logistics operator for a first pilot shipment, and a Stellar engineer's review of the design.

Pedro built Radox; Leo and Vhendala joined for this hackathon. One rail, every corridor. Thank you.

## Claims check

Slide numbers in this table are from the earlier 9-slide order; the claims for the deck v11 are tracked in deck/REVIEW.md (rounds 4 and 5).

Count: 27 claims (numbers and factual assertions on slides). Sources are files in this folder unless stated.

| # | Slide | Claim | Source |
|---|---|---|---|
| 1 | 1 | Title and tagline "First corridor: Rio–Miami" | SUBMISSION.md (Project title and Tagline rows) |
| 2 | 1 | Scale track | PITCH.md slide 1 |
| 3 | 1, 4 | Testnet, test keys | proofs/lifecycle.json (`network: testnet`); VERIFY-LEO.md |
| 4 | 2 | Two custodians sign the same transaction | proofs/lifecycle.json lifecycle; VERIFY-LEO.md b; REVIEW-contract.md |
| 5 | 2 | Token stays with holder in transit | proofs/lifecycle.json `holder_balance_after_redeem: "0"` and holder key unchanged; PITCH.md slide 2 |
| 6 | 2, 4 | Burn is existing `redeem`, policy not on-chain enforced, needs holder signature | PITCH.md slide 2; wording note rule 1 |
| 7 | 2 | Innovation hedge: none found in directories searched 2026-10-25 | RESEARCH-raven.md §5; PITCH.md script notes |
| 8 | 3 | Handover chain: warehouse, port, carrier, customs | proofs/lifecycle.json actors; DEMO-SCRIPT.md 0:00 row |
| 9 | 3 | "Several times" (fallback, not "4+") | SUBMISSION.md Problem solved row |
| 10 | deck 2-3, spoken | 45M, ~11%, 22%, R$900M, US$85M (market figures, not traction) | PROBLEM-NUMBERS.md rows 1, 2, 3, 7, 5 (45M ocean, 2021 data; ~11% unscoped, 2025); REVIEW-PROBLEM.md; deck/REVIEW.md round 4 |
| 11 | deck 3 | US$2.5T global trade finance gap, market size only | [[adb-trade-finance-gap-survey-dec-d033]] (ADB, Dec 2025) |
| 12 | 3, spoken | No customers yet; hypothesis only | CRITERIA.md (evidence is an assumption); STATE.md line 74; claims note, Problem evidence row |
| 13 | 4 | 7 successful testnet transactions | proofs/lifecycle.json; VERIFY-LEO.md b (Horizon `successful` true for all 7) |
| 14 | 4 | Contract ID CCBJVXMJ…H4LII | proofs/lifecycle.json; VERIFY-LEO.md a |
| 15 | 4 | Seven hashes listed | proofs/lifecycle.json lifecycle |
| 16 | 4 | 9 refusals | proofs/lifecycle.json failures (9, `hash_or_sim: simulation`); VERIFY-LEO.md d. Individual refusals not re-run by the verifier |
| 17 | 4 | 24 tests pass | VERIFY-LEO.md e |
| 18 | 4 | `verify-head` MATCH, head 2d74fec0…5414 | VERIFY-LEO.md f |
| 19 | 4 | Six actors are test keys held by one harness | PITCH.md Claims guard (Demo) |
| 20 | 4 | Events last about 7 days; `head` survives | PITCH.md slide 4; SUBMISSION.md (getEvents about 7 days) |
| 21 | 4 | Holder balance 0 after burn | VERIFY-LEO.md c; proofs/lifecycle.json |
| 22 | 5, 9 | 3 Soroban contracts on mainnet, public repo created 2026-08-19 | PITCH.md Claims guard; [[wording-the-rio-miami-deck-readme-ef38]] rule 3 (wasm and one instance checked; the other two instances not matched by ID) |
| 23 | 5 | No contract code before Sun 09:00; planning files 24–25 Oct are prior work | wording note rule 9; SUBMISSION.md Prior work row |
| 24 | 5, 9 | Code written by AI coding agents; narration AI voice from Pedro's voice | SUBMISSION.md (AI tooling note, Description); DEMO-SCRIPT.md header; PITCH.md Deliverables |
| 25 | 6, 7, 8 | No users, no pilot, none agreed, no pricing, no endorsement | PITCH.md Claims guard; claims note |
| 26 | 8 | Mainnet blocked until matrix passes; no audit; SCF planned, not submitted; USD leg not built | SUBMISSION.md Production path; wording note rules 5 and 6 |
| 27 | 9 | Team roles: Pedro Saragossy founder; Leo Schlanger developer; Vhendala supervision and product review; Leo and Vhendala joined for hackathon | PITCH.md slide 9; wording note rule 7 |

Open items for the caller (not claims):
- Slide 5 API-connection row: delivered or not is not recorded in the folder; keep "not delivered" unless a hash exists.
- Slide 7 pricing: left "not priced yet"; add a line only if Pedro confirms.
- Slide 3: re-open the ADB page before export (the Dec 2025 summary was read second-hand).
- Screenshot files `shot-handover-expert.png` and `shot-page-delivered.png` do not exist yet; names are placeholders.
- Word counts: titles ≤ 8, on-slide ≤ 30, notes ≤ 60 (counted by hand; run a count before export). Spoken text counted at 368 words; slide counts verified by script (all within limits).
