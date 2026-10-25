# Form answers: one final paste

Portal fields in form order. Copy the text inside each box as it is; paste everything in one go and never reload the form page. Two fields wait: video link and deck file. Only Pedro checks the terms box and submits.

## Project title (required; 72 chars)

```text
Radox Custody Rail: dual-signed custody for goods in transit, on Stellar
```

## Tagline (optional, up to 120 chars; 25 chars)

```text
First corridor: Rio–Miami
```

## Description (required, Markdown, up to 8000 chars; 3482 chars)

```text
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

Nine refusal branches, run by simulation, are recorded with their error results in `proofs/lifecycle.json`. In a second shipment, two teammates authorised their handovers from their own computers with their own testnet keys, by their account; only public keys and signed authorisation entries were exchanged (`proofs/three-machine.json`). In a local test run, a read-only endpoint of the closed Radox backend read the same record and returned the same head; its curl output, in the README, is the only evidence.

**Check it yourself.** `node scripts/verify-head.mjs <key>` reads the shipment's transactions from Horizon, recomputes the head and compares it with the value on the contract (MATCH). The public page, https://rio-miami-rail.vercel.app, does the same in the browser with its Verify head button. `node scripts/handover-signers.mjs` lists who authorised each handover.

**Existed before / built here.** Before the event: the Radox platform, its three mainnet contracts and the `transfer_agent` contract used for the burn. Built at HackMeridian, from the first commit at 2026-10-25 09:00 UTC: the `custody_registry` contract and its 24 unit tests, the testnet harness, the verification scripts, the public page and both proof sets.

Testnet only, test keys, no audit. Everything on testnet runs with test accounts, not real companies.
```

## Problem solved (optional; 692 chars)

```text
About 45 million ocean bills of lading are issued a year (DCSA, Feb 2023, 2021 data); in 2025 about 11% were issued electronically (DCSA, as of 2025). 22% of recorded cargo thefts in 2025 involved insiders (TT Club & BSI Cargo Theft Report, Apr 2026). These are market figures, not our traction. In our working assumption, a container that crosses a border changes hands many times: warehouse, port, carrier, customs, recipient. Each party keeps its own record, and a token that represents the cargo has no trustworthy link to where the cargo physically is. Whoever holds the token cannot check the custody history without trusting the party that reports it. No customer has confirmed it yet.
```

## Challenges (optional; 1279 chars)

```text
1. Our first two-signer script crashed before submitting anything: with js-stellar-sdk 17.3.0 the simulated auth entries are plain objects, not accessor methods, and protocol 29 returns `sorobanCredentialsAddressV2`. Fixed by signing each custodian's entry with `authorizeEntry` and passing them to `Operation.invokeContractFunction({ auth })`.
2. `stellar contract invoke` on a read-only call only simulates and returns no hash; `--send=yes` was needed to get on-chain proof.
3. An AI reviewer agent found two major bugs before deploy: a route that revisits an address let `deliver` succeed with zero handovers, and the contract instance TTL was never extended, so it could have archived about a week after deploy, possibly during judging. Both fixed with tests before deploy.
4. The first unit tests did not compile: the contract is `no_std`, so the test module needed `extern crate std`, and the `try_` assertions only type-checked once entry points returned `Result<_, Error>` instead of panicking.
5. For the second shipment, our check of the teammates' signed entries first rejected valid signatures. Protocol 29 address-bound credentials are signed over a different payload than the legacy ones; we changed the check to use that payload, and a wrong key is still rejected.
```

## What's next (optional; 859 chars)

```text
Rio–Miami is our first corridor, not the product. Our goal is a shared, SWIFT-like custody standard and an end-to-end rail that companies along a supply chain could use; neither exists yet. Next we will connect the rail to the Radox platform's physical-asset flow (a read-only Radox API endpoint already reads this registry in a local test run), seek introductions to one financial institution and one port, airport or logistics operator for a first pilot shipment, ask a Stellar engineer to review the design, and prepare an SCF Build application. Mainnet waits for an audit and the issuer-account lock described in the README. We intend to approach chambers of commerce, ports and airports about integrating their systems. Today no such standard, integration, adoption or partnership exists: this weekend proves the record on Stellar testnet with test keys.
```

## Repository link (required, public HTTPS)

```text
https://github.com/pwsaragossy/rio-miami-rail
```

## Demo link (optional)

```text
https://rio-miami-rail.vercel.app
```

## Video link (required, YouTube or Vimeo)

```text
{{VIDEO URL: central sends it after Pedro's upload}}
```

## Deck file (required, PDF/PPTX/PPT/HTML up to 20 MiB)

```text
{{UPLOAD: final deck PDF from the deck session}}
```

## Thematic track (optional, pick one)

```text
Stellar Unlocked
```

## Tech stack (optional, comma-separated, up to 25; 20 items)

```text
Stellar testnet, Soroban, Rust, soroban-sdk 29.0.1, wasm32v1-none, Cargo, Stellar CLI 28.1.0, Soroban authorization (require_auth), Stellar Asset Contract, Stellar RPC, Horizon, Friendbot, JavaScript, Node.js, npm, @stellar/stellar-sdk 17.3.0, HTML, CSS, Vercel, Radox transfer_agent (prior work)
```

## Prior work disclosure (optional; 1306 chars)

```text
Before HackMeridian (2026-10-25 09:00 UTC) we built Radox, a platform for tokenized real-world assets. Its three Soroban contracts (token_sale, yield_distributor, maturity_settlement) run on Stellar mainnet since June-July 2026; their source is public, contracts only, at https://github.com/pwsaragossy/radox since 2026-08-19 (the published token_sale is a newer version, v8, than the deployed v7; the other two match). That repo carries its own, different licence. The Radox backend is closed and not published. The burn in our redeem transaction calls an instance of Radox's existing transfer_agent contract, deployed on testnet from its existing wasm; its source is closed and we did not write it at the event. A read-only Radox API endpoint that reads this registry was written during the event, on a private branch of the closed Radox backend (2026-10-25); it is not part of this repo and its source is not published. Nothing from the public Radox repo was copied into this repo. Before the event we also wrote design notes (2026-10-20, no code) and planning documents (2026-10-24 and 25), and chief-of-staff, a Claude Code plugin we use for planning and review (first commit 2026-10-22). The GitHub repository was created empty on 2026-10-24 22:49 UTC; the first commit is at 2026-10-25 09:00:17 UTC.
```

## AI tooling note (optional; 1083 chars)

```text
Tools: Claude Code (Anthropic's coding agent) mainly with Claude Opus 5.5 (`claude-opus-5-5`), and Claude Sonnet 5.5 for some review subagents; chief-of-staff, a Claude Code plugin we wrote before the event (declared as prior work); Voicebox 0.5.0 (Qwen3-TTS 1.7B via mlx-audio), run locally on Pedro's Mac, for the video narration ("Narration: AI voice generated from Pedro's voice"); Playwright for the screen recordings; python-pptx scripts, written by Claude Code, for the deck; Raven, a Stellar documentation gateway, for Stellar lookups. What they did: Claude Code agents wrote the Soroban contract, unit tests, testnet harness, verification scripts, shipment page, documentation, the deck and its build script, and separate AI reviewer agents checked the contract, the scripts and every public text. A human developer reviewed the contract's functions, auth checks and error codes, the dependency pin and the signing logic; the page and the later scripts were not reviewed line by line by a human. AI_USAGE.md in the repo lists every file, how it was made and who reviewed it.
```

## Accepted terms (required)

Pedro checks the box.
