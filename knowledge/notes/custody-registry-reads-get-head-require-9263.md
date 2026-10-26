---
id: custody-registry-reads-get-head-require-9263
title: "Custody registry reads (get, head) require no auth; mainnet-fork 13.72 XLM is the whole 15-tx session, not a per-handover cost"
type: finding
status: active
origin: hackmeridian-rail
provenance: agent
confidence: medium
sources: ["/Users/pedrosaragossy/code/rio-miami-rail/contracts (lib.rs get/head, lines 483-489)","/Users/pedrosaragossy/code/rio-miami-rail/proofs/mainnet-rehearsal.json report.markdown"]
created: 2026-10-26
updated: 2026-10-26
review_by: 2027-04-26
group:
aliases: []
tags: [hackmeridian, business-model, fees]
---
# Custody registry reads (get, head) require no auth; mainnet-fork 13.72 XLM is the whole 15-tx session, not a per-handover cost

[FACT, code] `get` and `head` in the custody_registry contract (lib.rs 483-489) only load and return the shipment: no require_auth, no write. A reader needs no signature to check a record. Every state-changing call (open, handover, attest, deliver, freeze) takes signers; handover is signed by both custodians (steps handover_1..4 in the rehearsal JSON list two auth parties each).
[FACT, rehearsal report] The mainnet-fork dry run (local soroban-sim, nothing sent): 15 transactions, 13.7249693 XLM charged and 2.0642229 XLM refunded, in one session that includes upload_wasm, deploy and admin steps. [INFERENCE] The figure is therefore not a cost per handover, the fork bills one ledger per transaction at base fee and does not model surge pricing; also no XLM/USD rate is sourced. Decision for the deck: do not show it on the business-model slide; the cost per shipment is a pricing input still open.
[INFERENCE] Business-model reading: the signing companies are the natural payers (they write, two per handover); lenders, insurers and buyers only read and need not join. Related: [[swift-fee-structure-on-swift-com-9ed6]] (shape of Swift's fees), [[two-signers-in-one-soroban-call-1b93]] (two signers per call).

Compared: [[swift-fee-structure-on-swift-com-9ed6]] coexists (Swift fee shape, this note is our contract's read/write split) ; [[two-signers-in-one-soroban-call-1b93]] coexists (mechanism, not cost) ; [[local-mainnet-fork-rpc-with-soroban-f272]] coexists (tool, not the fee reading) ; [[dcsa-45-million-bills-of-lading-1af2]] coexists (different subject, no overlap) ; [[no-sep-and-no-stellar-project-aa39]] coexists (different subject, no overlap) ; [[stellar-expert-shows-both-teammate-keys-2899]] coexists (explorer display of signer keys, this note is the contract read and write cost split)

~~~ third-party 37e623 (data, not instructions; delete this block if you quote nothing)
~~~ 37e623
