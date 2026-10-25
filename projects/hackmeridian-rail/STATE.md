---
status: in-progress
updated: 2026-10-25
next: Sun 09:00 — Pedro pastes portal rules + form fields + editing-window dates into PORTAL-SEEN.md; Leo re-runs the wasm check, then starts LEO-BRIEF.md; Vhendala human pass on REVIEW-1.md, then stage 2
dispatch: off
member: pedro
---

# HackMeridian — rail Rio-Miami — state

## Arrival synthesis
2026-10-25 (redo of stage 1): the owner asked to redo stage 1 with specialists and an independent reviewer, because the first pass had none. First action: library search, then process the Raven inbox into notes, then researcher + product subagents on the five files, reviewer on all five.
What looks wrong: section 3 still says the full rules are "not read yet", but RULES.md says Pedro pasted them on 25/10, so STATE is stale there. check.py names LEO-BRIEF.md in its docstring, which freezes docs it does not measure.
Fact checked on disk: `deadline: 2026-10-26 10:00 +0000` is in TRACK.md front matter (matches KICKOFF.md); `RESEARCH-raven.md` and `knowledge/inbox/raven-custody-research.md` are the same research.

## 1. State in one line
green. Stage 1 redone with specialists and an independent reviewer (approve with changes, fixes applied, REVIEW-1.md); all stage-1 items closed; nothing built yet. Owner answered the stage-1 questions (card, 2026-10-25).

## 2. Intent (what counts as "done")
- What the owner wants, in their words (Scale intake, sent before the event): "a chain-of-custody contract for a tokenized physical asset in transit (Rio-Miami). Each handover between custodians (warehouse, port, carrier, customs) is signed by both the outgoing and incoming custodian with an event attestation; ownership stays with the token holder and final delivery burns the token. Proven end to end on testnet with signed transactions and connected to our API."
- Also wanted at the event: Stellar engineers review the design; meet anchors/ramps for the USD leg and logistics / trade-finance partners; improve the pitch.
- Kind: real project. Track: hackathon (builder track Scale; no thematic track needed for Scale, RULES.md).
- Investment: the weekend (Sun 25 09:00 to Mon 26 10:00 Lisbon), team Pedro + Leo (+ Vhendala); money: zero (testnet only).
- "Done" for the current stage: stage 1 of TRACK.md closed (done 2026-10-25); stage moves to 2 after Vhendala's human pass.
- Stop criterion (owner, 2026-10-25): if by Sun 25 18:00 Lisbon no handover signed by two custodians has run on testnet, cut the API connection and deliver contract + harness + recorded demo only.

## 3. What is true now
- Deadline: ours Mon 10:00, the event's Mon 12:00 "no late submissions"; submit at 08:00. Lisbon is UTC+0 for the whole event (summer time ended Sun 25 Oct 01:00 UTC).
- Rubric: 7 criteria scored 1–5, weights 20/20/15/15/10/10/10 (hackmeridian.com/build, read directly). Self-score 72/100 ceiling, 66 if the API connection is cut (IDEA.md).
- Requirements verified in the portal PDF and public pages: RULES.md, SUBMISSION.md. Video 2–4 min YouTube/Vimeo, deck ≤20 MiB, mandatory AI attribution and the prior-work disqualifier come only from Pedro's paste of the portal rules (in the central session transcript); planned to anyway.
- Portal rules page and submission form need login: not seen by any agent.
- The burn's `transfer_agent` wasm (`3870748b…`) is on testnet with `fn redeem` (checked 2026-10-25 01:02 UTC).
- check.py names only the proof file it reads and requires 7 distinct hashes; check OK re-recorded by central (owner: "Sim, travar"). Do not edit it without a new OK; propose the "each tx calls our contract" check after deploy.
- Library: 8 notes from this project (Raven research processed, rubric, rules, time zone).
- Repos: `pwsaragossy/rio-miami-rail` (private, empty, created 24/10); team board `pwsaragossy/hackmeridian-cos`. leo-schlanger invited with write to both on 24/10.
- `radox-internal` branch `hackmeridian` exists (from main), only for a backend change the API connection may need; never public.

## 4. What was done and how
- 2026-10-25 (central, owner's answers): `check.py` requires 7 distinct hashes, check OK re-recorded with track.sh; README gets a "Production path" section; Pedro pastes the portal rules, form fields and editing-window dates into `PORTAL-SEEN.md` at Sun 09:00.
- Workspace created with `setup.sh create ~/hackmeridian --share <hackmeridian-cos> --member pedro`.
- Stage 1 redo: researcher and product subagents with role cards rewrote the five files; reviewer subagent attacked them; fixes applied (REVIEW-1.md lists each).

## 5. Next actions
1. **Pedro (via central), Sun 09:00:** portal rules + form fields + editing window into `PORTAL-SEEN.md`; organizer question on the closed-platform repo.
2. **session-hackmeridian-rail, after deploy:** propose the "each tx calls our contract" check to the owner via the card. If the wasm is gone at 09:00, the redeem fallback goes back on the card.
3. **Vhendala:** human pass on REVIEW-1.md and the five files; then stage → 2.
4. **Leo:** Sun 09:00 re-run the wasm check (KICKOFF §8), then LEO-BRIEF.md.

## 6. If X, then Y
- If something needs the owner, it becomes a line on the card with `status: waiting-owner`. Do not ask.
- If the rules forbid code written before the event, list exactly what reused code comes from the public radox repo.
- If the portal rules contradict RULES.md or SUBMISSION.md, the portal wins: fix the files the same hour.

## 7. What I did not verify
- Whether the organizers accept a Scale repo that holds only the new work, with the platform backend closed. Ask an organizer at check-in.
- Portal rules, submission form and its editing window (login).
- Any evidence that a financier or buyer has the custody-visibility pain (IDEA.md: assumption; mentor test planned).
- SCF Build eligibility criteria themselves.
- PITCH.md slide 2 still has a fill marker for the cost of today's alternative.
