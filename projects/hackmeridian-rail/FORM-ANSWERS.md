# Form answers: one final paste

Portal fields in the order of the live portal (Pedro's paste, 26 Oct ~02:00 UTC). Copy the text inside each box as it is; paste everything in one go and never reload the form page. Two fields wait: video link and deck file. Only Pedro checks the terms box and submits.

## Project title (required; 18 chars)

```text
Radox Custody Rail
```

## Tagline (optional, up to 120 chars; 101 chars)

```text
SWIFT for goods in transit, on Stellar: every handover signed by both companies, checkable by anyone.
```

Waits on Pedro's button. Alternatives: `SWIFT for goods in transit, on Stellar` (38 chars, what the portal holds now) or `One shared custody record for goods in transit: every handover signed by both companies, checkable by anyone.` (109 chars).

## Description (required, Markdown, up to 8000 chars; 5807 chars)

```text
**A container crosses a border through several companies and agencies (for example a warehouse, a port, a carrier, customs and the buyer), and each keeps its own records. No record is shared among them, so none of them can check what the others say about who held the goods. The money that rides on those records is large: the WTO says 80 to 90 per cent of world trade relies on trade finance. Radox Custody Rail is a shared record that each company on the route signs into, like SWIFT for goods: at each handover, the company giving the goods and the company receiving them both sign, the step is added to a hash chain that no one can rewrite (an administrator can freeze a shipment but cannot change past steps), and anyone who needs to know (the buyer, an insurer, a lender) can check the whole history against one 32-byte value stored on the contract. This repo is its first piece, running on Stellar testnet: a Soroban contract where every handover is authorised by both custodians, hash-chained, and checkable by anyone from public data.**

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

Nine refusal branches, run by simulation, are recorded with their error results in `proofs/lifecycle.json`. In a second shipment, two teammates signed their own handovers with their own testnet keys; only public keys and signed authorisation entries were exchanged (`proofs/three-machine.json`). The Radox backend, in a local development run, read the first shipment's record and returned the same head as `verify-head` (README, Architecture).

**One rail, many supply chains.** On a third registry, two test companies' chains ran side by side: internal handovers between units of the same company, an external handover joining them, and a second shipment sharing two stops. Ten successful transactions, both heads MATCH, no new contract code (`proofs/multi-chain.json`). The record format is published as an open spec, `CUSTODY-SPEC.md`, so any Stellar issuer can implement it or reuse the contract under Apache-2.0.

**Stellar ecosystem.** `custody_registry` is an open Apache-2.0 Soroban contract that stores a token address and never calls the token, so any tokenized Stellar asset can carry a custody record. Radox will open API access to Stellar issuers. Stellar holds about US$4 billion in tokenized real-world assets (SDF, as of 1 Sep 2026), and we found no Stellar project that records a handover signed by two custodians (LumenLoop directory and SCF submissions, plus Scout for SEPs, searched 24–25 Oct 2026).

**Check it yourself.** `node scripts/verify-head.mjs <key>` reads the shipment's transactions from Horizon, recomputes the head and compares it with the value on the contract (MATCH). The public page, https://rio-miami-rail.vercel.app, does the same in the browser with its Verify head button. `node scripts/handover-signers.mjs` lists who authorised each handover.

**Ask one question, get the answer.** A company on the route, or a financier, will be able to ask the Radox API, `GET /api/custody/shipments/:key`, and get the shipment's status, current custodian, route and number of signed handovers, read from this contract. The endpoint is in the closed Radox backend; it ran only in a local development run on testnet and is not publicly hosted.

**Rehearsed against mainnet state.** The same contract build (wasm `8230ed93…`) ran its custody lifecycle (without the token and burn steps) against a local fork of Stellar mainnet (soroban-sim, protocol 29): all 15 transactions applied, all 9 refusal branches were refused, and the run was charged 13.72 XLM in fees (`scripts/mainnet-rehearsal.mjs`, `proofs/mainnet-rehearsal.json`). Nothing was sent to mainnet; the mainnet deploy is a later signing ceremony.

**Existed before / built here.** Before the event: the Radox platform, its three mainnet contracts and the `transfer_agent` contract used for the burn. Built at HackMeridian, from the first commit at 2026-10-25 09:00 UTC: the `custody_registry` contract and its 26 tests, the testnet harness, the verification scripts, the public page, the open spec and four proof sets.

Runs on Stellar testnet.
```

## Problem solved (optional; 1247 chars)

```text
About 45 million ocean bills of lading are issued a year (DCSA, Feb 2023, 2021 data); in 2025 about 11% were issued electronically (DCSA, as of 2025). 22% of recorded cargo thefts in 2025 involved insiders (TT Club & BSI Cargo Theft Report, Apr 2026). ADB estimates the global trade finance gap at about US$2.5 trillion, unchanged from 2023 (ADB Global Trade Finance Gap Survey, Dec 2025). These are market figures, not results of this project. Our design target is the US–Brazil goods corridor, about US$94.2 billion in 2025 (US Census Bureau, exports plus imports); Brazil was Florida's largest goods export market in 2025 (USTR). A container that crosses a border changes hands many times: warehouse, port, carrier, customs, recipient. Each party keeps its own record, and a token that represents the cargo has no trustworthy link to where the cargo physically is. Whoever holds the token cannot check the custody history without trusting the party that reports it. Ports and airports run legacy systems that are hard to integrate. With the rail, each company will integrate once, not pair by pair: a legacy system will join through one adapter to the Radox API, and a financier can read which custodian last signed for the goods before paying.
```

## Challenges (optional; 1327 chars)

```text
1. Our first two-signer script crashed before submitting anything: with js-stellar-sdk 17.3.0 the simulated auth entries are plain objects, not accessor methods, and protocol 29 returns `sorobanCredentialsAddressV2`. Fixed by signing each custodian's entry with `authorizeEntry` and passing them to `Operation.invokeContractFunction({ auth })`.
2. `stellar contract invoke` on a read-only call only simulates and returns no hash; `--send=yes` was needed to get on-chain proof.
3. An AI reviewer agent found, before the testnet deploy, that a route that revisits an address let `deliver` succeed with zero handovers, and that the contract instance TTL was never extended, so it could have archived about a week after deploy, possibly during judging. Both were fixed with tests (commit `9b66e00`, with three more review fixes).
4. The first unit tests did not compile: the contract is `no_std`, so the test module needed `extern crate std`, and the `try_` assertions only type-checked once entry points returned `Result<_, Error>` instead of panicking.
5. For the second shipment, our check of the teammates' signed entries first rejected valid signatures. Protocol 29 address-bound credentials are signed over a different payload than the legacy ones; we changed the check to use that payload, and a wrong key is still rejected.
```

## What's next (optional; 1210 chars)

```text
Rio–Miami is our first corridor, not the product. We are building the end-to-end custody rail for goods in transit: a shared, SWIFT-like standard for every company along a supply chain. Radox is part of the Rio–Miami trade-corridor initiative and its technology rail: every port, airport and chamber that joins it will join the rail, through one adapter to the Radox API. Radox is in conversations with chambers of commerce in Brazil and Miami. Next we connect the rail to the Radox platform's physical-asset flow (a read-only Radox API endpoint reads this registry in a local development run), run the first live shipment with a financial institution and a port or logistics operator, have a Stellar engineer review the design, and apply to SCF Build. Mainnet follows an audit and the issuer-account lock described in the README. Business model: a recurring fee per connected institution plus a fee per shipment. It borrows the shape of SWIFT's published fee structure: Swift, a cooperative owned by its members, charges an entry fee, annual charges (including network connection) and network-usage fees on message traffic (swift.com billing rules, accessed 25 October 2026). We are not affiliated with Swift.
```

## Repository link (required, public HTTPS)

```text
https://github.com/pwsaragossy/rio-miami-rail
```

The repo is private (github.com returns 404 to a visitor, checked 26 Oct). It goes public only on Pedro's OK, planned 06:00 UTC.

## Project website link (optional)

```text
https://rio-miami-rail.vercel.app
```

The portal asks for llms.txt, robots.txt and sitemap.xml on this site. Production already serves all three (HTTP 200, same as page/ on main). The llms.txt there describes only the first shipment; a refreshed draft with the rail story, the spec and the four proof sets is in website-files/llms.txt. Putting it live is a production deploy and waits on Pedro. Landing v3 (branch landing-v3) is not approved, so the link stays on production.

## Video link (required, YouTube or Vimeo)

```text
{{VIDEO URL: central sends it after Pedro's upload}}
```

Blocker: the video is on hold by Pedro ("Vídeo ainda não"). Required field; the form cannot be submitted without it.

## Deck file (required, PDF/PPTX/PPT/HTML up to 20 MiB)

```text
{{UPLOAD: deck/radox-custody-rail.pdf}}
```

File checked 26 Oct: 760,710 bytes (0.73 MiB, under 20 MiB), 10 pages, built 01:07 UTC. Cover: "Radox Custody Rail", "SWIFT for goods in transit, on Stellar" and the line "One shared custody record for goods in transit: every handover signed by both companies, checkable by anyone." It matches the title field whichever tagline Pedro picks.

## Thematic track (optional, pick one)

```text
Stellar Unlocked
```

Pedro's choice (24 Oct). Check that the option is still in the portal list when pasting.

## Tech stack (optional, comma-separated, up to 25; 20 items)

```text
Stellar testnet, Soroban, Rust, soroban-sdk 29.0.1, wasm32v1-none, Cargo, Stellar CLI 28.1.0, Soroban authorization (require_auth), Stellar Asset Contract, Stellar RPC, Horizon, Friendbot, JavaScript, Node.js, npm, @stellar/stellar-sdk 17.3.0, HTML, CSS, Vercel, Radox transfer_agent (prior work)
```

## Prior work disclosure (optional; 1499 chars)

```text
Before HackMeridian (2026-10-25 09:00 UTC) we built Radox, a platform for tokenized real-world assets. Its three Soroban contracts (token_sale, yield_distributor, maturity_settlement) run on Stellar mainnet since June-July 2026; their source is public, contracts only, at https://github.com/pwsaragossy/radox since 2026-08-19 (the published token_sale is a newer version, v8, than the deployed v7; the other two match). That repo carries its own, different licence. The Radox backend is closed and not published. The cargo token is registered, minted and delivered to the holder in setup, and burned in our redeem transaction with `redeem(token, from, amount, ref_id)`, through an instance of Radox's existing transfer_agent contract (`CAYD3EFT…SJWH`), deployed on testnet from its existing wasm; its source is closed and we did not write it at the event. A read-only Radox API endpoint, `GET /api/custody/shipments/:key`, which calls this registry's `get(key)`, was written during the event, on a private branch of the closed Radox backend (2026-10-25); it is not part of this repo and its source is not published. Nothing from the public Radox repo was copied into this repo. Before the event we also wrote design notes (2026-10-20, no code) and planning documents (2026-10-24 and 25), and chief-of-staff, a Claude Code plugin we use for planning and review (first commit 2026-10-22). The GitHub repository was created empty on 2026-10-24 22:49 UTC; the first commit is at 2026-10-25 09:00:17 UTC.
```

## AI tooling note (optional; 1009 chars)

```text
Tools: Claude Code (Anthropic's coding agent) mainly with Claude Opus 5.5 (`claude-opus-5-5`), and Claude Sonnet 5.5 for some review subagents; chief-of-staff, a Claude Code plugin we wrote before the event (declared as prior work); Voicebox 0.5.0 (Qwen3-TTS 1.7B via mlx-audio), run locally on Pedro's Mac, for the video narration ("Narration: AI voice generated from Pedro's voice"); Playwright for the screen recordings; python-pptx scripts, written by Claude Code, for the deck; Raven, a Stellar documentation gateway, for Stellar lookups. What they did: Claude Code agents wrote the Soroban contract, unit tests, testnet harness, verification scripts, shipment page, documentation, the deck and its build script, and separate AI reviewer agents checked the contract, the scripts and every public text. A human developer reviewed the contract's functions, auth checks and error codes, the dependency pin and the signing logic. AI_USAGE.md in the repo lists every file, how it was made and who reviewed it.
```

## Accepted terms (required)

Pedro checks the box.
