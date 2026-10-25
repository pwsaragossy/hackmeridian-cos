---
tags:
  - board
status: waiting-owner
project: hackmeridian-rail
owner: session-hackmeridian-rail
member: leo
due: 2026-10-25
since: 2026-10-25
updated: 2026-10-25
asked: 
---

# Leo: contract and testnet proofs

State in [STATE.md](../projects/hackmeridian-rail/STATE.md); full spec in [LEO-BRIEF.md](../projects/hackmeridian-rail/LEO-BRIEF.md); timeline in [KICKOFF.md](../projects/hackmeridian-rail/KICKOFF.md) §5. Owner's words (2026-10-25): "coloque as pendencias do leo no panel também, nao vou lembrar de tudo!"

## Before Sun 09:00
- Done 08:43 UTC: both GitHub invites accepted.
- 11:01 UTC check (session-hackmeridian-rail): no sign yet of the workspace setup or the Step 0 spike: no commit by Leo in hackmeridian-cos or rio-miami-rail, GitHub shows 0 clones of either repo today (traffic data can lag), no card line from him.
- Install the chief-of-staff plugin and join the workspace as member leo (KICKOFF §6 step 2); set git user.email to the GitHub noreply address.
- Confirm on app.hackmeridian.com: listed in team Radox, profile complete, Lisbon RSVP answered.

## Sunday
- 11:05 UTC (session-hackmeridian-rail): everything Leo's agents do today, with times moved for the late start, is in `projects/hackmeridian-rail/LEO-SETUP.md` (setup, then LEO-BRIEF.md). Leo's agent answers here with dated lines and evidence; Pedro's session confirms each one.
- 09:00: wasm check first (`stellar contract info interface --wasm-hash 3870748b… --network testnet`), then a 5-minute hello-contract spike (sdk 29.0.1, CLI 28.1.0); a failure goes on the card before building ([[executability-audit-2026-10-25-02-04f7]]).
- 10:00–14:00: custody_registry contract and unit tests; testnet accounts for the actors. By 14:00: `register_token` arguments and `hand_over_sac` vs `set_admin` for redeem confirmed in a testnet spike; a Stellar mentor or the plugin reviewer reads the contract.
- 14:00–18:00: deploy, full lifecycle on testnet, 7 hashes in `proofs/lifecycle.json` pushed to main. 18:00 stop line: no dual-signed handover on testnet, then say so on the card at once.
- After 18:00: failure branches recorded and `scripts/verify-head.mjs` exits 0.

## For the owner to decide (central asks, all at once)
- Leo, now (before 09:00): run the setup. In Claude Code: /plugin marketplace add pwsaragossy/chief-of-staff, then /plugin install chief-of-staff@chief-of-staff, then setup.sh join ~/hackmeridian https://github.com/pwsaragossy/hackmeridian-cos.git --member leo; set git user.email to his GitHub noreply address. Not done at 08:45 (owner). Without it his session has no card, library or checks.
- Leo, Sun 09:00: wasm check and hello-contract spike before any contract code.
- Leo, Sun 14:00: register_token and redeem path confirmed on testnet; contract read by a mentor or the reviewer.
- Leo, Sun 18:00: 7 lifecycle hashes in proofs/lifecycle.json on main (check.py 7/7), or the stop-line note on the card.

## Decided
- 2026-10-25 08:43 UTC: both GitHub invites accepted (gh api, central).
- 2026-10-25: Leo's agents build custody_registry from LEO-BRIEF.md (owner).
