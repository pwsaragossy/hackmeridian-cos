# Brief for Leo's agents — `custody_registry` contract

Internal: contains Radox-internal references (paths, instance IDs). Never copy into rio-miami-rail.

Paste this whole file as the first prompt of Leo's project session (opened in
`~/hackmeridian/projects/hackmeridian-rail`), or point the session to it. Written by Pedro's
session on 2026-10-25; Pedro's session owns the project, the pitch and the Radox API connection.
Questions for Pedro go on the project card (`board/HackMeridian rail.md`), never to Pedro directly.

Role card: engineer. Reviewer: a Stellar mentor or the plugin reviewer (contract read by 14:00); Vhendala does a manual product review only.

## Mission

Build `custody_registry`, a small Soroban contract with **no money and no token inside**, in
`github.com/pwsaragossy/rio-miami-rail` under `contracts/custody_registry/`. It records who holds a
tokenized physical shipment in transit, handover by handover, each handover signed by **both**
custodians. Ownership of the asset (a SAC token administered by the existing Radox `transfer_agent`)
never moves during transit.

Done = the 4 checks at the bottom pass, with testnet hashes.

## Hard rules

1. **No code before Sun 25 Oct 09:00 Lisbon.** The rules require showing what was built during the
   event; the first commit in the repo must be after that time.
2. **Do not change, copy or reimplement `transfer_agent`.** It is prior work, closed source, money path.
   The burn stays in its `redeem`. Its compiled code is already on testnet (wasm hash
   `3870748b709f7b8531c7ebbbc975712333f61949831350ff7192f7076fc6bff1`, checked 2026-10-25), so the
   harness **deploys its own instance** from that hash with test keys
   (`stellar contract deploy --wasm-hash 3870748b… -- --config '{"admin":"<G>","operator":"<G>"}'`) —
   no Radox key, no Radox source. Read its interface with
   `stellar contract info interface --wasm-hash 3870748b… --network testnet`. Never use the Radox
   instance `CAF4JIUZ…SFC7`. In production the intended policy (not enforced on-chain) is that the Radox backend co-signs `redeem` only after the registry
   says `Delivered` (Pedro's side, private).
3. `soroban-sdk = "29.0.1"` (crates.io, 2026-10-21; testnet RPC reports protocol 29). **Do not add
   OpenZeppelin `stellar-*` 0.8.0**: they require `soroban-sdk ^28` and will not build with 29.
   Events with `#[contractevent]`.
4. Stellar facts are looked up live (Raven gateway tools `search` + `execute`, or the `soroban` skill),
   never from memory. See `RESEARCH-raven.md` in this folder.
5. A unit test is not proof of network behaviour: every function is executed on **testnet**, signed,
   and its hash written down.
6. No secrets in the repo: keys in env vars or `stellar keys`, `.env` gitignored.
7. No partner or client names in code, README or commits — roles only (exporter, warehouse, port,
   carrier, customs, event source, operator); use made-up container, AWB and port identifiers; no real carrier, port or bill-of-lading numbers.
8. **AI attribution is required by the rules** (RULES.md, SUBMISSION.md). Keep `AI_USAGE.md` at the repo
   root: one line per file or folder saying it was generated with AI ("AI coding agent"; no vendor or model name unless Pedro lifts that rule on the card) and what a human
   reviewed. Undisclosed prior work disqualifies; so add nothing written before Sun 09:00.
9. Commit small and often: the commit history is the judges' evidence of work during the event.
10. Before the first commit set git user.email to the GitHub noreply address; no rewrite or force-push after Sun 09:00. Before every push run grep -rE "S[A-Z2-7]{55}" over the tree; keys live only in env or `stellar keys`.
11. LICENSE = full Apache-2.0 text in the first commit; license = "Apache-2.0" in Cargo.toml and package.json; copyright line "Copyright 2026 the rio-miami-rail contributors"; copy nothing from pwsaragossy/radox (all rights reserved) or radox-internal.

## Design (decided; change only with a reason written on the card)

State per shipment, persistent storage, TTL extended on read and write:

```
Shipment {
  key: BytesN<32>,          // sha256 of container/AWB number + origin; must be unique
  token: Address,           // the SAC asset token (prior work)
  current_custodian: Address,
  route: Vec<Address>,      // custodians in order, fixed at open
  seq: u32,                 // handovers done
  head: BytesN<32>,         // hash chain, see below
  status: Open | Delivered | Frozen,
}
```

Functions:

- `__constructor(admin, operator)`.
- `open(key, token, route, docs_root: BytesN<32>)` — `operator.require_auth()`; **refuse a repeated key**; first
  custodian = `route[0]`; `head` per the layout below; event `opened`.
- `handover(key, from, to, evidence_hash: BytesN<32>, assurance: u32)` — `from.require_auth()` **and** `to.require_auth()`;
  require `status == Open`, `from == current_custodian`, `to == route[seq + 1]`;
  `seq += 1`; `head` per the layout below; event `handover` with
  `assurance` (3 = both signed in person; 2 = one by delegation; 1 = external attestation only).
  Asset ownership does not change.
- `attest(key, source, kind: u32, event_hash: BytesN<32>)` — `source.require_auth()`; only a `source` the admin registered (`add_source` /
  `remove_source`); updates `head` per the layout below (does not change `seq`) and emits `attested`; blocks nothing.

### `key` recipe (off-chain, fixed)

`key = sha256(utf8(UPPER(container_or_awb) + "|" + UPPER(origin_unlocode)))`, no spaces, e.g. (made up)
`sha256("TEST1234567|BRRIO")`. The harness computes it and passes the 32 bytes; the contract never
sees the plain identifier.

### `head` byte layout (contract, verify-head and the page must all use exactly this)

`||` is plain byte concatenation into one `Bytes`, then `env.crypto().sha256(&bytes).to_bytes()`.
- `addr(x)` = `x.to_xdr(&env)` (`use soroban_sdk::xdr::ToXdr`; the XDR bytes of the address as an
  `ScVal`, per developers.stellar.org/docs/build/guides/conversions/address-conversions). In JS:
  `nativeToScVal(x, { type: "address" }).toXDR()`.
- `be32(n)` = the `u32` as 4 bytes big-endian (`n.to_be_bytes()`; JS `DataView.setUint32(0, n, false)`).
- `BytesN<32>` values enter as their raw 32 bytes. The first byte is a tag so the three kinds never collide.

```
open:     head = sha256( 0x01 || key || docs_root )
handover: head = sha256( 0x02 || head || addr(from) || addr(to) || evidence_hash || be32(seq) || be32(assurance) )   // seq = value after += 1
attest:   head = sha256( 0x03 || head || addr(source) || be32(kind) || event_hash || be32(seq) )                    // seq = current, unchanged
```

`deliver`, `freeze`, `unfreeze` do not change `head`. Unit test 1 pins this: a fixed key, docs_root,
two test addresses and one handover, with the expected 32-byte `head` written as a hex constant in
the test; `verify-head.mjs` runs the same vector with `--selftest` and must print the same hex.
- `deliver(key, final_custodian, holder)` — `final_custodian` must be the last of the route and the
  current custodian; `final_custodian.require_auth()` and `holder.require_auth()`; `status = Delivered`;
  event `delivered`. (The burn is *not* here.)
- `freeze(key)` / `unfreeze(key)` — admin; exits for lost / seized cargo, court order, sanction.
- `pause` / `resume` (admin) and `emergency_pause` (optional pauser), checked by every write.
- Reads: `get(key)`, `head(key)`, `version()`.

Errors: one `#[contracterror]` enum; every refusal has its own code (wrong custodian, out of route,
not open, duplicate key, unknown source, paused, frozen).

Why `head`: RPC `getEvents` keeps only ~7 days, so events are not the history source. The history is
the arguments of the shipment's own transactions, read from **Horizon**
(`GET https://horizon-testnet.stellar.org/transactions/<hash>/operations`: the `invoke_host_function`
record carries `function` and `parameters`, each a base64 `ScVal`), for the hashes listed in
`proofs/lifecycle.json` (`open` + the 4 `handover`, plus a top-level `"attest": [{ "hash": "…" }]`
if any attest ran). `verify-head.mjs` and the public page read the **same** list from the **same**
Horizon endpoint, recompute `head` with the layout above, and compare with the on-chain `head(key)`
(simulated read). SDF's public Horizon keeps one year of history; the next testnet reset
(scheduled 2026-12-16, [[stellar-testnet-resets-wipe-contracts-and-dfe4]]) wipes it anyway, and the
saved `proofs/tx/<hash>.json` copies are the fallback (`verify-head.mjs --offline`).

Every exit has a terminal or recoverable state: a handover that is never signed leaves the shipment
`Open` with the same custodian (nothing to clean); a lost shipment is `Frozen` by the admin; a
cancelled delivery request stays `Open`.

## Step 0 — toolchain spike, 5 minutes, before any real code (Sun 09:00)

Nobody has yet deployed an sdk-29 wasm with stellar CLI 28.1.0 (the newest CLI) on protocol 29.
Prove it in a throwaway folder **outside** the repo (so the repo's first commit stays clean):

1. `stellar --version` → 28.1.0; `rustup target add wasm32v1-none`.
2. `stellar contract init /tmp/hello-spike`; in its `contracts/hello-world/Cargo.toml` (and the workspace
   `Cargo.toml`) set `soroban-sdk = "29.0.1"`; `stellar contract build`.
3. `stellar keys generate spike --network testnet --fund`; `stellar contract deploy --wasm <the .wasm>
   --source spike --network testnet` → contract ID.
4. `stellar contract invoke --id <C…> --source spike --network testnet -- hello --to spike` → tx hash.
5. `curl -s https://horizon-testnet.stellar.org/transactions/<hash>/operations` shows `parameters`
   (this is the history source for verify-head and the page).

Pass = all five ran; write CLI version, sdk version and the tx hash as one line on the card. Fail at
any step = one card line with the exact error before building anything else (fallbacks: build with
`cargo build --target wasm32v1-none --release`; deploy with js-stellar-sdk).

## Step 0b — `transfer_agent` spike on testnet, done before 12:00 (7 of 7 depends on it)

The interface read at 2026-10-25 08:50 UTC (`stellar contract info interface --wasm-hash
3870748b709f7b8531c7ebbbc975712333f61949831350ff7192f7076fc6bff1 --network testnet`) gives:

- `__constructor(config: Config { admin, operator })`
- `register_token(token, seller, settlement, payment_asset)`, all `Address`; stored as
  `TokenReg { payment_asset, seller, settlement }`. For the harness: `token` = the shipment SAC,
  `seller` = exporter, `settlement` = exporter, `payment_asset` = the native XLM SAC
  (`stellar contract id asset --asset native --network testnet`).
- `mint(token, to, amount)`, `deliver(token, to, amount)`, `redeem(token, holder, amount, ref_id: u64)`.
- `hand_over_sac(token, new_admin)`: moves the SAC admin **away** from the agent (the exit path). It is
  **not** how the agent gets control. For `redeem` to burn, the issuer calls the SAC's own
  `set_admin(<transfer_agent instance>)` in setup; `hand_over_sac` is not used in the demo.

Not in the interface, so the spike decides it: who must sign each call (admin, operator, seller,
holder) and whether `register_token` needs the agent to already be SAC admin. Method: on a throwaway
asset, run setup → `set_admin` → `register_token` → `mint` 1 → `deliver` 1 → `redeem` 1, each with a
**simulation first** (`--send=no`, or js-stellar-sdk `simulateTransaction`) and record the auth
entries it asks for. Write the result as one card line ("register_token auth: …; redeem auth: …;
set_admin before register_token: yes/no") and keep the script as the harness's setup. If `redeem`
fails, the card line carries the error code (`AgentError` enum, or `SAC #10` = trustline made before
clawback was on) and the redeem fallback goes back to the card for Pedro's session.

## Deliverables, in order (commit each one when it passes)

1. Contract + unit tests (`cargo test`), including every refusal path and the `head` recompute.
2. Build `wasm32v1-none --release`; deploy to testnet; write contract ID + wasm hash in `DEPLOYMENTS.md`.
3. Testnet harness `scripts/lifecycle.mjs` (js-stellar-sdk; each custodian signs its own auth entry
   with `authorizeEntry`). **Setup** (hashes kept apart under `setup` in the proof file): friendbot-fund
   the test accounts (issuer, agent admin, operator, seller, holder, warehouse, port, carrier, customs,
   recipient); issuer flags `auth_required` + `auth_revocable` + `auth_clawback_enabled` **before any
   trustline** (a trustline created before clawback is on makes `redeem` fail with `SAC #10` — this cost
   Radox a ceremony once); trustlines of seller and holder; deploy the asset's SAC; issuer `set_admin`
   → the harness's own `transfer_agent` instance; `register_token`; `mint` to the seller; `transfer_agent.deliver` (sends the minted token to the holder; not the registry's `deliver`). **Lifecycle** (the 7 that count): `open` → 4 `handover` (route warehouse → port → carrier
   → customs → recipient) → `deliver` → `transfer_agent.redeem(token, holder, amount, ref_id)` with
   operator + holder auth, burning the token. Write every hash to `proofs/lifecycle.json`. Also the failure branches: wrong signer, out-of-route, after freeze,
   while paused — each with the failing tx or simulation result recorded.
   Before `redeem`, the harness reads `custody_registry.get(key)` and aborts unless status is Delivered; it records "redeem_precondition": "Delivered" as an extra top-level key in proofs/lifecycle.json (check.py reads only `lifecycle`). It also saves each lifecycle tx's Horizon JSON to proofs/tx/<hash>.json (verify-head unchanged). After `set_admin`, record whether the issuer account was locked. Name the keys so the demo reads owner-operated: issuer and agent admin = 'exporter', operator = 'rail operator'.
4. `scripts/verify-head.mjs <key>`: reads the shipment's transactions from Horizon (list and layout
   in Design above, not events) and recomputes `head`; exit 0 when it matches the on-chain `head`.

Pedro's session uses `proofs/lifecycle.json` and the contract ID for the README, the Radox API
connection, the public shipment page and the demo, so keep those two file names. The proof file
shape is fixed — the target check (`check.py` in this folder) reads it from `main`:

```json
{
  "network": "testnet",
  "custody_registry": "C…", "transfer_agent_instance": "C…", "token": "C…",
  "setup":     [{ "step": "issuer_flags", "hash": "<64 hex>" }, "…"],
  "lifecycle": [{ "step": "open", "hash": "…" }, { "step": "handover", "hash": "…" }, "×4",
                { "step": "deliver", "hash": "…" }, { "step": "redeem", "hash": "…" }],
  "failures":  [{ "case": "wrong_signer", "error": "…", "hash_or_sim": "…" }, "…"]
}
```

`lifecycle` must hold exactly 7 entries in that order: open, handover ×4, deliver, redeem.

## Checks (done when all pass)

- `cargo test` green.
- `proofs/lifecycle.json` holds the 7 lifecycle hashes (open, 4 handovers, deliver, redeem), each
  `SUCCESS` on the public testnet RPC, and the holder's token balance is 0 after `redeem`.
- `node scripts/verify-head.mjs <key>` exits 0.
- Failure branches recorded with their error codes.

## Timeline (Lisbon)

Sun 09:00 first command: `stellar contract info interface --wasm-hash 3870748b709f7b8531c7ebbbc975712333f61949831350ff7192f7076fc6bff1 --network testnet`; if it fails, write a card line before building. By 14:00 a Stellar mentor or the plugin reviewer reads the contract. Sun 09:00–10:00 design review with Pedro's session (card) · 10:00–14:00 contract + tests ·
14:00–18:00 deploy + full lifecycle on testnet (**18:00 is the stop line**: if no two-signature
handover ran on testnet by then, tell the card at once) · after 18:00 failure branches and
`verify-head`.

Close each session with `/chief-of-staff:handoff`.
