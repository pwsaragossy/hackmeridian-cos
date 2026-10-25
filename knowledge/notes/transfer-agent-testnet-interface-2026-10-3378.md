---
id: transfer-agent-testnet-interface-2026-10-3378
title: "transfer_agent testnet interface 2026-10-25: register_token args and hand_over_sac is the exit path"
type: finding
status: active
origin: hackmeridian-rail
provenance: agent
confidence: medium
sources: ["stellar contract info interface --wasm-hash 3870748b709f7b8531c7ebbbc975712333f61949831350ff7192f7076fc6bff1 --network testnet (2026-10-25 08:50 UTC)", "projects/hackmeridian-rail/LEO-BRIEF.md"]
created: 2026-10-25
updated: 2026-10-25
review_by: 2027-04-25
group:
aliases: []
tags: []
---
# transfer_agent testnet interface 2026-10-25: register_token args and hand_over_sac is the exit path

Read live 2026-10-25 08:50 UTC with stellar CLI 28.1.0. The Radox transfer_agent wasm 3870748b... on testnet exposes `__constructor(config: Config { admin, operator })`, `register_token(token, seller, settlement, payment_asset)` (all Address, stored as `TokenReg { payment_asset, seller, settlement }`), `mint(token, to, amount)`, `deliver(token, to, amount)`, `redeem(token, holder, amount: i128, ref_id: u64)`, `set_authorized(token, addr, authorized)` and `hand_over_sac(token, new_admin)`. Inference from the signature: `hand_over_sac` moves the SAC admin away from the agent (exit path); the agent gets control through the issuer's SAC `set_admin`. The interface does not say who must sign each call: the Step 0b spike in LEO-BRIEF.md decides it with simulations. Related: [[review-of-executability-audit-2026-10-6701]] [[two-signers-in-one-soroban-call-1b93]].

Compared: [[review-of-executability-audit-2026-10-6701]] coexists (that review found the arguments missing, this note records them live) ; [[executability-audit-2026-10-25-02-04f7]] coexists (plan audit, not the agent interface) ; [[soroban-versions-on-2026-10-25-9619]] coexists (tool versions, not this contract's functions) ; [[stellar-testnet-resets-wipe-contracts-and-dfe4]] coexists (network reset dates, other topic) ; [[brl-and-usd-ramps-on-stellar-1e41]] coexists (ramps research, other topic) ; [[ucc-article-7-and-brazilian-rules-77dd]] coexists (legal note, out of scope) ; [[hackmeridian-2026-rules-and-submission-requirement-5868]] coexists (event rules, other topic) ; [[no-sep-and-no-stellar-project-aa39]] coexists (ecosystem search, other topic) ; [[no-text-says-a-hackmeridian-scale-7074]] coexists (repo rules question, other topic)
