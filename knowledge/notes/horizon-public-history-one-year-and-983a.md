---
id: horizon-public-history-one-year-and-983a
title: "Horizon public history one year and slated for deprecation; archived Soroban state is restored on access"
type: finding
status: active
origin: hackmeridian-rail
provenance: agent
confidence: medium
sources: ["https://developers.stellar.org/docs/data/indexers (undated, read 2026-10-25)","https://developers.stellar.org/docs/data/apis/horizon (note dated 2024-08-01, read 2026-10-25)","https://developers.stellar.org/docs/learn/fundamentals/contract-development/storage/state-archival (read 2026-10-25)"]
created: 2026-10-25
updated: 2026-10-25
review_by: 2027-04-25
group:
aliases: [Horizon deprecation, Horizon one year retention, state archival restore]
tags: [stellar, horizon, history, soroban, state-archival]
---
# Horizon public history one year and slated for deprecation; archived Soroban state is restored on access

[FACT, medium; read by an engineer specialist subagent on 2026-10-25]
- The Stellar indexers page says "Horizon will soon be deprecated, but for now it is the only way to get some of this data". It gives no date.
- The Horizon page notes that "the publicly accessible SDF-hosted Horizon had its historical data truncated to one year" (2024-08-01). It points to third-party Horizon providers for longer retention.
- Galexie exports ledger metadata to a data lake and is the base of the Composable Data Pipeline.
- Soroban persistent entries whose TTL expires are archived, not deleted, and are restored automatically when an InvokeHostFunction touches them; RestoreFootprintOp also restores them. A restored entry gets only a short TTL (current ledger + 4095, a network parameter). Temporary entries are deleted for good.
- Not found in the docs: whether events can be restored. Treat events as gone after the RPC window, which is about 7 days by default ([[stellar-rpc-getevents-keeps-about-7-187e]]).

Consequence for the rail: "replay from Horizon" works for the hackathon, not for years of history. Long-term history needs our own indexer (Galexie) or a third-party Horizon. ENGINEER-BRIEF.md question 2 asks a Stellar engineer which one.

Compared: [[stellar-rpc-getevents-keeps-about-7-187e]] coexists (that note is the RPC event window, this one is Horizon and state archival) ; [[multi-company-chain-proof-on-testnet-672b]] coexists (a proof run, not a data-retention fact) ; [[swift-fee-structure-on-swift-com-9ed6]] coexists (different subject, no overlap in what it states) ; [[two-signers-in-one-soroban-call-1b93]] coexists (authorization, not data retention) ; [[wording-market-figures-in-the-deck-dadf]] coexists (different subject, no overlap in what it states)
