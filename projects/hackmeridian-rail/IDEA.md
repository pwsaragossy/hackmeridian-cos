# Idea, scored against the criteria

Criteria and weights: CRITERIA.md.

## Idea (one sentence, scored)

**Every handover of a tokenized physical shipment between Rio and Miami is signed by both the
outgoing and the incoming custodian on Stellar, ownership stays with the holder, and delivery burns
the title** — users: exporter, custodians, buyer, financier; problem: nobody can prove the custody chain
in real time.

Self-score against the rubric (1–10, before building; the reviewer redoes it after): Ecosystem 8 ·
User value 7 · Technical 8 if the 7 txs land · Innovation 8 · Progress 9 (clean split) · Market 6
(no pilot customer to show) · UX **3 without a screen, 7 with one**.

## Scope — approved by the owner on 2026-10-25 (recorded in central at stage 2)

Max 3 must-haves:
1. `custody_registry` + tests, deployed on testnet (Leo's agents, LEO-BRIEF.md).
2. Lifecycle harness with the 7 txs + `verify-head` + failure branches (Leo's agents).
3. **A public read-only shipment page** (static, reads the contract on testnet: route, current
   custodian, each handover with both signers, assurance, tx links, `head` verified) — Pedro's
   sessions. Covers UX (10%) and gives judges a public URL.

Conditional 4th: **the Radox API connection** (private branch). The intake promised it, and Scale scores
milestone completion against the intake, so it stays in — but it is exactly what the approved stop
criterion cuts if no dual-signed handover runs on testnet by Sun 18:00. If cut, the README says so.

Cut / later: passkey signing by the custodians in a phone UI, event-source adapters, the USD leg.
