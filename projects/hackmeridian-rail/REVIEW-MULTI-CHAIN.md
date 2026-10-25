# Review of commit 9fed1c8 (README "Many supply chains, one rail", AI_USAGE.md, scripts/multi-chain.mjs)

Verdict: APPROVE WITH CHANGES (all changes are small wording or completeness; no overclaim found).

## Verified
- 9 table hashes on Horizon testnet (live, 2026-10-25): all `successful: true`, one invoke_host_function op each, parameters[0] = CDDWEENF6DKM4AHFWDBHQTYPLC3STMVFPXHXYDORLD53WDZM3FF3KJX4. Functions and addresses decoded from XDR match every row: open x2 (ac1ca8e4 -> A-warehouse GADDD, b189aec4 -> A-yard GB22K), handover 9a810a33 GADDD->GCIEL, 98136578 GB22K->GCIEL, 7d75acbd and 3ea5237f GCIEL->GBDUA, 81555aa1 GBDUA->GCTQX, deliver c0f44571 (to GCTQX... holder GBJFX) and c7aad14f (GBDUA, holder GDCLB). Order and ledgers ascend 5386477..5386486.
- verify-head, both keys (404c2ca9..., 836ec9f9...): MATCH, MATCH.
- No secret keys: grep 'S[A-Z2-7]{55}' on proofs/multi-chain.json and scripts/multi-chain.mjs returns nothing.
- "No token moves": script never calls the token (line 23 constant, recorded only as an `open` argument; no transfer/mint/redeem). "Signed by both custodians": contract handover has from.require_auth() and to.require_auth().
- No claim of real companies, pilot, adoption, standard, or on-chain company ownership; README states the directory is off chain and not a contract field.

## Findings
1. Minor, completeness. The table omits the registry deploy transaction (328ceaa90b084925c2ac64c732982fa2749223dba3bd739d64b7d1ce8a6d77b7, in proofs/multi-chain.json setup), so a judge cannot confirm from the README that the contract at CDDW... is the custody_registry.
   Add row first: `| deploy registry | \`328ceaa90b084925c2ac64c732982fa2749223dba3bd739d64b7d1ce8a6d77b7\` |`
2. Minor, usability. Quote: "using the keys in the proof file; both print MATCH." A judge must dig the keys out of the JSON.
   Replace: "Check either shipment with `PROOF_FILE=proofs/multi-chain.json node scripts/verify-head.mjs <key>`; keys: `404c2ca977251e7c4139143161814def648a92094d5dff63c2694c89b9adddeb` (TEST3286578) and `836ec9f9bc09a08a3ef445f1bdd6d1094ba3222d8651fb2c82100274cc497b8a` (TEST3286579); both print MATCH."
3. Minor, tone. Heading "Many supply chains, one rail" plus "Each ... never mix" asserts more than two test shipments show. Suggest heading "Several supply chains, one rail: two test companies on one registry" and "the two chains never mix" -> "each shipment has its own key and head, so the two chains are tracked separately".
4. Minor, AI_USAGE.md. Row `proofs/multi-chain.json ... | —` has an empty review column. Replace "—" with "9 hashes checked successful on Horizon, contract and function per row decoded from XDR, verify-head MATCH for both shipments (independent reviewer agent, 2026-10-25)". Also the README row says "later wording edits not re-checked"; update it to say this section was reviewed in this pass.
5. Nit. README says "A-terminal" and "B-vessel" are shared "stops"; the "internal/external" kinds exist only in the off-chain proof file. Already disclosed; no change needed.
