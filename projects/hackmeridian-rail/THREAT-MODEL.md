# Threat model section for the README (leo-agent, 2026-10-25)

Paste-ready for the README, after "Production path" (the rail session owns README.md). Every line
is backed by the contract (`contracts/custody_registry/src/lib.rs` at 56c149c), a test, or a tx.
The long version with citations is JUDGE-QA.md.

---

## Threat model

What the contract enforces, and what it does not. Testnet only, no audit.

| Threat | Enforced on chain? | How, or why not |
|---|---|---|
| A custodian hands over without the other side agreeing | Yes | `handover` calls `require_auth()` on both `from` and `to`. The property test `prop_handover_needs_both_custodians` tries every signer set without both custodians, and all of them are refused with the state unchanged. |
| Skipping a stop, going backwards, or delivering early | Yes | `to` must be the next stop, `from` the current custodian, and `deliver` needs `seq` at the last stop (errors #1, #2, #10). The property test `prop_route_invariants_and_head_chain` runs random routes (with revisits) and random call sequences against a model. |
| Rewriting or reordering history | Yes, detectable | Each step folds into the 32-byte `head`. Anyone replays the transactions from Horizon and compares (`scripts/verify-head.mjs`, MATCH on both shipments). The head verifies history; it cannot rebuild it. |
| Replaying a signature or reusing it for another call | Yes | Soroban auth entries carry a nonce and an expiry, and are bound to the contract, function and arguments. `scripts/remote-auth.mjs` also refuses other registries, functions, sub-calls and unknown addresses before signing. |
| Custodians that collude, or keys held by one party | No | Two colluding custodians can sign a handover that never happened. The head proves who signed, not that the cargo moved. In our first shipment one harness held every key. The second shipment used teammates' own keys on their own computers. |
| Lost custodian key | Partly | A shipment stops at that stop. The admin can `freeze` it ("lost or seized cargo"). There is no key rotation inside a shipment. |
| A powerful admin | Limited | The admin can freeze or unfreeze, pause or resume, and manage the source allow-list. It cannot change a route, a custodian or the head. The contract has no upgrade function: a new version is a new deploy. |
| State archival | Mitigated | Every write extends the instance and the shipment to about 30 days (518,400 ledgers). An idle shipment can still archive, and it can be restored. |
| A second token, or a paper bill of lading, for the same cargo | No | It is not prevented on chain (README "Production path"). |
| Bugs in the contract | Not ruled out | 24 unit tests and 2 property tests pass. A review before deploy fixed 2 major issues. It has not been audited. |
