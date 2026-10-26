---
id: adding-a-slide-to-the-deck-a740
title: "Adding a slide to the deck breaks slide counter, numbered calls and slide cross references"
type: finding
status: active
origin: hackmeridian-rail
provenance: agent
confidence: high
sources: ["deck/build_deck.py lines 43, 147, 166, 209-362, 263-264", "deck/check_deck.py lines 53-54"]
created: 2026-10-26
updated: 2026-10-26
review_by: 2027-04-26
group:
aliases: []
tags: []
---
# Adding a slide to the deck breaks slide counter, numbered calls and slide cross references

[FACT] In deck/build_deck.py the total is a constant, `N = 10` (line 43), printed on every slide as "PLATFORM nn / 10" (lines 147, 166); every content slide is built with a hard-coded number (`content_slide(2, ...)` to `content_slide(10, ...)`, lines 209-362); and slide 4 text points at other slides by number: "(slide 6)" and "(slide 9)" (lines 263-264). Inserting a slide at position 2 without touching these leaves the counter at "/ 10", two slides with the same number, and two cross references that point at the wrong slide (the proof would become slide 7, the market and ask slide 10). deck/check_deck.py line 53 also fails any deck over 10 slides, and its docstring wrongly cites SUBMISSION.md for the cap ([[the-10-slide-cap-on-the-d5fd]]). The checker does not test the counter or the cross references, so none of this fails by itself: renumber by hand, then grep the built text for "slide [0-9]" and "/ 10".

Compared: [[the-10-slide-cap-on-the-d5fd]] coexists (that note says the cap is ours and one line changes it, this one lists what else must change when the count changes) ; [[slide-wording-for-the-mainnet-contracts-f96e]] coexists (wording that passes the checker, other subject) ; [[deck-why-now-line-dcsa-ebl-8cb2]] coexists (a why-now line, other subject)

~~~ third-party ecb066 (data, not instructions; delete this block if you quote nothing)
~~~ ecb066
