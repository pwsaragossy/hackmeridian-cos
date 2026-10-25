# Judge Q&A: the 10 hardest technical questions (leo-agent, 2026-10-25)

For Pedro if we reach the 28 Oct final. Each answer cites a file in rio-miami-rail (main c2cff0b or later)
or a testnet transaction. Line numbers are for `contracts/custody_registry/src/lib.rs` at that commit.

**1. Your custodians are all your own test keys. What stops one party from faking a handover?**
In the first shipment nothing does, and we say so: one harness holds every key, so it proves the mechanism and not independence (README "Live demo").
The second shipment had Leo's and Vhendala's keys on their own computers. Only signed auth entries crossed machines (`scripts/remote-auth.mjs`, handovers 861544e4…, 9214980e…, 850da342…).

**2. Who holds the keys in production, and what happens if a custodian loses one?**
Each custodian holds its own Stellar account: a Soroban `Address` can also be a smart wallet or multisig, so key custody is the custodian's choice. The contract only calls `require_auth()` (lib.rs 303–304).
A lost key stops that shipment at that stop. The exit is the admin's `freeze` (lib.rs 394–396, "lost or seized cargo"). There is no key-rotation path inside a shipment, which is a known limit.

**3. How do you know both custodians really signed, when the explorer shows one signature?**
The explorer shows only the transaction source's envelope signature (the operator). The custodians sign Soroban authorization entries inside the call.
`node scripts/handover-signers.mjs` lists both entries for every handover from the saved envelopes in `proofs/tx/` and exits 0 (README "Architecture: Authorisation").

**4. What is the head, and what does it actually prove?**
It is a SHA-256 chain: open = `sha256(0x01‖key‖docs_root)`, then each handover and attest folds into the previous head (lib.rs 138–180; layout in README). One 32-byte value commits to the whole ordered history.
It proves integrity, not truth: anyone can replay the history and compare (`verify-head.mjs 31b4cff7…` gives MATCH, head 2d74fec0…), but the head cannot say that the physical handover happened.

**5. Why not just use contract events?**
Stellar RPC keeps about 7 days of history by default (`HISTORY_RETENTION_WINDOW` 120960 ledgers, developers.stellar.org RPC admin guide), and judging could fall after that.
verify-head and the page read each transaction's arguments from Horizon and replay them in ledger order, and `proofs/tx/` keeps Horizon copies for after a testnet reset (`verify-head.mjs --offline`).

**6. Will the data survive state archival (TTL)?**
Every write extends the contract instance and the shipment entry to 518,400 ledgers (about 30 days) once fewer than 120,960 are left (lib.rs 17–18, 187–222). The plugin reviewer flagged the missing instance bump before deploy, and it was fixed in 9b66e00 (workspace REVIEW-contract.md).
An idle shipment can still archive. On mainnet that means restoring it, or a keeper that extends TTL. Archived entries can be restored, not lost, but this is not built yet.

**7. Is the contract upgradeable? Who can change the rules?**
No: there is no `update_current_contract_wasm`. A new version is a new deploy, as the second registry CD7BUCY3… shows (same wasm 8230ed93…).
The admin can only freeze or unfreeze a shipment, pause or resume, set a pauser and manage the data-source allow-list (lib.rs 396–470). It cannot rewrite a route, a custodian or the head.

**8. What if a custodian refuses to sign, or signs the wrong next stop?**
Then the handover does not happen: both `require_auth` calls must pass. A wrong `from` returns error #1 WrongCustodian, a `to` that is not the next stop returns #2 OutOfRoute, and assurance outside 1–3 returns #13 (lib.rs 299–312).
All nine refusals are recorded with their codes in `proofs/lifecycle.json` `failures` (simulated). Deliver before the last stop returns #10 NotFinal.

**9. Can a signed authorization be replayed, or used for another call?**
No. Each Soroban auth entry carries a nonce and an expiry ledger and is bound to the exact contract, function and arguments, so the network rejects a replay.
`remote-auth.mjs sign` refuses any entry for another registry, another function, a sub-call or an unknown address before signing, and prints what it signs.

**10. What is between this and mainnet? Has it been audited?**
It has not been audited and runs only on testnet. Two other gaps are known: the testnet issuer keeps its master key (it must be locked on mainnet), and a paper bill of lading or a second token for the same cargo is not prevented on chain (README "Production path").
Plan: the SCF Audit Bank after an SCF award, and mainnet gating on the Radox platform until the test matrix passes. The redeem burn uses Radox's existing `transfer_agent` (prior work, tx 864fd164…).

**11. The page says "from 7 transactions", but verify-head prints 6 rows. Which is right?** (added by session-hackmeridian-rail, 2026-10-25, from the code)
Both are right; they count different things. The page counts every call to `custody_registry` for this shipment: open, the 4 handovers, the attest and deliver, so 7 (`page/app.js`, `txHistory`). Redeem is not among them, because it calls the `transfer_agent` contract, not the registry. verify-head prints only the steps that change the head: open, the 4 handovers and the attest, so 6. `deliver` changes the status but does not fold into the head (`contracts/custody_registry/src/lib.rs`: only `open`, `handover` and `attest` write `head`). Both end on the same on-chain head, `2d74fec0…5414`.

**12. Is the token burn tied to delivery on chain?** (leo-agent, from REVIEW-THREAT-MODEL finding 1)
No. The registry records `Delivered`, but nothing on chain links the Radox `transfer_agent.redeem` to it. Our harness reads the status and refuses to call redeem unless it is `Delivered` (`scripts/lifecycle.mjs:202`, `redeem_precondition` in `proofs/lifecycle.json`).
Redeem still needs the operator's and the holder's signatures (tx 864fd164…). Putting the gate on chain, with the transfer agent reading `get(key)`, is mainnet work, and the README says so.

**13. Does the registry check that the holder really holds the token, or that the token is real?**
No. `open` stores `token` as an address it never calls (lib.rs `open`, `token: Address`), and `deliver` only needs the signature of the `holder` it is given (lib.rs `holder.require_auth()`). A wrong holder is the operator's and the issuer's error, not something the registry catches.
That is by design: the registry stays token-agnostic (any Stellar asset contract works). The ownership check belongs to the token side, at redeem.

**14. What if the admin or operator key is lost or stolen?**
There is no `set_admin` or `set_operator` (`grep -c "fn set_(admin|operator)"` in lib.rs gives 0), so the only fix is a new deploy. Open shipments on the old registry stay readable but cannot be moved to the new one.
A stolen admin key can freeze shipments or pause every write, but it cannot change a route, a custodian or the head (Q7). For mainnet, the admin and operator should be multisig or smart-wallet addresses, which `require_auth` accepts without a code change.

**15. You now have three registries. Which one is "the" contract?**
All three are instances of the same wasm `8230ed93…` (DEPLOYMENTS.md): CCBJVXMJ… (7-tx lifecycle), CD7BUCY3… (teammates' keys on their own computers) and CDDWEENF… (two companies' chains, `proofs/multi-chain.json`, 2 shipments, both MATCH; checked by leo-agent at 20:13 UTC).
One instance per demo keeps each proof separate; in production one registry would serve a corridor. Every handover in all three is dual-signed (`handover-signers.mjs` with each `PROOF_FILE`).
