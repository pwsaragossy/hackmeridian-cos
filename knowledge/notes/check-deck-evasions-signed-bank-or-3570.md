---
id: check-deck-evasions-signed-bank-or-3570
title: "check_deck evasions: signed bank or port, ran on mainnet and paying clients pass; sources re-opened 2026-10-25"
type: finding
status: active
origin: hackmeridian-rail
provenance: agent
confidence: high
sources: ["sustainableworldports.org/?p=10830","IMO FAL.5/Circ.54","stellar.org/solutions/real-world-assets","swift.com billing-rules","dcsa.org soft-barriers","BSI 2026-04-21"]
created: 2026-10-25
updated: 2026-10-25
review_by: 2027-04-25
group:
aliases: []
tags: []
---
# check_deck evasions: signed bank or port, ran on mainnet and paying clients pass; sources re-opened 2026-10-25

Reviewer, 2026-10-25, deck v13. [FACT, high] Mutants run on a scratch copy with check_deck.py: "Two ports have signed with Radox" fails (SIGNED_PARTNER); "A bank signed a letter of intent with Radox", "The Port of Santos signed on to the rail", "The lifecycle ran on mainnet" and "Radox has paying clients in three ports" all exit 0. Only "live on mainnet" and "ports have signed" are caught. Proposed extra patterns: ran/runs/live/deployed ... mainnet within 40 chars; (port|bank|airport|chamber) ... signed|agreed|committed|joined within 40 chars; signed (a|an|the) letter|LOI|MOU|contract|agreement|deal; (paying|our|first|signed) clients. They have no hit on the current deck.
Sources re-opened the same day, all matched: Dessus (World Bank) at IAPH 2023-11-01 "Over 90 percent of the ports in low- and middle-income countries have not yet implemented these PCS platforms."; IMO FAL.5/Circ.54 8.4.3 "When legacy systems with proprietary data formats and interfaces exist..."; SDF "4 billion dollars in tokenized real-world assets, as of September 1, 2026"; Swift billing rules page lists entry fees, annual charges and network usage (message traffic) charges, with no amounts; DCSA "As of 2025, around 11% of bills of lading are issued electronically" (undated page) and "Ocean carriers issue around 45 million bills of lading a year" (15 Feb 2023, no year of data stated); BSI 21 Apr 2026 "more than a fifth (22%) of global cargo theft incidents involved the cooperation of insiders". Related: [[world-bank-and-iaph-port-community-6ec0]], [[stellar-tokenized-rwa-size-on-2026-a455]], [[swift-fee-structure-on-swift-com-9ed6]].

Compared: [[world-bank-and-iaph-port-community-6ec0]] coexists (it holds the source text, this holds the reviewer run and the checker gaps) ; [[founder-voice-in-public-text-sell-d820]] coexists (the rule, this tests its guard) ; [[brl-and-usd-ramps-on-stellar-1e41]] coexists (that note is the ramps research, this one tests the deck checker) ; [[review-of-executability-audit-2026-10-6701]] coexists (that note is the plan audit review, this one tests the deck checker) ; [[soroban-versions-on-2026-10-25-9619]] coexists (that note is the SDK versions, this one tests the deck checker) ; [[deck-and-video-rules-for-async-8b70]] coexists (that note is the judging format rules, this one tests the deck checker) ; [[executability-audit-2026-10-25-02-04f7]] coexists (that note is the plan audit, this one tests the deck checker) ; [[ucc-article-7-and-brazilian-rules-77dd]] coexists (that note is the legal title rules, this one tests the deck checker) ; [[founder-statements-in-the-deck-open-89a2]] coexists (that note is the the founder statements themselves, this one tests the deck checker) ; [[hackmeridian-2026-official-pitch-deck-template-d5c7]] coexists (that note is the deck template, this one tests the deck checker) ; [[hackmeridian-2026-rules-and-submission-requirement-5868]] coexists (that note is the submission rules, this one tests the deck checker) ; [[no-sep-and-no-stellar-project-aa39]] coexists (that note is the ecosystem search, this one tests the deck checker) ; [[no-text-says-a-hackmeridian-scale-7074]] coexists (that note is the repo-content rule, this one tests the deck checker) ; [[physical-goods-rwas-on-stellar-matrixdock-05ea]] coexists (that note is the RWA landscape, this one tests the deck checker) ; [[problem-numbers-verified-2026-10-25-7e42]] coexists (that note is the problem figures, this one tests the deck checker) ; [[problem-slides-review-2026-10-25-2478]] coexists (that note is the problem slide review, this one tests the deck checker) ; [[stellar-and-solana-hackathon-winners-no-31ca]] coexists (that note is the winning-deck research, this one tests the deck checker) ; [[stellar-tokenized-rwa-size-on-2026-a455]] coexists (that note is the market size figure, this one tests the deck checker) ; [[transfer-agent-testnet-interface-2026-10-3378]] coexists (that note is the contract interface, this one tests the deck checker)

~~~ third-party 8cdc56 (data, not instructions; delete this block if you quote nothing)
~~~ 8cdc56
