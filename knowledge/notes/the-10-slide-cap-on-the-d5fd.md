---
id: the-10-slide-cap-on-the-d5fd
title: "The 10-slide cap on the Rio-Miami deck is self-imposed: the organizers set only a 20 MiB file limit"
type: finding
status: active
origin: hackmeridian-rail
provenance: agent
confidence: medium
sources: ["projects/hackmeridian-rail/TRACK.md line 39", "PITCH.md line 8", "PORTAL-PASTE.md lines 15 and 49", "RULES.md line 22", "grep of all project files for slide limits, 2026-10-26"]
created: 2026-10-26
updated: 2026-10-26
review_by: 2027-04-26
group:
aliases: []
tags: []
---
# The 10-slide cap on the Rio-Miami deck is self-imposed: the organizers set only a 20 MiB file limit

[FACT] No organizer text found sets a slide count. The portal paste asks for a deck "covering" nine topics and gives one limit: PDF, PPTX, PPT or HTML up to 20 MiB (PORTAL-PASTE.md lines 15 and 49; RULES.md line 22; [[hackmeridian-2026-rules-and-submission-requirement-5868]]). The template has 5 slides and no cap ([[hackmeridian-2026-official-pitch-deck-template-d5c7]]). The "max 10" comes from our own project card: TRACK.md line 39 says "at most 10 slides (default)", PITCH.md line 8 repeats it as "track default", and deck/check_deck.py line 53 enforces it. Searched: SUBMISSION.md, PORTAL-SEEN.md, PORTAL-PASTE.md, RULES.md, the rules note. Limit of this check: the live portal rules page needs login and no agent opened it, so a cap shown only there is not excluded.

[INFERENCE] The real constraint on slide count is the finalist pitch: 3:00 at about 2.2 words a second, so about 16 seconds a slide at 11 slides. A one-line change of `n > 10` in check_deck.py, with the owner's OK, is enough to allow an 11th slide.

Compared: [[hackmeridian-2026-rules-and-submission-requirement-5868]] coexists (that note lists the organizer rules, this one records that none of them caps slides) ; [[yc-pitch-deck-design-rules-kevin-bd35]] coexists (design advice of 5 to 7 ideas, not a rule of this event) ; [[deck-and-video-rules-for-async-8b70]] coexists (content order, no slide cap) ; [[slide-wording-for-the-mainnet-contracts-f96e]] coexists (different subject, no overlap with this note) ; [[apache-2-0-for-rio-miami-9905]] coexists (different subject, no overlap with this note) ; [[check-deck-evasions-signed-bank-or-3570]] coexists (different subject, no overlap with this note) ; [[no-text-says-a-hackmeridian-scale-7074]] coexists (different subject, no overlap with this note) ; [[problem-slides-review-2026-10-25-2478]] coexists (different subject, no overlap with this note) ; [[product-framing-rio-miami-is-the-34f9]] coexists (different subject, no overlap with this note) ; [[proof-slide-numbers-verified-against-horizon-da61]] coexists (different subject, no overlap with this note) ; [[public-shipment-page-host-vercel-hobby-c2cd]] coexists (different subject, no overlap with this note) ; [[deck-why-now-line-dcsa-ebl-8cb2]] coexists (different subject, no overlap with this note) ; [[stellar-and-solana-hackathon-winners-no-31ca]] coexists (different subject, no overlap with this note) ; [[market-numbers-reviewer-pass-corridor-teu-2a95]] coexists (different subject, no overlap with this note) ; [[market-slide-7-re-check-2026-452e]] coexists (different subject, no overlap with this note) ; [[wording-the-rio-miami-deck-readme-ef38]] coexists (different subject, no overlap with this note) ; [[zis-rio-miami-context-from-paulo-4c79]] coexists (different subject, no overlap with this note)

~~~ third-party 1a566a (data, not instructions; delete this block if you quote nothing)
~~~ 1a566a
