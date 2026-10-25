---
status: in-progress
updated: 2026-10-25
next: Sun 09:00 — Pedro pastes the submission form fields into PORTAL-SEEN.md; Leo re-runs the wasm check, then starts LEO-BRIEF.md; Vhendala manual product review of REVIEW-1.md, then stage 2. Pedro asks an organizer at check-in: is a Scale repo with only the new work (backend closed) accepted? Portal capture: thematic track saved and form fields, then form dry-run.
dispatch: off
member: pedro
---

# HackMeridian — rail Rio-Miami — state

## Arrival synthesis
2026-10-25 (redo of stage 1): the owner asked to redo stage 1 with specialists and an independent reviewer, because the first pass had none. First action: library search, then process the Raven inbox into notes, then researcher + product subagents on the five files, reviewer on all five.
What looks wrong: (both fixed 2026-10-25).
Fact checked on disk: `deadline: 2026-10-26 10:00 +0000` is in TRACK.md front matter (matches KICKOFF.md); `RESEARCH-raven.md` and `knowledge/inbox/raven-custody-research.md` are the same research.

## 1. State in one line
green. Stage 1 redone with specialists and an independent reviewer (approve with changes, fixes applied, REVIEW-1.md); all stage-1 items closed; nothing built yet. Owner answered the stage-1 questions (card, 2026-10-25).

## 2. Intent (what counts as "done")
- What the owner wants, in their words (Scale intake, sent 2026-10-21 about 14:25 UTC, before the event): "a chain-of-custody contract for a tokenized physical asset in transit (Rio-Miami). Each handover between custodians (warehouse, port, carrier, customs) is signed by both the outgoing and incoming custodian with an event attestation; ownership stays with the token holder and final delivery burns the token. Proven end to end on testnet with signed transactions and connected to our API."
- Also wanted at the event: Stellar engineers review the design; meet anchors/ramps for the USD leg and logistics / trade-finance partners; improve the pitch.
- Kind: real project. Track: hackathon (builder track Scale; thematic track Stellar Unlocked (optional for Scale), chosen by Pedro 2026-10-24).
- Investment: the weekend (Sun 25 09:00 to Mon 26 10:00 Lisbon), team Pedro, Leo, Vhendala (3); money: zero (testnet only).
- "Done" for the current stage: stage 1 of TRACK.md closed (done 2026-10-25); stage moves to 2 after Vhendala's manual product review.
- Stop criterion (owner, 2026-10-25): if by Sun 25 18:00 Lisbon no handover signed by two custodians has run on testnet, cut the API connection and deliver contract + harness + recorded demo only.

## 3. What is true now
- Deadline: the portal's project editing window runs Sun 25 09:00 to Mon 26 10:00 Lisbon (owner, 2026-10-25: "9am do dia 25 até 10am do dia 26, já falamos disso"). Mon 10:00 is the hard close, not a buffer; the event's Mon 12:00 is when hacking ends and gives no extra time to us. Submit at 08:00. Rubric: 1–10 per criterion (portal rules page, settled 2026-10-25). Lisbon is UTC+0 for the whole event (summer time ended Sun 25 Oct 01:00 UTC).
- Rubric: 7 criteria, weights 20/20/15/15/10/10/10; scale 1–5 on hackmeridian.com/build but 1–10 in the portal rules (PORTAL-PASTE.md), checked at Sun 09:00. Self-score 72/100 ceiling, 66 if the API connection is cut (IDEA.md).
- Requirements verified in the portal PDF and public pages: RULES.md, SUBMISSION.md. Video 2–4 min YouTube/Vimeo, deck ≤20 MiB, mandatory AI attribution and the prior-work disqualifier come from Pedro's paste of the portal rules, now verbatim on disk in PORTAL-PASTE.md; binding.
- Portal rules page and submission form need login: not seen by any agent.
- The burn's `transfer_agent` wasm (`3870748b…`) is on testnet with `fn redeem` (checked 2026-10-25 01:02 UTC).
- check.py names only the proof file it reads and requires 7 distinct hashes; check OK re-recorded by central (owner: "Sim, travar"). Do not edit it without a new OK; propose the "each tx calls our contract" check after deploy.
- Library: library notes tagged hackmeridian-rail.
- Repos: `pwsaragossy/rio-miami-rail` (private, empty, created 24/10); team board `pwsaragossy/hackmeridian-cos`. leo-schlanger invited with write to both on 24/10.
- `radox-internal` branch `hackmeridian` exists (from main), only for a backend change the API connection may need; never public.

## 4. What was done and how
- 2026-10-25 (central, owner's answers): pushes to both repos and testnet deploys of the shipment page are pre-authorized for the weekend (repo public and submission still need the owner's OK); Vhendala does a manual product review, not code; the Mon 00:00 fresh-run is an independent agent on a clean clone.
- 2026-10-25 (central, owner's answers): `check.py` requires 7 distinct hashes, check OK re-recorded with track.sh; README gets a "Production path" section; Pedro pastes the portal rules, form fields and editing-window dates into `PORTAL-SEEN.md` at Sun 09:00.
- Workspace created with `setup.sh create ~/hackmeridian --share <hackmeridian-cos> --member pedro`.
- Stage 1 redo: researcher and product subagents with role cards rewrote the five files; reviewer subagent attacked them; fixes applied (REVIEW-1.md lists each).

## 5. Next actions
1. **Pedro (via central), Sun 09:00:** portal rules + form fields + editing window into `PORTAL-SEEN.md`; organizer question on the closed-platform repo.
2. **session-hackmeridian-rail, after deploy:** propose the "each tx calls our contract" check to the owner via the card. If the wasm is gone at 09:00, the redeem fallback goes back on the card.
3. **Vhendala:** manual product review of REVIEW-1.md and, later, the page, deck, video and README as a judge would (no code review, no repo invite); then stage → 2. The Mon 00:00 fresh run of the README on a clean clone is an independent agent that wrote none of the code, launched by central. The contract is read by a Stellar mentor or the plugin reviewer by 14:00.
4. **Leo:** Sun 09:00 re-run the wasm check (KICKOFF §8), then LEO-BRIEF.md.

## 6. If X, then Y
- Paulo's letter (owner, 2026-10-25: "você sabe que nossa força vem da carta do paulo, certo?"): unsigned draft, due Sun noon, fallback Sun 18:00; base case is unsigned. Marketing specialist + reviewer (2026-10-25): it is context for User Value, Market and possibly Ecosystem (1–2 of 100 per point), not the strength; the 7-tx demo is. Public material names ZIS only after Paulo's written OK; never the video's "Backed by" clip, G20 line or trade figures. Full rules on the card and in [[which-zis-video-versions-paulo-saw-1bb9]].
- Video and team photo belong to Vhendala (owner, 2026-10-25): account and test upload now, narration, final upload; card `board/Vhendala video and team photo.md`.
- No legal work during the hackathon (pedro, 2026-10-25): "regra daqui pra frente no hackathon: não é momento de envolver jurídico." No legal specialist, no legal research (UCC, Brazilian law, KYC, IP terms), no legal questions to pedro. The track's `licences` item is done by the engineer card as a plain list of dependency licences (the repo is Apache-2.0), with no legal analysis. Legal library notes already written stay as they are and are not used.
- If something needs the owner, it becomes a line on the card with `status: waiting-owner`. Do not ask.
- If the rules forbid code written before the event, list exactly what reused code comes from the public radox repo.
- If the portal rules contradict RULES.md or SUBMISSION.md, the portal wins: fix the files the same hour.
- If check.py is below 7/7 when Pedro gives the submit OK (Mon 08:00), track.sh refuses unless the OK words start with 'waive: <reason>' (track.sh:289-298); central runs track.sh verify first and puts the count in the question; Leo must push proofs/lifecycle.json to main.
- If the portal shows the editing window closing earlier than Mon 10:00: ask an organizer at ONE16 the same hour and email meridian@growwithguava.com how a late edit is submitted; write the answer in PORTAL-SEEN.md.
- If an organizer refuses a Scale repo without the closed backend: cut the API connection and deliver the registry as infrastructure; do not publish the backend.
- Vhendala's manual product review does not block Leo's start at 09:00; if she cannot be reached Pedro closes the pass himself.

## 7. What I did not verify
- Whether the organizers accept a Scale repo that holds only the new work, with the platform backend closed. Ask an organizer at check-in.
- Portal rules, submission form and its editing window (login).
- Any evidence that a financier or buyer has the custody-visibility pain (IDEA.md: assumption; mentor test planned).
- SCF Build eligibility criteria themselves.
- PITCH.md slide 3 (problem) still has a {{source needed}} marker for how handovers are documented today.
- Open-slot markers in PITCH use {{fill}}; double square brackets are parsed as a library citation by the checker.
