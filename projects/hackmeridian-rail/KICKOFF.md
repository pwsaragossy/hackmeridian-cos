# Kickoff — Sun 25 Oct 09:00 Lisbon

Written on 2026-10-24/25, before the event. No code exists yet; the first commit in
`pwsaragossy/rio-miami-rail` happens after 09:00 Sun.

## 1. Where the line between prior work and new work is (read first)

Radox already has, in the private `radox-internal` (checked on origin/main `fb46527d`):

- **Whole physical asset ("phygital", V7)**: `backend/src/routes/phygitalRoutes.js` — purchase, custody fees,
  resale, and a **withdrawal** flow: holder requests → company quotes → holder pays → company marks
  `ship` and `deliver` (each with a document) → holder confirms "Recebi" → token burned.
- **The burn already exists on-chain**: `transfer_agent.redeem(token, holder, amount, ref_id)` claws back
  the SAC balance with operator + holder auth (`contracts/transfer_agent/src/lib.rs:509`).
  Testnet: `CAF4JIUZBLTQCSL2ZOX4ZEZ7FQDCGVBDVCBXRAJJRM6RW77BBX44SFC7` (wasm `3870748b…`, v5, from
  `caatinga.artifacts.json`). Not on mainnet. Its source is NOT in the public repo.
- Public since 2026-08-19 (`github.com/pwsaragossy/radox`): token_sale, yield_distributor,
  maturity_settlement only.

So **"final delivery burns the token" is prior work**. The new work the judges score (Scale:
milestone completion against the intake) is:

1. the **chain of custody** between delivery request and burn: each handover (warehouse → port →
   carrier → customs → recipient) signed by **both** outgoing and incoming custodian in one call,
   with an attestation (document hash, location, timestamp) emitted as an event;
2. ownership never moves during transit (the holder keeps the token the whole time);
3. the last handover to the recipient is what unlocks the burn (calling or gating `redeem`);
4. proof on testnet, hash by hash, and a connection to the Radox API.

The README must say this split in one table: "existed before / built at HackMeridian".

## 2. Target (proposal, waits for owner approval on the card)

Full lifecycle on testnet: open → 4 dual-signed handovers (warehouse, port, carrier, customs) →
deliver = **6 signed testnet transactions** (burn by the existing `redeem` shown after), each verifiable by hash on the public RPC.
`check:` will be a script that reads the 6 hashes from a file and asks the public RPC for each
(exit 0 when all 6 are SUCCESS). Written in stage 1, frozen when the owner approves.

## 3. Design — decided, in LEO-BRIEF.md

The contract design comes from the Radox architecture panel of 2026-10-20 (`custody_registry`: `open`,
dual-signed `handover`, `attest` from registered sources, `deliver`, `freeze`, pause; an on-chain `head`
hash chain so the off-chain history stays verifiable past the 7-day event window; `assurance` levels).
The burn is **not** in the registry: the Radox backend co-signs `transfer_agent.redeem` only after the
registry says `Delivered`. Full spec, rules and checks: [LEO-BRIEF.md](LEO-BRIEF.md).

## 4. Connection to the Radox API (stays private)

The Radox backend is never published. The connection is the `ship` / `deliver` steps of the
withdrawal reading or writing the custody contract. That change, if needed, goes on the private
branch `hackmeridian` of `radox-internal` and is disclosed in the README as "integration in the
closed platform" with the testnet tx hashes as proof. Everything else is in the public repo.

## 5. Timeline (Lisbon time; hard stop Mon 10:00, site says 12:00)

| When | What | Gate |
|---|---|---|
| Sun 09:00–10:00 | Read full rules in the portal; close stage 1; design decisions above | review-1 |
| Sun 10:00–14:00 | Contract + unit tests; testnet accounts for the 6 actors | first handover on testnet |
| Sun 14:00–18:00 | Full lifecycle on testnet, hashes recorded | **18:00 stop criterion** (proposal) |
| Sun 18:00–23:00 | API connection; README; architecture section with contract IDs | review-2 |
| Mon 00:00–06:00 | Demo (offline-safe) + screen recording; deck ≤10 slides; pitch | review-3 |
| Mon 06:00–08:00 | Repo public after scrub; package; links opened logged out | review-4 |
| Mon 08:00 | Submit (2 h before own deadline) | owner OK |

## 6. Ready on each machine before 09:00

- Accept the GitHub invites (`rio-miami-rail`, `hackmeridian-cos`).
- Plugin installed and `setup.sh join ~/hackmeridian https://github.com/pwsaragossy/hackmeridian-cos.git --member <name>`.
- `stellar --version` (Pedro's Mac: 28.1.0), `rustup target list --installed` includes `wasm32v1-none`
  (Pedro's Mac: yes), Node ≥ 20 (Pedro's Mac: 26.12.0).
- Testnet RPC reachable: `https://soroban-testnet.stellar.org` (24/10: protocol 29, ledger 5371940).

## 7. Roles (owner, 2026-10-25)

- **Pedro's sessions**: own the project and the board, the pitch (deck, script, video), the Radox API
  connection on the private `hackmeridian` branch, the README and the submission.
- **Leo's agents**: the `custody_registry` contract, unit tests, testnet deploy, lifecycle harness and
  `verify-head` — brief in [LEO-BRIEF.md](LEO-BRIEF.md).
- **Vhendala**: QA and reviewer — runs the review items of each stage and watches the plugin panel
  (Pedro's second screen); anything red becomes a line on the card at once.
- Still to ask an organizer at check-in: is a Scale repo with only the new work (platform closed) accepted?

## 8. Facts checked on 2026-10-25 (after the Raven research in RESEARCH-raven.md)

- Testnet RPC `getVersionInfo`: stellar-core 30.0.0, **protocolVersion 29**.
- crates.io: `soroban-sdk` latest **29.0.1**; OpenZeppelin `stellar-tokens` / `stellar-access` / `stellar-macros`
  latest **0.8.0**, which require `soroban-sdk ^28.0.0` — **they do not build together with 29.x**.
- Decision from that: **no OpenZeppelin token**. The asset is already a SAC token managed by the Radox
  `transfer_agent` (prior work); the custody contract only tracks who holds the physical object and
  never mints. Use `soroban-sdk = "29.0.1"` and `#[contractevent]` for the attestation events.
- Dual signature: `require_auth()` on both custodians; each signs its own auth entry
  (js-stellar-sdk `authorizeEntry`); G-accounts and C-addresses both work (RESEARCH-raven.md §3).
- `getEvents` keeps about 7 days: the demo must not depend on events older than that; store the
  current custodian and the handover count in contract storage too.
- No Stellar SEP for attestations exists; nobody in the ecosystem does dual-signed custody handover
  (RESEARCH-raven.md §5) — this is the "new" claim for the pitch, worth saying to the SDF judges.
- Mentor question ready: which ramp covers USD to a C-address (SEP-45 is Draft; candidates in §6).
