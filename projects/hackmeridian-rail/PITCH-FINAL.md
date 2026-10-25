# PITCH-FINAL: Radox Custody Rail deck (9 slides) + spoken pitch

Built from PITCH.md (binding: Claims guard, Copy rules), DEMO-SCRIPT.md, SUBMISSION.md, VERIFY-LEO.md, `proofs/lifecycle.json` (rio-miami-rail, read with `gh api` 2026-10-25), template order from [[hackmeridian-2026-official-pitch-deck-template-d5c7]]. Wording rules: [[wording-the-rio-miami-deck-readme-ef38]], [[claims-hackmeridian-material-may-and-may-3e4f]]. ZIS: [[zis-in-public-material-radox-is-bc05]], no OK assumed, so ZIS and Paulo appear nowhere and the corridor is the "unnamed bridge".

Order = template (Cover, Solution, PMF/problem, Technical workflow) + 4 added slides after Technical workflow + Team last. Look: LOOK.md (dark proof slides, cream text slides, min 24 pt body, 40 pt titles).

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

## Slides

### 1. Cover (dark)
- Title: Radox Custody Rail: dual-signed custody, on Stellar
- On-slide : First corridor: Rio–Miami. HackMeridian 2026, Scale track. Testnet build, test keys.
- Proof element: the Rio → Miami hairline with four lime dots; label "Testnet - test keys - not real custodians"; repo `github.com/pwsaragossy/rio-miami-rail`.
- Speaker notes : Full title: "Radox Custody Rail: dual-signed custody for goods in transit, on Stellar". We built a public record of who holds a shipment, signed by both sides of every handover. Everything shown ran on Stellar testnet this weekend.

### 2. Solution: Every handover, signed by both hands (cream)
- Title: Every handover, signed by both hands
- On-slide : `custody_registry`: outgoing and incoming custodian sign the same transaction. The token stays with its holder in transit. After Delivered, the operator burns it.
- Proof element: screenshot `shot-handover-expert.png` (one dual-signed handover on stellar.expert, both auth entries visible; handover 1, hash 635c99ac...).
- Speaker notes : Two custodians must authorise one call, or it fails. The record keeps a hash chain, `head`. The burn is the existing `redeem`. The operator runs it only after the registry shows Delivered. That is Radox platform policy, not enforced on-chain by the registry, and `redeem` still needs the holder's signature. We found none in the directories searched 2026-10-25.

### 3. PMF (problem), now deck slides 2 and 3 (cream)
Deck v8 (deck/build_deck.py) puts the problem before the solution, in two slides. Every number is a row of PROBLEM-NUMBERS.md, wording per REVIEW-PROBLEM.md and deck/REVIEW.md round 4. Do not write "paper" or "inside job".
- Slide 2 "Who holds the cargo right now?": 45M ocean bills of lading issued a year (DCSA, Feb 2023, 2021 data); ~11% of bills of lading issued electronically, 2025 (DCSA, as of 2025; Jan 2025 guide: 5.7%); 22% of recorded cargo thefts in 2025 involved insiders (TT Club & BSI, Apr 2026). The two DCSA figures are separate scopes and years, never one population.
- Slide 3 "Cargo goes missing. A bank got fooled.": R$900M est. direct loss, 8,570 cargo robberies in Brazil, 2025 (NTC&Logística, 28 Mar 2026); US$85M HSBC loss on forged documents for oil trades that never happened (Hin Leong, Global Trade Review, 18 Nov 2024); US$2.5T global trade finance gap, market size only (ADB, Dec 2025). Hypothesis line: a financier cannot see who holds the goods before paying; no customer has confirmed it. Closing line: "These numbers size the market problem. They are not results of ours, and we do not claim our build prevents any of it."
- Speaker notes : These are market figures, not our results. No number here measures the handover itself; the insider share is the closest. Our hypothesis is that a financier cannot easily see who holds the goods. No customer has confirmed it yet.

### 4. Technical workflow: How it runs on Stellar (dark)
- Title: How it runs on Stellar
- On-slide : open, 4 dual-signed handovers, deliver, burn. 7 successful testnet transactions. 9 invalid cases refused. 24 contract tests pass. `verify-head` recomputes the chain: MATCH.
- Proof element: diagram (open → h1 → h2 → h3 → h4 → deliver → redeem) with contract ID `CCBJVXMJ…H4LII` and 8-character hashes 2b3d51f0, 635c99ac, 56a0f006, ac268a49, 5199d4fb, 919def8c, 864fd164; full table above in the appendix link / README.
- Speaker notes : Six actors, all test keys held by one harness: this proves the mechanism, not independent custodians. Nine refusals (wrong custodian, wrong signer, early delivery and six more) were checked as simulations. Events last about seven days on the RPC, so `head`, a hash chain on the contract, lets anyone recompute the history. Holder balance after the burn is zero.

### 5. (added) Prior work vs HackMeridian: What we built this weekend (cream)
- Title: Prior work versus this weekend
- On-slide : Existed: Radox platform, 3 Soroban contracts on mainnet, `transfer_agent`. Built here: `custody_registry`, test harness, `verify-head`, shipment page. Code written by AI coding agents.
- Proof element: two-column table (existed / built here) plus commit timeline after Sun 25 Oct 09:00; pointer to `AI_USAGE.md` (per-file: tool, and which named person read it). API connection row only if a hash exists; otherwise "not delivered" {{fill: Mon 06:00 check}}.
- Speaker notes : Radox's three mainnet contracts, public since 2026-08-19, and `transfer_agent` are prior work, disclosed. No contract code existed before Sunday 09:00; planning files dated 24 and 25 October did. The burn is the existing `redeem`, not new work. Code, tests and scripts were written by Claude Code agents. `AI_USAGE.md` lists who read what.

### 6. (added) Users and value: Who uses it (cream)
- Title: Who uses it, and why
- On-slide : Exporter, custodians (warehouse, port, carrier, customs), buyer, financier. Value: a financier can see where the goods are, and who signed for them, before paying. No users yet.
- Proof element: the public shipment page screenshot `shot-page-delivered.png` (rio-miami-rail.vercel.app, label "Testnet - test keys - not real custodians").
- Speaker notes : No customers, exporters or pilot exist yet. These are the roles the contract models. The page is read-only and public: anyone with a container number sees the chain and can press Verify head. A custody record keyed to the container number; in production it would sit beside the carrier's bill of lading, not integrated here.

### 7. (added) Business model and go-to-market: The rail is ours, the format is public (cream)
- Title: The rail is ours; the format is public
- On-slide : SWIFT model: public record format; Radox runs the rail and API. Revenue: fee from the institution operating it; not priced yet. Next: one pilot shipment with one producer; none agreed.
- Proof element: none beyond the Rio → Miami line; footnote "Context: a Rio–Miami trade-corridor initiative. No agreement, endorsement or pilot." (unnamed bridge). Pricing line {{fill: only if Pedro confirms}}; otherwise left as "not priced yet".
- Speaker notes : Radox is the rail, never the issuer; the client is a financial institution. Regulation and licences belong to the client and local counsel. Go-to-market is one corridor, Rio to Miami, and one pilot shipment with one producer; nobody has agreed yet. We would approach a financial institution and a logistics operator. No endorsement or letter from any body exists.

### 8. (added) Market and next steps: From one corridor to a standard (cream)
- Title: From one corridor to a standard
- On-slide : Next: full testnet matrix, then mainnet; an audit is not done. Planned: an SCF Build application (not yet submitted). Future: a USD on-ramp leg; not built.
- Proof element: link to the open question "which ramp delivers USD to a C-address (SEP-45 draft)". No anchor or ramp named.
- Speaker notes : Mainnet is not this weekend. Physical-asset offers stay blocked outside testnet until the test matrix passes. No audit has happened; an SCF audit would start only after an award. We plan to apply to SCF; nothing is filed and we claim no eligibility. The USD leg is future tense: nothing is built or under contract.

### 9. Team: Why us (cream)
- Title: Why us
- On-slide : Pedro Saragossy, founder, captain. Leo Schlanger, developer. Vhendala, supervision, product review. Leo and Vhendala joined for the hackathon. Narration is an AI voice generated from Pedro's voice.
- Proof element: team photo (each person's consent first; max 3 lines per member); footer line "Code written with AI coding agents (Claude Code); see AI_USAGE.md"; line "Radox: 3 Soroban contracts on Stellar mainnet (public repo, created 2026-08-19)".
- Speaker notes : Pedro built Radox and its three mainnet contracts. Leo and Vhendala joined this weekend. The video narration is an AI voice generated from Pedro's voice, not a person reading live. Code, tests and scripts were written with AI coding agents; humans decided scope and checked the proofs. Radox has no users or revenue yet.

## Pitch item (portal)

- Problem: About 45 million ocean bills of lading are issued a year (DCSA, 2023), and DCSA reports only about 11% were electronic in 2025; insiders were involved in 22% of recorded cargo thefts in 2025 (TT Club & BSI, Apr 2026). These are market figures, not our traction. Our hypothesis: a financier cannot easily see who holds the goods (no customers yet).
- Solution: `custody_registry`: both custodians sign every handover in one Stellar transaction; a hash chain makes the history checkable; the existing `redeem` burns the token after Delivered.
- Demo: Rio–Miami lifecycle on testnet: 7 successful transactions, 9 refusals, `verify-head` MATCH, public shipment page; test keys, one harness.
- Why this team: Pedro runs Radox with 3 Soroban contracts on mainnet; Leo and Vhendala joined this weekend; AI agents wrote the code and we say so.
- Next step: a first pilot shipment with one producer (none agreed), full testnet matrix, SCF Build application (planned), then mainnet.

## Spoken pitch (finalists, 3:00)

Rehearsal: not yet; timed reads by Pedro needed twice.

Words (395, counted by script 2026-10-25; about 3:00 at 2.2 words a second):

A container leaves Rio for Miami and changes hands several times: warehouse, port, carrier, customs. About 45 million ocean bills of lading are issued a year, and DCSA says only about 11% of bills of lading were electronic in 2025. In more than one in five recorded cargo thefts, insiders were involved. Those are market figures, not our results. Our hypothesis is that a financier cannot easily see who holds the goods. No customer has confirmed it yet.

So we built a public record of the chain on Stellar. It is called Radox Custody Rail. Its contract, custody registry, has one rule: every handover needs both signatures, the custodian handing over and the custodian receiving, in the same transaction. If either one is missing, the call fails.

Here is what ran on Stellar testnet. One shipment, seven successful transactions: open, four dual-signed handovers, deliver, and a burn. Nine invalid cases were refused: the wrong custodian, out of route, a wrong signer, early delivery, and five more. Twenty-four contract tests pass. And one command recomputes the whole history from the chain and matches the contract's head hash. Anyone can run it. The public shipment page does the same with a button.

I want to be exact about what this proves. All six actors are test keys held by one harness. This proves the mechanism, not independent custodians. The burn is the existing redeem from our platform; the operator runs it only after the registry shows Delivered. That is our platform policy, not something the registry enforces. And the record is not a bill of lading. In production it would sit beside the carrier's one.

Why us. Pedro built Radox, which already has three Soroban contracts deployed on Stellar mainnet. Leo and Vhendala joined for this hackathon. We used AI coding agents to write the code, and the narration in our video is an AI voice generated from Pedro's voice. Our repository lists, file by file, who wrote what and who read it.

Next. We want one pilot shipment with one producer; none is agreed yet. Then the full testnet matrix, and only then mainnet. We plan to apply to the Stellar Community Fund; nothing is filed. A USD leg is future work, not built.

One corridor, one public format, every handover signed by both hands. Thank you.

## Claims check

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
| 10 | deck 2-3, spoken | 45M, ~11%, 22%, R$900M, US$85M (market figures, not traction) | PROBLEM-NUMBERS.md rows 1, 2, 3, 7, 5; REVIEW-PROBLEM.md; deck/REVIEW.md round 4 |
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
