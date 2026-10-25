# Form answers — paste source for the portal (internal until Pedro's OK)

Write each final answer here, count it, then paste all in one go (never reload the form page).
Plan, sources and limits: SUBMISSION.md "Portal form, field by field". Only Pedro checks the terms box and submits.

| Field | Limit | Chars | Status |
|---|---|---|---|
| Project title | unseen | 0 | waiting on Pedro's pick (card) |
| Tagline | 120 | 0 | draft in SUBMISSION.md |
| Description | 8000, Markdown | 0 | Sun 20:30–22:00 |
| Problem solved | unseen, keep < 1500 | 0 | review-4 |
| Challenges | unseen, keep < 1500 | 0 | Mon 06:00 |
| What's next | unseen, keep < 1500 | 776 (draft) | review-4 |
| Repository link | HTTPS, public | — | Mon 06:00 |
| Demo link | — | — | Sun 18:00 |
| Video link | YouTube/Vimeo | — | Mon 08:00 |
| Deck file | ≤ 20 MiB | — | Mon 06:00 |
| Thematic track | one | — | Stellar Unlocked |
| Tech stack | ≤ 25 items | 0 items | Mon 06:00 |
| Prior work disclosure | unseen | 0 | review-4 |
| AI tooling note | unseen | 0 | review-4 |

## Answers

### Technical, fragment for the three-machine proof (draft 2026-10-25, review-4 pending)

In a second testnet shipment, two team members authorised their own handovers from their own computers, each with a testnet key that, by their account, never left that computer; only public keys and signed authorisation entries were exchanged, and the operator's machine checked each entry before submitting. The other keys in that shipment (warehouse, recipient, holder and operator) are our test keys on one machine. Four transactions, all successful, and verify-head recomputes the same head (proof: proofs/three-machine.json on the repo's three-machine branch, also in the README).

### What's next (draft 2026-10-25, review-4 pending)

Rio–Miami is our first corridor, not the product. Next we will connect the rail to the Radox platform's physical-asset flow (a read-only Radox API endpoint already reads this registry on testnet), ask logistics and trade-finance mentors whether a custodian's signature could replace a scanned stamp, and prepare an SCF Build application. Mainnet waits for an audit and the issuer-account lock described in the README. Longer term, we aim to grow this into a shared standard for custody of tokenized goods across trade corridors, as SWIFT did for payment messages, and we intend to approach chambers of commerce, ports and airports to integrate with their systems. Today no such standard, adoption or partnership exists: this weekend proves the record on Stellar testnet with test keys.
