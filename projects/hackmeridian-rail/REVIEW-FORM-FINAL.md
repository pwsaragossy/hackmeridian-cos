# Review: FORM-ANSWERS.md (final paste)

Verdict: approve with changes (1 medium, 1 low; no blocker)

## Checked and fine
- Field order matches SUBMISSION.md table (title, tagline, description, problem, challenges, what's next, repo, demo, video, deck, track, stack, prior work, AI note, terms). Char counts in headings match the boxes. Only placeholders: Video link, Deck file. No notes/TODO inside boxes.
- API sentence matches README line 108: local development run, curl output only, judges cannot reproduce. Head 2d74fec0...5414 in README is the first (lifecycle) shipment.
- What's next: future tense for standard, rail, integrations, pilot; "Today no such ... exists" closes it; no partner/mentor/chamber/port/airport named (generic categories only, same as README); no customers or live pilot claimed.

## Findings

1. MEDIUM, ambiguous reference. The sentence sits right after the second-shipment sentence, so "the same record" reads as the second shipment; README's head is the first shipment's.
Quote: "In a local test run, a read-only endpoint of the closed Radox backend read the same record and returned the same head; its curl output, in the README, is the only evidence."
Replace: "In a local development run, a read-only endpoint of the closed Radox backend read the first shipment's record and returned the same head as `verify-head`; the curl output in the README is the only evidence, and it cannot be reproduced from this repo."
(adds ~60 chars; Description stays far under 8000)

2. LOW, wording drift. What's next says "local test run", README says "local development run".
Quote: "(a read-only Radox API endpoint already reads this registry in a local test run)"
Replace: "(a read-only Radox API endpoint already reads this registry in a local development run, not reproducible from this repo)"
(859 -> ~900 chars, update the heading count)
