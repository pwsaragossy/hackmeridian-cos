# Form answers — paste source for the portal (internal until Pedro's OK)

Write each final answer here, count it, then paste all in one go (never reload the form page).
Plan, sources and limits: SUBMISSION.md "Portal form, field by field". Only Pedro checks the terms box and submits.

| Field | Limit | Chars | Status |
|---|---|---|---|
| Project title | unseen | 72 | Pedro's text |
| Tagline | 120 | 25 | Pedro's text |
| Description | 8000, Markdown | 3309 | draft, review-4 |
| Problem solved | unseen, keep < 1500 | 692 (draft) | review-4 |
| Challenges | unseen, keep < 1500 | 1279 | draft, review-4 |
| What's next | unseen, keep < 1500 | 810 (draft) | review-4 |
| Repository link | HTTPS, public | https://github.com/pwsaragossy/rio-miami-rail | public after Leo's scrub and Pedro's OK |
| Demo link | — | https://rio-miami-rail.vercel.app | live (llms.txt, robots.txt, sitemap.xml served) |
| Video link | YouTube/Vimeo | — | Mon 08:00 |
| Deck file | ≤ 20 MiB | — | Mon 06:00 |
| Thematic track | one | — | Stellar Unlocked |
| Tech stack | ≤ 25 items | 12 items | from the repo |
| Prior work disclosure | unseen | 1306 | draft, review-4 |
| AI tooling note | unseen | 1083 | draft, review-4 |

## Answers

### Project title (Pedro, 2026-10-25)

Radox Custody Rail: dual-signed custody for goods in transit, on Stellar

### Tagline (Pedro, 2026-10-25)

First corridor: Rio–Miami

### Description (draft 2026-10-25, review-4 pending)

**Our goal is an end-to-end custody rail for goods in transit: a shared, SWIFT-like standard that companies along a supply chain, from origin to destination, could use. Neither the standard nor the rail exists yet. This repo is the first piece we built, run on Stellar testnet: a Soroban contract where every handover is authorised by both custodians, hash-chained, and checkable by anyone from public data.**

One shipment is one record in our `custody_registry` contract. The operator opens it with an ordered route of custodians. Each handover calls the contract once, and the call requires `require_auth()` from both the outgoing and the incoming custodian; a wrong custodian, an out-of-route step or a bad assurance level is refused. Delivery needs the final custodian and the token holder. Every step folds into one 32-byte `head` kept on the contract, so one value commits to the whole history. After delivery, the cargo token is burned through Radox's existing transfer agent (prior work, disclosed below).

**Proof on Stellar testnet** (registry `CCBJVXMJYWPHTDJHDFPRGKPGXGEP24JOPJAMUS5C3BMZJTRTWR2H4LII`):

| Step | Transaction |
|---|---|
| open | [2b3d51f0…9902](https://stellar.expert/explorer/testnet/tx/2b3d51f0cdf113d34a7c20dd373142c379926bd3bd24ca0a9cb6d4718e379902) |
| handover 1 | [635c99ac…bd38](https://stellar.expert/explorer/testnet/tx/635c99ac73cb13416e6b52f29ac9a067fbc615e01b8de962eb36245db3f0bd38) |
| handover 2 | [56a0f006…7cc2](https://stellar.expert/explorer/testnet/tx/56a0f006e3373df34c96ae7b0f02c4b66753ccaca6ccc48fe5125bb65e7b7cc2) |
| handover 3 | [ac268a49…c4b2](https://stellar.expert/explorer/testnet/tx/ac268a49e00ddf4745c9026bf01e3c77e5c451a7e2396100ef590a36ecc3c4b2) |
| handover 4 | [5199d4fb…0b7a](https://stellar.expert/explorer/testnet/tx/5199d4fb6b2833662327deecbf5fcaf058a0d7a464f97974edd107f5de400b7a) |
| deliver | [919def8c…4e37](https://stellar.expert/explorer/testnet/tx/919def8c0b3f29ae650f5f1ea6d632e49efd4a9442381c84c83d858ad2144e37) |
| redeem (burn) | [864fd164…644d](https://stellar.expert/explorer/testnet/tx/864fd1644d30bf708a59f94ca5b0fc303a50deccfd96099bd32dfb67e215644d) |

Nine refusal branches, run by simulation, are recorded with their error results in `proofs/lifecycle.json`. In a second shipment, two teammates authorised their handovers from their own computers with their own testnet keys, by their account; only public keys and signed authorisation entries were exchanged (`proofs/three-machine.json`).

**Check it yourself.** `node scripts/verify-head.mjs <key>` reads the shipment's transactions from Horizon, recomputes the head and compares it with the value on the contract (MATCH). The public page, https://rio-miami-rail.vercel.app, does the same in the browser with its Verify head button. `node scripts/handover-signers.mjs` lists who authorised each handover.

**Existed before / built here.** Before the event: the Radox platform, its three mainnet contracts and the `transfer_agent` contract used for the burn. Built at HackMeridian, from the first commit at 2026-10-25 09:00 UTC: the `custody_registry` contract and its 24 unit tests, the testnet harness, the verification scripts, the public page and both proof sets.

Testnet only, test keys, no audit. Everything on testnet runs with test accounts, not real companies.

### Challenges (from Leo's 12:55 card lines, final per his ~14:05 call; item 5 from the second shipment)

1. Our first two-signer script crashed before submitting anything: with js-stellar-sdk 17.3.0 the simulated auth entries are plain objects, not accessor methods, and protocol 29 returns `sorobanCredentialsAddressV2`. Fixed by signing each custodian's entry with `authorizeEntry` and passing them to `Operation.invokeContractFunction({ auth })`.
2. `stellar contract invoke` on a read-only call only simulates and returns no hash; `--send=yes` was needed to get on-chain proof.
3. An AI reviewer agent found two major bugs before deploy: a route that revisits an address let `deliver` succeed with zero handovers, and the contract instance TTL was never extended, so it could have archived about a week after deploy, possibly during judging. Both fixed with tests before deploy.
4. The first unit tests did not compile: the contract is `no_std`, so the test module needed `extern crate std`, and the `try_` assertions only type-checked once entry points returned `Result<_, Error>` instead of panicking.
5. For the second shipment, our check of the teammates' signed entries first rejected valid signatures. Protocol 29 address-bound credentials are signed over a different payload than the legacy ones; we changed the check to use that payload, and a wrong key is still rejected.

### Tech stack (from Cargo.toml, package.json and the page, 2026-10-25)

Stellar testnet, Soroban, Rust, soroban-sdk 29.0.1, wasm32v1-none, Cargo, Stellar CLI 28.1.0, Soroban authorization (require_auth), Stellar Asset Contract, Stellar RPC, Horizon, Friendbot, JavaScript, Node.js, npm, @stellar/stellar-sdk 17.3.0, HTML, CSS, Vercel, Radox transfer_agent (prior work)

### Prior work disclosure (draft 2026-10-25, review-4 pending)

Before HackMeridian (2026-10-25 09:00 UTC) we built Radox, a platform for tokenized real-world assets. Its three Soroban contracts (token_sale, yield_distributor, maturity_settlement) run on Stellar mainnet since June-July 2026; their source is public, contracts only, at https://github.com/pwsaragossy/radox since 2026-08-19 (the published token_sale is a newer version, v8, than the deployed v7; the other two match). That repo carries its own, different licence. The Radox backend is closed and not published. The burn in our redeem transaction calls an instance of Radox's existing transfer_agent contract, deployed on testnet from its existing wasm; its source is closed and we did not write it at the event. A read-only Radox API endpoint that reads this registry was written during the event, on a private branch of the closed Radox backend (2026-10-25); it is not part of this repo and its source is not published. Nothing from the public Radox repo was copied into this repo. Before the event we also wrote design notes (2026-10-20, no code) and planning documents (2026-10-24 and 25), and chief-of-staff, a Claude Code plugin we use for planning and review (first commit 2026-10-22). The GitHub repository was created empty on 2026-10-24 22:49 UTC; the first commit is at 2026-10-25 09:00:17 UTC.

### AI tooling note (draft 2026-10-25, review-4 pending; Pedro: name everything)

Tools: Claude Code (Anthropic's coding agent) mainly with Claude Opus 5.5 (`claude-opus-5-5`), and Claude Sonnet 5.5 for some review subagents; chief-of-staff, a Claude Code plugin we wrote before the event (declared as prior work); Voicebox 0.5.0 (Qwen3-TTS 1.7B via mlx-audio), run locally on Pedro's Mac, for the video narration ("Narration: AI voice generated from Pedro's voice"); Playwright for the screen recordings; python-pptx scripts, written by Claude Code, for the deck; Raven, a Stellar documentation gateway, for Stellar lookups. What they did: Claude Code agents wrote the Soroban contract, unit tests, testnet harness, verification scripts, shipment page, documentation, the deck and its build script, and separate AI reviewer agents checked the contract, the scripts and every public text. A human developer reviewed the contract's functions, auth checks and error codes, the dependency pin and the signing logic; the page and the later scripts were not reviewed line by line by a human. AI_USAGE.md in the repo lists every file, how it was made and who reviewed it.

### Problem solved (draft 2026-10-25, review-4 pending)

About 45 million ocean bills of lading are issued a year (DCSA, Feb 2023, 2021 data); in 2025 about 11% were issued electronically (DCSA, as of 2025). 22% of recorded cargo thefts in 2025 involved insiders (TT Club & BSI Cargo Theft Report, Apr 2026). These are market figures, not our traction. In our working assumption, a container that crosses a border changes hands many times: warehouse, port, carrier, customs, recipient. Each party keeps its own record, and a token that represents the cargo has no trustworthy link to where the cargo physically is. Whoever holds the token cannot check the custody history without trusting the party that reports it. No customer has confirmed it yet.

### Technical, fragment for the three-machine proof (draft 2026-10-25, review-4 pending)

In a second testnet shipment, two team members authorised their own handovers from their own computers, each with a testnet key that, by their account, never left that computer; only public keys and signed authorisation entries were exchanged, and the operator's machine checked each entry before submitting. The other keys in that shipment (warehouse, recipient, holder and operator) are our test keys on one machine. Four transactions, all successful, and verify-head recomputes the same head (proof: proofs/three-machine.json in the repo, linked from the README).

### What's next (draft 2026-10-25, review-4 pending)

Rio–Miami is our first corridor, not the product. Next we will connect the rail to the Radox platform's physical-asset flow (a read-only Radox API endpoint already reads this registry on testnet), put one specific question to logistics and trade-finance practitioners: could a custodian's signature replace a scanned stamp?, and prepare an SCF Build application. Mainnet waits for an audit and the issuer-account lock described in the README. Longer term, we aim to grow this into a shared standard for custody of tokenized goods across trade corridors, as SWIFT did for payment messages, and we intend to approach chambers of commerce, ports and airports to integrate with their systems. Today no such standard, adoption or partnership exists: this weekend proves the record on Stellar testnet with test keys.
