---
id: brl-and-usd-ramps-on-stellar-1e41
title: "BRL and USD ramps on Stellar and SEP-45 for C-addresses (2026-10-24)"
type: finding
status: active
origin: hackmeridian-rail
provenance: agent
confidence: low
sources: ["https://lumx.io/blog-posts/lumx-launches-brl-usdc-corridor-on-stellar-for-institutional-payment-settlement-in-brazil", "https://developers.stellar.org/docs/platforms/anchor-platform/sep-guide/sep45", "https://developers.stellar.org/docs/learn/fundamentals/anchors"]
created: 2026-10-25
updated: 2026-10-25
review_by: 2026-12-25
group:
aliases: []
tags: [stellar, anchors, ramps, brazil, usd, sep-45]
---
# BRL and USD ramps on Stellar and SEP-45 for C-addresses (2026-10-24)

Candidates for a Brazil to US money leg on Stellar, found on 2026-10-24; their operating status and which SEPs each supports were not verified, so confidence is low:

- BRL side: Lumx (BRL-USDC corridor for institutional settlement, announced 2026-08-04); PagFinance (BRLP, a regulated BRL settlement token); TroqPay (Brazilian merchants receive Pix and USD); Mercado Bitcoin (USDC on Stellar since 2022-05-31); SCF projects "Instant payments on Pix with USDC" and "Regulated BRL Settlement on Stellar".
- USD side: Coinme (US cash), U.S. Bank USBDC pilot on Stellar (2026-09-09), USDT0 via Ramp Network (2026-09-02), Meru (on-ramp through a US bank account, SCF).
- Standards: SEP-6 (programmatic), SEP-24 (hosted, the anchor does KYC), SEP-31 (cross-border). For a smart account (C-address) to authenticate with an anchor there is **SEP-45, still Draft**, with an Anchor Platform guide; which BR or US anchors implement it was not found. SCF #41 "Latch: C-Address Onboarding" is a candidate for C-address onboarding.

Use: a mentor question at the event (which ramp pays USD to a C-address), not a build dependency. Context: [[no-sep-and-no-stellar-project-aa39]].

Compared: [[no-sep-and-no-stellar-project-aa39]] coexists (that note covers custody projects, this one covers money ramps) ; [[soroban-versions-on-2026-10-25-9619]] coexists (SDK versions, different subject) ; [[hackmeridian-2026-rules-and-submission-requirement-5868]] coexists (event rules, other topic)
