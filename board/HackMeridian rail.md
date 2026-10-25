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
asked: 2026-10-25 01:25 +0100
---

# HackMeridian rail

State in [STATE.md](../projects/hackmeridian-rail/STATE.md).

## For the owner to decide (central asks, all at once)
- Sun 09:00, in central: record two OKs the owner already gave in words (the hook asks one click each): `track.sh ok … check` for `python3 check.py`, and `track.sh ok … scope` with the quote below.

## Decided
- 2026-10-25: scope freeze — must-haves: (1) custody_registry + tests on testnet, (2) lifecycle harness with the 7 txs + verify-head + failure branches, (3) a public read-only shipment page reading the contract on testnet; conditional 4th: the Radox API connection, cut at the Sun 18:00 stop line if behind. Owner's words: "Sim, inclui a página pública do embarque como terceira entrega obrigatória; a ligação com a API fica como quarta condicional."
- 2026-10-25: stop criterion — if by Sun 25 18:00 Lisbon no two-custodian handover has run on testnet, cut the API connection and deliver contract + harness + recorded demo (owner).
- 2026-10-25: target — open → 4 dual-signed handovers → deliver → burn (redeem), 7 signed testnet transactions in proofs/lifecycle.json, so the judges see the whole cycle (owner). The check command is written in stage 1 and recorded with track.sh ok.
- 2026-10-25: roles — Pedro's sessions own the project, pitch, Radox API connection and submission; Leo's agents build custody_registry from LEO-BRIEF.md; Vhendala is QA/reviewer and watches the panel (owner).
- 2026-10-24: code in a new repo `pwsaragossy/rio-miami-rail`, private until submission; the radox-internal backend stays closed (owner).
- 2026-10-24: Leo (leo-schlanger) gets write on the code repo and the team board (owner).
