# PITCH-FINAL: Radox Custody Rail deck (10 slides, v11) + spoken pitch

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

## Slides (v11)

1. Cover: "Radox Custody Rail". One record for the goods, from origin to delivery, that every company along the way could share. Toward a SWIFT-like standard on Stellar; pilot corridor Rio–Miami. Testnet, test keys.
2. Problem, "Who holds the whole chain?": hypothesis (each company records only its own leg; not yet tested with a customer); 45M ocean bills of lading a year (DCSA, Feb 2023, 2021 data); ~11% electronic, 2025 (DCSA); 22% of recorded cargo thefts in 2025 involved insiders (TT Club & BSI, Apr 2026); unnamed bridge line.
3. What it costs, "Cargo goes missing. A bank got fooled.": R$900M (NTC, 8,570 robberies, 2025); US$85M HSBC, Hin Leong (GTR); US$2.5T gap, market size only (ADB). "Not results of ours."
4. The proposal, "A SWIFT-like standard: integrate once": the goal is a shared, SWIFT-like custody standard that companies along a supply chain, from origin to destination, could use. Neither the standard nor the rail exists yet. 10 vs 5 links; open (contract, Apache-2.0; verify without login) vs Radox operates (onboarding, closed API, paid by the financial institution, not priced).
5. The rail, "One rail, origin to delivery": open → warehouse → port → carrier → customs → recipient → delivered → burned; rule of every link: both sides sign one transaction (delivery: recipient and holder), or the call fails; head hash chain; token stays with holder. Built: the lifecycle on testnet; design: real companies, standard, integrations.
6. The proof, "The lifecycle ran on testnet": 7 hashes, 7 successful, 9 refused (simulated), 24 unit tests, verify-head MATCH; second shipment (proofs/three-machine.json), two team members signing from their own computers; all test keys.
7. "Why Stellar: all signers, one call": multi-party auth, events plus head, token stays then burns; nearest neighbours, no SEP; Apache-2.0.
8. "Built this weekend, on disclosed prior work": prior work, built here, AI attribution.
9. "One rail, every corridor": market figures from MARKET-NUMBERS.md section 4 (US$94.2B US–Brazil goods trade, US$6.1B Florida to Brazil, global line), labelled "figures, not ours"; the model, a subscription per connected institution plus a fee per shipment, after Swift's billing shape, with no prices; now and next; the ask (locked: the video 2:30 row quotes it).
10. Team: Pedro Wakigawa Saragossy, Leo Schlanger, Vhendala; links; AI line.

## Pitch item (portal)

- Problem: Goods cross borders through many companies, and each keeps its own record of its own leg; no shared record follows the goods, so a financier cannot see who holds them before paying. Our hypothesis; no customer has confirmed it. (About 45M ocean bills of lading a year, DCSA 2023; ~11% electronic in 2025, DCSA.)
- Solution: Radox Custody Rail: one public record on Stellar that would follow the goods from origin to delivery across the companies in the chain. Each link moves only when both sides sign one transaction. The lifecycle is proven on testnet with test keys (Rio–Miami). The SWIFT-like standard, real companies and integrations are future work, none confirmed.
- Demo: Rio–Miami lifecycle on testnet: 7 successful transactions, 9 refusals, `verify-head` MATCH, public shipment page; test keys, one harness.
- Why this team: Pedro runs Radox with 3 Soroban contracts on mainnet; Leo and Vhendala joined this weekend; AI agents wrote the code and we say so.
- Next step: a first pilot shipment with one producer (none agreed), full testnet matrix, SCF Build application (planned), then mainnet.

## Spoken pitch (finalists, 3:00, v11 order)

Rehearsal: not yet; timed reads by Pedro needed twice.

Words (387, wc -w, 2026-10-25; limit 396 for 3:00 at 2.2 words a second):

A container leaves Rio for Miami and changes hands several times: warehouse, port, carrier, customs. DCSA reports about 45 million ocean bills of lading are issued a year, and only about 11% were electronic in 2025. TT Club and BSI report insiders were involved in 22% of recorded cargo thefts in 2025. These are market figures, not our results. Our hypothesis: each company keeps its own record of its own leg, nobody holds the chain end to end, and a financier cannot see who holds the goods before paying. No customer has confirmed it yet.

So our goal is a shared, SWIFT-like custody standard that companies along a supply chain, from origin to destination, could use: each would integrate once, not pair by pair. Neither the standard nor the rail exists yet.

What we are building toward is one rail, origin to delivery, across the companies in the chain, not inside one company's system. The double signature is only the rule of each link: both sides sign one Stellar transaction, or the call fails.

On Stellar testnet, one shipment: seven successful transactions, open, four dual-signed handovers, deliver, and a burn. Nine invalid calls refused. Twenty-four unit tests pass. All keys are test keys: this proves the mechanism, not independent companies. The burn is our existing redeem, Radox policy, not enforced on-chain. The record would sit beside the carrier's bill of lading, not replace it.

Why Stellar. Soroban authorizes both companies of a link in one call, so the handover is atomic. We replay the history from Horizon and check it against the head stored in the contract. We found no Stellar project recording a handover signed by two custodians.

This weekend we built the custody registry contract, the testnet harness and the public shipment page, on disclosed prior work: Radox, with three Soroban contracts on mainnet. AI coding agents wrote the code; the video narration is an AI voice generated from Pedro's voice.

Next: one Rio-Miami pilot shipment, none agreed yet. We plan to apply to the Stellar Community Fund; nothing is filed. A USD leg is not built. Our ask: introductions to one financial institution and one port, airport or logistics operator for a first pilot shipment, and a Stellar engineer's review of the design.

Pedro built Radox; Leo and Vhendala joined for this hackathon. One rail for goods, every corridor. Thank you.

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
