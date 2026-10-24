# Brief for Leo's agents — `custody_registry` contract

Paste this whole file as the first prompt of Leo's project session (opened in
`~/hackmeridian/projects/hackmeridian-rail`), or point the session to it. Written by Pedro's
session on 2026-10-25; Pedro's session owns the project, the pitch and the Radox API connection.
Questions for Pedro go on the project card (`board/HackMeridian rail.md`), never to Pedro directly.

Role card: engineer. Reviewer: Vhendala's session (QA) plus the plugin reviewer.

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
   instance `CAF4JIUZ…SFC7`. In production the Radox backend co-signs `redeem` only after the registry
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
   carrier, customs, event source, operator).

## Design (decided; change only with a reason written on the card)

State per shipment, persistent storage, TTL extended on read and write:

```
Shipment {
  key: BytesN<32>,          // sha256 of container/AWB number + origin; must be unique
  token: Address,           // the SAC title token (prior work)
  current_custodian: Address,
  route: Vec<Address>,      // custodians in order, fixed at open
  seq: u32,                 // handovers done
  head: BytesN<32>,         // hash chain, see below
  status: Open | Delivered | Frozen,
}
```

Functions:

- `__constructor(admin, operator)`.
- `open(key, token, route, docs_root)` — `operator.require_auth()`; **refuse a repeated key**; first
  custodian = `route[0]`; `head = sha256(docs_root)`; event `opened`.
- `handover(key, from, to, evidence_hash, assurance)` — `from.require_auth()` **and** `to.require_auth()`;
  require `status == Open`, `from == current_custodian`, `to == route[seq + 1]`;
  `seq += 1`; `head = sha256(head || from || to || evidence_hash || seq)`; event `handover` with
  `assurance` (3 = both signed in person; 2 = one by delegation; 1 = external attestation only).
  Asset ownership does not change.
- `attest(key, source, kind, event_hash)` — only a `source` the admin registered (`add_source` /
  `remove_source`); updates `head` and emits `attested`; blocks nothing.
- `deliver(key, final_custodian, holder)` — `final_custodian` must be the last of the route and the
  current custodian; `final_custodian.require_auth()` and `holder.require_auth()`; `status = Delivered`;
  event `delivered`. (The burn is *not* here.)
- `freeze(key)` / `unfreeze(key)` — admin; exits for lost / seized cargo, court order, sanction.
- `pause` / `resume` (admin) and `emergency_pause` (optional pauser), checked by every write.
- Reads: `get(key)`, `head(key)`, `version()`.

Errors: one `#[contracterror]` enum; every refusal has its own code (wrong custodian, out of route,
not open, duplicate key, unknown source, paused, frozen).

Why `head`: RPC `getEvents` keeps only ~7 days, so the full history lives off-chain; the on-chain
`head` lets anyone recompute and verify that history from the events.

Every exit has a terminal or recoverable state: a handover that is never signed leaves the shipment
`Open` with the same custodian (nothing to clean); a lost shipment is `Frozen` by the admin; a
cancelled delivery request stays `Open`.

## Deliverables, in order (commit each one when it passes)

1. Contract + unit tests (`cargo test`), including every refusal path and the `head` recompute.
2. Build `wasm32v1-none --release`; deploy to testnet; write contract ID + wasm hash in `DEPLOYMENTS.md`.
3. Testnet harness `scripts/lifecycle.mjs` (js-stellar-sdk; each custodian signs its own auth entry
   with `authorizeEntry`). **Setup** (hashes kept apart under `setup` in the proof file): friendbot-fund
   the test accounts (issuer, agent admin, operator, seller, holder, warehouse, port, carrier, customs,
   recipient); issuer flags `auth_required` + `auth_revocable` + `auth_clawback_enabled` **before any
   trustline** (a trustline created before clawback is on makes `redeem` fail with `SAC #10` — this cost
   Radox a ceremony once); trustlines of seller and holder; deploy the asset's SAC; issuer `set_admin`
   → the harness's own `transfer_agent` instance; `register_token`; `mint` to the seller; `deliver` to
   the holder. **Lifecycle** (the 7 that count): `open` → 4 `handover` (route warehouse → port → carrier
   → customs → recipient) → `deliver` → `transfer_agent.redeem(token, holder, amount, ref_id)` with
   operator + holder auth, burning the title. Write every hash to `proofs/lifecycle.json`. Also the failure branches: wrong signer, out-of-route, after freeze,
   while paused — each with the failing tx or simulation result recorded.
4. `scripts/verify-head.mjs`: reads the events of a shipment and recomputes `head`; exit 0 when it
   matches the on-chain `head`.

Pedro's session uses `proofs/lifecycle.json` and the contract ID for the README, the Radox API
connection and the demo, so keep those two file names.

## Checks (done when all pass)

- `cargo test` green.
- `proofs/lifecycle.json` holds the 7 lifecycle hashes (open, 4 handovers, deliver, redeem), each
  `SUCCESS` on the public testnet RPC, and the holder's token balance is 0 after `redeem`.
- `node scripts/verify-head.mjs <key>` exits 0.
- Failure branches recorded with their error codes.

## Timeline (Lisbon)

Sun 09:00–10:00 design review with Pedro's session (card) · 10:00–14:00 contract + tests ·
14:00–18:00 deploy + full lifecycle on testnet (**18:00 is the stop line**: if no two-signature
handover ran on testnet by then, tell the card at once) · after 18:00 failure branches and
`verify-head`.

Close each session with `/chief-of-staff:handoff`.
