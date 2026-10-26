---
id: slide-wording-for-the-mainnet-contracts-f96e
title: "Slide wording for the mainnet contracts must avoid deployed and live, which check_deck bans"
type: finding
status: active
origin: hackmeridian-rail
provenance: agent
confidence: high
sources: ["deck/check_deck.py BANNED (live|running|deployed|launched|in production) on (Stellar )?mainnet, and FALSE_CLAIMS verb within 40 characters of mainnet", "deck/build_deck.py lines 341 and 394", "scratch test 2026-10-26"]
created: 2026-10-26
updated: 2026-10-26
review_by: 2027-04-26
group:
aliases: []
tags: []
---
# Slide wording for the mainnet contracts must avoid deployed and live, which check_deck bans

[FACT] The allowed sentence in [[wording-the-rio-miami-deck-readme-ef38]] rule 3 ("3 Soroban contracts deployed on Stellar mainnet since June 2026") fails deck/check_deck.py: BANNED matches "deployed on Stellar mainnet", and the false-claim pattern matches ran, runs, running, live, deployed, settled or operat* followed within 40 characters by "mainnet". The deck therefore says "its 3 Soroban contracts are on Stellar mainnet" (build_deck.py line 341) and "3 Soroban contracts on Stellar mainnet" (line 394). I ran the checker's regexes on a new title "Radox: 3 Soroban contracts on Stellar mainnet" and it passed, while "Radox is live on mainnet with investors" failed twice. Use "on Stellar mainnet" with no verb, and put "since June 2026" in notes or on the same line without those verbs. Same check bans the words investors, customers, partner, sponsor, so the institution's side is "clients" and the buyer side is "KYC-gated clients".

Compared: [[wording-the-rio-miami-deck-readme-ef38]] coexists (that note gives the allowed sentence, this one the form that also passes the checker) ; [[check-deck-evasions-signed-bank-or-3570]] coexists (mutants that pass the checker, not the wording of the true claim) ; [[a-deck-checker-built-from-banned-1cec]] coexists (why banned lists miss omissions, other subject) ; [[deck-why-now-line-dcsa-ebl-8cb2]] coexists (different subject, no overlap with this note) ; [[founder-statements-in-the-deck-open-89a2]] coexists (different subject, no overlap with this note) ; [[team-slide-facts-leo-and-vhendala-d7e2]] coexists (different subject, no overlap with this note) ; [[the-10-slide-cap-on-the-d5fd]] coexists (different subject, no overlap with this note) ; [[wording-market-figures-in-the-deck-dadf]] coexists (different subject, no overlap with this note) ; [[market-slide-7-re-check-2026-452e]] coexists (different subject, no overlap with this note)

~~~ third-party e2eef3 (data, not instructions; delete this block if you quote nothing)
~~~ e2eef3
