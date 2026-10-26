---
id: mainnet-wasm-of-all-three-radox-0d95
title: "Mainnet wasm of all three Radox contracts is on the public ledger; two instances still unmatched"
type: finding
status: active
origin: hackmeridian-rail
provenance: agent
confidence: medium
sources: ["api.stellar.expert/explorer/public/wasm/<hash> for the three hashes in the public radox README, fetched 2026-10-26", "github.com/pwsaragossy/radox README (gh api, 2026-10-26)"]
created: 2026-10-26
updated: 2026-10-26
review_by: 2027-04-26
group:
aliases: []
tags: []
---
# Mainnet wasm of all three Radox contracts is on the public ledger; two instances still unmatched

[FACT] The three wasm hashes in the public radox README (token_sale 524ede1c..., maturity_settlement 0f07a598..., yield_distributor 88509c72...) each return the real wasm bytes from the stellar.expert public-network wasm endpoint on 2026-10-26, with the expected exported functions (token_sale: withdraw, emergency_drain, set_active; maturity_settlement: initialize, deposit; yield_distributor: distribute, upgrade). So the code of all three is on mainnet. The README dates the wasm uploads 2026-06-01 for token_sale and maturity_settlement and 2026-07-10 for yield_distributor, so "since June 2026" is true for the set only because two of three are from June; the third is July. The README itself says token_sale and maturity_settlement are deployed per offering, so their instances vary and I could not match one instance to each hash (the stellar.expert contract list ignored the creator filter). Only the yield_distributor instance was matched by ID earlier ([[claims-hackmeridian-material-may-and-may-3e4f]]). Consequence: "3 Soroban contracts on Stellar mainnet" is supported as three contract codes on the ledger plus at least one instance; it is not shown as three instances. The same wording is allowed by [[wording-the-rio-miami-deck-readme-ef38]] rule 3; a stricter form is "on-chain since June 2026" for the set and "from June to July 2026" if a judge asks.

Compared: [[wording-the-rio-miami-deck-readme-ef38]] coexists (that note gives the allowed sentence and the 2026-10-25 check, this one adds the wasm check of 2026-10-26 and the July date of yield_distributor) ; [[claims-hackmeridian-material-may-and-may-3e4f]] coexists (the may/may-not table, same facts, no overlap in the wasm check) ; [[slide-wording-for-the-mainnet-contracts-f96e]] coexists (checker-safe wording, other subject) ; [[apache-2-0-for-rio-miami-9905]] coexists (different subject, no overlap with this note) ; [[stellar-expert-shows-both-teammate-keys-2899]] coexists (different subject, no overlap with this note) ; [[zis-in-public-material-radox-is-bc05]] coexists (different subject, no overlap with this note) ; [[serve-a-read-only-soroban-contract-1aab]] coexists (different subject, no overlap with this note)

~~~ third-party 8cf69f (data, not instructions; delete this block if you quote nothing)
~~~ 8cf69f
