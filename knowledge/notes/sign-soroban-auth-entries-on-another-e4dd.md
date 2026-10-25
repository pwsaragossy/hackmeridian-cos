---
id: sign-soroban-auth-entries-on-another-e4dd
title: "Sign Soroban auth entries on another machine: custodian signs own entries, operator submits"
type: howto
status: active
origin: hackmeridian-rail
provenance: agent
confidence: high
sources: ["rio-miami-rail three-machine scripts/remote-auth.mjs (4d5707a, de412a5)", "@stellar/stellar-sdk 17.3.0 lib/esm/base/auth.js", "testnet rehearsal 2026-10-25, 3 handovers + deliver SUCCESS, verify-head MATCH"]
created: 2026-10-25
updated: 2026-10-25
review_by: 2027-04-25
group:
aliases: []
tags: [stellar, soroban, auth, howto, custody]
---
# Sign Soroban auth entries on another machine: custodian signs own entries, operator submits

[FACT, tested on testnet 2026-10-25] A party can authorise a Soroban call from its own computer without ever sharing its key, and the party that pays for the transaction can be someone else. Steps that worked with `@stellar/stellar-sdk` 17.3.0:

1. Operator machine: build each unsigned entry yourself, without simulating: an `xdr.SorobanAuthorizationEntry` with `sorobanCredentialsAddressV2` (address, random int64 nonce, empty signature) and a `rootInvocation` for the exact contract function and arguments, no sub-invocations. Building it by hand means entries for later steps (a second handover whose state does not exist yet) can be signed in the same round trip. Write the XDR (base64) and one agreed expiry ledger into a request file per signer.
2. Signer machine: decode the XDR itself, show contract, function, arguments and expiry in words, refuse anything not expected, then `authorizeEntry(entry, keypair, validUntilLedger, networkPassphrase)`, which signs a hash that covers the network, nonce, expiry, address (V2) and the whole invocation (SDK source, `buildAuthorizationEntryPreimage`). Write the signed XDR to a response file. It contains no secret.
3. Operator machine: check each signed entry has the same `rootInvocation` and address as requested, add the operator's own signed entries, put all in `Operation.invokeContractFunction({ auth })`, simulate (this verifies the signatures), `rpc.assembleTransaction`, sign as source, send. The signatures do not depend on the transaction source or sequence number, so the response can wait hours until the expiry ledger.

Gotchas: an account that signs must exist on-ledger (fund it with friendbot); in `invokeOp`-style helpers generate any random value (deploy salt) once, outside the closure that runs for both simulation and send, or the second run fails with `Auth, InvalidAction`; in 17.3.0 `rootInvocation.subInvocations` is an array property and the signature sits at `credentials.addressV2.signature` (JSON key `address_v2`). The signer cannot be fooled by a description field because it reads none; its remaining trust is the registry address and the list of known addresses, which must reach it by a second channel. Used by [[js-stellar-sdk-17-3-0-a83c]] conventions and the general idea in [[two-signers-in-one-soroban-call-1b93]].

[INFERENCE] The maximum allowed expiry (a ledger bound set by the network) was not measured; the tool asks for 36 hours at most by default and refuses requests over 7 days.

Compared: [[two-signers-in-one-soroban-call-1b93]] coexists (general method, this is the tested remote-machine variant with the request/response files); [[js-stellar-sdk-17-3-0-a83c]] coexists (SDK object shape, this uses it)

