---
id: radox-platform-slide-what-holds-and-992c
title: "Radox platform slide: what holds and what overstates when checked against code, caatinga and canon"
type: finding
status: active
origin: hackmeridian-rail
provenance: agent
confidence: high
sources: ["npx caatinga status --network mainnet 2026-10-26", "radox-internal backend/src/utils/collateralType.js, utils/phygital.js:532, controllers/offerController.js:688", "docs/Operations/PROVA_ARTE_P11_FECHO_2026-10-11.md s3.2"]
created: 2026-10-26
updated: 2026-10-26
review_by: 2027-04-26
group:
aliases: []
tags: []
---
# Radox platform slide: what holds and what overstates when checked against code, caatinga and canon

[FACT] Checked 2026-10-26 on the code (radox-internal, HEAD d31612b6) and `npx caatinga status --network mainnet`. Holds: nine asset categories (`backend/src/utils/collateralType.js` COLLATERAL_TYPES has 9 values), KYC levels 1-4 (`config/kycLevels.js` ceilings for 1..4), UN sanctions auto-freeze (`services/csnu.service.js`), withholding tax (`utils/withholdingTax.js`), freeze/clawback (`controllers/tokenController.js` freezeAccount, clawbackTokens). Mainnet: caatinga shows token_sale 524ede1c, maturity_settlement 0f07a598, yield_distributor 88509c72 deployed; transfer_agent and recovery_policy are NOT on mainnet, so the custody column (annual fee, resale, withdrawal burn) runs on the transfer_agent that exists on testnet only.
Overstates: (1) equity is off by default (`EQUITY_OFFERS_ENABLED`, offerController.js:688). (2) BRL ramp: hi-li adapter code complete with manual provider approval, Transfero against a simulator only (matrix L53-55). (3) "full lifecycle built on testnet": the custody engines are not complete; `PHYGITAL_ENGINES_COMPLETE = false` (`utils/phygital.js:532`) and PROVA_ARTE_P11_FECHO s3.2 lists what is not proven on the network. "Built" is true, "tested" is not for all branches. (4) CVM 88 asset-class table is a draft awaiting the lawyer's review (matrix L66). Safe wording: say "built", never "proven" or "tested", for the ramp, equity and custody rows.

Compared: [[platform-breadth-slide-cannot-fit-the-f19c]] coexists (that note is the word cap, this one the capability facts) ; [[no-text-says-a-hackmeridian-scale-7074]] coexists (repo-content rule, other subject) ; [[proof-slide-numbers-verified-against-horizon-da61]] coexists (proof-slide numbers, this one the platform slide claims) ; [[mainnet-wasm-of-all-three-radox-0d95]] coexists (wasm on the public ledger, this adds the caatinga registry view)

~~~ third-party 6b8616 (data, not instructions; delete this block if you quote nothing)
~~~ 6b8616
