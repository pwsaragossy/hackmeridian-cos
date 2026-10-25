---
tags:
  - board
status: waiting-owner
project: hackmeridian-rail
owner: session-hackmeridian-rail
member: pedro
due: 2026-10-26
since: 2026-10-24
updated: 2026-10-25
asked: 2026-10-25 01:05 +0000
---

# HackMeridian rail

State in [STATE.md](../projects/hackmeridian-rail/STATE.md).

## For the owner to decide (central asks, all at once)
- **Check OK re-record (one click):** `check.py` changed only in its docstring (the `LEO-BRIEF.md` mention removed; it now names only `proofs/lifecycle.json`, what it measures). Logic unchanged. Central re-records the check OK with track.sh.
- **check.py strength (reopens the check OK if yes):** today 7 copies of any successful testnet hash pass. Add "the 7 hashes are distinct" and "each tx calls our contract"? Recommendation: yes, distinct hashes at least (5 lines, same check). (reviewer finding 7)
- **Portal copy at check-in (Pedro, ~10 min, Sun 09:00):** log in, copy the rules page, the submission form fields and the "project editing window" dates into `projects/hackmeridian-rail/PORTAL-SEEN.md`. No agent can see them (login). (finding 1)
- **README "Production path" section** (mainnet plan, audit status, what is testnet-only, SCF Build eligibility): README text only, no new feature; Scale judges "production readiness" and "SCF eligibility". OK to include? Recommendation: yes. (finding 2)
- **Redeem fallback:** the burn's `transfer_agent` wasm is on testnet today (checked 01:02 UTC); if it is gone at Sun 09:00, the 7th tx needs a fallback (redeploy from the private source = prior work). Decide only if it happens.

## Next (2026-10-25, session-hackmeridian-rail)
- Stage 1 redo done: researcher + product subagents re-checked RULES, SUBMISSION, CRITERIA, IDEA, KICKOFF; reviewer verdict "approve with changes", all fixes applied: `projects/hackmeridian-rail/REVIEW-1.md`. review-1 closed with that evidence. Target and scope unchanged.
- Main changes: rubric is scored 1–5 (not 1–10); video/deck specs, AI attribution and the prior-work disqualifier are only in Pedro's paste (planned to anyway); Scale needs no thematic track; timeline now has the event programme, a 14:00 checkpoint, mentors from 11:00, the form dry-run; self-score 72/100 ceiling, 64 if the API connection is cut; User value evidence is an assumption (mentor test Sun 11:00).
- Vhendala: human final pass on REVIEW-1.md and the five files; then stage → 2.
- Raven research processed into 5 library notes (+3 from the specialists). The inbox file stays until central retires it (same text as `RESEARCH-raven.md`).

## Decided
- 2026-10-25: target + check OK recorded with track.sh (frozen with check.py) — owner's words: "acho que pode colocar o burn aí no último, para fechar o ciclo".
- 2026-10-25: scope OK recorded with track.sh — owner's words: "Sim, inclui a página pública do embarque como terceira entrega obrigatória; a ligação com a API fica como quarta condicional."
- 2026-10-25: scope freeze — must-haves: (1) custody_registry + tests on testnet, (2) lifecycle harness with the 7 txs + verify-head + failure branches, (3) a public read-only shipment page reading the contract on testnet; conditional 4th: the Radox API connection, cut at the Sun 18:00 stop line if behind. Owner's words: "Sim, inclui a página pública do embarque como terceira entrega obrigatória; a ligação com a API fica como quarta condicional."
- 2026-10-25: stop criterion — if by Sun 25 18:00 Lisbon no two-custodian handover has run on testnet, cut the API connection and deliver contract + harness + recorded demo (owner).
- 2026-10-25: target — open → 4 dual-signed handovers → deliver → burn (redeem), 7 signed testnet transactions in proofs/lifecycle.json, so the judges see the whole cycle (owner). The check command is written in stage 1 and recorded with track.sh ok.
- 2026-10-25: roles — Pedro's sessions own the project, pitch, Radox API connection and submission; Leo's agents build custody_registry from LEO-BRIEF.md; Vhendala is QA/reviewer and watches the panel (owner).
- 2026-10-24: code in a new repo `pwsaragossy/rio-miami-rail`, private until submission; the radox-internal backend stays closed (owner).
- 2026-10-24: Leo (leo-schlanger) gets write on the code repo and the team board (owner).
