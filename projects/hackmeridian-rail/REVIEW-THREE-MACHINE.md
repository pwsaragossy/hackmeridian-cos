Reviewer: independent reviewer subagent (role card reviewer), briefed by session-hackmeridian-rail; work reviewed: product wording (DEMO-SCRIPT row 0:40, FORM-ANSWERS, README)
Time: Sun Oct 25 16:14 UTC 2026

# Verdict: APPROVE WITH CHANGES. No false fact. The claim "custodians on their own computers" is true as a chain fact for the signatures, but "key never left that computer" and "two of us" need rewording. All three texts overstate by implication in one place each.

## Checked and true (evidence)
- Horizon testnet, all successful: handover 1 `861544e4` ledger 5384199; handover 2 `9214980e` 5384200; handover 3 `850da342` 5384201; deliver `849c268d` 5384202. Also the registry deploy `7d2c30d8` (5383657) and open `34860ed8` (5383658) are successful. All six were submitted by the operator account GCOFS2CF... (the source account), as the texts say.
- Branch `three-machine` head is d02424d. `verify-head.mjs 8f32b176...` printed `recomputed d9cf3a5f...614d`, `on-chain` the same, `MATCH`. `handover-signers.mjs` printed "both signed" for all 3 handovers and the deliver, with auth entries: warehouse+leo, leo+vhendala, vhendala+recipient, recipient+holder.
- Leo's key GDWN...TPPW and Vhendala's key GAUK...CEFR in the proof file equal the keys on their cards (leo-agent 14:31 UTC, vhendala-agent 15:16 UTC) and the `signer` in their response files. Each response signs two entries (Leo: h1-to, h2-from; Vhendala: h2-to, h3-from). The response files hold only `entries`, `format`, `request_id`, `signer`, `until_ledger`; the entries hold a public key and an ed25519 signature, no secret.
- README (local 4f90bb1, ahead 4 of origin/main, not pushed) matches the proof: hashes, ledgers, registry CD7BUCY3..., route, "records custody only, no mint or redeem".
- A successful `require_auth` on chain proves that someone holding the private key of GDWN... and of GAUK... produced those signatures. The explorer shows only the operator's source signature; none of the three texts says an explorer shows two signatures. Good, keep it so.
- DEMO row 0:40 narration: 71 words, 21.5 s at 3.3 words/s, so it fits the 25 s row with 3.5 s spare. The new sentence is 16 words (about 4.8 s).

## What is evidence and what is their word
| Claim | Status |
|---|---|
| Leo's and Vhendala's keys signed the entries | Evidence (chain, signatures verified by the contract at submit) |
| Responses carry no secret, only signed entries | Evidence (file fields above) |
| The accounts leo-schlanger and vhendala pushed their response files | Weak evidence (commit 1d06d6c 16:08 UTC, 1ad0d6f 15:50 UTC "update from vhendala"; shows account control, not which machine signed) |
| "Key never left that computer" | Their word, relayed by their agents' cards ("leo-agent", "vhendala-agent"). Not provable from chain or files. A key could be generated, held or typed anywhere. |
| "Operator's machine checked each entry before submitting" | Our word and our script (`remote-auth.mjs submit`); the 16:10 board note says it was checked. Reproducible by a judge from the code. |

## Findings, ranked

### F1 (high): "key never left that computer" is stated as fact in FORM-ANSWERS and README
A skeptical judge cannot check it and will see "agent-posted card" as the only source. Say what the evidence shows and attribute the rest.
- FORM-ANSWERS, replace the whole fragment with:
  "In a second testnet shipment, two team members authorised their handovers from their own computers, each with a testnet key that, by their account, never left that computer. Only public keys and signed authorisation entries were exchanged (the response files hold no secret); our machine checked each entry before submitting. Warehouse, recipient and holder were still our test keys on one machine, so this shows the mechanism, not independent companies. Four authorisation transactions (three handovers and the delivery), all successful, and verify-head recomputes the same head (proof: proofs/three-machine.json on the repo's three-machine branch, also in the README)."
- README first sentence of the section, replace with:
  "In a second testnet shipment, two team members authorised their handovers from their own computers, each with a testnet key that, by their account, never left that computer. Only public keys and signed authorisation entries were exchanged (the response files hold no secret); the operator's machine checked each entry against the request and submitted the transactions. The other custodians (warehouse, recipient, holder) and the operator are still test keys on one machine, so this is a mechanism demonstration, not independent companies."

### F2 (high): "two of us" in Pedro's voice is ambiguous and slightly wrong
Pedro is not one of the two; he is the operator and holds the warehouse, recipient and holder keys. "Two of us" can be heard as "Pedro and one other", or as all-team custody. The clone says "our own keys" for keys Pedro did not hold.
- DEMO row 0:40, replace the sentence "In a second shipment, two of us authorised from our own computers, with our own keys." with:
  "In a second shipment, two teammates authorised from their own computers, with their own keys."
  (15 words; the row becomes 70 words, 21.2 s, still fits.)

### F3 (medium): the screen for row 0:40 does not show the second shipment
The clip is `handover-signers.mjs` on the default proof file, which is the first shipment (lifecycle.json). The narration then talks about a second shipment with no visual, and the 0:20 row just said "all actors are test keys held by one harness". A judge sees a contradiction on screen. Fix without changing the claim: after the first clip, add 4 to 5 s of the same command on the second proof, with the narration as above:
  `PROOF_FILE=proofs/three-machine.json node scripts/handover-signers.mjs` (last line: "every handover and deliver: both custodians signed"; hold on the `leo GDWN...TPPW` and `vhendala GAUK...CEFR` lines).
  Add a caption: "Second shipment: Leo and Vhendala signed on their own computers." If the extra clip is not made, delete the new sentence from the voice-over and keep the claim in the README and form only, because an unseen claim in a 25 s row costs more than it adds. Do not say "visible on stellar.expert": the explorer lists only the operator signature.

### F4 (low): "Four transactions" can be read as the whole shipment
The shipment has six successful transactions (deploy, open, 3 handovers, deliver). The README table lists four. The form says "Four transactions, all successful". Use "four authorisation transactions" (as in the F1 text) or add the deploy and open to the README table with ledgers 5383657 and 5383658.

### F5 (low): "their own handovers"
Each handover was authorised by two parties; the other party in handovers 1 and 3 was a test key on our machine. "Their own handovers" can read as "they alone". The F1 text says "authorised their handovers" with the counter-party caveat; if you want it shorter: "signed the handovers they took part in".

### F6 (note, no change): wording that must stay out
Do not write "real custodians", "partners", "independent companies", "two signatures on the explorer", or "verified on their devices". "Team members" is correct (Leo and Vhendala are the team). No partnership is implied by the current texts.

## Not checked
- I did not re-verify the ed25519 signatures cryptographically myself; I relied on the contract accepting them on chain (successful transactions) and on the 16:10 board note that the session verified them independently.
- I did not check which machine, OS or network Leo and Vhendala used, nor that the keys were created by them; only their agents' card statements exist.
- I did not run the video clip, nor test whether the 0:40 narration fits the final recording; the 3.3 words/s figure is the brief's.
- I did not open the README on GitHub (the repo is private and 4f90bb1 is not pushed), nor check the `three-machine` branch link from a logged-out browser.
- I did not check other rows of DEMO-SCRIPT, the rest of FORM-ANSWERS or the rest of the README.
