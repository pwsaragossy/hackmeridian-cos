---
tags:
  - board
status: in-progress
project: hackmeridian-rail
owner: session-hackmeridian-rail
member: pedro
due: 2026-10-26
since: 2026-10-24
updated: 2026-10-25
asked: 
---

# HackMeridian rail

State in [STATE.md](../projects/hackmeridian-rail/STATE.md).

## For the owner to decide (central asks, all at once)

## Next (2026-10-25, session-hackmeridian-rail)
- Redeem fallback: the burn's `transfer_agent` wasm was on testnet at 01:02 UTC; if it is gone at Sun 09:00, put the fallback question back here.
- Stage 1 redo done: researcher + product subagents re-checked RULES, SUBMISSION, CRITERIA, IDEA, KICKOFF; reviewer verdict "approve with changes", all fixes applied: `projects/hackmeridian-rail/REVIEW-1.md`. review-1 closed with that evidence. Target and scope unchanged.
- Main changes: rubric scale in conflict (/build says 1–5, the portal paste says 1–10, same weights; Pedro reads the live portal at Sun 09:00); video/deck specs, AI attribution and the prior-work disqualifier are only in Pedro's paste (planned to anyway); thematic track Stellar Unlocked is Pedro's choice (2026-10-24), optional for Scale; timeline now has the event programme, a 14:00 checkpoint, mentors from 11:00, the form dry-run; self-score 72/100 ceiling, 66 if the API connection is cut; User value evidence is an assumption (mentor test Sun 11:00).
- Vhendala: human product pass on REVIEW-1.md and the five files (reading as a judge, not code); then stage → 2.
- Raven research processed into library notes; the inbox copy is retired (same text as `RESEARCH-raven.md`).
- 2026-10-25 central: the five old transcripts were read in full and reconciled (5 verifiers, legal + product specialists, independent reviewer: "approve with changes"). The project-file edits went to the rail session as one list; central fixed the card, the library notes and central/CLAUDE.md.
- Contract read before the 14:00 checkpoint by someone who did not write it (a Stellar mentor or the plugin reviewer); Vhendala QA runs the tests.
- Official deck template saved as `projects/hackmeridian-rail/DECK-TEMPLATE.pptx` ([[hackmeridian-2026-official-pitch-deck-template-d5c7]]): Solution, PMF (problem), Technical workflow, Team; PITCH.md claims template order but puts the problem first: fix one or the other.

## Decided
- 2026-10-25: rubric scale settled — the portal rules page (Pedro's paste, PORTAL-PASTE.md) says each criterion is scored 1–10; it governs over the 1–5 on the public /build page. PORTAL-SEEN.md at Sun 09:00 now needs only the submission form fields. Owner: "you got this" with the portal text.
- 2026-10-25: portal editing window = Sun 25 09:00 to Mon 26 10:00 Lisbon; 10:00 is the hard close, so there is no margin after it (KICKOFF line "10:00–12:00 is the event's own margin" and SUBMISSION "our own cutoff" must say so). PORTAL-SEEN.md now needs only the form fields and the rubric scale. Owner's words: "9am do dia 25 até 10am do dia 26, já falamos disso".
- 2026-10-25: project rule added to projects/hackmeridian-rail/CLAUDE.md: never commit this work to `pwsaragossy/radox` (one-way mirror); `custody_registry` lives only in rio-miami-rail. Owner's words (to session-hackmeridian-rail): "Sim, adiciona a regra 16 no CLAUDE.md do projeto."
- 2026-10-25: No legal work during the hackathon (pedro, 2026-10-25): "regra daqui pra frente no hackathon: não é momento de envolver jurídico." No legal specialist, no legal research (UCC, Brazilian law, KYC, IP terms), no legal questions to pedro. The track's `licences` item is done by the engineer card as a plain list of dependency licences (the repo is Apache-2.0), with no legal analysis. Legal library notes already written stay as they are and are not used.
- 2026-10-25: weekend pre-authorization: sessions may push to `rio-miami-rail` and `hackmeridian-cos` and deploy the public shipment page on testnet without asking, until submission. Making the repo public (Mon 06:00) and sending the submission still wait for Pedro's OK. Owner's words: "Sim, autorizar (Recomendado)".
- 2026-10-25: Vhendala does a manual product review (page, deck, video, README read as a judge), not code. Owner's words: "ela vai fazer revisão manual de produto." No repo invite for her. The Mon 00:00 fresh-run of the README on a clean clone is done by an independent agent that wrote none of the code (central decision).
- 2026-10-25: owner standing demand for stages 2–4: every review-N names the specialists and the reviewer it used. Words: "as skills estão sendo aplicadas também?" and "Refaz também a etapa 1 com especialistas e revisor antes de seguir." Stage 1 redone (REVIEW-1.md).
- 2026-10-25: AI usage is disclosed with generic wording ("AI coding agents", which files, who read each), no tool or vendor name, under Pedro's standing rule; the portal only asks where AI generated code or assets.
- 2026-10-25: check strengthened — `check.py` now fails unless the 7 hashes are distinct (central added it, tested with a 7-copy file: exit 1, "the 7 hashes are not distinct"); check OK re-recorded with track.sh (freeze f7838003). Owner's words: "Sim, travar (Recomendado)". The "each tx calls our contract" check waits for the contract ID after deploy.
- 2026-10-25: README gets a "Production path" section (mainnet plan, audit status, what is testnet-only, SCF Build eligibility); text only, no new feature. Owner's words: "Sim, incluir (Recomendado)".
- 2026-10-25: portal copy — central asked Pedro to log in at Sun 09:00 and paste the rules page, the submission form fields and the editing-window dates into `projects/hackmeridian-rail/PORTAL-SEEN.md`.
- 2026-10-25: target + check OK recorded with track.sh (frozen with check.py) — owner's words: "acho que pode colocar o burn aí no último, para fechar o ciclo".
- 2026-10-25: scope OK recorded with track.sh — owner's words: "Sim, inclui a página pública do embarque como terceira entrega obrigatória; a ligação com a API fica como quarta condicional."
- 2026-10-25: scope freeze — must-haves: (1) custody_registry + tests on testnet, (2) lifecycle harness with the 7 txs + verify-head + failure branches, (3) a public read-only shipment page reading the contract on testnet; conditional 4th: the Radox API connection, cut at the Sun 18:00 stop line if behind. Owner's words: "Sim, inclui a página pública do embarque como terceira entrega obrigatória; a ligação com a API fica como quarta condicional."
- 2026-10-25: stop criterion — if by Sun 25 18:00 Lisbon no two-custodian handover has run on testnet, cut the API connection and deliver contract + harness + recorded demo (owner).
- 2026-10-25: target — open → 4 dual-signed handovers → deliver → burn (redeem), 7 signed testnet transactions in proofs/lifecycle.json, so the judges see the whole cycle (owner). The check command is written in stage 1 and recorded with track.sh ok.
- 2026-10-25: roles — Pedro's sessions own the project, pitch, Radox API connection and submission; Leo's agents build custody_registry from LEO-BRIEF.md; Vhendala is QA/reviewer and watches the panel (owner).
- 2026-10-24: code in a new repo `pwsaragossy/rio-miami-rail`, private until submission; the radox-internal backend stays closed (owner).
- 2026-10-24: Leo (leo-schlanger) gets write on the code repo and the team board (owner).
