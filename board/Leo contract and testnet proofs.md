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
- 11:30 UTC (leo-agent): contract + unit tests on rio-miami-rail main — 02f577a (Apache-2.0 LICENSE + NOTICE, workspace, AI_USAGE.md) and 3ce8880 (custody_registry + 16 tests). `cargo test` 16/16 green, clippy clean, wasm 10341 bytes. `head` test vector pinned in test.rs and computed independently in JS (key af078925…, open 4d279350…, handover 7f75df7c…); verify-head --selftest will print the same hex. Errors (Result, #[contracterror]): 1 WrongCustodian, 2 OutOfRoute, 3 NotOpen, 4 DuplicateKey, 5 UnknownSource, 6 Paused, 7 Frozen, 8 NotFound, 9 BadRoute (len<2 or a repeated adjacent stop), 10 NotFinal, 11 NotFrozen, 12 NoPauser. Additions beyond the brief: `set_pauser(Option)` and `is_paused()` read. Secret grep empty. Plugin reviewer (role card reviewer) is reading the contract now; deploy after its verdict.
- 11:19 UTC (leo-agent): Step 0b PASS (throwaway asset SPK1, own transfer_agent instance CBOM5ZZR65EFXF4E7L7GF5F5AES3DSYBYNZHHXJYPDGZTSDFKGVPZM7U from wasm 3870748b…, SAC CDPDAHCGQVVSU735NQJBCLMVUE72SLVLX7JTD62O42AVX5ZRDRNEIX6J). register_token auth: admin (exporter) only; set_admin before register_token: no (register_token SUCCESS before set_admin, f223037b06696aad0e487976b71a86668d57963b7e952b073d7de2c2b50bff01; a second call = AgentError #2 AlreadyRegistered). sac.set_admin(agent): issuer 9b92180dcd8f22ee576b7c72054286a57e3f048466bbdeaa23b4bed49c6d685a. mint auth: admin — afa05231404c9c93fc8076c0a84d17f55ff90a3fd153a5b43253286e24a22861. transfer_agent.deliver auth: seller — cf35077d3a28d8d6c5e753317845c2f1092d3992d5aef07397545827b7d6b6fa. redeem auth: operator + holder — 7f8a682900cec83fd9d0ec71623c005fb2b05d5f0a76e9a49a7bdd72e0ee38bf; holder balance 10000000 → 0 (burned). Trustline auth: issuer flag (`set-trustline-flags --set-authorize` before set_admin) works; issuer flags set before trustlines, no SAC #10. Issuer not locked after set_admin (thresholds 0/0/0, master weight 1). All 5 `successful: true` on Horizon. Deviation: seller is a separate account, not the exporter/issuer (an issuer holds no trustline to its own asset); settlement = exporter. Script becomes the harness setup.
- 11:16 UTC (leo-agent): arrival — read LEO-SETUP, LEO-BRIEF, STATE, project CLAUDE.md; first action Step 0; written here, not in STATE.md (STATE.md is Pedro's session's). Fact checked on disk: wasm 3870748b… still on testnet with `fn redeem` (`stellar contract info interface`, 11:10 UTC). Note: this Claude session started before the plugin was installed, so its hooks are off here; sync is by hand until Leo opens a fresh session.
- 11:16 UTC (leo-agent): Step 0 PASS — stellar CLI 28.1.0, soroban-sdk 29.0.1 (Cargo.lock), hello deployed CALNJB6DW5BCMHVGMZIDNLQ2GHA4HW5EP3Q2F26NAGVBFSAHOM2NX5JK, invoke tx 70bfc037bd7272d6e1616b80fec29f611197a04055ec5db63620a282bcbcc3c9. Horizon `parameters` = [0 Address (contract), 1 Sym "hello", 2 Str "spike"]: `parameters[1]` is the function name, args follow. Note: `stellar contract invoke` treats a read-only call as simulation only; `--send=yes` is needed to get a hash.
- 11:16 UTC (leo-agent): two-signature spike PASS — `both(a, b)` with two `require_auth`, each signer's entry signed with `authorizeEntry`, a third account as tx source: SUCCESS c6d06f2f9059b6c68074018103e1b64797035adc94e54b598b22568c9ab01c07. Finding for the harness: js-stellar-sdk is 17.3.0 (js-xdr 5) — XDR values are plain objects (`entry.credentials.type`), not accessor methods, and protocol 29 simulation returns `sorobanCredentialsAddressV2` entries; `authorizeEntry` signs them as-is. Build ops with `Operation.invokeContractFunction({ auth })`.
- 11:10 UTC (leo-agent): setup done — workspace ok (member leo, push: true), email 37229572+leo-schlanger@users.noreply.github.com (set per repo, not global), stellar 28.1.0, rustup 1.29.1 + wasm32v1-none, node v24.18.1, rio-miami-rail cloned at 0a980f9. Paths differ from LEO-SETUP: workspace and code live in Leo's Desktop/hackaton-meridian/ (WSL), not ~/hackmeridian and ~/code.

## For the owner to decide (central asks, all at once)
- Leo, now: the plugin reviewer (someone who did not write it) reads the contract; verdict on this card before 14:00, then deploy custody_registry on testnet; contract ID on this card.
- Leo, Sun 14:00 checkpoint: first dual-signed handover on testnet, or one line on this card saying why not.
- Leo, Sun 14:00–18:00: lifecycle harness, 7 distinct hashes in proofs/lifecycle.json on main (check.py 7/7), verify-head exits 0, failure branches recorded.
- Leo, Sun 18:00 stop line: no dual-signed handover on testnet → say so here at once (the API connection is cut).
- Leo, Sun 20:30–22:00: one line here per thing that really broke (Step 0, 0b, two-signature, failure branches): it is the portal's Challenges field.
- Leo, Mon 06:00: AI_USAGE.md per-file list matches the repo, and the Claude model names you used, for the AI tooling field.

## Decided
- 2026-10-25 11:09–11:30 UTC: setup done, Step 0, Step 0b and the two-signature spike passed, contract + 16 tests on main (card lines above).
- 2026-10-25 08:43 UTC: both GitHub invites accepted (gh api, central).
- 2026-10-25: Leo's agents build custody_registry from LEO-BRIEF.md (owner).
