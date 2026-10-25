# Kickoff — Sun 25 Oct 09:00 Lisbon (= 09:00 UTC)

Contains Radox-internal references (paths, commits). Never copy this file or LEO-BRIEF.md into rio-miami-rail.

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
3. the last handover to the recipient authorises the burn: the harness reads status == Delivered, then the operator calls the existing `redeem`;
4. proof on testnet, hash by hash, and a connection to the Radox API.

The README must say this split in one table: "existed before / built at HackMeridian".

Pre-event design and planning exists: the Radox architecture panel of 2026-10-20 and the planning files in hackmeridian-cos dated 24-25 Oct (KICKOFF, LEO-BRIEF, PITCH outline, check.py). No contract code before Sun 09:00.

## 2. Target (owner, 2026-10-25)

Full lifecycle on testnet: open → 4 dual-signed handovers (warehouse → port → carrier → customs →
recipient) → deliver → burn (`redeem` on the harness's own instance of the existing `transfer_agent`) =
**7 signed testnet transactions**, each verifiable by hash on the public RPC. The burn is in so the
judges see the whole cycle without reading Radox.
`check:` is `python3 check.py` (approved, frozen): it reads the 7 hashes from `proofs/lifecycle.json`
and asks testnet Horizon for each (exit 0 when all 7 are SUCCESS).

## 3. Design — decided, in LEO-BRIEF.md

The contract design comes from the Radox architecture panel of 2026-10-20 (`custody_registry`: `open`,
dual-signed `handover`, `attest` from registered sources, `deliver`, `freeze`, pause; an on-chain `head`
hash chain so the off-chain history stays verifiable past the 7-day event window; `assurance` levels).
The burn is **not** in the registry: the Radox backend is meant to co-sign `transfer_agent.redeem` (policy, not enforced on-chain) only after the
registry says `Delivered`. Full spec, rules and checks: [LEO-BRIEF.md](LEO-BRIEF.md).

## 4. Connection to the Radox API (stays private)

The Radox backend is never published. The connection is the `ship` / `deliver` steps of the
withdrawal reading or writing the custody contract. That change, if needed, goes on the private
branch `hackmeridian` of `radox-internal` and is disclosed in the README as "integration in the
closed platform" with the testnet tx hashes as proof. Everything else is in the public repo.

## 5. Timeline (all times UTC+0 = Lisbon: summer time ended Sun 25 Oct 01:00 UTC [[lisbon-is-utc-0-for-the-9963]])

Two deadlines: **ours Mon 10:00** (TRACK.md) and the **event's Mon 12:00**, "no late submissions"
(hackmeridian.com). Submitting at **08:00** leaves 2 h to our deadline and 4 h to the event's.
The event itself ends 16:00, but only the 12:00 submission time matters.

| When | What | Gate |
|---|---|---|
| Sun 09:00–10:00 | Check-in; ask the organizers (not mentors: they start 11:00) the repo question (§7); Pedro logs into the portal, opens the rules page and the submission form, saves the field list, the editing-window dates, the rules text and the rubric scale it states (1–5 or 1–10) to `PORTAL-SEEN.md` here; Leo: wasm check first (§8); Pedro: form dry-run in the same login | Vhendala manual product review of REVIEW-1 and of the page, deck, video and README (does not delay Leo's start) |
| Sun 10:00–14:00 | Leo: contract + unit tests, testnet accounts for the 6 actors. Pedro: shipment page skeleton against a labelled sample fixture. Mentor user test (IDEA.md) at 11:30-11:45, 13:30-14:00, 15:00-17:00 (11:00-12:00 is the opening ceremony and team formation); a Stellar mentor or the plugin reviewer reads the contract by 14:00 (someone who did not write it); keep a mentor log for the README | 14:00 checkpoint: no dual-signed handover on testnet yet → one line on the card |
| Sun 14:00–18:00 | Leo: full lifecycle, hashes in `proofs/lifecycle.json`. Pedro: page wired to the testnet contract (reads real data) | **18:00 stop line**: no dual-signed handover on testnet, then cut the API connection |
| Sun 18:00–19:00 | Page deployed to a public URL, `head` verified on screen | |
| Sun 19:00–20:30 | Dinner, no work | |
| Sun 20:30–22:00 | README sections (Prior work, Built at HackMeridian, AI usage, contract IDs) + Production path (§9); dry-run the submission form with placeholder links. API connection only if the lifecycle ran by 18:00, hard stop 21:00; "connected" = a read-only Radox testnet endpoint returning custodian, status and head, shown as curl output | review-2 |
| Sun 22:00–Mon 00:00 | Deck draft with the real hashes; demo script with the page as the last scene | |
| Mon 00:00–03:00 | Record the video (target 3:00, rehearsed twice, offline backup); an independent agent that wrote none of the code, launched by central, runs the README on a clean clone | review-3 |
| Mon 03:00–06:00 | Rest, or fixes from review-3 only | |
| Mon 06:00–08:00 | Repo public after scrub; deck as PDF; video on YouTube or Vimeo; every link opened logged out | review-4 |
| Mon 08:00 | Submit | owner OK |
| Mon 08:00–10:00 | Buffer for our deadline (2 h); 10:00–12:00 is the event's own margin, not to be used | |

Event programme inside these blocks (hackmeridian.com/schedule, read 2026-10-25): opening ceremony
11:00–11:30, team formation 11:45–12:00, lunch 12:00–13:30, optional workshops 13:30–17:05, dinner
19:00–20:30, Mon briefing 09:00–09:15; mentors 11:00–23:00. Count about 3 h of Sun 10:00–22:00 as
not building.

Shipment page brief. Entry: opens the demo shipment, no input. Primary action: 'Verify head' recomputes the chain on screen. Loading: skeleton plus text. Empty: open shipment, 0 handovers. Error: RPC or Horizon unreachable shows the proofs snapshot labelled 'snapshot, not live'; an unknown key gets its own message. Head mismatch: visible failure. Fixed label: 'Testnet - test keys - not real custodians'. State via getLedgerEntries or simulate; history via Horizon, not getEvents. Contrast 4.5:1, keyboard focus, no colour-only status, readable at projector size.

The page is a must-have (frozen scope), so it has its own lines above; if Leo's lifecycle slips past
18:00, the page still ships on the contract's first handovers and the README says what ran.

## 6. Ready on each machine before 09:00

1. Leo accepts both invites (rio-miami-rail, hackmeridian-cos) at github.com/notifications.
2. In Claude Code: /plugin marketplace add pwsaragossy/chief-of-staff, then /plugin install chief-of-staff@chief-of-staff, then setup.sh join ~/hackmeridian https://github.com/pwsaragossy/hackmeridian-cos.git --member leo.
3. Before the first commit: git config user.email to the GitHub noreply address on every machine that commits (no history rewrite or force-push after Sun 09:00).
4. Leo and Vhendala each confirm on app.hackmeridian.com that they are listed in team Radox, completed the profile and answered the Lisbon RSVP, and are in person at ONE16. Vhendala needs no repo invite and no plugin: she does a manual product review only.
- `stellar --version` (Pedro's Mac: 28.1.0), `rustup target list --installed` includes `wasm32v1-none`
  (Pedro's Mac: yes), Node ≥ 20 (Pedro's Mac: 26.12.0).
- Testnet RPC reachable: `https://soroban-testnet.stellar.org` (re-checked 25/10 00:49 UTC: protocol 29).

## 7. Roles (owner, 2026-10-25)

- **Pedro's sessions**: own the project and the board, the public shipment page, the pitch (deck,
  script, video), the Radox API connection on the private `hackmeridian` branch (conditional), the
  README and the submission. Load risk: this is a lot for one person across the same 27 h; if the page
  slips, it outranks the API connection and the deck polish.
- **Leo's agents**: the `custody_registry` contract, unit tests, testnet deploy, lifecycle harness and
  `verify-head` — brief in [LEO-BRIEF.md](LEO-BRIEF.md).
- **Vhendala**: manual product review only, reading the page, deck, video and README as a judge would; no code review, no repo invite. A Stellar mentor or the plugin reviewer reads the contract by 14:00; an independent agent (central launches it) runs the README on a clean clone at Mon 00:00. Anything red becomes a line on the card at once.
- Still to ask an organizer at check-in: is a Scale repo with only the new work (platform closed) accepted?

## 8. Facts re-checked live on 2026-10-25 00:49 UTC (RPC, crates.io API, Raven stellarDocs)

- Testnet is wiped on the scheduled reset of 2026-12-16 [[stellar-testnet-resets-wipe-contracts-and-dfe4]].
- Testnet RPC `getVersionInfo`: node build stellar-core 30.0.0, **protocolVersion 29** (re-run, same).
- The burn's wasm is still on testnet: `stellar contract info interface --wasm-hash 3870748b…
  --network testnet` returned the spec with `fn redeem` (2026-10-25 01:02 UTC). Re-run it at Sun 09:00.
- crates.io: `soroban-sdk` latest **29.0.1** (GitHub release 2026-10-12, crate updated 2026-10-21); `stellar-tokens` latest **0.8.0**
  (2026-10-20), whose dependency is `soroban-sdk ^28.0.0` (read from its 0.8.0 dependency list) —
  **it does not build together with 29.x**. `stellar-access` / `stellar-macros` 0.8.0 were
  not re-read this time: unverified here, same family and version as `stellar-tokens`.
- Decision from that: **no OpenZeppelin token**. The asset is already a SAC token managed by the Radox
  `transfer_agent` (prior work); the custody contract only tracks who holds the physical object and
  never mints. Use `soroban-sdk = "29.0.1"` and `#[contractevent]` for the attestation events.
- Dual signature: `require_auth()` on both custodians; each signs its own auth entry
  (js-stellar-sdk `authorizeEntry`); G-accounts and C-addresses both work (RESEARCH-raven.md §3).
- `getEvents` keeps about 7 days (stellarDocs re-read: "7 day retention window"): the demo must not depend on events older than that; store the
  current custodian and the handover count in contract storage too.
- Dual auth confirmed again in the docs: no limit on how many addresses call `require_auth` in one
  contract (stellarDocs, authorization page, "authorizing multiple addresses").
- No Stellar SEP for attestations was found, and no ecosystem project found doing dual-signed
  custody (RESEARCH-raven.md §5) — a directory search, so say "we found none", never "none exists".
- Passkey smart accounts: removed from PITCH.md slide 4 and the script notes on 2026-10-25 (passkey
  signing is cut from scope, so the claim would be false).
- Wording: "burn" is prior work (`redeem`); say so on the slide (PITCH.md slides 2, 4 and 5 do).
- Mentor question ready: which ramp covers USD to a C-address (SEP-45 is Draft; candidates in RESEARCH-raven.md).

## 9. Production path (README section text)

Production path (README section). Mainnet: not this weekend; testnet only. Physical-asset offers on the Radox platform are blocked outside testnet until the full test matrix is proven (re-check against origin/main before publishing; no flag names or file paths in the public README). On mainnet the asset issuer account must be locked after the SAC admin handover; the testnet demo does not do this (record in proofs whether it was locked). Audit: none. The SCF Audit Bank serves SCF-awarded projects, so it can start only after an award. A paper bill or a second token for the same cargo is not prevented on chain. Evidence lifetime: testnet resets about quarterly (next 2026-12-16) and getEvents keeps about 7 days; the committed Horizon JSON of the 7 txs and the video are what remain. SCF Build: planned, not submitted; no eligibility claim. The older public radox repo (all rights reserved) is a different repo from this Apache-2.0 one; nothing was copied.
