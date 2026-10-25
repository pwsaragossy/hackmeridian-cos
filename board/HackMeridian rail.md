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
---

# HackMeridian rail

State in [STATE.md](../projects/hackmeridian-rail/STATE.md).

## For the owner to decide (central asks, all at once)
- Sun 09:00, in central: approve the frozen check `python3 check.py` for the approved target (track.sh ok … check; the hook asks for one click).
- Scope freeze (stage 2, proposal in projects/hackmeridian-rail/IDEA.md): add a public read-only shipment page (reads the contract on testnet) as the 3rd must-have — covers Product Design & UX (10%) and the public URL; the Radox API connection stays as the conditional 4th, cut at the 18:00 stop line if behind (recommended).

## Decided
- 2026-10-25: stop criterion — if by Sun 25 18:00 Lisbon no two-custodian handover has run on testnet, cut the API connection and deliver contract + harness + recorded demo (owner).
- 2026-10-25: target — open → 4 dual-signed handovers → deliver → burn (redeem), 7 signed testnet transactions in proofs/lifecycle.json, so the judges see the whole cycle (owner). The check command is written in stage 1 and recorded with track.sh ok.
- 2026-10-25: roles — Pedro's sessions own the project, pitch, Radox API connection and submission; Leo's agents build custody_registry from LEO-BRIEF.md; Vhendala is QA/reviewer and watches the panel (owner).
- 2026-10-24: code in a new repo `pwsaragossy/rio-miami-rail`, private until submission; the radox-internal backend stays closed (owner).
- 2026-10-24: Leo (leo-schlanger) gets write on the code repo and the team board (owner).
