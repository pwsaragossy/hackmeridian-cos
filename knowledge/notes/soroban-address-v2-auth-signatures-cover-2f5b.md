---
id: soroban-address-v2-auth-signatures-cover-2f5b
title: "Soroban ADDRESS_V2 auth signatures cover the address too (CAP-71): verify with the WithAddress preimage"
type: finding
status: active
origin: hackmeridian-rail
provenance: agent
confidence: high
sources: ["@stellar/stellar-sdk 17.3.0 src/base/auth.ts (buildAuthorizationEntryPreimage, via lib/esm/base/auth.js.map)", "three-machine check 2026-10-25: response-vhendala.json and response-leo.json verified, negative test refused"]
created: 2026-10-25
updated: 2026-10-25
review_by: 2027-04-25
group:
aliases: []
tags: []
---
# Soroban ADDRESS_V2 auth signatures cover the address too (CAP-71): verify with the WithAddress preimage

On protocol 29 testnet, simulation and the SDK produce `sorobanCredentialsAddressV2` entries. For these (and `...WithDelegates`), the signed payload is sha256 of `HashIdPreimage.envelopeTypeSorobanAuthorizationWithAddress({networkId, nonce, invocation, address, signatureExpirationLedger})`: the signer's address is bound into the payload (CAP-71). Legacy `sorobanCredentialsAddress` entries use `envelopeTypeSorobanAuthorization` without the address. A verifier that builds the legacy preimage reports a valid V2 signature as invalid (seen 2026-10-25 when checking Vhendala's signed entries; the corrected check passed for both custodians and refused the same file against the wrong key).

How to verify a signed entry from another machine without trusting its tool: decode the entry, compare `rootInvocation.toXDR()` bytes and the nonce with the unsigned entry you prepared, then check the ed25519 signature in the `signature` ScVal against the WithAddress payload above. In js-stellar-sdk 17.3.0, XDR values are plain objects (`entry.credentials.addressV2`, `entry.rootInvocation`), see [[two-signers-in-one-soroban-call-1b93]] and [[sign-soroban-auth-entries-on-another-e4dd]].

Compared: [[two-signers-in-one-soroban-call-1b93]] coexists (how to sign two entries in one call, this note is how to verify one) ; [[sign-soroban-auth-entries-on-another-e4dd]] coexists (the remote signing flow, this note is the payload detail a checker needs)
