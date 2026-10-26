> **Reviewer corrections (REVIEW-STUDIES.md, approve with changes), applied by leo-agent:** the Audit Bank needs SCF funding AND an eligible category (financial protocols, high-dependency data services, high-traction dApps; official FAQ). That condition is on the critical path: scope the audit to the financial path (registry + transfer_agent + the on-chain gate), confirm the category with SCF before #46 closes (2026-11-08), and raise that risk's probability from 3 to 4. The README now says this (rio-miami-rail 78a1060), and also that the instance TTL bump extends the code (soroban-sdk 29.0.1 storage.rs:616–632, checked by leo-agent).

# Study: what is still missing before Radox Custody Rail can go to Stellar mainnet

Role: engineer (with the security card for the risk part). Written 2026-10-25, about 23:55 UTC, by an engineer specialist subagent working read-only. Nothing was edited, committed, deployed or signed. The only reads against the network were read-only RPC calls (`getVersionInfo`, `getHealth`, `getFeeStats`, `getNetwork`, `stellar network settings`) to `https://mainnet.sorobanrpc.com`.

**Answer (engineer):** the contract logic has been shown to work on a local mainnet fork (same wasm, protocol 29). It is still **not mainnet-ready**. Five classes of work must come first: an on-chain redeem gate, admin and operator rotation with a decided upgrade path, multisig and HSM-held keys plus the issuer lock, an audit that covers both custody_registry and the closed transfer_agent (which is not deployed on mainnet), and a history/indexer plan to replace testnet Horizon. Estimate: 3–5 weeks of engineering to reach audit-ready, then 11–20 weeks through the Audit Bank pipeline, then a capped pilot. Confidence medium. The engineering range is my own inference. The audit range comes from the official Audit Bank page.

**Answer (security):** the top risk is a single compromised or lost key. In the demo, one key is issuer, transfer_agent admin and registry admin (`scripts/lifecycle.mjs:61`). That key can freeze or pause everything and has no replacement path, and the token burn is not tied to custody on chain. **The first action** is to add admin/operator rotation and put the admin behind a multisig before anything else is deployed.

Evidence tags: **[FACT]** means read in code, a config value, command output or an official page (URL, date read). **[INFERENCE]** means reasoned and not observed, with a note on how to verify it. All "read" dates are 2026-10-25 UTC unless stated otherwise.

---

## 0. Inputs read

| Input | What it gave |
|---|---|
| `rio-miami-rail` main `f76e649`: `contracts/custody_registry/src/lib.rs` (506 lines), `test.rs`, `prop_test.rs`, `scripts/lifecycle.mjs`, `DEPLOYMENTS.md`, `README.md` (Architecture, Closed interfaces, Production path, Threat model) | The current contract and its documented limits |
| `origin/landing-v3` `40d3c26` / `b42c521` (read with `git show`): `scripts/mainnet-rehearsal.mjs`, `proofs/mainnet-rehearsal.json` | Fee and TTL numbers from a local mainnet fork. **Not merged into main** (main has no `mainnet-rehearsal.mjs`). |
| Workspace: `THREAT-MODEL.md`, `REVIEW-THREAT-MODEL.md`, `REVIEW-contract.md`, `REVIEW-CUSTODY-SPEC.md`, `JUDGE-QA.md`, `STATE.md` | Prior review findings and owner rulings |
| Library notes (cited as [[id]]) | Testnet reset, RPC retention, Horizon retention, versions, auth signing, transfer_agent interface, mainnet-fork howto |
| Live mainnet RPC `https://mainnet.sorobanrpc.com` (23:50–23:51 UTC) | Protocol, retention, fee stats, every network setting |
| Stellar Raven MCP: `skills.stellar-dev.smart-contracts` (SKILL.md, security.md, testing.md, development.md at commit `e9ab7dbb`), `skills.openzeppelin-stellar.upgrade-stellar-contracts` (commit `6f215af6`), stellarDocs pages (observedAt 23:51–23:53 UTC) | Platform rules, checklists, docs wording |
| Web (WebFetch/WebSearch, 23:51–23:53 UTC): stellar.org Audit Bank page, communityfund.stellar.org/awards, developers.stellar.org RPC providers, crates.io API, CoinGecko and Coinbase spot price | Audit program terms, SCF terms, provider list, crate versions, XLM/USD |

---

## 1. Requirements as numbers (most are unknown and need the owner)

| Requirement | Value | Status |
|---|---|---|
| Shipments per month in a pilot | unknown | Owner question Q1. The cost table assumes 100/month and 10x = 1,000/month as **[INFERENCE] assumptions** |
| Handovers per shipment | 4 in the demo route (5 stops) [FACT `proofs/mainnet-rehearsal.json`] | Real routes are unknown |
| Shipment lifetime on chain (in transit) | unknown. Ocean Rio–Miami transit is weeks [INFERENCE] | Q2 |
| How long records must stay verifiable | unknown (years for trade records? [INFERENCE]) | Q3. This decides the indexer choice (D2) |
| Latency target for a handover | none stated. A ledger closes every 5,000 ms target [FACT mainnet `scp_timing.ledger_target_close_time_milliseconds` 5000] | Q4 |
| Availability of read API/page | none stated | Q4 |
| Budget | zero at the hackathon [FACT STATE.md §2] | Q5 |
| Compliance scope | Legal review is a **prerequisite**. No legal analysis here, per the owner's ruling (STATE.md §6) | see G |

Load arithmetic, done back-of-envelope: 1,000 shipments/month × 7 registry transactions (open, 4 handovers, attest, deliver) = 7,000 tx/month, about 0.0027 tx/s on average. The mainnet per-ledger limit is 2,000 Soroban txs per ledger [FACT `contract_execution_lanes.ledger_max_tx_count` 2000]. Throughput is therefore not a constraint at any plausible pilot volume. The constraints are keys, audit and history.

---

## 2. System as it is, trust boundaries, assets

```text
 [Custodian i]  (own key, own machine; G-account or smart account)
      │ signs Soroban auth entry (ADDRESS_V2, bound to network+nonce+expiry+invocation)
      ▼ ── TB1: file/API hand-off of signed entries (remote-auth.mjs today) ──
 [Rail operator]  hot key: pays fees, signs tx envelope, alone authorises `open`
      │ ── TB2: Stellar RPC provider (third party on mainnet; SDF hosts none) ──
      ▼
 [custody_registry]  admin: freeze/unfreeze/pause/resume/pauser/sources; no rotation, no upgrade
      ╳ no on-chain link ╳
 [transfer_agent] (closed, prior work; SAC admin)  ── [SAC token] ── [issuer account, master key not locked on testnet]
      ▲ redeem called by the harness only after it reads `Delivered` off chain (lifecycle.mjs:200-205)
 ── TB3: off-chain readers: Radox API (closed), page (Vercel), verify-head (Horizon history) ──
 ── TB4: AI coding agents and workspace members who can read `.env` and keys on dev machines ──
```

Assets ranked by damage if lost or tampered with:
1. The SAC admin / transfer_agent admin and the issuer key. Tampering means minting, clawback or burning tokens that represent cargo value.
2. The registry admin key. With it an attacker can freeze or pause every shipment, and today it can never be replaced.
3. The operator key. It opens shipments, chooses routes and pays fees. Compromise means key squatting, false routes and a drained fee balance.
4. Custodian keys. A stolen one can sign false handovers. A lost one blocks the shipment at that stop.
5. Integrity of the history (head chain) and its long-term availability.
6. Commercial confidentiality: routes, custodian addresses and container identity are public on chain.

Attacker goals: redeem or burn a token without real delivery; fake a handover; freeze or ransom the rail; learn who ships what.

Data classification: everything on chain is **public** (state and events). Document preimages behind `docs_root` and `evidence_hash` are **confidential** and live off chain (store not designed: F3). Keys are **restricted**.

---

## 3. Gap list

Severity: **blocker** (no mainnet without it), **should** (before a pilot with real custodians), **nice**. Effort: **S** ≤ 2 days, **M** 3–10 days, **L** > 10 days, for one engineer who knows the code [INFERENCE].

### (A) Contract changes, custody_registry

| # | Gap | Sev | Effort | Depends on | Source |
|---|---|---|---|---|---|
| A1 | **On-chain redeem gate.** `transfer_agent.redeem` is not tied to `Delivered`; only the JS harness checks it. Option (a), recommended: the agent (or a thin gate contract that is the only party allowed to call redeem) reads `custody_registry.get(key)` and requires `status == Delivered && holder == redeem holder`. This needs a token→shipment-key binding (A5/E5) and keeps the registry token-agnostic. Option (b): `deliver` calls the agent, which couples the registry to one token contract. | blocker | M | E2 (change to the closed agent, which has an `upgrade` entrypoint), B1 scope | [FACT] README "The registry does not gate redeem on chain"; `scripts/lifecycle.mjs:200-205`; REVIEW-THREAT-MODEL finding 1; JUDGE-QA Q12 |
| A2 | **Admin and operator rotation.** There is no `set_admin` / `set_operator`, so a lost or compromised key means redeploying, and open shipments cannot migrate. Add a two-step `propose_admin` / `accept_admin`, a `set_operator` (admin-only), and events for both. | blocker | S | ADR-1 | [FACT] lib.rs has no such fn (`grep`); JUDGE-QA Q14; README threat row "A powerful admin" |
| A3 | **Upgrade path decision (ADR-1 below).** There is no `update_current_contract_wasm` today. Either add `upgrade(new_wasm_hash)` gated by the multisig admin (optionally with a timelock and an event), plus storage-compatibility tests, or decide that the registry stays immutable and write the migration plan (a new instance per version, old instances stay readable). | blocker (the decision); the code is S–M | S–M | C1 | [FACT] docs "Upgrading contracts" (`env.deployer().update_current_contract...`, the address does not change, the wasm must already be uploaded), stellarDocs observed 23:51 UTC; OZ upgrade skill: "a contract becomes immutable simply by not provisioning any upgrade function", "an upgrade to a contract without one permanently loses upgradeability", "storage consistency is not verified" |
| A4 | **Custodian key recovery inside a shipment.** A lost custodian key stops the shipment, and the only exit is `freeze`. Add `replace_custodian(key, stop_index, new)` authorised by admin + new address (+ the previous custodian, or an off-chain dispute record hashed into `head`). It must be folded into the head so the verifier still matches. | should | M | ADR-1, head-format version bump | [FACT] README row "Lost custodian key: Partly … no key rotation inside a shipment" |
| A5 | **Holder/token checks.** `open` never checks that `token` is a token, and `deliver` never checks that `holder` holds it. Options: an admin-maintained token allowlist; a `token → key` uniqueness map (which also blocks two shipments on one token); a read-only `TokenClient::balance(holder) > 0` at `deliver`. | should (blocker if A1 is not done) | S–M | A1, E5 | [FACT] README row "Delivering to someone who does not hold the token"; JUDGE-QA Q13; security.md "Token-consumer review: any contract that takes a token address must assume it may be native XLM's SAC, a wrapped classic asset's SAC, or a custom contract" |
| A6 | **Events for every privileged change.** `pause`, `resume`, `emergency_pause`, `set_pauser`, `add_source` and `remove_source` emit nothing; only freeze/unfreeze emit `StatusChanged`. Monitoring (D4) cannot see an admin action without them. | should | S | – | [FACT] lib.rs; security.md checklist "Events emitted for auditable state changes (and error codes never renumbered)" |
| A7 | **Bound the route length.** `route: Vec<Address>` is unbounded and stored in one persistent entry. Add a cap (for example ≤ 32 stops). | should | S | – | [FACT] lib.rs `open`; REVIEW-contract finding 9; security.md §10 "Cap iteration counts explicitly"; mainnet `contract_data_entry_size_bytes` 65536 |
| A8 | **Retune TTL for mainnet.** On mainnet a new persistent entry already starts at 2,073,600 ledgers = 120 days, and the maximum is 3,110,400 = 180 days. The contract's `extend_ttl(120_960, 518_400)` fires only when < 7 days remain and then extends to only 30 days. A shipment idle near the end of its life will archive about a month later. Use thresholds sized for mainnet (for example a 30-day threshold extended to 120–180 days) or `extend_ttl_with_limits`. Also bump the instance in `emergency_pause`, `resume`, `set_pauser` and `remove_source`. | should | S | Q2/Q3 | [FACT] mainnet `state_archival.min_persistent_ttl` 2073600, `max_entry_ttl` 3110400 (stellar network settings, 23:50 UTC); rehearsal: code live-until 67,210,530 − upload ledger 65,136,931 = 2,073,599; lib.rs:23-24; development.md "Protocol 26 added … `extend_ttl_with_limits`" |
| A9 | **Correct a README claim.** The threat-model row says "the contract code's TTL is the deployer's to extend". In soroban-sdk 29.0.1, `instance().extend_ttl` extends **both the instance and the contract code**, so the code stays live while writes happen. Only an idle contract needs a keeper (D3). | should (accuracy for auditors) | S | – | [FACT] `soroban-sdk-29.0.1/src/storage.rs:619-621` "the threshold check and TTL extensions are done for both the contract code and contract instance" |
| A10 | **Key privacy.** `key = sha256(container \| origin)`. ISO container numbers are low-entropy, so anyone can brute-force which containers are on the rail. Use a salted key (HMAC with an operator secret, or a random key mapped off chain). | should | S | F3 | [FACT] README Radox API table "`sha256(container \| origin)`". **[INFERENCE]** on brute force: the space is about 26³·10⁶ ≈ 1.8·10¹⁰ per origin, which a GPU covers at about 10⁹–10¹⁰ SHA-256/s in seconds to minutes. Verify by timing hashcat on one key |
| A11 | **Policy on attest after Delivered/Frozen.** It is allowed today and moves `head` after the redeem precondition was read. Decide and test the choice; if A1 reads `head`, refuse it after `Delivered`. | should | S | A1 | [FACT] REVIEW-contract finding 6 (kept on purpose); README row "Event sources" |
| A12 | **No timeout or dispute path** when a custodian refuses to sign. Add a deadline field plus an admin resolution recorded in `head`, or accept this explicitly as a residual risk. | nice | M | A4 | [FACT] README row "A custodian refuses to sign" |
| A13 | **Build provenance.** Pin the SDK to the mainnet protocol at deploy time. Mainnet is on protocol 29 today; stellar-core 30.0.0 shipped 2026-10-16 but protocol 30 has not been voted ([[soroban-versions-on-2026-10-25-9619]]). Re-test after any vote. Publish a reproducible build (toolchain, `Cargo.lock`, the wasm sha256 that matches the deployed hash). | should | S | – | [FACT] mainnet `getVersionInfo` → `protocolVersion: 29`, core 29.0.0, RPC 29.0.0 (23:51 UTC); skill versions.md "pin the SDK major matching the network you deploy to" |

### (B) Security assurance

| # | Gap | Sev | Effort | Depends on | Source |
|---|---|---|---|---|---|
| B1 | **Third-party audit** of custody_registry **and** transfer_agent **and** the A1 gate, as one scope, after a code freeze. Audit Bank: SDF pays the first audit; 5% co-pay is paid upfront and refunded if critical/high/medium findings are fixed within 20 business days. Eligibility: SCF-funded projects that are "close to launching on Stellar mainnet" with "stable code, comprehensive documentation". Readiness review uses STRIDE. Timeline: match ~2 weeks after readiness, schedule 3–6 weeks, audit 2–8 weeks. | blocker | L (11–20 weeks elapsed) | A1–A8 frozen; an SCF award (B1 is gated by SCF funding); E2 source access for the auditor | [FACT] stellar.org/grants-and-funding/soroban-audit-bank (read 23:52 UTC). Note a source conflict: the Raven skill lists partner firms (OtterSec, Veridise, Runtime Verification, CoinFabrik, Certora, Zellic, Code4rena); the official page lists Certora, Halborn, Oak Security, OtterSec, Runtime Verification, Spearbit + Cantina, Veridise, Zellic. **Use the official page.** Scout `listAudits` has no Radox report on record (source scope only; not a claim of "unaudited"). |
| B2 | **Static analysis**: `cargo scout-audit` (CoinFabrik, latest 0.3.17 of 2026-09-25) and OpenZeppelin Soroban security detectors, with every finding triaged in the repo. | should (the Audit Bank expects it) | S | – | [FACT] security.md "Before requesting an audit: run the static analyzers, complete the checklists above, document your threat model"; crates.io API 23:52 UTC |
| B3 | **Beyond the 26 tests**: `cargo-fuzz` targets for every entrypoint (`SorobanArbitrary` comes with `testutils`); `cargo mutants` (no surviving mutants on auth and route checks); property tests run in CI with random `PROP_SEED` and `PROP_CASES` ≥ 10,000 (today 64 seeded cases each); negative tests for every new entrypoint (A2–A5). | should | M | B4 | [FACT] `prop_test.rs:34-45` (defaults 64, seed `0x5EED_2026_1025`); 26 tests passed (REVIEW-THREAT-MODEL "Checked"); testing.md Fuzz / Mutation sections |
| B4 | **CI does not exist** (no `.github/`). Add test + release build (`wasm32v1-none`) + scout + `cargo audit` + `npm audit` on every push, with the wasm hash as a build artifact. | should | S | – | [FACT] `ls -a` of repo root; testing.md CI example |
| B5 | **Formal checks of the invariants** (`seq` monotonic, `deliver` only at the last stop, `head` = fold of history, auth on both custodians) with Certora Sunbeam or Komet. | nice | M–L | B3 | [FACT] security.md Tooling "Formal verification" |
| B6 | **Threat model to audit standard.** The README table is good but needs: (i) the A9 correction; (ii) new rows for key brute force (A10), operator key-squatting (a compromised operator pre-opens predictable keys → `DuplicateKey` DoS), single-key concentration (issuer = agent admin = registry admin = `exporter`, `lifecycle.mjs:61`), the A1 gate's cross-contract trust, and AI agents and dev tooling as actors with key access (TB4); (iii) a STRIDE table per component, which is the format the Audit Bank readiness review uses. | blocker (Audit Bank readiness) | S–M | A1–A5 design | [FACT] REVIEW-THREAT-MODEL (missing rows, mostly applied); Audit Bank page "security standards based on the STRIDE threat modeling framework" |
| B7 | **Dependency advisories**: `cargo audit` / `npm audit` not run in this study. soroban-sdk 29.0.1 (2026-10-21 on crates.io) is newer than the lines fixed by GHSA-x2hw-px52-wp4m ([[soroban-versions-on-2026-10-25-9619]]), but this was not rechecked. | should | S | B4 | Not checked (see §10) |
| B8 | **Complete the fork rehearsal.** It ran registry-only, because "transfer_agent is not on mainnet" (`mainnet-rehearsal.mjs` header), with throwaway single-key accounts. Extend it with: transfer_agent + SAC + issuer flags + lock, a multisig admin, the A1 gate, an archive/restore scenario, and an upgrade (if ADR-1 chooses one). Merge it to main. Fidelity limits of soroban-sim: "Not modelled: classic operations (funding is an override), ExtendFootprintTtl and RestoreFootprint operations, several transactions per ledger, per-ledger limits and surge pricing". | should | M | A1, C1, E1 | [FACT] `proofs/mainnet-rehearsal.json` report; [[local-mainnet-fork-rpc-with-soroban-f272]] |
| B9 | **Bug bounty** after launch (Immunefi lists Stellar programs for core/SDK and OZ-Stellar; a project bounty would be our own). | nice | S | Phase 3 | [FACT] security.md "Audits and bounties" |

### (C) Keys and operations

| # | Gap | Sev | Effort | Depends on | Source |
|---|---|---|---|---|---|
| C1 | **Separate roles, multisig admin.** Today one `exporter` key is issuer, transfer_agent admin and registry admin. On mainnet: registry admin = a multisig G-account (Soroban's built-in Stellar-account auth "supports the Stellar multisig with medium threshold") or an OZ smart-account/multisig contract (`__check_auth`). Separate keys for issuer, agent admin, registry admin, operator and pauser. No code change is needed for the multisig itself, because `require_auth` accepts any Address. | blocker | S–M | A2 | [FACT] `lifecycle.mjs:61` comment "issuer, transfer-agent admin, registry admin"; docs `/learn/fundamentals/contract-development/authorization#stellar-account` (observed 23:53 UTC); JUDGE-QA Q14 |
| C2 | **Operator key in an HSM/KMS or signing service** (it signs every envelope and alone authorises `open`), with a fee budget account, alerting and channel accounts or a relayer (the OpenZeppelin Relayer is listed in the Stellar docs) for parallel submission. | blocker for pilot | M | D1 | [FACT] docs `/tools/openzeppelin-contracts` "Relayer: Infrastructure for relaying transactions on Stellar" |
| C3 | **Issuer setup and lock, irreversible, in order:** set flags `AUTH_REQUIRED \| AUTH_REVOCABLE \| AUTH_CLAWBACK_ENABLED` **before any trustline** (the harness notes a trustline made before clawback is on breaks redeem, SAC #10) → deploy SAC → `set_admin(agent)` → test `hand_over_sac` exit → set issuer master weight 0. After the lock, flags, signers and home domain can never change. Rehearse the whole sequence on testnet and on the fork before mainnet. | blocker | S (plus a rehearsal) | E1–E3 | [FACT] `lifecycle.mjs:136-138`; docs control-asset-access: "Clawback enabled … requires that revocable is also set"; "locking your account means you'll never be able to do anything with it ever again"; SAC docs "The issuer of the asset will be the initial administrator … can later be moved with set_admin"; README Production path step 2; `proofs/lifecycle.json` `issuer_after_set_admin.master_weight` = 1 on testnet |
| C4 | **Runbooks and incident response** (see §6 for the top 3). Detection → contain (pause/freeze) → rotate (A2) → restore → notify → record. | blocker for pilot | S–M | A2, A6, D4 | NIST SP 800-61 Rev. 3 (card source); security.md checklist "Emergency controls (pause) and incident runbook defined" |
| C5 | **Emergency pauser** assigned to a different person and device from the admin, with a quarterly drill: pause on a fork, then resume by admin. | should | S | C1 | [FACT] lib.rs `emergency_pause` (only the admin resumes) |
| C6 | **Mainnet secrets kept out of agent reach.** No mainnet secret in any `.env`, workspace or machine where AI coding agents run (TB4). Separate signer machines; a key ceremony with written backups; a recovery test. | blocker | S | C1 | [FACT] workspace CLAUDE.md "chaves em .env"; README AI usage (agents wrote the code) |

### (D) Infrastructure

| # | Gap | Sev | Effort | Depends on | Source |
|---|---|---|---|---|---|
| D1 | **Mainnet RPC.** SDF hosts no public mainnet RPC (only testnet/futurenet). Choose a paid primary plus at least one fallback from the providers page, and check CORS for the public page. | blocker | S | – | [FACT] developers.stellar.org/docs/data/apis/rpc/providers (WebFetch 23:52 UTC): 16 mainnet providers in the table, public endpoints incl. `mainnet.sorobanrpc.com`, Gateway, Nodies, OnFinality, Lightsail (+ archive RPC), Ankr (full archive); SDF row "Mainnet: No". `mainnet.sorobanrpc.com` returned `access-control-allow-headers: *` (curl 23:51 UTC) |
| D2 | **History and indexer.** `verify-head` and the page replay transaction arguments from Horizon. On mainnet: RPC keeps 7.0 days (measured), SDF Horizon keeps one year and is "nearing end-of-life in favor of RPC", events are not restorable. Use Galexie/Hubble or an archive RPC, port `verify-head` to that source, and dump the per-shipment history (tx args + Horizon/RPC JSON) to our own store at each write. | blocker (for the "verify it yourself" claim beyond 7 days / 1 year) | M | Q3 | [FACT] mainnet `getHealth` `ledgerRetentionWindow` 120960, oldest→latest close time 1792367468→1792972263 = 604,795 s = 7.0 days (23:51 UTC); docs `/data` "SDF-hosted Horizon keeps one year of history and is nearing end-of-life"; [[horizon-public-history-one-year-and-983a]], [[stellar-rpc-getevents-keeps-about-7-187e]] |
| D3 | **TTL keeper and restore handling.** A job that reads `live_until` for the instance, the code and every open/recent shipment and extends them (anyone can send `ExtendFootprintTTLOp`); clients handle `restorePreamble` on simulation (auto-restore exists since protocol 23). | should | S–M | A8 | [FACT] development.md "Anyone can extend any entry's TTL via ExtendFootprintTTLOp"; docs state-archival "archived entries included in a transaction's restore list … are automatically restored" and simulateTransaction "restorePreamble" |
| D4 | **Monitoring/alerting** on registry events (after A6) and on transfer_agent/SAC events: `pause`, `freeze`, admin change, any `clawback`/`mint` not matched to a shipment, operator fee balance, RPC health, TTL horizon. The OpenZeppelin Monitor supports Stellar. | should | M | A6, D1 | [FACT] docs `/tools/openzeppelin-contracts` "Monitor"; security.md Tooling "OpenZeppelin Monitor … Stellar support" |
| D5 | **Token-side fees not measured on mainnet.** The fork rehearsal skipped mint/deliver/redeem. Re-run them on the fork (B8). Testnet `redeem` charged 20,877 stroops = 0.0020877 XLM (testnet config, order of magnitude only). | should | S | B8 | [FACT] `proofs/tx/864fd164….json` `fee_charged` 20877 |
| D6 | **Network-switch guards.** The page, the Radox API (env contract id plus its existing network guard) and the scripts must refuse a mismatched passphrase or contract id. `mainnet-rehearsal.mjs` already refuses anything that is not localhost + PUBLIC; production tools need the inverse guard. | should | S | – | [FACT] `mainnet-rehearsal.mjs` lines 16-17; [[serve-a-read-only-soroban-contract-1aab]] trap (4) "the network guard refuses to start" |

### (E) Asset/token side (transfer_agent is closed prior work)

| # | What must be true on mainnet | Sev | Effort | Depends on | Source |
|---|---|---|---|---|---|
| E1 | transfer_agent **is deployed on mainnet** from a known wasm hash. It is not today: "transfer_agent is not on mainnet". The public Radox mainnet contracts are `token_sale`, `yield_distributor` and `maturity_settlement`. | blocker | S (deploy) | B1, C1 | [FACT] `mainnet-rehearsal.mjs` header; README "Prior work" |
| E2 | Its **closed source is in the audit scope** (auditor access under NDA), and every privileged entrypoint has a named mainnet holder: `upgrade`, `propose_admin`/`accept_admin`, `set_operator`, `admin_transfer`, `admin_clawback`, `admin_set_authorized`, `set_emergency_pauser`, `hand_over_sac`. Signers and effects of the uncalled functions are "not confirmed". | blocker | M | B1 | [FACT] README "Interface functions this repo does not call"; [[transfer-agent-testnet-interface-2026-10-3378]] |
| E3 | The **SAC admin chain** issuer → agent is done with the issuer lock (C3), and the exit path (`hand_over_sac`) is tested before the lock. | blocker | S | C3 | [FACT] README Production path step 2; [[transfer-agent-testnet-interface-2026-10-3378]] (exit path is an inference from the signature) |
| E4 | Holder onboarding: with `AUTH_REQUIRED` each holder needs a trustline and `set_authorized`. Since protocol 26 a contract can create a trustline via the SAC `trust` function. Decide who pays reserves. | should | S | F2 | [FACT] `lifecycle.mjs:137-138`; SAC docs "As of Yardstick, Protocol 26 (CAP-73), the SAC's trust function allows a contract to create an asset's trustline" |
| E5 | **One token ↔ one shipment** is enforced somewhere (registry map, or agent `TokenReg` carrying the shipment key), so a second token for the same cargo cannot share the custody record. Title/paper bill of lading stays out of scope. | should | S–M | A1, A5 | [FACT] README row "A second token, or a paper bill of lading … No" |
| E6 | `deliver` on the agent is clawback + mint (not a SAC transfer). The token's history therefore shows burn/mint pairs, so explorers and accounting must be told. | nice | S | – | [FACT] README Closed interfaces table, `deliver` row |

### (F) Off-chain integration

| # | Gap | Sev | Effort | Depends on | Source |
|---|---|---|---|---|---|
| F1 | **Radox API on mainnet**: mainnet RPC config, env contract id, network guard, migrations applied, and the ~30 already-failing unit tests on the `hackmeridian` branch fixed, so a mainnet change can be judged. | should | M | D1 | [FACT] [[serve-a-read-only-soroban-contract-1aab]] (traps 3–5) |
| F2 | **Custodian onboarding and signing UX.** Each custodian needs an on-ledger, funded account (a signer "must exist on-ledger"). Replace the `remote-auth.mjs` CLI with a wallet flow: Freighter sign-auth-entries, or passkey smart accounts. Show contract, function and arguments before signing; enforce the registry address via a second channel. | blocker for a pilot with real custodians | M–L | C1, D1 | [FACT] [[sign-soroban-auth-entries-on-another-e4dd]], [[two-signers-in-one-soroban-call-1b93]]; docs guestbook "smart wallet … Smart Account Kit and the OpenZeppelin Smart Account contracts" |
| F3 | **Evidence store** for the preimages of `docs_root` / `evidence_hash`: access control, retention, integrity (hash re-check on read), backup and restore test. | should | M | Q3 | [FACT] README row "What a handover attests … the contract does not check what the hash points to" |
| F4 | **Contract tests at the API boundary** (the `GET /api/custody/shipments/:key` shape) run against the mainnet fork in CI. | should | S | B4, B8 | [FACT] README Radox API table |
| F5 | **Operating agreement with custodians** (SLA, dispute path for A12, who pays fees). This is a product/commercial item, not code. | should | – | G | [INFERENCE] |

### (G) Compliance

| # | Gap | Sev | Effort | Source |
|---|---|---|---|---|
| G1 | **Legal review is a prerequisite** before any mainnet pilot. Per the owner's ruling, no legal analysis is done during the hackathon. | blocker | – (owner) | [FACT] STATE.md §6 "No legal work during the hackathon (pedro, 2026-10-25)" |

---

## 4. ADRs (decisions the team must record before audit)

**ADR-1, upgradeability.** Context: the registry has no upgrade function (immutable) and no key rotation. Options: (1) stay immutable, add rotation (A2), and ship new versions as new instances; (2) add an `upgrade` gated by the multisig admin with a timelock and an event; (3) the OZ `Upgradeable`/`UpgradeableMigratable` macros. Option 3 is blocked today: OZ crates 0.8.0 (released 2026-10-20, MIT) require `soroban-sdk ^28`, while the contract is on 29.0.1 [FACT crates.io API 23:52 UTC; [[soroban-versions-on-2026-10-25-9619]]]. **Recommendation:** option 1 plus A2 for the pilot ("do less"; immutability is itself a trust feature for a custody record), with a written revisit trigger: the first audit finding that needs a fix on live shipments, or OZ supporting sdk 29. Consequence: a bug fix means a new instance, and open shipments finish on the old one. Exit cost: low.

**ADR-2, redeem gate placement.** Options: (a) the agent or a gate reads the registry (recommended); (b) the registry calls the agent; (c) keep the gate off chain and accept the residual risk. Option (c) is the "do not build" choice. It is rejected because the burn of a token that stands for cargo would then depend on a script, not on the chain (JUDGE-QA Q12).

---

## 5. Risk register (likelihood × impact, 1–5 each)

| Risk | L | I | Score | Fix owner | Control | Verification |
|---|---|---|---|---|---|---|
| Single key (`exporter`) compromised: mint/clawback/freeze all | 3 | 5 | 15 | Leo + Pedro | C1, C6, A2 | Fork rehearsal with multisig: a single signature is refused |
| Burn/redeem without real delivery (off-chain gate bypassed) | 3 | 5 | 15 | Leo + agent owner | A1, A5, E5 | Negative test: redeem before `Delivered` fails on chain |
| Registry admin key lost: no rotation, no upgrade | 3 | 4 | 12 | Leo | A2, C1 | Test: rotate admin, old key refused |
| Colluding custodians sign a false handover | 2 | 5 | 10 | Pedro (product) | Out-of-band evidence (F3), attest sources; accepted residual | Pilot review of evidence hashes |
| History unverifiable after 7 days / 1 year | 4 | 3 | 12 | Leo | D2 | `verify-head` MATCH from the indexer alone on a 30-day-old shipment |
| Container identity leak via key brute force | 4 | 2 | 8 | Leo | A10 | Time a brute force before and after |
| Operator key compromise: key squatting, fee drain | 2 | 3 | 6 | Leo | C2, D4 | Alert fires on an unknown `open` |
| Audit not obtainable (no SCF award → no Audit Bank) | 3 | 4 | 12 | Pedro | SCF #46 (deadline 2026-11-08) or a self-paid audit | Award letter or a signed audit SOW |

---

## 6. Pre-mortem and runbooks

Pre-mortem: six months after a mainnet pilot it has failed. Most plausible stories:
1. A dev machine that held `.env` with the single admin/issuer key was used by an AI agent session; the key leaked and tokens were clawed back and re-minted. Early signal: any mainnet secret found in a workspace. Stopper: C1, C6.
2. A redeem was submitted through the API for an undelivered shipment because the gate lived in a script. Stopper: A1.
3. A judge or a bank opened the "verify it yourself" page 13 months later and Horizon no longer had the history. Stopper: D2.

Runbooks for the top 3 (plain steps; they need A2/A6 to exist first):
- **Admin/issuer key suspected compromised:** (1) the pauser calls `emergency_pause` on the registry and `emergency_pause` on the agent; (2) the multisig co-signers rotate the admin (A2) and remove the compromised signer from the multisig account; (3) list every `mint`/`clawback`/`freeze` since the suspected time from the indexer (D2); (4) the new admin resumes; (5) notify custodians and holders; record it in the incident log.
- **Custodian key lost mid-shipment:** (1) the admin calls `freeze(key)`; (2) verify the custodian's identity off chain; (3) `replace_custodian` (A4), or close the shipment and open a new key; (4) `unfreeze`; (5) record the evidence hash.
- **RPC provider outage / archived entry:** (1) switch to the fallback RPC (D1); (2) if simulation returns `restorePreamble`, submit the restore or let auto-restore apply; (3) the keeper (D3) extends the instance and live shipments; (4) post-mortem on the TTL alert threshold.

---

## 7. Ordered roadmap

| Phase | Goal | Work (gap ids) | Exit criterion | Elapsed |
|---|---|---|---|---|
| **0 Hackathon** (now) | Proof on testnet + mainnet fork | Done: 26 tests, testnet lifecycle, fork rehearsal (landing-v3). Still to do: merge the rehearsal into main and correct the README with A9. | Submission | done (to 2026-10-26) |
| **1 Audit-ready** | Frozen code that an auditor would accept | ADR-1, ADR-2; A1–A8, A10, A11, A13; B2–B4, B6, B7, B8; C1 design; E2 source access; D2 design; SCF #46 application | Static analysis clean; fuzz + mutants green; STRIDE doc; fork rehearsal including token + multisig; tag + wasm hash frozen | 3–5 weeks of engineering [INFERENCE: about 13 S/M items at 1–5 days each] |
| **2 Audited** | Independent findings fixed | B1 (registry + agent + gate); remediation within 20 business days; re-run B3/B8 on the fixed tag | Final audit report with no open critical/high/medium | 11–20 weeks [FACT ranges from the Audit Bank page: 2 + 3–6 + 2–8 weeks + ≤20 business days remediation] |
| **3 Mainnet pilot** | Real custodians, capped value | C1–C6 live; D1, D3, D4 live; E1, E3, C3 lock; F1, F2, F3; G1 signed off; deploy the audited hash; publish the hash and source; bounty B9 | N shipments with a cap per shipment (owner sets N and the cap); every runbook drilled once | 2–4 weeks [INFERENCE] |

Critical path: SCF award → Audit Bank readiness → audit. The engineering work in phase 1 runs in parallel with the SCF review. Readiness "typically follows the SCF Build testnet tranche" [FACT Audit Bank page].

---

## 8. Cost table (rough)

XLM/USD = **0.167267** (CoinGecko, last_updated 1792972334 = 2026-10-25 23:52 UTC; Coinbase spot 0.167491 at the same minute). Fees are from the **local mainnet fork** (protocol 29, base fee 100 stroops; the tool states it ports stellar-core's resource fee, rent and refund checks) [FACT `proofs/mainnet-rehearsal.json`, landing-v3]. Net charge = balance decrease (exporter 100 → 86.5251033 XLM = 13.4748967 charged across its 7 txs, matching the report).

| Item | XLM | USD | Source / arithmetic |
|---|---|---|---|
| Upload wasm (10,672 bytes, includes 120-day rent) | 13.4010850 | 2.24 | rehearsal step 13 |
| Deploy instance | 0.0485279 | 0.0081 | step 14 |
| `add_source` | 0.0231488 | 0.0039 | step 15 |
| **One-time total** | **13.4727617** | **2.25** | sum |
| `open` (new persistent entry, 120-day minimum rent) | 0.1167129 | 0.0195 | step 16 |
| `handover` ×4 | 4 × 0.0015427 = 0.0061708 | 0.0010 | steps 17, 18, 20, 21 |
| `attest` ×1 | 0.0009998 | 0.0002 | step 19 |
| `deliver` | 0.0094762 | 0.0016 | step 22 |
| **Registry fees per shipment** (5 stops, 1 attest) | **0.1333597** | **0.0223** | sum; each extra handover +0.0015427 XLM ($0.00026) |
| Token side per shipment (mint, deliver, redeem) | not measured on mainnet | – | D5. Testnet redeem 0.0020877 XLM is testnet config only |
| Pilot: 100 shipments/month (assumed) | 13.34 | 2.23 /month | 100 × 0.1333597 |
| 10x: 1,000 shipments/month | 133.36 | 22.31 /month | 1,000 × 0.1333597 |
| Inclusion-fee surge sensitivity | +100 stroops × 7 tx = +0.00007 / shipment | ~0 | mainnet `getFeeStats` Soroban inclusion fee mode 200, p99 200 stroops (23:51 UTC) vs base 100 |
| XLM price sensitivity | – | ×10 price → $0.22 / shipment | arithmetic |
| TTL keeper (extensions beyond 120 days) | not measured | – | **[INFERENCE]** bounded above by about one `open`-sized rent per 120 days per kept entry, about 0.35 XLM/entry/year. Verify with `stellar contract extend --send=no` on the fork or mainnet simulation. Code+instance stay live while there are writes (A9). |
| Audit via Audit Bank | 5% of audit cost upfront, refundable | – | [FACT] Audit Bank page; requires SCF funding |
| Audit self-paid | no public price list | **[INFERENCE, low]** $15k–$60k for registry + agent + gate | $3M+ across 40+ audits ≈ $75k average (SDF blog figure; my own division, and mostly larger DeFi scopes). Get two quotes |
| SCF Build award (funding side) | up to $150K in XLM, tranches MVP / Testnet / Mainnet (percentages not stated on the page) | – | [FACT] communityfund.stellar.org/awards (23:52 UTC); SCF #46 deadline 2026-11-08 |
| RPC / indexer hosting | public endpoints are listed (no SLA stated); paid tiers not priced here | open | D1/D2. Q5 |
| Custodian account reserves | base reserve 0.5 XLM on the fork report; minimum balance per account is a multiple of it | small | [FACT] fork report "base reserve 0.5000000 XLM"; the exact multiple was not read here |

Operations cost (people) dominates fees by orders of magnitude [INFERENCE]: on-call for C4, keeper/monitoring upkeep, and custodian support.

---

## 9. What would change the conclusion

- If the owner chooses the **"do not build" path** for the redeem gate (ADR-2 c) and accepts that residual risk in writing, A1 drops from blocker to should. The audit and key work still stand.
- **No SCF award** → the Audit Bank is not available; the self-paid audit becomes the critical path cost.
- **A protocol 30 vote** before deploy → rebuild with the matching SDK major and re-run every test and rehearsal (A13).
- **Volume of 10⁵+ shipments/month** → fees are still under $2.3k/month, but per-ledger limits, channel accounts and indexer cost become design inputs.
- **Records must live for many years** → D2 becomes the largest infrastructure item (own Galexie lake or a paid archive).

## 10. Residual risk to accept (owner, in writing)

1. Colluding custodians can sign a handover that never happened; the head proves who signed, not that the cargo moved. Owner: Pedro.
2. Everything on chain is public (routes, custodian addresses, timing), even after A10. Owner: Pedro.
3. If ADR-1 keeps the contract immutable, a bug found on live shipments can only be fixed by a new instance. Owner: Pedro + Leo.
4. transfer_agent stays closed source; outsiders trust the audit, not the code. Owner: Pedro.

## 11. Not checked

- `cargo test`, `cargo audit`, `npm audit` and `cargo scout-audit` were not run in this study. The 26-test result comes from REVIEW-THREAT-MODEL.
- Mainnet fees for the transfer_agent/SAC flows, `ExtendFootprintTTL` and `RestoreFootprint` (soroban-sim does not model the last two).
- SCF Handbook tranche percentages and mainnet-tranche deliverables (not on the awards page; Handbook not read in this run).
- Paid RPC/indexer prices; the Audit Readiness Checklist document itself (linked from the Audit Bank page, not opened).
- Whether `require_auth` on a G-account multisig works end to end for our two-signer handover (documented as medium threshold, not tested).
- The behaviour of the closed transfer_agent internals (source not available).
- The exact multiple of base reserve for account minimum balance.
- Who operates `mainnet.sorobanrpc.com` beyond its listing on the providers page.

## 12. Open questions for the owner (for the project card)

1. Q1: expected shipments per month in the pilot, and the cap per shipment's value?
2. Q2: how long is a shipment open on chain (days)?
3. Q3: how many years must a record stay verifiable by a third party?
4. Q4: availability/latency target for the read API and page?
5. Q5: budget for audit (if no Audit Bank), RPC/indexer and on-call?
6. Q6: will Radox apply to SCF #46 (deadline 2026-11-08) with this as a milestone? The Audit Bank depends on it.
7. Q7: can the auditor get transfer_agent source, and who holds its `upgrade` and admin rights on mainnet?
8. Q8: ADR-1, immutable + rotation (recommended) or upgradeable?
9. Q9: who are the co-signers of the admin multisig, and who holds the emergency pauser?

## Library

cited: [[stellar-testnet-resets-wipe-contracts-and-dfe4]], [[transfer-agent-testnet-interface-2026-10-3378]], [[local-mainnet-fork-rpc-with-soroban-f272]], [[soroban-versions-on-2026-10-25-9619]], [[stellar-rpc-getevents-keeps-about-7-187e]], [[horizon-public-history-one-year-and-983a]], [[scf-build-participant-rules-entity-in-a7b1]], [[two-signers-in-one-soroban-call-1b93]], [[sign-soroban-auth-entries-on-another-e4dd]], [[serve-a-read-only-soroban-contract-1aab]]

saved: none. This run was limited to writing a single file. Candidate notes for the next session to save with `library.sh new`: (1) mainnet state-archival settings on 2026-10-25 (min_persistent_ttl 2,073,600 = 120 days, max 3,110,400; mainnet RPC retention 7.0 days measured); (2) in soroban-sdk 29.0.1 `instance().extend_ttl` also extends the contract code (storage.rs:619-621), which contradicts the README row; (3) registry fee per shipment on the mainnet fork, 0.1333597 XLM; (4) Audit Bank terms read 2026-10-25 (5% refundable co-pay, 2/3–6/2–8-week pipeline, official partner list). Note (1) updates [[stellar-rpc-getevents-keeps-about-7-187e]] (coexists: mainnet vs testnet numbers).

---

## Versions

- **v1** (draft, 23:56 UTC): a gap list A–G built from the code, the workspace reviews and the live sources.
- **v2** (this file): checked against the stated judge, an SDF engineer / Soroban auditor looking for a missing class of work or an unsourced claim. Changes: (i) added A9 after reading the SDK source, which shows the README's code-TTL row is wrong; (ii) added A10 key brute force, B6 single-key concentration and the AI-agent actor (TB4), which earlier reviews missed; (iii) replaced the skill's Audit Bank partner list with the official page and wrote the conflict down; (iv) split fees into measured (fork) vs not measured (token side, keeper) instead of extrapolating; (v) tagged every non-observed number [INFERENCE] with how to verify it. Classes covered against the Raven security.md contract checklist: authorization ✓ (A2, C1), reinitialization ✓ (uses `__constructor`, no gap), external calls ✓ (A1/A5 gate), arithmetic ✓ (`overflow-checks = true` in Cargo.toml, no signed inputs), typed keys ✓ (`DataKey` enum), TTL ✓ (A8, A9, D3), bounded loops ✓ (A7), events ✓ (A6), upgrade path ✓ (A3/ADR-1), emergency controls + runbook ✓ (C4, C5, §6). Client-side checklist: passphrase guard ✓ (D6), simulate before submit ✓ (existing harness), operation shown to signer ✓ (F2), contract address verified ✓ (F2, second channel), trustline status ✓ (E4).

### Never-skip checklist, engineer card

- [x] Every library claim cites its [[id]]. **Not done:** saving new findings with `library.sh new` (run limited to one file; four candidate notes listed under Library).
- [x] Requirements include numbers or are marked unknown with an open question (§1, Q1–Q5).
- [x] Existing code and platform features checked before proposing new components (multisig via built-in account auth, OZ Monitor/Relayer, SAC `trust`, auto-restore, existing `freeze`/pause).
- [x] Simplest option evaluated: ADR-1 option 1 (immutable + rotation) recommended; ADR-2 "keep the gate off chain" written with its rejection reason.
- [x] Cost at expected and 10x load, fees measured. Operations cost named but not priced (Q5).
- [x] Exit cost/lock-in stated: RPC provider (≥2, swappable), OZ crates (blocked by the sdk version), soroban-sim (local tool only), Audit Bank (tied to SCF).
- [x] Security: trust boundaries TB1–TB4, secret handling (C6), authn/authz (A2, C1), data in transit/at rest (§2, F3); money path threat-modelled (§2, §5).
- [x] Rollback/recovery for each irreversible step: issuer lock (rehearse first, test the exit before the lock, C3/E3), deploy (new instance, ADR-1), funds (pause + rotation runbook §6).
- [x] Failure modes with detection and recovery (§5, §6, D4).
- [x] Dependencies: licence and maintenance listed for soroban-sdk 29.0.1 (2026-10-21), OZ stellar-* 0.8.0 (MIT, 2026-10-20, sdk ^28), cargo-scout-audit 0.3.17 (2026-09-25). **Advisories not rechecked** (B7, §11).
- [x] Estimate given as a range with its main assumption; first deliverable is a thin slice (the phase 1 fork rehearsal with token + multisig runs end to end).

### Never-skip checklist, security card

- [x] Library claims cite [[id]]. **Not done:** new notes saved (see above).
- [x] Assets and attacker goals named before threats (§2).
- [x] System diagram with trust boundaries (§2).
- [x] Secrets: where they live (demo: one `exporter` key, `.env` on dev machines), who can read them (members, AI agents: TB4), rotation (none today → A2) and revocation (multisig signer removal, C1).
- [x] Every claimed control verified by file, setting or test, or labelled. The multisig medium threshold is documented, not tested (§11).
- [x] Personal/financial data: on-chain data public; preimages confidential off chain (F3); container identity leak (A10). Retention is an open question (Q3).
- [x] AI agents and third-party tools treated as actors: TB4, C6, B6; RPC providers as third parties (TB2, D1).
- [x] Detection and recovery assessed: D4 monitoring, §6 runbooks, D3 restore. Backups of the evidence store are not yet tested (F3).
- [x] Each risk has likelihood, impact, fix owner and a verification step (§5).
- [x] Internet-exposed surface enumerated: public registry state/events, page (Vercel), Radox API route (rate-limited 300/60 s per README), RPC endpoints, public repo (after the scrub). All are intended, except the container identity exposure via predictable keys (A10).
- [x] Residual risk listed for the owner to accept in writing (§10).
