---
id: claims-hackmeridian-material-may-and-may-3e4f
title: "Claims HackMeridian material may and may not make while no partner, pilot or customer is signed"
type: finding
status: active
origin: hackmeridian-rail
provenance: agent
confidence: medium
sources: ["hackmeridian.com/terms.html sec 05, 06, 14 (13 Aug 2026)", "PORTAL-PASTE.md lines 46-53", "Horizon and stellar.expert mainnet checks 2026-10-25", "public radox README 2026-10-25"]
created: 2026-10-25
updated: 2026-10-25
review_by: 2026-11-25
group:
aliases: [traction claims, partner names, pilot claim, overclaim]
tags: [legal, claims, hackmeridian, traction]
---
# Claims HackMeridian material may and may not make while no partner, pilot or customer is signed

Why it matters: [FACT] the event terms (section 05, opened 2026-10-25) forbid misrepresenting your work, identity or eligibility, and allow removal without refund; the portal rules (PORTAL-PASTE.md) say undisclosed prior work disqualifies and that users and traction "help explain" a project, which invites a stretch. The team also indemnifies the organizer for claims from its submission (section 14). The deck, README, video and form answers are all public.

**Facts, with how well each is known.** Verified today: the mainnet issuer GBONFES3...G6GD has auth_required, auth_revocable and auth_clawback_enabled all true (Horizon); yield_distributor exists on mainnet at the ID in the public radox README, created 2026-07-10, wasm hash equal to the README, 7 invocations (stellar.expert API). Not verified by me on chain: the token_sale and maturity_settlement instances (the README gives only wasm hashes and a deploy date of 2026-06-01). Radox-internal commercial facts are not recorded here; claim no users, customers, revenue or pilot. The public radox README itself says "live on mainnet since June 2026" and speaks of "the current offering", which a reader will take as live business.

| Topic | May say | Must not say |
|---|---|---|
| Mainnet | "3 Soroban contracts deployed on Stellar mainnet since June-July 2026 (public repo, dates)" | "live with users", "live offering", "customers", "investors" |
| Pilot | "next step: a first pilot shipment on Rio-Miami; none agreed yet" | "pilot with one producer", "running a pilot" |
| Partners | roles only: "a financial institution", "a logistics operator"; "we intend to approach..." | any name (any partner, programme, chamber or person), endorsement, "in partnership with", "supported by" |
| Traction field | "None claimed. Pre-revenue. Contracts deployed on mainnet." | users, volume, revenue, "traction" |
| Problem evidence | "hypothesis, being tested with mentors" | "financiers need this", unsourced numbers |
| SCF | "we plan to apply to SCF #46" (draft, not submitted per extract) | "our SCF Build application" as if filed, "SCF-funded", "SCF-eligible" |
| Team | "Leo Schlanger, developer"; "Vhendala, QA and review" | "Soroban developer" (not confirmed), titles nobody has |
| Review | "design reviewed by <role> at HackMeridian on <date>" only after it happens | "reviewed by Stellar engineers" before it happens, "audited" ever |
| Novelty | "we found none in the directories searched on 2026-10-24" | "nobody does this" |
| Burn | "after Delivered the operator burns the token (existing redeem)" | "the contract burns", "new work" for the burn |
| USD leg | future tense, no anchor named | any working USD flow, any named ramp |
| Demo | "testnet, test keys, six test actors, not real custodians" | real carrier, port or customs names; real container or B/L numbers |

Why no names even if friendly: [INFERENCE] naming a third party without its written consent risks a confidentiality or NDA breach (nobody has said whether one exists, open question) and false-endorsement exposure, and the rail PITCH.md already forbids partner names. A signed letter or a named quote is the only thing that changes this, and then only for the wording the person approved.

Counter-argument: judges reward traction and a stretch might win points. The cost asymmetry is the answer: a stretch can move at most the User Value (20), Market (10) and Hackathon Progress (10) criteria by some points, while a misrepresentation finding can remove the whole entry.


Owner decision 2026-10-25 19:59 UTC (board, Sessions build and submission, lines 56-57): public text may say "Radox has openings with ports and airports, and chambers of commerce are opening doors" and that chambers of commerce in Brazil and in Miami are engaged with Radox on the corridor. Still no chamber, ZIS or Paulo named, and no concrete ask. This overrides the chambers line under "must not say".

Compared: [[hackmeridian-scale-intake-as-submitted-the-7fb5]] coexists (that note is what was submitted, this one is what may be said now) ; [[ucc-article-7-and-brazilian-rules-77dd]] coexists (title wording only) ; [[wording-the-rio-miami-deck-readme-ef38]] coexists (that howto lists replacement wording per slide and file, this note gives the legal basis, the verification trail and the table of what may and may not be said, and both agree on the wording) ; [[wording-market-figures-in-the-deck-dadf]] coexists (different subject, no overlap in what it states)
