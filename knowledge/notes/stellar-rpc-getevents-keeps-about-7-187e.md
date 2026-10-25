---
id: stellar-rpc-getevents-keeps-about-7-187e
title: "Stellar RPC getEvents keeps about 7 days: keep current state in contract storage"
type: finding
status: active
origin: hackmeridian-rail
provenance: agent
confidence: medium
sources: ["https://developers.stellar.org/docs/data/apis/rpc/admin-guide/configuring (default retention 120960 ledgers, about 7 days, operator-configurable; read 2026-10-25)","https://developers.stellar.org/docs/build/guides/events/publish", "https://developers.stellar.org/docs/build/guides/events/replay-ledger-close-meta", "https://developers.stellar.org/docs/build/smart-contracts/example-contracts/events"]
created: 2026-10-25
updated: 2026-10-25
review_by: 2027-01-25
group:
aliases: []
tags: [stellar, events, rpc, architecture]
---
# Stellar RPC getEvents keeps about 7 days: keep current state in contract storage

Stellar RPC `getEvents` returns contract events from a retention window of about 7 days (the docs say 7 days in general; the exact window of the public testnet RPC was not checked). Older history needs an indexer (replaying ledger close meta) or a third-party indexer.

Consequence for design: anything a demo, page or judge must read after a week (current holder, handover count, the last attestation) belongs in contract storage, with events only as the feed. An on-chain hash chain (`head` updated on each step) lets anyone verify an off-chain copy of the full history later.

Current event form in Rust is the `#[contractevent]` macro; `env.events().publish` looks like the legacy path (inference from the official example; formal deprecation not verified). On testnet, stellar-core 25.1.0 cut the maximum entry TTL to about 4 weeks, so persistent storage needs TTL extension for anything longer. Related: [[soroban-versions-on-2026-10-25-9619]].

Compared: none similar

