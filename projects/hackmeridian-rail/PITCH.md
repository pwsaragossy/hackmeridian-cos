# Pitch — outline v0 (2026-10-25, before the event)

Base: the HackMeridian template (Google Slides `114XIdYHwVNNhdx1lRt2qvVRsU7RdmPycEKoo059TWC0`):
cover + Solution, PMF (problem), Technical workflow, Team. The template alone does not cover what
**Scale** asks (portal, "Requirements"): problem, solution, target users, value proposition, team,
future vision, business model, market opportunity, go-to-market. Scale is scored on: milestone
completion against the intake goals, SCF eligibility, production readiness, ecosystem impact.
So the deck keeps the template's look and order and adds 4 slides. Max 10 (track default).

Judging is async (video, deck, repo, answers); live pitch only for finalists, Wed 28 Oct.

Copy rules (Radox canon): Radox is the **rail**, never the issuer; the partner is a **financial
institution / client** (never "sponsor" outside); regulation and licences are the client's and local
counsel's, in every external material; a token is never title by itself — possession of cargo only
when tied to the bailee's document (carrier or warehouse). No partner or client names. Every number
comes from a source in this folder or the proofs; `[[fill]]` marks what only the build can give.

## Slides

| # | Template slot | Title | Message (one per slide) | Proof on the slide |
|---|---|---|---|---|
| 1 | Cover | Radox — the custody rail for real-world goods in transit | Rio → Miami, on Stellar | team, track (Scale · Stellar Unlocked) |
| 2 | PMF (problem) | Who holds the cargo right now? | Between seller and buyer a shipment changes hands 4+ times (warehouse, port, carrier, customs); each handover is paper, and nobody can prove the chain to a financier in real time | `[[fill: one sourced number on trade-finance gap or document delays]]` |
| 3 | Solution | Every handover, signed by both hands | `custody_registry`: outgoing and incoming custodian sign the same transaction; ownership stays with the token holder; delivery unlocks the burn | screenshot of one dual-signed handover on stellar.expert |
| 4 | Technical workflow | How it runs on Stellar | open → 4 dual-signed handovers → deliver → `redeem` burns (prior work); `head` hash chain survives the 7-day event window; passkey smart accounts for custodians | diagram + contract ID + 6 tx hashes `[[fill: proofs/lifecycle.json]]` |
| 5 | (added) What we built this weekend | Prior work vs HackMeridian | table: existed (3 mainnet contracts, transfer_agent on testnet, phygital whole-asset flow) / built here (custody_registry, harness, verify-head, API connection) | commit timeline after Sun 09:00 |
| 6 | (added) Users and value | Who uses it | exporter, custodians (warehouse/port/carrier/customs), buyer, financier; value: a financier can see where the goods are and who signed for them before paying | — |
| 7 | (added) Business model and go-to-market | The rail is ours, the standard is public | SWIFT model: public record format, roles and events; Radox operates the rail and the API; first corridor Rio → Miami; pilot with one producer | `[[fill: pricing line only if Pedro confirms]]` |
| 8 | (added) Market and next steps | From one corridor to a standard | USD leg via a listed on-ramp; first milestone of our SCF Build application = this contract on testnet `[[confirm wording with Pedro]]`; then the full testnet matrix, then mainnet | link to the mentor question on ramps |
| 9 | Team | Why us | Pedro Saragossy — founder, Radox live on Stellar mainnet; Leo Schlanger — developer; Vhendala — QA and review | photos |

## Demo video (backup and async judging)

1. 0:00–0:20 problem in one line + the map Rio → Miami.
2. 0:20–1:30 the lifecycle running: open, each handover with both signatures, `deliver`; stellar.expert
   tab on each hash.
3. 1:30–2:00 `verify-head` recomputing the chain from events (exit 0).
4. 2:00–2:30 the Radox side: the delivery unlocking the existing burn.
Length to adjust to the rules once read in the portal.

## Script notes for the SDF judges

- "Stellar Unlocked": we use core features together — multi-party `require_auth` in one invocation,
  SAC admin control (freeze/clawback) for title, passkey smart accounts, and events with an on-chain hash
  chain. Nobody in the ecosystem indexes we checked does dual-signed custody (RESEARCH-raven.md §5).
- Ask the mentors: which ramp delivers USD to a C-address (SEP-45 draft).

## Open

- Video length, deck format and submission fields: from the full rules (portal, needs Pedro's login).
- The Google Slides file is the template copy; the final deck is built there after the proofs exist.
