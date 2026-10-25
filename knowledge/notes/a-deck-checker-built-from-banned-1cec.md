---
id: a-deck-checker-built-from-banned-1cec
title: "A deck checker built from banned words passes a deck stripped of its required disclosures"
type: finding
status: active
origin: hackmeridian-rail
provenance: agent
confidence: high
sources: [deck/check_deck.py, deck/REVIEW.md]
created: 2026-10-25
updated: 2026-10-25
review_by: 2027-04-25
group:
aliases: []
tags: []
---
# A deck checker built from banned words passes a deck stripped of its required disclosures

A deck check made only of banned-word regexes, hash checks, slide count and font size passed a deliberately broken copy of the Rio-Miami deck (reviewer subagent, 2026-10-25): AI attribution and prior-work text removed, "No users or revenue yet" replaced with "Our users love it and revenue is growing", "24" changed to "240", the full name cut to "Pedro". It exited 0. The disqualifiers in the rules are omissions (undisclosed prior work, missing AI note), and a banned list cannot see an omission ([[hackmeridian-2026-rules-and-submission-requirement-5868]], [[wording-the-rio-miami-deck-readme-ef38]]).

Fix used in deck/check_deck.py of hackmeridian-rail: a REQUIRED list of disclosures that must appear somewhere on the slides (full name, tool name, AI_USAGE.md, prior-work header, first commit time, "No users or revenue yet", "none agreed yet", "not built", the test count), plus banned overclaim phrases. Proof: the same kind of mutated copy now fails with 4 failures, the real deck passes. Lesson: test any checker by mutating its input before trusting its exit 0; it still cannot read images or check numbers other than the listed ones.

Compared: none similar

