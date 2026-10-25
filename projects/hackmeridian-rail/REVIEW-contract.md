Role: reviewer
Reviewing: engineer output, `custody_registry` contract — rio-miami-rail commit 3ce8880, `contracts/custody_registry/src/lib.rs` + `src/test.rs`, against `projects/hackmeridian-rail/LEO-BRIEF.md` (Design, head byte layout, Hard rules)
Verdict: approve with changes
Reason: auth, head layout and error codes match the brief byte for byte (head vector recomputed independently); one state-machine hole lets `deliver` skip every handover when the route revisits an address, and the contract instance TTL is never extended, which puts the page's later reads at risk.

## Findings (ranked by severity)

1. [major] **`deliver` can fire at seq 0 when the route revisits an address.** `open` refuses only *adjacent* duplicates (lib.rs:251-255); `deliver` checks `final_custodian == last && == current_custodian` (lib.rs:359-360) but never `seq == route.len()-1`. With route `[A, B, A]` the shipment opens with A as current custodian, A is also last, so A + any holder deliver with zero handovers. — evidence: [FACT] reproduced, scratch test `rv_deliver_without_any_handover_when_route_revisits` (status Delivered, seq 0) in a copy of the crate; confidence high. The brief's wording ("last of the route and the current custodian", Design §deliver) has the same gap, so the code follows the letter of the spec. The demo route (5 distinct roles) is not affected; the hole matters because the redeem precondition is "status == Delivered". — fix: in `deliver` require `s.seq == s.route.len() - 1` (return `NotFinal`), and/or refuse any repeated address in `open` (`BadRoute`); add the test.

2. [major] **Contract instance TTL is never extended.** Admin, Operator, Paused, Pauser live in instance storage (lib.rs:225-227, 421, 432) and no function calls `env.storage().instance().extend_ttl`. Testnet state-archival settings read live 2026-10-25 (getLedgerEntries, ConfigSetting STATE_ARCHIVAL, ledger 5380892): `minPersistentTTL = 120960` (~7 days), `maxEntryTTL = 3110400`. Shipment entries are bumped to 518400 (lib.rs:200-211), but the instance (and the wasm code entry) that every call needs is left at whatever the deploy gave it. — evidence: [FACT] scratch test `rv_instance_and_source_ttl_not_extended`: instance TTL unchanged across a full lifecycle. [SUSPICION, low-medium] once the instance archives (~7 days after deploy, i.e. inside the judging window if judging runs past ~1 Nov), the public page's *simulated* `head(key)` read may return a restore preamble instead of a value; I did not verify simulation behaviour on archived instances. — fix: extend instance TTL in every write (and in `load`), or run `stellar contract extend --durability persistent` on instance + wasm after deploy and record it in DEPLOYMENTS.md.

3. [minor] **Source registrations decay.** `attest` checks `has(Source)` (lib.rs:326-332) but never extends it; only `add_source` does (lib.rs:409-411). — evidence: [FACT] scratch test: source TTL 518400 → 118400 after 400 000 ledgers and an attest. Mitigated by protocol auto-restore on writes. — fix: extend the Source key in `attest`.

4. [minor] **Pause does not cover admin writes.** Brief: "pause / resume … checked by every write". `freeze`, `unfreeze`, `add_source`, `remove_source`, `set_pauser` never call `require_not_paused` (lib.rs:375-435). — evidence: [FACT] scratch test `rv_admin_writes_ignore_pause` passes; the in-repo test name `pause_blocks_every_write` (test.rs:356) overclaims. Letting the admin freeze during a pause is defensible, but it is an undocumented deviation. — fix: either add the check or write the exception on the card and rename the test.

5. [minor] **`assurance` is unbounded.** Brief defines 3/2/1; handover accepts any u32 (lib.rs:285, no check). — evidence: [FACT] scratch test `rv_assurance_unbounded` (0 and u32::MAX accepted). Also note the value is self-declared: the contract requires both signatures in every case, so "2 = one by delegation" and "1 = external attestation only" cannot be told apart on-chain. — fix: refuse values outside 1..=3 with a new error code; say in the README that assurance is a declared label.

6. [minor] **`attest` runs on Frozen and Delivered shipments and moves `head`.** lib.rs:333-335 does not look at status. — evidence: [FACT] scratch test `rv_attest_after_delivered_and_frozen_moves_head`. Consistent with "blocks nothing", but `head(key)` keeps changing after the redeem precondition was read; `verify-head` must list post-delivery attests in `proofs/lifecycle.json` or it will not match. — fix: decide on the card (refuse after Delivered, or document); test it either way.

7. [minor] **Holder is not recorded.** `deliver` takes `holder` with auth (lib.rs:356) but stores nothing about it in `Shipment`; only the event (≈7-day retention) and the tx parameters carry it. The off-chain policy "co-sign redeem only after Delivered" cannot check that the redeem `holder` is the one who signed `deliver` from `get(key)`. — evidence: [FACT] lib.rs:52-60, 363. — fix: optional `holder: Option<Address>` in Shipment, or accept and say so.

8. [minor] **Test gaps vs deliverable 1 ("every refusal path").** No test that `deliver` fails without the holder's signature, that `open` fails without operator auth (only `auths()[0]==operator` is asserted, test.rs:120-124), or that pause/add_source/remove_source/set_pauser/unfreeze reject a non-admin. `handover_without_incoming_signature_fails` (test.rs:412-438) is `#[should_panic]` with no expected message, so it would also pass on an unrelated panic. — fix: use `mock_auths` with the missing signer and assert `try_*` returns `Err(Err(_))` (auth error) per function.

9. [note] Route length is unbounded (lib.rs:248-255); a huge route only costs the operator fees. `token` is not validated as a contract. Extra error codes 8-12 beyond the brief's list are fine (one code per refusal holds). Freeze/unfreeze emit `status_changed`, which the brief does not name — fine, but tell the page author.

10. [note] `AI_USAGE.md` states "Leo: functions, auth checks and error codes against the design" as human review done. If that review has not happened yet (this review is an AI one), the line is a claim, not a fact (hard rule 8).

## Premises tested
| Premise | Evidence | Result |
|---|---|---|
| head layout matches the brief byte for byte | Independent Python recompute (`scratchpad/headvec.py`): `addr` = ScVal disc 18 ‖ ScAddress ACCOUNT 0 ‖ PublicKey ED25519 0 ‖ 32 bytes; tags 0x01/0x02/0x03; be32 | key, open and handover hex all equal test.rs:16-18. **Holds.** |
| `to_xdr` gives the ScVal XDR of the address | soroban-sdk-29.0.1/src/xdr.rs:101-105 (`serialize_to_bytes(val)`) | Holds; matches brief's `nativeToScVal(x,{type:"address"}).toXDR()` |
| handover hashes seq *after* +=1; attest hashes current seq | lib.rs:299-300, 334; test.rs:172, 176 | Holds |
| deliver/freeze/unfreeze do not touch head | lib.rs:348-403 | Holds |
| Both custodians must sign handover | lib.rs:288-289; test.rs:136-143, 412-438 | Holds (auth failures are host errors, not contract codes — expected) |
| final custodian + holder on deliver; operator on open; admin on freeze/pause/sources | lib.rs:240, 355-356, 376, 390, 406, 415, 420, 425, 430 | Holds in code; not all are negatively tested (finding 8) |
| deliver only after the full route | lib.rs:359-360 | **Fails** for revisiting routes (finding 1) |
| Event names are `opened`, `handover`, `attested`, `delivered` | soroban-sdk-macros-29.0.1/src/derive_event.rs:126 (`to_snake_case` of struct name) | Holds |
| TTL extended on read and write (shipments) | lib.rs:197-212 | Holds for shipments; not for instance/sources (findings 2, 3) |
| Hard rule 3: sdk 29.0.1, no OpenZeppelin | Cargo.toml workspace dep, Cargo.lock (no `stellar-tokens/access/macros`), build output `soroban-sdk v29.0.1` | Holds |
| Hard rule 2: no transfer_agent code | lib.rs has no token calls; `token` is stored only | Holds |
| Hard rule 6: no secrets | `grep -rEn "S[A-Z2-7]{55}"` over the tree (excluding target): no hits; `.gitignore` covers `.env*`, `.stellar/`, keys | Holds |
| Hard rule 7: no partner names | grep for project/partner names and the Radox instance ID: no hits; test addresses are synthetic | Holds |
| Hard rule 11: licence | LICENSE 202 lines Apache-2.0; `license = "Apache-2.0"` workspace; copyright line in lib.rs:1 and test.rs:1 | Holds |
| `cargo test` 16/16 | Ran at 3ce8880 | Holds (16 passed) |

## Never-skip checklist
- Library claims cite [[id]]; new findings saved: cited notes used below; **no library.sh note saved** (this run had no library write instruction; the testnet archival numbers are a candidate note — see Questions).
- Specialist's Never-skip list checked: engineer card not supplied in the brief to this reviewer; audited against the brief's Deliverable 1 and Checks instead (below).
- ≥3 premises tested: done (table above, 15 rows).
- Load-bearing citations opened: brief, SDK source (xdr.rs, storage.rs, derive_event.rs), testnet RPC config — done.
- Key numbers recomputed: head vector (3 hashes) recomputed independently; TTL constants checked against live archival settings (120960 threshold = minPersistentTTL; 518400 < maxEntryTTL 3110400).
- Strongest contrary case written: done (below).
- Contradictions with library/other specialists: [[two-signers-in-one-soroban-call-1b93]] (two `require_auth`, one entry each) agrees with lib.rs:288-289; [[soroban-versions-on-2026-10-25-9619]] agrees with Cargo.toml. No other specialist output on this contract was available.
- Cited notes opened: all three opened, status active, no retire/merge judged in this work.
- Owner's manual work: listed below, feasible.
- Pre-mortem: done.
- Versions/outside judge: the judge named is the brief + `cargo test`; every finding points to a brief line, code line or reproduced scratch test.
- Severity + evidence per finding: done; suspicions labelled.

## Specialist's checklist audit (brief Deliverable 1 and Design)
- Contract with every function in Design (`__constructor`, open, handover, attest, deliver, freeze, unfreeze, pause, resume, emergency_pause, add_source, remove_source, get, head, version): **present**.
- `#[contracterror]` enum, one code per refusal incl. the 7 named: **present** (lib.rs:24-40).
- `#[contractevent]` events: **present**.
- Unit test 1 pins head with hex constants: **present** (test.rs:88-99), and the vector is right.
- "including every refusal path": **only partly** (finding 8).
- `verify-head.mjs --selftest` printing the same hex: **absent** (Deliverable 4, not due in this commit; test.rs:13 says it is shared).
- Refuse repeated key: **present** (lib.rs:241-247, test.rs:184-192).

## Strongest contrary case
"Approve as is": the operator is trusted and picks the route, so a revisiting route is an operator mistake, not an attack; the demo route has five distinct roles; auto-restore since protocol 23 makes TTL a fee question, not a correctness one; the brief's own deliver rule is what the code implements. Answer: true for the 7-transaction demo, which this code will pass. But a Stellar judge reading the contract sees that "Delivered" — the one bit the redeem policy trusts — can be reached with no handover, and a one-line `seq` check closes it; and the page is read after the demo, when instance TTL becomes live risk. Hence "approve with changes", not reject.

## Owner's manual work
1. Add the `seq == route.len()-1` check (and optionally refuse repeated addresses) + test — ~10 min.
2. Instance/source TTL extension, or a post-deploy `stellar contract extend` step recorded in DEPLOYMENTS.md — ~10 min.
3. Decide on the card: pause vs admin writes, attest after Delivered, assurance range — 5 min, then small code/test changes.
4. Re-run `cargo test`; regenerate test snapshots; commit (rule 9). All feasible before the 14:00 mentor read if started now.

## Pre-mortem
Six months on (or one week on): the judge opens the public shipment page after the demo, the `head(key)` simulated read fails because the contract instance archived ~7 days after deploy, and the "verify it yourself" claim visibly breaks. Second story: a mentor reading lib.rs spots that `deliver` does not check `seq`, builds `[A,B,A]`, and the dual-signed-custody claim is called unproven. Missing checks: an instance-TTL step in the deploy script, and a test that a revisiting route cannot deliver early.

## Not checked
- Behaviour of RPC `simulateTransaction` for a read whose contract instance is archived (finding 2's page impact) — not run on testnet.
- Testnet execution of any function (hard rule 5): no deployment exists in this commit (no DEPLOYMENTS.md, no proofs/).
- Two `require_auth` on the same address in one frame (e.g. `deliver` with holder == final_custodian): not tested; harmless either way.
- The engineer role card's own Never-skip list (not provided).
- Hard rule 1 timing: first commit d10cb84 is 2026-10-25 09:00:17 +0000; Lisbon is UTC+0 after the DST change at 02:00 that day, so it is after 09:00 Lisbon — checked, but not in scope.

## Questions for the owner
1. Should `open` refuse any repeated address on the route (not just adjacent), or should revisits be allowed with the `seq` check in `deliver`?
2. During a pause, may the admin still freeze/unfreeze and edit sources? (Brief says every write is checked.)
3. Is `attest` after Delivered allowed? If yes, the proof file must list those attest hashes or verify-head will fail.
4. Is the human review line in AI_USAGE.md for lib.rs already true?
5. Save the testnet archival settings (minPersistentTTL 120960, maxEntryTTL 3110400, read 2026-10-25) as a library note?

## Library
cited: [[two-signers-in-one-soroban-call-1b93]], [[soroban-versions-on-2026-10-25-9619]], [[transfer-agent-testnet-interface-2026-10-3378]] (opened; confirms the registry must not call transfer_agent — it does not)
saved: none

## Fixes applied (leo-agent, 2026-10-25, rio-miami-rail 9b66e00)
1. major, deliver with a repeated route address: `deliver` now also requires `seq == route.len() - 1`; test `repeated_address_in_route_cannot_skip_handovers`.
2. major, instance TTL: `bump_instance` on the constructor and every write (save, add_source, pause).
3. minor, source TTL: extended on every `attest`.
4. minor, pause and admin writes: `add_source` / `remove_source` now refuse while paused (test `pause_blocks_sources_but_not_freeze`). Kept on purpose: `freeze` / `unfreeze` work while paused, they are the exit a pause is for; `pause` / `resume` / `set_pauser` are the pause controls themselves.
5. minor, assurance range: error 13 `BadAssurance` outside 1..=3; test `refuses_assurance_out_of_range`.
6. minor, attest on Frozen/Delivered: kept — the brief says attest "blocks nothing"; a late customs or delivery-confirmation event is still evidence.
7. minor, holder not stored: `Shipment.holder: Option<Address>`, set on `deliver`; test `holder_recorded_on_delivery`.
8. minor, missing negative auth tests: added for handover (incoming and outgoing), open (operator), deliver (holder) and admin calls; the old `should_panic` replaced by a checked host auth error.
Result: `cargo test` 24/24, clippy clean; deployed as wasm 8230ed93… (DEPLOYMENTS.md).
