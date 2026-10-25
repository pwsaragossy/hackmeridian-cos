# Three-machine shipment: steps (leo-agent proposal, 2026-10-25 14:45 UTC)

Goal (Sessions card): an extra shipment where Leo and Vhendala each sign a handover from their own
computer with their own testnet key; only public keys move. `proofs/lifecycle.json`, `check.py`
and the frozen 7 stay untouched.

Tool: `scripts/remote-sign.mjs` on rio-miami-rail main (ae25dac). `prepare` simulates the call and
writes a request with the unsigned auth entries; each signer runs `sign` on their own machine and
sends back a file with only their signed entry; anyone with a funded testnet account runs `submit`.
Tested on a throwaway registry (CB2JIOYL…FIAW3): open 5113d502…, handover 40c3de5d… (2 keys),
handover 52b1dde9… (2 keys), final state seq 2; missing signature, wrong signer and tampered
request are refused. The exchanged files are public data (no secrets).

## Plan
- Registry: the official CCBJVXMJ…H4LII. `open` needs its operator key, which lives only on Leo's
  computer (`rail-operator`, GCXY…J4OF): Leo opens. `handover` needs no operator: any funded
  account can be the source and submit.
- Route: [Pedro, Leo, Vhendala]. Handover 1 Pedro → Leo (Pedro + Leo sign), handover 2 Leo →
  Vhendala (Leo + Vhendala sign). Three machines, each signs at least one handover. No deliver,
  no token (the shipment stays Open at seq 2; `token` is the registry address, unused).
- Made-up container `TEST3000001|BRRIO`; evidence hash = sha256(`handover-<i>|TEST3000001`).
- Leo's key: GDWNU6TTJCZOQ3ZQI5NYALATL7IVMHR4PWEP5E3TXEK7EKOJNDORTPPW.

## Steps
1. Pedro and Vhendala, each on their own computer: `stellar keys generate <alias> --network testnet --fund`,
   then post `stellar keys address <alias>` (public key only) on their card.
2. Leo: `open` with the route above (prepare + submit as operator); hash on Leo's card.
3. Handover 1: one side runs `prepare` (source = own funded key) and shares `h1.json`; Pedro and Leo
   each run `SIGNER_SECRET=$(stellar keys show <alias>) node scripts/remote-sign.mjs sign h1.json > h1-<name>.json`
   and share the output; the preparer runs `submit h1.json h1-*.json`.
4. Handover 2: the same with Leo and Vhendala. Prepare only after handover 1 is SUCCESS.
5. Rail session: write the new proof file (e.g. `proofs/three-machines.json`: key, route, 3 hashes, who
   signed from where) and check it on Horizon; then deck and video may say "signed on three different machines".

The `sign` step prints the contract, function and arguments it signs to stderr: check them before sharing.
The signature is valid for ~4000 ledgers (~5.5 h) after `prepare`.
