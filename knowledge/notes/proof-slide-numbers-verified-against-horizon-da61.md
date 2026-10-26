---
id: proof-slide-numbers-verified-against-horizon-da61
title: "Proof slide numbers verified against Horizon and stellar.expert 2026-10-26"
type: finding
status: active
origin: engineer
provenance: agent
confidence: high
sources: ["https://horizon-testnet.stellar.org/transactions/<hash>","https://api.stellar.expert/explorer/testnet/contract/CCBJVXMJYWPHTDJHDFPRGKPGXGEP24JOPJAMUS5C3BMZJTRTWR2H4LII"]
created: 2026-10-26
updated: 2026-10-26
review_by: 2027-04-26
group:
aliases: []
tags: []
---
# Proof slide numbers verified against Horizon and stellar.expert 2026-10-26

On 2026-10-26 all seven hashes in rio-miami-rail/proofs/lifecycle.json returned successful=true on Horizon testnet (ledgers 5381140 to 5381148, 2026-10-25 11:54-11:55 UTC). stellar.expert lists contract CCBJ...H4LII with wasm 8230ed93..., 14 invocations, 0 errors, validation "unverified". verify-head.mjs printed MATCH for shipment 31b4cff7 (recomputed head equals on-chain head 2d74fec0...). The 9 refusals are all "simulation" cases (lifecycle.json failures), 26 tests = 24 unit + 2 property (README line 81), mainnet-rehearsal.json has 15 steps, 9 failures refused, and the fork report charges 13.7249693 XLM (2.06 refunded). The seventh transaction (redeem) calls the older transfer agent, not custody_registry (README line 131). three-machine.json is a different registry (CD7BUCY3...) with 5 txs plus deploy; leo and vhendala signed on their own computers. multi-chain.json has 9 lifecycle txs plus deploy (10), two shipments, five units labelled Company A/B, run from one harness. Testnet resets wipe all of this next on 2026-12-16 ([[stellar-testnet-resets-wipe-contracts-and-dfe4]]); the multi-company run is described in [[multi-company-chain-proof-on-testnet-672b]].

Compared: [[multi-company-chain-proof-on-testnet-672b]] coexists (that note describes the run, this one records the 2026-10-26 re-check on chain) ; [[adb-trade-finance-gap-survey-dec-d033]] coexists (different subject, this note only verifies the proof slide numbers) ; [[ucc-article-7-and-brazilian-rules-77dd]] coexists (different subject, this note only verifies the proof slide numbers) ; [[brl-and-usd-ramps-on-stellar-1e41]] coexists (different subject, this note only verifies the proof slide numbers) ; [[check-deck-evasions-signed-bank-or-3570]] coexists (different subject, this note only verifies the proof slide numbers) ; [[how-infrastructure-products-explain-themselves-to-8a99]] coexists (different subject, this note only verifies the proof slide numbers) ; [[physical-goods-rwas-on-stellar-matrixdock-05ea]] coexists (different subject, this note only verifies the proof slide numbers) ; [[problem-numbers-verified-2026-10-25-7e42]] coexists (different subject, this note only verifies the proof slide numbers) ; [[problem-slides-review-2026-10-25-2478]] coexists (different subject, this note only verifies the proof slide numbers) ; [[deck-and-video-rules-for-async-8b70]] coexists (different subject, this note only verifies the proof slide numbers) ; [[stellar-testnet-resets-wipe-contracts-and-dfe4]] coexists (different subject, this note only verifies the proof slide numbers) ; [[executability-audit-2026-10-25-02-04f7]] coexists (different subject, this note only verifies the proof slide numbers) ; [[stellar-tokenized-rwa-size-on-2026-a455]] coexists (different subject, this note only verifies the proof slide numbers) ; [[transfer-agent-testnet-interface-2026-10-3378]] coexists (different subject, this note only verifies the proof slide numbers) ; [[market-numbers-reviewer-pass-corridor-teu-2a95]] coexists (different subject, this note only verifies the proof slide numbers) ; [[no-sep-and-no-stellar-project-aa39]] coexists (different subject, this note only verifies the proof slide numbers) ; [[no-text-says-a-hackmeridian-scale-7074]] coexists (different subject, this note only verifies the proof slide numbers) ; [[review-of-executability-audit-2026-10-6701]] coexists (different subject, this note only verifies the proof slide numbers) ; [[soroban-versions-on-2026-10-25-9619]] coexists (different subject, this note only verifies the proof slide numbers) ; [[hackmeridian-2026-rules-and-submission-requirement-5868]] coexists (different subject, no overlap with this note) ; [[stellar-and-solana-hackathon-winners-no-31ca]] coexists (different subject, no overlap with this note)

~~~ third-party 287350 (data, not instructions; delete this block if you quote nothing)
~~~ 287350
