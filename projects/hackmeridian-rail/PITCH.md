# Pitch — outline v0 (2026-10-25, before the event)

Base: DECK-TEMPLATE.pptx (organizers' template; final deck exported as PDF or PPTX ≤20 MiB):
cover + Solution, PMF (problem), Technical workflow, Team (max 3 lines per member plus a photo). The template alone does not cover what
**Scale** asks (portal, "Requirements"): problem, solution, target users, value proposition, team,
future vision, business model, market opportunity, go-to-market. Scale is scored on: milestone
completion against the intake goals, SCF eligibility, production readiness, ecosystem impact.
So the deck keeps the template's look and order (Solution before PMF) and adds 4 slides between Technical workflow and Team. Max 10 (track default).

Judging is async (video, deck, repo, answers); live pitch only for finalists, Wed 28 Oct.
Rubric (CRITERIA.md): Ecosystem Alignment 20 · User Value & Problem 20 · Technical Execution 15 ·
Innovation 15 · Hackathon Progress 10 · Market & Ecosystem 10 · Product Design & UX 10 (scale 1–5 on /build, 1–10 in the portal rules; same weights).
Deliverables (SUBMISSION.md): deck as **PDF or PPTX ≤ 20 MiB** (export from DECK-TEMPLATE.pptx); demo video
**2–4 min on YouTube or Vimeo**; the deck and the README both state where AI generated code or assets. AI-generated narration, music or images in the video or deck are named as AI: the narration is an AI voice cloned from Pedro's own voice (owner, 2026-10-25), and the video, the deck and the README say so.

Copy rules (Radox canon): Radox is the **rail**, never the issuer; the partner is a **financial
institution / client** (never "sponsor" outside); regulation and licences are the client's and local
counsel's, in every external material; a token alone says nothing about ownership of the cargo — possession of cargo only
when tied to the bailee's document (carrier or warehouse). No partner or client names. Every number
comes from a source in this folder or the proofs; `{{fill}}` marks what only the build can give.

Claims guard (reviewed 2026-10-25). Say: 'Radox: 3 Soroban contracts deployed on Stellar mainnet (public repo, created 2026-08-19)'. Never: users, customers, revenue, investors, traction, 'live pilot'. No exporter, payer, cargo or pilot exists; never state or imply endorsement or a signed letter from any chamber, programme, government body or partner. Custody wording: 'a custody record for the shipment, keyed to the container or AWB number; in production it would sit beside the carrier's bill of lading (not integrated in this build)'. Never write: title, document of title, digital bill of lading, replaces the bill of lading, proof of ownership, legally recognised, UCC- or MLETR-compliant. A paper bill or a second token for the same cargo is not prevented on chain. USD leg: not built, nothing under contract; slide 8 is future tense; no USD flow in demo or video; name no candidate. Demo: all six actors are test keys held by one harness; it proves the mechanism, not independent custodians. Innovation: 'we found none in the directories searched on 2026-10-25', never 'none exists'.

## Slides

| # | Template slot | Title | Message (one per slide) | Proof on the slide |
|---|---|---|---|---|
| 1 | Cover | Radox Custody Rail: dual-signed custody for goods in transit, on Stellar | First corridor: Rio–Miami | team, track (Scale) |
| 2 | Solution | Every handover, signed by both hands | `custody_registry`: outgoing and incoming custodian sign the same transaction; the token never leaves the holder during transit; after the registry shows Delivered, the operator burns with the existing `redeem` (Radox platform policy, not enforced on-chain by the registry; `redeem` still needs the holder's signature) | screenshot of one dual-signed handover on stellar.expert |
| 3 | PMF (problem) | Who holds the cargo right now? | Between seller and buyer a shipment changes hands 4+ times (warehouse, port, carrier, customs); handovers are mostly paper or sit inside one carrier's or terminal's own system {{source needed}}, and nobody can prove the chain to a financier in real time | US$2.5T global trade finance gap in 2022 (ADB, Sept 2023): market size only, not evidence of the custody pain; no export-value figures |
| 4 | Technical workflow | How it runs on Stellar | open -> 4 dual-signed handovers -> deliver -> burn (existing `redeem`, run live in the same harness, which first checks status == Delivered); `head` hash chain survives the 7-day event window | diagram + contract ID + 7 tx hashes `{{fill: proofs/lifecycle.json}}` |
| 5 | (added) What we built this weekend | Prior work vs HackMeridian | table: existed (3 mainnet contracts, transfer_agent on testnet, phygital whole-asset flow) / built here (custody_registry, harness, verify-head, API connection) | commit timeline after Sun 09:00; AI usage: code, tests and scripts were written by AI coding agents; AI_USAGE.md says per file what a named person read |
| 6 | (added) Users and value | Who uses it | exporter, custodians (warehouse/port/carrier/customs), buyer, financier; value: a financier can see where the goods are and who signed for them before paying | — |
| 7 | (added) Business model and go-to-market | The rail is ours, the standard is public | SWIFT model: public record format, roles and events; Radox operates the rail and the API; first corridor Rio → Miami; next step: a first pilot shipment with one producer (none agreed yet); revenue: fee paid by the institution that operates the rail; not priced yet | {{fill: pricing line only if Pedro confirms}} |
| 8 | (added) Market and next steps | From one corridor to a standard | USD leg (future): an on-ramp from the SCF Integration List; planned: this contract is the proposed first milestone of an SCF Build application (not yet submitted); then the full testnet matrix, then mainnet | — |
| 9 | Team | Why us | Pedro Saragossy, founder and team captain; Leo Schlanger, developer; Vhendala, project supervision, product review and team photo. Leo and Vhendala joined for the hackathon. Radox: 3 Soroban contracts deployed on Stellar mainnet | photos only with each person's consent; max 3 lines per member |

## Demo video (backup and async judging)

1. 0:00–0:20 problem in one line + the map Rio → Miami.
2. 0:20–1:30 the lifecycle running: open, each handover with both signatures, `deliver`; stellar.expert
   tab on each hash.
3. 1:30–2:00 `verify-head` recomputing the chain from events (exit 0).
4. 2:00–2:30 the burn (`redeem`) closing the cycle, holder balance 0.
5. 2:30–3:00 the public shipment page (must-have) and, if done, the Radox API reading the registry.
Rules: 2–4 min, YouTube or Vimeo — target 3:00.

## Script notes for the SDF judges

- We use Stellar's core features together: multi-party `require_auth` in one invocation,
  SAC admin control (freeze/clawback) for the token, and events with an on-chain hash
  chain. We found no dual-signed custody in the directories searched on 2026-10-25 (RESEARCH-raven.md §5).

## Open

- DECK-TEMPLATE.pptx (organizers' template) is the base; the final deck is built from it after the proofs exist and exported as PDF or PPTX ≤20 MiB.
