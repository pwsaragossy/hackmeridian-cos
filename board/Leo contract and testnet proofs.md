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
- 11:16 UTC (leo-agent): arrival — read LEO-SETUP, LEO-BRIEF, STATE, project CLAUDE.md; first action Step 0; written here, not in STATE.md (STATE.md is Pedro's session's). Fact checked on disk: wasm 3870748b… still on testnet with `fn redeem` (`stellar contract info interface`, 11:10 UTC). Note: this Claude session started before the plugin was installed, so its hooks are off here; sync is by hand until Leo opens a fresh session.
- 11:16 UTC (leo-agent): Step 0 PASS — stellar CLI 28.1.0, soroban-sdk 29.0.1 (Cargo.lock), hello deployed CALNJB6DW5BCMHVGMZIDNLQ2GHA4HW5EP3Q2F26NAGVBFSAHOM2NX5JK, invoke tx 70bfc037bd7272d6e1616b80fec29f611197a04055ec5db63620a282bcbcc3c9. Horizon `parameters` = [0 Address (contract), 1 Sym "hello", 2 Str "spike"]: `parameters[1]` is the function name, args follow. Note: `stellar contract invoke` treats a read-only call as simulation only; `--send=yes` is needed to get a hash.
- 11:16 UTC (leo-agent): two-signature spike PASS — `both(a, b)` with two `require_auth`, each signer's entry signed with `authorizeEntry`, a third account as tx source: SUCCESS c6d06f2f9059b6c68074018103e1b64797035adc94e54b598b22568c9ab01c07. Finding for the harness: js-stellar-sdk is 17.3.0 (js-xdr 5) — XDR values are plain objects (`entry.credentials.type`), not accessor methods, and protocol 29 simulation returns `sorobanCredentialsAddressV2` entries; `authorizeEntry` signs them as-is. Build ops with `Operation.invokeContractFunction({ auth })`.
- 11:10 UTC (leo-agent): setup done — workspace ok (member leo, push: true), email 37229572+leo-schlanger@users.noreply.github.com (set per repo, not global), stellar 28.1.0, rustup 1.29.1 + wasm32v1-none, node v24.18.1, rio-miami-rail cloned at 0a980f9. Paths differ from LEO-SETUP: workspace and code live in Leo's Desktop/hackaton-meridian/ (WSL), not ~/hackmeridian and ~/code.

## For the owner to decide (central asks, all at once)
- Leo, now (before 09:00): run the setup. In Claude Code: /plugin marketplace add pwsaragossy/chief-of-staff, then /plugin install chief-of-staff@chief-of-staff, then setup.sh join ~/hackmeridian https://github.com/pwsaragossy/hackmeridian-cos.git --member leo; set git user.email to his GitHub noreply address. Not done at 08:45 (owner). Without it his session has no card, library or checks.
- Leo, Sun 09:00: wasm check and hello-contract spike before any contract code.
- Leo, Sun 14:00: register_token and redeem path confirmed on testnet; contract read by a mentor or the reviewer.
- Leo, Sun 18:00: 7 lifecycle hashes in proofs/lifecycle.json on main (check.py 7/7), or the stop-line note on the card.

## Decided
- 2026-10-25 08:43 UTC: both GitHub invites accepted (gh api, central).
- 2026-10-25: Leo's agents build custody_registry from LEO-BRIEF.md (owner).
