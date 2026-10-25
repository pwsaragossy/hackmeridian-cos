---
id: js-stellar-sdk-17-3-0-a83c
title: "js-stellar-sdk 17.3.0 on protocol 29: auth entries are plain objects with sorobanCredentialsAddressV2"
type: finding
status: active
origin: hackmeridian-rail
provenance: agent
confidence: high
sources: ["rio-miami-rail package-lock.json (@stellar/stellar-sdk 17.3.0, @stellar/js-xdr 5.0.0)", "rio-miami-rail scripts/lib/stellar.mjs:46,56-64,79", "testnet tx c6d06f2f9059b6c68074018103e1b64797035adc94e54b598b22568c9ab01c07"]
created: 2026-10-25
updated: 2026-10-25
review_by: 2027-04-25
group:
aliases: []
tags: [stellar, soroban, js-sdk]
---
# js-stellar-sdk 17.3.0 on protocol 29: auth entries are plain objects with sorobanCredentialsAddressV2

[FACT, observed 2026-10-25 on testnet protocol 29, see [[soroban-versions-on-2026-10-25-9619]]] With `@stellar/stellar-sdk` 17.3.0 (lockfile pulls `@stellar/js-xdr` 5.0.0), the auth entries returned by `simulateTransaction` are plain objects: `entry.credentials.type`, not `entry.credentials()`. Old accessor-style code crashes client-side with `TypeError: e.credentials is not a function` before anything is sent. Protocol 29 simulation returns `type: 'sorobanCredentialsAddressV2'` with the address under `credentials.addressV2` (not `.address`). `authorizeEntry(entry, keypair, validUntilLedger, passphrase)` signs these entries as they are; build the op with `Operation.invokeContractFunction({ contract, function, args, auth })`. Working code: rio-miami-rail `scripts/lib/stellar.mjs` (`credOf = e.credentials.addressV2 ?? e.credentials.address`). First dual-signed success with this pattern: c6d06f2f… The general two-signer method is in [[two-signers-in-one-soroban-call-1b93]].

[INFERENCE] That the plain-object shape comes from js-xdr 5 (rather than the SDK layer) was not traced in source.

Compared: [[soroban-versions-on-2026-10-25-9619]] coexists (that note pins Rust, CLI and protocol versions, this one the JS client behaviour on that protocol); [[executability-audit-2026-10-25-02-04f7]] coexists (audit of the plan, not SDK behaviour); [[two-signers-in-one-soroban-call-1b93]] coexists (general method, this adds the 17.3.0 V2 object shape)
