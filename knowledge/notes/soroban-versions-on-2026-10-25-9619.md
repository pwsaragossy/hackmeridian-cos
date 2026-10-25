---
id: soroban-versions-on-2026-10-25-9619
title: "Soroban versions on 2026-10-25: sdk 29.0.1, testnet protocol 29, OpenZeppelin 0.8.0 needs sdk 28"
type: finding
status: active
origin: hackmeridian-rail
provenance: agent
confidence: high
sources: ["https://github.com/stellar/rs-soroban-sdk/releases/tag/v29.0.1", "https://github.com/stellar/stellar-core/releases/tag/v30.0.0", "crates.io stellar-tokens 0.8.0 (checked 2026-10-25)", "soroban-testnet.stellar.org getVersionInfo (2026-10-25)"]
created: 2026-10-25
updated: 2026-10-25
review_by: 2026-11-25
group:
aliases: []
tags: [stellar, soroban, versions]
---
# Soroban versions on 2026-10-25: sdk 29.0.1, testnet protocol 29, OpenZeppelin 0.8.0 needs sdk 28

As of 2026-10-25, the newest `soroban-sdk` is 29.0.1 (2026-10-12; it fixes a wrong wasmi pulled in by 29.0.0 of 2026-10-07). The public testnet RPC answered `getVersionInfo` with stellar-core 30.0.0 and **protocolVersion 29**: the core binary for protocol 30 shipped on 2026-10-16, but the network has not voted 30 yet. The newest stellar-cli seen is 28.1.0 (2026-09-26).

OpenZeppelin `stellar-tokens`, `stellar-access` and `stellar-macros` are at 0.8.0 on crates.io and require `soroban-sdk ^28.0.0`, so they do not build together with 29.x. For a new contract on testnet today: `soroban-sdk = "29.0.1"` and no OpenZeppelin crate, or pin sdk 28 to use OpenZeppelin.

Older SDK lines: advisory GHSA-x2hw-px52-wp4m (CVE-2026-32322) is fixed in 25.3.0 and 23.5.3; contracts on older 25.x or 23.x should upgrade. The bug detail was not read.

Re-check before relying on it: these numbers change every few weeks, and a protocol 30 vote on testnet changes the SDK choice. Dual-signer auth is in [[two-signers-in-one-soroban-call-1b93]].

Compared: none similar

