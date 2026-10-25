---
id: wording-the-rio-miami-deck-readme-ef38
title: "Wording the Rio-Miami deck, README and video without overclaiming"
type: howto
status: active
origin: hackmeridian-rail
provenance: agent
confidence: medium
sources: ["projects/hackmeridian-rail/PITCH.md, IDEA.md, KICKOFF.md, LEO-BRIEF.md", "github.com/pwsaragossy/radox README", "stellar.expert API and Horizon mainnet, 2026-10-25", "adb.org 2023 trade finance gaps survey"]
created: 2026-10-25
updated: 2026-10-25
review_by: 2027-01-25
group:
aliases: [claims guard, overclaim list]
tags: [hackmeridian, pitch, claims]
---
# Wording the Rio-Miami deck, README and video without overclaiming

HackMeridian names "misrepresenting your work" as conduct and makes undisclosed prior work a disqualifier ([[hackmeridian-2026-rules-and-submission-requirement-5868]]), and Scale judges score against the intake text ([[hackmeridian-scale-intake-as-submitted-the-7fb5]]). Use these replacements wherever the left column appears in PITCH.md, IDEA.md, KICKOFF.md, LEO-BRIEF.md, the README, the deck or the video script.

1. Burn. Not "delivery unlocks / gates / triggers the burn". Write: "Delivery authorises the burn: the operator burns with the existing `redeem` only after the registry reports Delivered. That is a policy of the Radox platform, not enforced on-chain by the registry, and `redeem` still needs the holder's signature." The harness must read the registry status before `redeem` and record that it did, otherwise the sentence is not shown.
2. Token and title. Say "token", never "title" (five places in the files use the word: IDEA.md line 9, CRITERIA.md line 15, LEO-BRIEF.md lines 55 and 106, PITCH.md line 49; PITCH.md slide 3 says "ownership stays with the token holder", which is the intake's own wording and stays only as a quote of it). Say "a custody record for the shipment, keyed to the container or AWB number; in production it would sit beside the carrier's bill of lading (not integrated in this build)"; never "title to cargo" or "replaces the bill of lading". A second token or a paper bill for the same cargo is not prevented on chain (the unique key covers only this registry). Legal basis and its limits: [[ucc-1-201-b-16-a-ce13]] and [[ucc-article-7-and-brazilian-rules-77dd]]. No legal cite in the deck.
3. Mainnet and traction. Write "3 Soroban contracts deployed on Stellar mainnet since June 2026 (public repo, created 2026-08-19)". Checked 2026-10-25: the wasm of all three is on mainnet, the `yield_distributor` instance in the public README exists (created 2026-07-10, 7 invocations), the issuer account has `auth_required`, `auth_revocable` and `auth_clawback_enabled` set, and Horizon shows wasm uploads from that issuer on 2026-06-01 and contract creations on 2026-06-02, 2026-07-06, 2026-07-10 and 2026-08-13 (the per-offering `token_sale` and `maturity_settlement` instances were not matched one by one to their IDs). Never "live with users", customers, revenue, investors or "live pilot". The public README says "live on mainnet", so the deck must not say more than it does.
4. Pilot. Not "pilot with one producer". Write "next step: a first pilot shipment with one producer (none agreed yet)". No exporter, payer or cargo exists. Never state or imply endorsement by any chamber, government body or programme, or a signed letter.
5. USD leg. Future tense. Not built, no anchor under contract. The demo and video show no USD flow. Do not name any candidate.
6. SCF. Not "first milestone of our SCF Build application" unless the application has been submitted. Write "planned: this contract is the proposed first milestone of an SCF Build application (round #46 closes 2026-11-08)" only if the owner agrees. The README never says "we are eligible": see [[scf-build-participant-rules-entity-in-a7b1]].
7. Team. "Pedro Saragossy, founder and team captain; Leo Schlanger, developer; Vhendala, QA and review. Leo and Vhendala joined for the hackathon." Never "Radox staff" or "co-founder" for them, and never "Soroban developer" for Leo (not confirmed). Photos need each person's consent.
8. AI usage. Name what happened, per file: which tool and model generated it, and which human or reviewer agent actually read it. Not "human-reviewed" unless a named person read that code. If the narration, music or images are AI-generated, say so.
9. Prior work. List the Radox platform, the three public contracts, `transfer_agent` on testnet (closed source, a new instance deployed from its wasm hash), AND the pre-event design: the 2026-10-20 architecture panel, plus the planning files dated 2026-10-24 and 2026-10-25 (KICKOFF, LEO-BRIEF, PITCH outline, `check.py`). State that no contract code was written before Sun 09:00.
10. Paper handovers. Not "each handover is paper". Write "handovers are mostly paper or sit inside one carrier's or terminal's own system" and mark it source needed. An electronic bill of lading may exist, so position the registry as the physical-custody layer under it.
11. Problem number (slide 2). Do not use export-value figures. A sourced context number: the global trade finance gap was US$2.5 trillion in 2022 (ADB, 2023 Trade Finance Gaps, Growth and Jobs Survey, September 2023; check whether a newer edition exists before use). It sizes the financing gap, it is not evidence of the custody pain, and the slide must say that.
12. Innovation. "We found none in the directories searched on 2026-10-25" ([[no-sep-and-no-stellar-project-aa39]]), never "none exists". Name the nearest neighbour, which releases milestone escrow on attested trade events, not on dual-signed custody.
13. Demo honesty. All six actors are test keys held by one harness: it proves the mechanism, not independent custodians. Say so on the slide and in the video. Mentor feedback is quoted verbatim, with the mentor's permission, and the number of mentors asked is stated.
14. Evidence lifetime. State in the README that testnet is reset about quarterly (next scheduled 2026-12-16) and which committed snapshots and video remain after that: [[stellar-testnet-resets-wipe-contracts-and-dfe4]].
15. Track name. Name "Stellar Unlocked" in the deck only after the portal shows it saved on the team or submission page. Until then describe the capabilities used (multi-party auth in one call, SAC authorize and clawback, events with a hash chain) without naming a track.
16. Only what ran. Slides 4 and 5 and the video list only steps with a SUCCESS testnet hash by Sun 22:00. If the API connection was cut, the README, deck and video say so against the intake sentence.

Compared: [[hackmeridian-scale-intake-as-submitted-the-7fb5]] coexists (the intake text to match, this note is wording rules) ; [[no-sep-and-no-stellar-project-aa39]] coexists (the search behind the innovation hedge, not wording rules) ; [[stellar-and-solana-hackathon-winners-no-31ca]] coexists (different subject, no overlap in what it states)

Superseded in part (2026-10-25 19:40, owner): where this note asks for a hedge or a "none confirmed"/"does not exist yet" label, [[founder-voice-in-public-text-sell-d820]] wins; the truth rules here still bind.
