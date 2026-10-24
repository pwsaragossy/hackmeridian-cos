---
tags:
  - board
status: waiting-owner
project: hackmeridian-rail
owner: session-hackmeridian-rail
member: pedro
due: 2026-10-26
since: 2026-10-24
updated: 2026-10-24
---

# HackMeridian rail

State in [STATE.md](../projects/hackmeridian-rail/STATE.md).

## For the owner to decide (central asks, all at once)
- Stop criterion: if by Sun 25 18:00 Lisbon no two-custodian handover has run on testnet, cut the API connection and deliver contract + harness + recorded demo (recommended).
- Target (proposal, to be confirmed in stage 1): the full lifecycle open → 4 dual-signed handovers (warehouse, port, carrier, customs) → deliver, 6 signed testnet transactions in proofs/lifecycle.json (the burn by the existing transfer_agent.redeem is a 7th, shown but prior work), each verifiable by hash on the public RPC.

## Decided
- 2026-10-25: roles — Pedro's sessions own the project, pitch, Radox API connection and submission; Leo's agents build custody_registry from LEO-BRIEF.md; Vhendala is QA/reviewer and watches the panel (owner).
- 2026-10-24: code in a new repo `pwsaragossy/rio-miami-rail`, private until submission; the radox-internal backend stays closed (owner).
- 2026-10-24: Leo (leo-schlanger) gets write on the code repo and the team board (owner).
