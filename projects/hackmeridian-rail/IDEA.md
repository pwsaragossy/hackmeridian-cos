# Idea, scored against the criteria

Criteria and weights: CRITERIA.md (scored 1–5).

## Idea (one sentence)

**Every handover of a tokenized physical shipment between Rio and Miami is signed by both the
outgoing and the incoming custodian on Stellar, ownership stays with the token holder, and delivery
burns the title.**

## User and problem

- **Beachhead user (behavioral):** a trade financier or buyer who pays against goods still in transit
  and today relies on paper handover documents and the carrier's own tracking page to know who holds
  the cargo. The exporter and the four custodians (warehouse, port, carrier, customs) are the people
  who must sign; they are not the buyer of the product.
- **Problem, one falsifiable sentence:** a party paying against goods in transit cannot check, without
  trusting one intermediary, who signed for the goods at each handover.
- **Current alternative and its cost:** bill of lading plus courier or carrier tracking plus
  insurer or surveyor inspection. Cost in time or money: **not sourced** — PITCH.md slide 2 still
  needs one sourced number.
- **Evidence of the problem:** *assumption.* What exists: (a) the owner's view; (b) Radox built a
  physical-asset withdrawal flow (ship, deliver, confirm "received", burn) in `radox-internal`:
  that shows we needed it, not that a buyer or financier is in pain, and it is prior work; (c) the
  ecosystem search found funded trade-finance projects (Airswift, Pipeline, BorderDollar,
  RESEARCH-raven.md §5), which is investor interest, not user behavior. No interview, no pilot, no
  usage number. Strength: weak. Confidence: low.
- **Riskiest assumption:** custodians (a port, customs) would ever co-sign handovers on-chain, and a
  financier would pay for that over the carrier's tracking. Cheapest test, at the event: ask 3
  mentors from logistics or trade finance one question each ("would you accept this signature
  instead of a scanned stamp?"). Kill signal: all say customs and ports will not sign; then the
  pitch changes from "custodians sign" to "an event source attests" (assurance level 1 exists).
  The demo uses test keys for all six actors: say so, never imply real custodians.

## Self-score (1–5, before building; the reviewer redoes it after)

Ecosystem 4 · User value 3 (assumption, no behavior evidence) · Technical 4 if the 7 txs land, 2 if
not · Innovation 4 (new on a directory search only) · Progress 4 (clean split, but the burn and token
admin are prior work) · Market 3 (no pilot customer) · UX 3 with the page, 1 without.
Weighted with the page and 7 txs: (4·20 + 3·20 + 4·15 + 4·15 + 4·10 + 3·10 + 3·10) / 5 = **72 / 100**
(3.6 of 5). The cheapest points: User value from one sourced number and one mentor quote; UX
from the page.

## Scope — approved by the owner on 2026-10-25 (frozen)

Max 3 must-haves:
1. `custody_registry` + tests, deployed on testnet (Leo's agents, LEO-BRIEF.md).
2. Lifecycle harness with the 7 txs + `verify-head` + failure branches (Leo's agents).
3. **A public read-only shipment page** (static, reads the contract on testnet: route, current
   custodian, each handover with both signers, assurance, tx links, `head` verified) — Pedro's
   sessions. Covers UX (10%) and gives judges a public URL.

Conditional 4th: **the Radox API connection** (private branch). The intake promised it, and Scale
scores milestone completion against the intake, so it stays in — but the approved stop criterion
cuts it if no dual-signed handover runs on testnet by Sun 18:00. If cut, the README says so.

Cut / later: passkey signing by the custodians in a phone UI, event-source adapters, the USD leg.
