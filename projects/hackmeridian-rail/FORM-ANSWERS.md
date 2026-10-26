# Form answers: one final paste

Portal fields in the order of the live portal (Pedro's paste, 26 Oct ~02:00 UTC). Copy the text inside each box as it is; paste everything in one go and never reload the form page. Two fields wait: video link and deck file. Only Pedro checks the terms box and submits.

## Project title (required; 18 chars)

```text
Radox Rail
```

## Tagline (optional, up to 120 chars; 101 chars)

```text
SWIFT for goods in transit, on Stellar: every handover signed by both companies, checkable by anyone.
```

Pedro's choice (26 Oct ~03:10 UTC): both approved lines joined. The portal holds `SWIFT for goods in transit, on Stellar` now; replace it with this text.

## Description (required, Markdown, up to 8000 chars; 7820 chars)

```text
**A container crosses a border through several companies and agencies (for example a warehouse, a port, a carrier, customs and the buyer), and each keeps its own records. No record is shared among them, so none of them can check what the others say about who held the goods. The money that rides on those records is large: the WTO says 80 to 90 per cent of world trade relies on trade finance. Radox Rail is a shared record that each company on the route signs into, like SWIFT for goods: at each handover, the company giving the goods and the company receiving them both sign, the step is added to a hash chain that no one can rewrite (an administrator can freeze a shipment but cannot change past steps), and anyone who needs to know (the buyer, an insurer, a lender) can check the whole history against one 32-byte value stored on the contract. This repo is its first piece, running on Stellar testnet: a Soroban contract where every handover is authorised by both custodians, hash-chained, and checkable by anyone from public data.**

**What it does.** One shipment is one record in our `custody_registry` contract, keyed by `sha256(container | origin)`. Its life has five steps. *Open*: the rail operator registers the ordered route of custodians. *Handover*: one call, with `require_auth()` from both the outgoing and the incoming custodian and an assurance level from 1 to 3; a wrong custodian, an out-of-route step or a bad level is refused. *Attest*: an allow-listed source (for example a gate scanner) adds an event hash without moving custody. *Deliver*: the final custodian and the token holder both authorise, and only after every handover is done. *Redeem*: the cargo token is burned through Radox's existing transfer agent (prior work, disclosed below). Custody moves; ownership stays with the token holder. Every step folds into one 32-byte `head` on the contract. The admin can freeze or pause but cannot change a route, a custodian or past steps, and the contract has no upgrade function.

**Proof on Stellar testnet** (registry `CCBJVXMJYWPHTDJHDFPRGKPGXGEP24JOPJAMUS5C3BMZJTRTWR2H4LII`, first shipment; every transaction has `successful: true` on Horizon):

| Step | Signers | Transaction |
|---|---|---|
| open | operator | [2b3d51f0…9902](https://stellar.expert/explorer/testnet/tx/2b3d51f0cdf113d34a7c20dd373142c379926bd3bd24ca0a9cb6d4718e379902) |
| handover 1 | warehouse, port | [635c99ac…bd38](https://stellar.expert/explorer/testnet/tx/635c99ac73cb13416e6b52f29ac9a067fbc615e01b8de962eb36245db3f0bd38) |
| handover 2 | port, carrier | [56a0f006…7cc2](https://stellar.expert/explorer/testnet/tx/56a0f006e3373df34c96ae7b0f02c4b66753ccaca6ccc48fe5125bb65e7b7cc2) |
| attest (gate event) | source | [33379211…8905](https://stellar.expert/explorer/testnet/tx/333792115c7a93abdbf4a45dc217b4bb332c69d14f95095d7d0dffc9d0068905) |
| handover 3 | carrier, customs | [ac268a49…c4b2](https://stellar.expert/explorer/testnet/tx/ac268a49e00ddf4745c9026bf01e3c77e5c451a7e2396100ef590a36ecc3c4b2) |
| handover 4 | customs, recipient | [5199d4fb…0b7a](https://stellar.expert/explorer/testnet/tx/5199d4fb6b2833662327deecbf5fcaf058a0d7a464f97974edd107f5de400b7a) |
| deliver | recipient, token holder | [919def8c…4e37](https://stellar.expert/explorer/testnet/tx/919def8c0b3f29ae650f5f1ea6d632e49efd4a9442381c84c83d858ad2144e37) |
| redeem (burn) | operator, token holder | [864fd164…644d](https://stellar.expert/explorer/testnet/tx/864fd1644d30bf708a59f94ca5b0fc303a50deccfd96099bd32dfb67e215644d) |

Around it: 26 contract tests pass (24 unit, 2 seeded property tests that draw random signer sets and random routes); nine refusal branches are recorded with their error results (`proofs/lifecycle.json`); a second shipment was signed by two teammates with their own testnet keys, exchanging only public keys and signed authorisation entries (`proofs/three-machine.json`); a third registry carried two test companies' chains side by side, with internal handovers, an external handover joining them and a second shipment sharing two stops: ten successful transactions, both heads MATCH, no new contract code (`proofs/multi-chain.json`). The record format is published as an open spec with test vectors, `CUSTODY-SPEC.md`.

**Check it yourself.** `node scripts/verify-head.mjs <key>` reads the shipment's transactions from Horizon (RPC events expire after about seven days, so we do not rely on them), recomputes the head and compares it with the value on the contract: MATCH. `node scripts/handover-signers.mjs` lists who authorised each handover. The public page, https://rio-miami-rail.vercel.app, reads Soroban RPC and Horizon from the browser, lists each transaction, recomputes the head with a Check the fingerprint button, and shows a labelled snapshot if testnet cannot be reached.

Judges can use the rail now, with no account or key: https://rio-miami-rail.vercel.app/docs has the API reference and a live panel that opens a shipment on Stellar testnet, runs handovers that need both companies' authorisation, shows the contract refusing a wrong handover, and recomputes the record's head (a 32-byte fingerprint of its history) in the browser.

**Against the pre-event intake.** Contract with both-custodian handovers and an event attestation: done (tx above). Delivery burns the token: done (redeem). Ownership stays with the holder: the registry records custody only. Proven end to end on testnet with signed transactions: done. Connected to our API: the Radox endpoint (closed backend, a separate API from the open testnet one above) read this contract in a local development run and returned the same head as `verify-head` (details below).

**Stellar ecosystem.** `custody_registry` is an open Apache-2.0 Soroban contract that stores a token address and never calls the token, so any tokenized Stellar asset can carry a custody record. Radox will open API access to Stellar issuers. Stellar holds about US$4 billion in tokenized real-world assets (SDF, as of 1 Sep 2026), and we found no Stellar project that records a handover signed by two custodians (LumenLoop directory and SCF submissions, plus Scout for SEPs, searched 24-25 Oct 2026).

**Ask one question, get the answer.** A company on the route, or a financier, will be able to ask the Radox API, `GET /api/custody/shipments/:key`, and get the shipment's status, current custodian, route and number of signed handovers, read from this contract. The endpoint is in the closed Radox backend; it ran in a local development run on testnet, where it returned status `Delivered`, `seq` 4 and the same head as `verify-head`; it is not publicly hosted.

**Production path.** Mainnet comes after the asset issuer account is locked and the contract is audited. We plan to request the audit through the SDF Audit Bank, which follows an SCF award; the next step is an SCF Build application with this contract as its first milestone.

**Rehearsed against mainnet state.** The same contract build (wasm `8230ed93…`) ran its custody lifecycle (without the token and burn steps) against a local fork of Stellar mainnet (soroban-sim, protocol 29): all 15 transactions applied, all 9 refusal branches were refused, and the run was charged 13.72 XLM in fees (`scripts/mainnet-rehearsal.mjs`, `proofs/mainnet-rehearsal.json`). Nothing was sent to mainnet; the mainnet deploy is a later signing ceremony.

**Existed before / built here.** Before the event: the Radox platform, its three mainnet contracts and the `transfer_agent` contract used for the burn. Built at HackMeridian, from the first commit at 2026-10-25 09:00 UTC: the `custody_registry` contract and its 26 tests, the testnet harness, the verification scripts, the public page, the open testnet API with its /docs reference page, the open spec and four proof sets.

Runs on Stellar testnet.
```

## Problem solved (optional; 1634 chars)

```text
A company that hands a container to the next one, and a lender or insurer that pays against that container, face the same gap. Each company keeps its own record of who held the goods, and a token that represents the cargo has no trustworthy link to where the cargo physically is. Whoever holds the token can check custody only by trusting the party that reports it. Ports and airports run legacy systems that are hard to integrate, so links pair by pair do not scale.

Size of the problem (market figures, not results of this project): about 45 million ocean bills of lading a year, about 11% of them issued electronically in 2025 (DCSA, Feb 2023, 2021 data; DCSA, as of 2025); 22% of recorded cargo thefts in 2025 involved insiders (TT Club & BSI Cargo Theft Report, Apr 2026); a global trade finance gap of about US$2.5 trillion, unchanged from 2023 (ADB Global Trade Finance Gap Survey, Dec 2025). Our design target is the US–Brazil goods corridor, about US$94.2 billion in 2025 (US Census Bureau, exports plus imports).

What changes. For a company: it will join once, through one adapter to the Radox API, not pair by pair, and a handover is recorded only when both it and the next company sign. For a financier: before paying, it will ask the Radox API which custodian last signed for the goods and how many signed handovers there are, and can recompute the whole history to check the answer. Separately, the open rail API on Stellar testnet (this repo's, not the Radox platform API) already lets anyone read a shipment and its history, and run a sandbox shipment, with no account or key: https://rio-miami-rail.vercel.app/docs.
```

## Challenges (optional; 1552 chars)

```text
1. Two companies, two machines, one transaction. A handover needs both custodians' signatures, and on protocol 29 each signs a Soroban authorisation entry with address-bound credentials (`sorobanCredentialsAddressV2`). Our first two-signer script crashed before submitting anything because js-stellar-sdk 17.3.0 returns plain objects, not accessor methods. We fixed it by signing each custodian's entry with `authorizeEntry` (`scripts/remote-auth.mjs`). Result: each company can sign with its own key on its own machine, exchanging only public keys and signed entries, as two teammates did for the second shipment (`proofs/three-machine.json`).
2. An AI reviewer agent found two defects before the testnet deploy: a route that revisits an address let `deliver` succeed with zero handovers, and the contract's storage lifetime was never extended, so it could have archived about a week after deploy, possibly during judging. Both were fixed with tests (commit `9b66e00`). Result: goods cannot be marked delivered before every handover is signed, and each write to a shipment extends its life to about 30 days.
3. History does not last on testnet: the RPC keeps events about seven days, and testnet resets about quarterly (next on 2026-12-16). We recompute each shipment's head from the transactions' own arguments on Horizon and commit Horizon copies of the proof transactions. Result: a buyer, insurer or lender can check a shipment's history later from public data without trusting us (`scripts/verify-head.mjs`: MATCH on every shipment in `proofs/`).
```

## What's next (optional; 1681 chars)

```text
Radox is a platform for tokenized real-world assets; its three Soroban contracts (token_sale, yield_distributor, maturity_settlement) run on Stellar mainnet since June-July 2026. Radox Rail, on Stellar testnet, is our next step from tokenized assets to goods in transit: it adds to a tokenized asset a record of who holds the goods, signed by both companies at each handover. We aim to grow it into a shared, SWIFT-like standard for custody of goods across trade corridors. Rio–Miami is our first corridor, not the product. Radox is part of the Rio–Miami trade-corridor initiative and its technology rail: every port, airport and chamber that joins it will join the rail, through one adapter to the Radox API. Radox is in conversations with chambers of commerce in Brazil and Miami.

Next: connect the rail to the Radox platform's physical-asset flow (a read-only Radox API endpoint already reads this registry in a local development run); let Stellar issuers run their own shipments on the rail, beyond the open testnet sandbox that is live now; run the first live shipment with a financial institution and a port or logistics operator; apply to SCF Build with this contract as its first milestone. The rail reaches mainnet after an audit and the issuer-account lock described in the README.

Business model: a recurring fee per connected institution plus a fee per shipment. It borrows the shape of SWIFT's published fee structure: Swift, a cooperative owned by its members, charges an entry fee, annual charges (including network connection) and network-usage fees on message traffic (swift.com billing rules, accessed 25 October 2026). We are not affiliated with Swift.
```

## Repository link (required, public HTTPS)

```text
https://github.com/pwsaragossy/rio-miami-rail
```

The repo is private (github.com returns 404 to a visitor, checked 26 Oct). It goes public only on Pedro's word; it is no longer automatic at 06:00 (Pedro, 26 Oct ~03:10 UTC).

## Project website link (optional)

```text
https://rio-miami-rail.vercel.app
```

The portal asks for llms.txt, robots.txt and sitemap.xml on this site. Production already serves all three (HTTP 200, same as page/ on main). The llms.txt there describes only the first shipment; a refreshed draft with the rail story, the spec and the four proof sets is in website-files/llms.txt. Pedro approved putting it live (26 Oct ~03:10 UTC). Landing v3 (branch landing-v3) is not approved, so the link stays on production.

## Video link (required, YouTube or Vimeo)

```text
{{VIDEO URL: central sends it after Pedro's upload}}
```

Blocker: the video is on hold by Pedro ("Vídeo ainda não"). Required field; the form cannot be submitted without it.

## Deck file (required, PDF/PPTX/PPT/HTML up to 20 MiB)

```text
{{UPLOAD: deck/radox-custody-rail.pdf}}
```

Pedro's choice: deck v14 (central, 26 Oct). Checked: 792,698 bytes (0.76 MiB, under 20 MiB), 11 pages, built 07:00 UTC; cover "Radox Rail", "SWIFT for goods in transit, on Stellar". Built by build_deck.py (python-pptx, converted to PDF with LibreOffice).

## Thematic track (optional, pick one)

```text
Stellar Unlocked
```

Pedro's choice (24 Oct). Check that the option is still in the portal list when pasting.

## Tech stack (optional, comma-separated, up to 25; 23 items)

```text
Stellar testnet, Soroban, Rust, soroban-sdk 29.0.1, wasm32v1-none, Cargo, Stellar CLI 28.1.0, Soroban authorization (require_auth), Stellar Asset Contract, Stellar RPC, Horizon, Friendbot, JavaScript, Node.js, npm, @stellar/stellar-sdk 17.3.0, HTML, CSS, Vercel, Vercel Functions, OpenAPI 3.1, soroban-sim (local mainnet fork), Radox transfer_agent (prior work)
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
