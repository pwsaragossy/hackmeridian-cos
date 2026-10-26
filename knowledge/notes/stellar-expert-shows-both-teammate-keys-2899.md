---
id: stellar-expert-shows-both-teammate-keys-2899
title: "stellar.expert shows both teammate keys in the handover call args of the three-machine tx 9214980e but only the operator under Signatures"
type: finding
status: active
origin: hackmeridian-rail
provenance: agent
confidence: medium
sources: ["stellar.expert testnet tx 9214980e (full hash in the body), Playwright, 2026-10-26 05:20 UTC", "Horizon testnet transactions 9214980e and 635c99ac, 2026-10-26"]
created: 2026-10-26
updated: 2026-10-26
review_by: 2027-04-26
group:
aliases: [explorer signers, two teammates frame]
tags: [hackmeridian, video, explorer]
---
# stellar.expert shows both teammate keys in the handover call args of the three-machine tx 9214980e but only the operator under Signatures

[FACT, opened 2026-10-26 ~05:20 UTC] The page for transaction 9214980ea8f3923ca0e036a803517dba2b3d1c1a12d8e5cbb481f31625eb7c0c (ledger 5384200, processed 2026-10-25 16:09:47 UTC, Successful, registry CD7B...NH3F) reads "GCOF...ASXN invoked contract CD7B...NH3F handover(..., GDWN...TPPW, GAUK...CEFR, ..., 3)". The two addresses are the teammates' own testnet keys (three-machine proof), the outgoing and the incoming custodian. The Signatures box lists one signature, the operator GCOFS2...XIASXN. Horizon also returns successful true for this transaction and for 635c99ac...bd38.

So an explorer frame can truthfully say "the call names both custodians", never "the explorer shows both signatures"; the proof that both authorised is the auth-entry listing of `scripts/handover-signers.mjs` (with `PROOF_FILE=proofs/three-machine.json` for this shipment). Same limit as the first shipment's frame in the older clips ([[wording-the-rio-miami-deck-readme-ef38]]).

Compared: [[proof-slide-numbers-verified-against-horizon-da61]] coexists (that note checks the deck's proof numbers, this one is what the explorer page shows per signer) ; [[sign-soroban-auth-entries-on-another-e4dd]] coexists (how the entries were signed, this one is how they appear on the explorer) ; [[no-sep-and-no-stellar-project-aa39]] coexists (novelty search, unrelated to the display) ; [[proof-slide-numbers-verified-against-horizon-0fff]] coexists (a second pass of the same deck-number check). ; [[hackmeridian-is-in-person-only-on-d6b2]] coexists (different subject, no overlap with this note) ; [[icc-fit-alliance-2026-ebl-survey-cdc7]] coexists (different subject, no overlap with this note) ; [[market-numbers-reviewer-pass-corridor-teu-2a95]] coexists (different subject, no overlap with this note) ; [[zis-in-public-material-radox-is-bc05]] coexists (different subject, no overlap with this note) ; [[stellar-and-solana-hackathon-winners-no-31ca]] coexists (different subject, no overlap with this note) ; [[two-signers-in-one-soroban-call-1b93]] coexists (that note is the require_auth mechanism, this one is what the explorer displays)
