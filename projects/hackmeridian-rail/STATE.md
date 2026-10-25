---
status: in-progress
updated: 2026-10-24
next: Sun 09:00 — review-1 by Vhendala (reviewer card) on RULES, SUBMISSION, CRITERIA, IDEA, KICKOFF; owner approves the check in central; Leo starts LEO-BRIEF.md
dispatch: off
member: pedro
---

# HackMeridian — rail Rio-Miami — state

## Arrival synthesis
2026-10-25 (redo of stage 1): the owner asked to redo stage 1 with specialists and an independent reviewer, because the first pass had none. First action: library search, then process the Raven inbox into notes, then researcher + product subagents on the five files, reviewer on all five.
What looks wrong: section 3 still says the full rules are "not read yet", but RULES.md says Pedro pasted them on 25/10, so STATE is stale there. check.py names LEO-BRIEF.md in its docstring, which freezes docs it does not measure.
Fact checked on disk: `deadline: 2026-10-26 10:00 +0000` is in TRACK.md front matter (matches KICKOFF.md); `RESEARCH-raven.md` and `knowledge/inbox/raven-custody-research.md` are the same research.

## 1. State in one line
green. Project opened on 2026-10-24, hacking starts Sun 25 Oct 09:00 Lisbon; nothing built yet.

## 2. Intent (what counts as "done")
- What the owner wants, in their words (Scale intake, sent before the event): "a chain-of-custody contract for a tokenized physical asset in transit (Rio-Miami). Each handover between custodians (warehouse, port, carrier, customs) is signed by both the outgoing and incoming custodian with an event attestation; ownership stays with the token holder and final delivery burns the token. Proven end to end on testnet with signed transactions and connected to our API."
- Also wanted at the event: Stellar engineers review the design; meet anchors/ramps for the USD leg and logistics / trade-finance partners; improve the pitch.
- Kind: real project. Track: hackathon (builder track Scale, thematic Stellar Unlocked).
- Investment: the weekend (Sun 25 09:00 to Mon 26 10:00 Lisbon), team Pedro + Leo (+ Vhendala); money: zero (testnet only).
- "Done" for the current stage: stage 1 of TRACK.md closed.
- Stop criterion (owner, 2026-10-25): if by Sun 25 18:00 Lisbon no handover signed by two custodians has run on testnet, cut the API connection and deliver contract + harness + recorded demo only.

## 3. What is true now
- Deadline: owner said 10:00 on 26/10; hackmeridian.com says hacking ends Mon 12:00, no late submissions. 10:00 kept as 2 h buffer. Lisbon is UTC+0 on 26/10 (summer time ends 25/10).
- Requirement for every project (portal PDF, 24/10): public GitHub repo with the project source; README with summary, problem, setup, env vars, demo; architecture overview with contract IDs; live demo or video, public URL for user-facing apps; evidence of an onchain testnet tx; disclose prior work.
- Scale is judged on: milestone completion against the intake goals, SCF eligibility, production readiness, ecosystem impact (hackmeridian.com). Async judging of video, deck, repo, answers; finalists pitch Wed 28.
- Full event rules are behind the portal login (app.hackmeridian.com/portal/rules); not read yet.
- Repos: `pwsaragossy/rio-miami-rail` (private, empty, created 24/10); team board `pwsaragossy/hackmeridian-cos`. leo-schlanger invited with write to both on 24/10.
- `radox-internal` branch `hackmeridian` exists (from main), only for a backend change the API connection may need; never public.

## 4. What was done and how
- Workspace created with `setup.sh create ~/hackmeridian --share <hackmeridian-cos> --member pedro`.

## 5. Next actions
1. **session-hackmeridian-rail (researcher):** read the full rules in the portal once the owner is logged in; close `rules` and `submission-reqs` in TRACK.md.
2. **session-hackmeridian-rail (product):** criteria with weights, idea scored, target + check proposed on the card.

## 6. If X, then Y
- If something needs the owner, it becomes a line on the card with `status: waiting-owner`. Do not ask.
- If the rules forbid code written before the event, list exactly what reused code comes from the public radox repo.

## 7. What I did not verify
- Whether the organizers accept a Scale repo that holds only the new work, with the platform backend closed. Ask an organizer at check-in.
