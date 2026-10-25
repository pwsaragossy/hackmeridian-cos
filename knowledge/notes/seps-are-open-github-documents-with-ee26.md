---
id: seps-are-open-github-documents-with-ee26
title: "SEPs are open GitHub documents with a lightweight approval process; CAPs change the core protocol"
type: finding
status: active
origin: hackmeridian-rail
provenance: agent
confidence: high
sources: ["https://developers.stellar.org/docs/learn/fundamentals/stellar-ecosystem-proposals (read via Raven stellarDocs, 2026-10-25 19:18 UTC)"]
created: 2026-10-25
updated: 2026-10-25
review_by: 2027-04-25
group:
aliases: [SEP process, how to propose a SEP]
tags: [stellar, sep, standard, hackmeridian]
---
# SEPs are open GitHub documents with a lightweight approval process; CAPs change the core protocol

[FACT, high; Stellar docs, Stellar Ecosystem Proposals page, read 2026-10-25] A SEP defines a standard for building infrastructure on top of Stellar so different entities (issuers, wallets, exchanges, service providers) "interoperate using a single common integration". It usually defines both a server side and a client side. SEPs are "publicly-created, open-source documents" that live in the GitHub repository (stellar/stellar-protocol) and "have a lightweight approval process". CAPs (Core Advancement Proposals) are different: they change the network's core protocol.

Use for the rail: a shared custody standard that companies integrate once fits what a SEP is meant to be, while a contract alone does not define the off-chain client and server sides. The page does not describe the status steps or who approves a SEP. Ask a Stellar engineer for that, as ENGINEER-BRIEF.md question 3 does. No SEP for chain of custody was found earlier: [[no-sep-and-no-stellar-project-aa39]].

Compared: [[no-sep-and-no-stellar-project-aa39]] coexists (that note says no custody SEP exists, this one says what a SEP is and how it is made) ; [[what-paulo-s-own-documents-and-7d76]] coexists (different subject, no overlap in what it states)
