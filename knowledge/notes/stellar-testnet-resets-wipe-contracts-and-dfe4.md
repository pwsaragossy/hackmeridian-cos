---
id: stellar-testnet-resets-wipe-contracts-and-dfe4
title: "Stellar testnet resets wipe contracts and history: next scheduled 2026-12-16, so proofs need snapshots"
type: finding
status: active
origin: hackmeridian-rail
provenance: agent
confidence: medium
sources: ["https://developers.stellar.org/docs/build/guides/basics/automate-reset-data", "https://developers.stellar.org/docs/networks", "Raven stellarDocs.search_docs, observed 2026-10-25 01:53 UTC"]
created: 2026-10-25
updated: 2026-10-25
review_by: 2027-01-25
group:
aliases: [testnet reset, testnet wipe]
tags: [stellar, testnet, proofs, hackmeridian]
---
# Stellar testnet resets wipe contracts and history: next scheduled 2026-12-16, so proofs need snapshots

Stellar's testnet (and futurenet) is reset about quarterly. A reset clears all ledger entries (accounts, trustlines, contract data) and also the transaction history kept by Stellar Core, Horizon and Stellar RPC; the guide says developers should not rely on accounts or balances persisting. The Raven stellarDocs search returned the "approximately quarterly" and "clear all ledger entries" wording directly; the full page text and the date below came through a summarising fetch tool, so the wording is second-hand.

The networks page (read 2026-10-25) lists one scheduled testnet reset: 2026-12-16. No earlier reset date is listed there, and the page does not say how the date is announced.

Consequence for HackMeridian (Rio-Miami rail): every proof that points at the public testnet (the seven lifecycle hashes in `proofs/lifecycle.json`, the shipment page reading the contract, the stellar.expert links, `check.py` reading Horizon) works for judging on 2026-10-26 to 2026-10-28 and for a review before 2026-12-16, then disappears. The durable evidence is therefore a committed snapshot (each transaction's Horizon JSON, the events dump that `verify-head` needs, a few explorer screenshots) plus the recorded video, and the README should say that the reset exists and when. The event-retention limit in [[stellar-rpc-getevents-keeps-about-7-187e]] is a shorter clock on the same problem: a `head` check from events only works for about a week unless the events are dumped at run time.

Measured on 2026-10-25 about 01:55 UTC: the public testnet RPC (`getHealth`) reports `ledgerRetentionWindow` 120960 ledgers, and its oldest and latest ledger close times are 604,795 seconds apart, which is 7.0 days. So RPC `getEvents` and `getTransaction` only see the last 7 days, while Horizon testnet keeps the full history until a reset (that is why `check.py` reads Horizon). A browser page can call both: the RPC answered a CORS preflight with `access-control-allow-origin: *`, and Horizon testnet echoed the request origin.

Not checked: whether the schedule was moved after 2026-10-25.

Compared: [[stellar-rpc-getevents-keeps-about-7-187e]] coexists (RPC event retention is a shorter clock, this note covers the wipe of the whole network) ; [[soroban-versions-on-2026-10-25-9619]] coexists (tool versions, a different topic) ; [[no-sep-and-no-stellar-project-aa39]] coexists (ecosystem search for prior art, not network data lifetime) ; [[brl-and-usd-ramps-on-stellar-1e41]] coexists (fiat ramps for the USD leg, not testnet resets) ; [[ucc-article-7-and-brazilian-rules-77dd]] coexists (a legal note on tokens and titles, a different topic)
