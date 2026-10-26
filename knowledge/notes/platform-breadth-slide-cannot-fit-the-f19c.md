---
id: platform-breadth-slide-cannot-fit-the-f19c
title: "Platform breadth slide cannot fit the 30-word on-slide cap; check_deck does not enforce it"
type: finding
status: active
origin: hackmeridian-rail
provenance: agent
confidence: medium
sources: ["deck/check_deck.py (no word-count rule)", "PITCH-FINAL.md line 103", "radox-internal docs/Project_Bible/02_feature_matrix.md", "scratchpad slide2/chk.py run 2026-10-26"]
created: 2026-10-26
updated: 2026-10-26
review_by: 2027-04-26
group:
aliases: []
tags: []
---
# Platform breadth slide cannot fit the 30-word on-slide cap; check_deck does not enforce it

[FACT] The caps "titles <= 8, on-slide <= 30, notes <= 60" live only in PITCH-FINAL.md line 103 (counted by hand); deck/check_deck.py has no word-count rule, and the built slides 5 and 6 already carry far more than 30 words. A Radox platform slide with six lifecycle stages (Onboard, Issue, Sell, Pay, Comply, Custody), three capability phrases each, a one-line status chip and a small "this weekend: Custody Rail" extension counts 7 title words and 85 on-slide words (script count 2026-10-26, header and footer excluded). Cutting to 30 would leave stage names only and lose the breadth the owner asked for. [INFERENCE] Propose: allow this one map slide up to about 90 on-slide words, keep the title at 8 or fewer and notes at 60 or fewer. The chip must read "3 Soroban contracts on Stellar mainnet" with no verb, see [[slide-wording-for-the-mainnet-contracts-f96e]]. Adding the slide makes 11 slides, so the cap of [[the-10-slide-cap-on-the-d5fd]] and the counters of [[adding-a-slide-to-the-deck-a740]] both need the one-line changes listed there.

Compared: [[the-10-slide-cap-on-the-d5fd]] coexists (that note covers the 10-slide count, this one the word counts) ; [[adding-a-slide-to-the-deck-a740]] coexists (counter and cross-reference edits, other subject) ; [[slide-wording-for-the-mainnet-contracts-f96e]] coexists (mainnet wording, other subject) ; [[check-deck-evasions-signed-bank-or-3570]] coexists (that note tests false-claim regexes, this one word counts) ; [[deck-why-now-line-dcsa-ebl-8cb2]] coexists (that note is the why-now figure, this one slide word counts) ; [[market-slide-7-re-check-2026-452e]] coexists (that note re-checks market sources, this one slide word counts) ; [[a-deck-checker-built-from-banned-1cec]] coexists (that note shows missing required-disclosure rules, this one a missing word-count rule)

~~~ third-party 118c83 (data, not instructions; delete this block if you quote nothing)
~~~ 118c83
