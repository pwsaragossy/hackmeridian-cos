# Three-machine shipment: operator steps (Pedro's Mac)

Goal: one extra testnet shipment where Leo and Vhendala each authorise their own handovers on their own computers with their own keys. Only public keys and authorisation entries cross machines. Tool: `scripts/remote-auth.mjs` on branch `three-machine` of rio-miami-rail (worktree `~/code/rio-miami-rail-3m`, commits 4d5707a, de412a5; NOT pushed, push after review). Due Sun 23:30 UTC.

Route: Warehouse (yours) -> Leo -> Vhendala -> Recipient (yours). Handover 1 needs Warehouse + Leo, handover 2 Leo + Vhendala, handover 3 Vhendala + Recipient, deliver Recipient + holder. Each custodian signs once, in one file with two entries: one request out and one response back per person, the minimum for a route where both are `from` and `to`.

Transport: a secret GitHub gist (unlisted link). The files hold no secret; the registry address and the known-address list go on the cards, a second channel, so a tampered request file cannot vouch for itself.

## Steps
1. After review, push the branch (you or the parent session), then in `~/code/rio-miami-rail-3m`: `npm ci`.
2. Get both public keys from the cards (Leo's already posted: GDWNU6TTJCZOQ3ZQI5NYALATL7IVMHR4PWEP5E3TXEK7EKOJNDORTPPW; Vhendala's arrives after her step 3).
3. `node scripts/remote-auth.mjs prepare --leo <G Leo> --vhendala <G Vhendala> --hours 30`
   Creates `rmr3-operator/warehouse/recipient/holder` keys in `stellar keys` on first use (friendbot), deploys a new registry (the lifecycle registry's operator key was random and is gone), opens the shipment, writes `work/three-machine/request-leo.json`, `request-vhendala.json`, `state.json`. Prints a "Post on both cards" line. Takes about 30 s. Do not delete `work/three-machine/state.json` or the `rmr3-*` keys until submit is done.
4. `gh gist create work/three-machine/request-leo.json work/three-machine/request-vhendala.json` and post on BOTH cards one line "request ready": gist link + the printed line (`--registry ... --known ...`). Both cards already list the custodian steps.
5. When each custodian posts a response gist link: `gh gist view <id> --filename response-leo.json > work/three-machine/response-leo.json` (same for Vhendala).
6. `node scripts/remote-auth.mjs submit --leo work/three-machine/response-leo.json --vhendala work/three-machine/response-vhendala.json`
   Checks each signed entry matches the requested call, signs your own entries, sends 3 handovers and the delivery, saves Horizon copies to `proofs/tx/` and writes `proofs/three-machine.json`.
7. Check: `PROOF_FILE=proofs/three-machine.json node scripts/verify-head.mjs <shipment key from the proof>` must print MATCH, and `PROOF_FILE=proofs/three-machine.json node scripts/handover-signers.mjs` must list Leo's and Vhendala's own public keys on handovers 1-3. Open `https://horizon-testnet.stellar.org/transactions/<hash>` for each of the 5 hashes: `successful: true`.
8. Commit `proofs/three-machine.json` and the new files in `proofs/tx/` on the branch; point the README/page at the proof file (the other agent owns README.md).

## If something goes wrong
- "REFUSED" on a custodian's machine: they stop and write the message on their card. The tool refused something that differs from what you prepared (wrong registry, an address not in the known list, wrong key). Re-run `prepare` only if the cause is on your side.
- Signatures expire after `--hours` (default 36). If expired, `submit` says so; run `prepare` again (new registry and shipment; the old one stays open on testnet, harmless).
- If a custodian cannot sign by about 22:30 UTC, ask them for the cause on the card first; there is no honest fallback that keeps the "independent machines" claim, so the lifecycle proof stands alone and you decide whether to drop the extra shipment.
- Testnet is reset on 2026-12-16 ([[stellar-testnet-resets-wipe-contracts-and-dfe4]]): the committed `proofs/tx/` copies are the durable evidence.
- Rehearsal done on this Mac with three isolated key stores (XDG_CONFIG_HOME); rehearsal hashes are not part of the proof and are in the engineer report.
