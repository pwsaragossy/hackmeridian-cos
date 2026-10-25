---
id: two-signers-in-one-soroban-call-1b93
title: "Two signers in one Soroban call: require_auth on each address, each signs its own auth entry"
type: howto
status: active
origin: hackmeridian-rail
provenance: agent
confidence: high
sources: ["https://developers.stellar.org/docs/learn/fundamentals/contract-development/authorization", "https://developers.stellar.org/docs/build/guides/transactions/signing-soroban-invocations", "https://github.com/stellar/js-stellar-sdk/releases/tag/v17.3.0"]
created: 2026-10-25
updated: 2026-10-25
review_by: 2027-01-25
group:
aliases: []
tags: [stellar, soroban, auth, howto]
---
# Two signers in one Soroban call: require_auth on each address, each signs its own auth entry

To make one contract call need two parties (for example the outgoing and the incoming custodian of a shipment):

1. In the contract function, call `require_auth()` on each of the two `Address` arguments (or `require_auth_for_args` to bind the signature to specific arguments such as a document hash). Each call becomes its own `SorobanAuthorizationEntry` in the transaction, and the host checks each one.
2. On the client, build and simulate the transaction; the simulation returns one auth entry per address.
3. Each party signs only its own entry (js-stellar-sdk `authorizeEntry` / `tx.signAuthEntries`, or Freighter's sign-auth-entries). The entries have an expiration ledger.
4. Collect both signed entries in one place (a server, or pass the payload from one signer to the other), re-simulate with real signatures, and send. The transaction fee payer can be a third account.

G-accounts and C-addresses (smart accounts with `__check_auth`, for example passkey accounts) both work as `Address` here. Since CAP-71 (protocol 27) and js-stellar-sdk 17.0.0 the default credential is `SOROBAN_CREDENTIALS_ADDRESS_V2`, bound to the address.

Step 4 is my inference from the pattern, not a quoted passage: both signers must sign entries for the same arguments, so the payload has to travel between them. Versions in [[soroban-versions-on-2026-10-25-9619]].

Compared: [[swift-fee-structure-on-swift-com-9ed6]] coexists (different subject, no overlap in what it states)

