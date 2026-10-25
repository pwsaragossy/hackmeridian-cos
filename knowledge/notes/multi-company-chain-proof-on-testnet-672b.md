---
id: multi-company-chain-proof-on-testnet-672b
title: "Multi-company chain proof on testnet: 10 transactions successful on Horizon, two test companies on one registry"
type: finding
status: active
origin: hackmeridian-rail
provenance: agent
confidence: high
sources: ["https://horizon-testnet.stellar.org/transactions/<hash> for the 10 hashes in rio-miami-rail proofs/multi-chain.json (checked 2026-10-25 ~19:40 UTC)"]
created: 2026-10-25
updated: 2026-10-25
review_by: 2027-04-25
group:
aliases: [multi-chain proof, one rail several supply chains]
tags: [hackmeridian, proof, testnet, deck]
---
# Multi-company chain proof on testnet: 10 transactions successful on Horizon, two test companies on one registry

[FACT, high] The 10 transaction hashes in rio-miami-rail `proofs/multi-chain.json` (registry CDDWEENF6DKM4AHFWDBHQTYPLC3STMVFPXHXYDORLD53WDZM3FF3KJX4, a second instance of the existing contract code) all return `successful: true` on Horizon testnet, created between 19:19:27 and 19:20:17 UTC on 2026-10-25. The file has two shipments, TEST3286578 and TEST3286579, routed over test keys labelled Company A and Company B. The labels come from an off-chain directory and are not a contract field. The two routes share stops.
[FACT] Pushed: GitHub main 7dd63f7 holds proofs/multi-chain.json (checked with gh api, 2026-10-25 19:40 UTC). The run's commit is ef0ca00 on GitHub; the local hash 9fed1c8 was replaced by a cherry-pick, so never cite 9fed1c8. Central checked both heads: MATCH offline and live.
Safe deck wording: "two test companies' chains on one registry, sharing stops, each dual-signed". Never "real companies" or "pilot". Dual signing per handover: [[two-signers-in-one-soroban-call-1b93]].

Compared: [[two-signers-in-one-soroban-call-1b93]] coexists (how dual signing works, this note is one run that used it) ; [[ucc-article-7-and-brazilian-rules-77dd]] coexists (different subject, no overlap in what it states) ; [[soroban-versions-on-2026-10-25-9619]] coexists (SDK versions, not a proof run) ; [[stellar-testnet-resets-wipe-contracts-and-dfe4]] coexists (the reset on 2026-12-16 will wipe this run, keep the hashes as the record) ; [[transfer-agent-testnet-interface-2026-10-3378]] coexists (token contract interface, not the custody proof)
