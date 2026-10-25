---
id: no-sep-and-no-stellar-project-aa39
title: "No SEP and no Stellar project does dual-signed physical custody handover (2026-10-24)"
type: finding
status: active
origin: hackmeridian-rail
provenance: agent
confidence: medium
sources: ["Raven LumenLoop directory search 'supply chain' (asOf 2026-10-24)", "Raven Scout SEP research search (asOf 2026-10-24)", "https://github.com/stellar/stellar-protocol/blob/master/ecosystem/sep-0053.md", "https://trustlesswork.com/escrow-times/use-case-traded-b2b"]
created: 2026-10-25
updated: 2026-10-25
review_by: 2026-12-25
group:
aliases: []
tags: [stellar, ecosystem, supply-chain, attestation, competitors]
---
# No SEP and no Stellar project does dual-signed physical custody handover (2026-10-24)

Search on 2026-10-24 (Raven: LumenLoop directory, SCF submissions, Scout SEP research) found **no SEP for attestations or chain of custody**, and no Stellar project that records a physical handover signed by both the outgoing and the incoming custodian. The SEPs returned are about other things: SEP-10 and SEP-45 (web auth), SEP-53 (sign and verify messages, Final), SEP-59, SEP-7.

Nearest neighbours, by semantic similarity only (not equivalence): AgTrail (food traceability, IoT + QR, Nigeria); Autify (supply-chain management); Airswift (tokenized receivables, SCF #16); Pipeline, "Commodity Trade Finance Protocol" (SCF #43, Build, US$140,000); BorderDollar (cross-border invoice finance, SCF #26); CashAbroad (logistics payments); Trustless Work (escrow released on delivery verification, "Trade & B2B" use case); ChainCred and LumosCore (verifiable data / attestation layers).

This is "not found in LumenLoop, SCF and Scout", not "does not exist": projects outside those directories, and private pilots, were not searched. Pipeline and Trustless Work are the closest substitutes a judge may name; the difference to state is custody of the physical object with two signers per step, not payment or financing. Ramps for the money leg: [[brl-and-usd-ramps-on-stellar-1e41]]. Closest neighbour found later (Raven, LumenLoop directory and SCF data, observed 2026-10-25 02:26 UTC): Kutana (slug kutana, SCF #45, awarded US$58,200, "Insurance Embedded Escrow for B2B Trade"), milestone escrow in USDC released on attested trade events, with KYB attestations and deal records anchored by Soroban contracts. It pays on trade milestones; it does not record a physical custody handover signed by two custodians, so the difference to state stays custody of the object, two signers per step.

Compared: [[soroban-versions-on-2026-10-25-9619]] coexists (different subject: SDK versions, not the ecosystem) ; [[hackmeridian-2026-rules-and-submission-requirement-5868]] coexists (event rules, other topic)
