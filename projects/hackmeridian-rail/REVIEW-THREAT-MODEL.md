# Review: README "Threat model and known limits" (rio-miami-rail HEAD b790cdf)

Verdict: **approve with changes.** No row is false at its core, but four "Yes" cells overclaim or hide who enforces them, one number is unsupported, and six limits a Soroban reader will find in lib.rs are missing.

Checked: `cargo test` from the repo root ran 26 tests, all passed (24 in `test::`, 2 in `prop_test::`; `/tmp/ct.log`). `grep upgrade|update_current_contract_wasm contracts/` finds nothing, so "no upgrade function" is true. TTL: 120,960 ledgers x 5 s = 7 days, 518,400 x 5 s = 30 days (right). Tx 864fd164 decoded: 2 auth entries, one source-account (operator, the tx source) and one for holder GBPFJ...GDJ; the effect is a 1.0000000 RMR1 clawback from that holder; `holder_balance_after_redeem` is "0". So the holder row's facts hold.

## Findings (most serious first)

### 1. Row "Skipping a stop..." and README step 5: the burn gate is off chain (major, add to the holder row)
Code: `scripts/lifecycle.mjs:200-205` checks `status == Delivered` in JS and then calls `transfer_agent.redeem`. Nothing on chain ties the redeem to `Delivered`. The holder row says "Ownership matters only where the token moves" but never says that this step is not gated by the registry (README line 21 does say it; the threat table must too).
Replace the holder row with:

| Delivering to someone who does not hold the token, or burning without delivery | No | `deliver` needs the signature of the `holder` address it is given, but the registry never checks that this address holds the token, and `open` never checks that `token` is a real token. The registry does not gate the burn either: `Delivered` is checked by our script before it calls the Radox `transfer_agent` (`scripts/lifecycle.mjs`), not on chain. In the demo, `redeem` (tx `864fd164…`) was signed by the operator and the real holder and took the holder's balance to 0. |

### 2. Row "Replaying a signature..." (mixes host and client, "Yes" is too wide)
Quote: "Yes | Soroban auth entries carry a nonce and an expiry, and are bound to the contract, function and arguments. `scripts/remote-auth.mjs` also refuses ..."
The first sentence is true, but it is the Soroban host that enforces it, not `custody_registry`; add the network passphrase (it is in the signed preimage, `authorizeEntry(..., NET)`). The second sentence is a client check on the custodian's machine, not on chain, and it checks only the registry address the custodian is told; it does not check the registry's wasm. A signed entry is valid until its expiry (36 h by default, 7 days maximum), and whoever holds the response file chooses when to submit it.
Replace with:

| Replaying a signature, or reusing it for another call | Yes, by the Soroban host | Each auth entry is signed over the network, a nonce, an expiry ledger and one invocation (contract, function, arguments), and the nonce is used once. The contract adds nothing here. Off chain, `scripts/remote-auth.mjs sign` refuses entries for another registry, other functions, sub-calls or unknown addresses before signing; it trusts the registry address it is given and does not check that registry's code. A signed entry stays valid until its expiry (36 h by default) and can be submitted by whoever holds it. |

### 3. Row "A custodian hands over without the other side agreeing": "tries every signer set" is not what the test does
Quote: "tries every signer set without both custodians".
`prop_handover_needs_both_custodians` draws one random mask of 4 candidates (from, to, two strangers) per case, 64 cases, fixed seed (`prop_test.rs:34-45, 296-`). The operator is not a candidate. State changed is checked as `(seq, head)` only.
Replace: "The property test `prop_handover_needs_both_custodians` draws random signer sets from {from, to, two strangers} (64 seeded cases); every set without both custodians is refused and `seq` and `head` are unchanged. `handover_without_incoming_signature_fails` and `..._outgoing_...` cover the two single-signer cases by name."
Also the "Skipping a stop" row: "random routes ... random call sequences" is accurate; add "(64 seeded cases)" so "random" is not read as exhaustive.

### 4. Row "Bugs in the contract": "fixed 2 major issues" has no source
Quote: "A review before deploy fixed 2 major issues."
Nothing in the repo or in `THREAT-MODEL.md` supports "2" or "major"; commit `9b66e00` lists five fixes (deliver needs every handover, TTL bumps, assurance range, holder recorded, pause covers sources). A judge who reads the log will count.
Replace: "26 tests pass (24 unit, 2 seeded property tests). A review before the testnet deploy led to the fixes in commit `9b66e00`. It has not been audited."

### 5. Row "State archival": slightly too strong
Quote: "Every write extends the instance and the shipment to about 30 days (518,400 ledgers)."
`extend_ttl(120_960, 518_400)` extends only when under 7 days remain. `remove_source`, `resume`, `set_pauser` and `emergency_pause` do not bump the instance. Source entries are bumped only by `add_source` and `attest`; contract code (wasm) TTL is not bumped by the contract at all.
Replace: "Writes to a shipment extend the instance and that shipment to about 30 days (518,400 ledgers) when under 7 days remain. Source entries are extended only when added or used, and the contract code's TTL is the deployer's to extend. An idle shipment or source can archive; it can be restored."

### 6. Row "A powerful admin": incomplete
Quote: "It cannot change a route, a custodian or the head."
True, but missing: the admin (and the optional pauser via `emergency_pause`) can halt every shipment's writes at once (only the admin resumes); there is no `set_admin` or `set_operator`, so a lost or compromised admin or operator key cannot be replaced (a new deploy is the only fix); in the demo, one address is both admin and operator (`remote-auth.mjs` constructor args). A registered source can also attest on any shipment, including Delivered and Frozen ones (see new row 3).
Replace the cell: "The admin can freeze or unfreeze, pause or resume, set one emergency pauser, and add or remove event sources. It cannot change a route, a custodian or past head values. A pause stops all writes on every shipment. There is no way to rotate the admin or operator key. The contract has no upgrade function: a new version is a new deploy."

### 7. Row "Rewriting or reordering history": say who is the attacker
On chain, the ledger itself is the history; the head matters for the off-chain copy (the Radox database, a mirror). "Yes, detectable" is right but unexplained. Add: "The threat is an off-chain copy (an indexer or database) that differs from the chain." Also `attest` is allowed after `Delivered` or `Frozen` (test comment "accepted in any status, by design"), so `final_head` can still move after delivery; say so in the new row below.

## Missing rows (a lib.rs reader will look for each)

Add after "A powerful admin":

| The operator alone chooses the route | No | `open` needs only the operator's signature. The custodians on the route do not consent at `open`; they consent only at their own handover. A wrong or hostile route cannot be corrected: the key is spent (`DuplicateKey`), and the only exit is `freeze`. |
| A custodian refuses to sign | No | Any custodian on the route can stop the shipment by not signing. There is no timeout or dispute step. The admin can only `freeze`. |
| Event sources (`attest`) | Limited | A registered source can append an attestation to any existing shipment, in any status (including Delivered and Frozen), with an arbitrary `kind` and `event_hash`; it blocks nothing and changes the `head`. The admin decides who is a source. |
| What the head proves | No | `evidence_hash` and `assurance` (1 to 3) are values the two custodians choose; the contract does not check what the hash points to or what the level means. |
| Who can read | Not private | `get`, `head` and `version` need no signature, and all state and events are public on chain. Do not put anything confidential in a key, a route or an evidence hash input. |
| Final custodian is also the holder | No (limit) | `deliver` calls `require_auth` on `final_custodian` and `holder`; if they are the same address the host refuses (same cause as the self-handover case noted in `prop_test.rs`). Not run by us; confirm with a test before keeping this sentence. |

Last row is a low-confidence finding (inferred from the test comment, not executed); drop it if it cannot be shown with a one-test run.

## Rows confirmed
- "Skipping a stop, going backwards, or delivering early": errors #1, #2, #10 match `WrongCustodian`, `OutOfRoute`, `NotFinal`; `deliver` requires `seq == last`.
- "Custodians that collude": true. Check separately that `proofs/three-machine.json` carries no `rehearsal: true` (it does not) before keeping "teammates' own keys on their own computers".
- "Lost custodian key" and "A second token...": true as written.
- "no upgrade function": true.
