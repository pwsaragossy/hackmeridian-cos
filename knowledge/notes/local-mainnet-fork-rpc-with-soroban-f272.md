---
id: local-mainnet-fork-rpc-with-soroban-f272
title: "Local mainnet fork RPC with soroban-sim serve"
type: howto
status: active
origin: hackmeridian-rail
provenance: agent
confidence: high
sources: ["github.com/theahaco/soroban-sim README and docs/rpc-facade.md (2026-10-25)", "run on Pedro's Mac 2026-10-25 ~23:30 WET"]
created: 2026-10-25
updated: 2026-10-25
review_by: 2027-04-25
group:
aliases: []
tags: [stellar, soroban, rpc, mainnet, testing]
---
# Local mainnet fork RPC with soroban-sim serve

`soroban-sim` (crates.io `soroban-sim-cli` 0.1.0, by theahaco) runs a local Stellar RPC that forks mainnet. It reads the real mainnet state lazily from https://mainnet.sorobanrpc.com, applies our transactions only locally, and never sends anything to the network. It runs protocol 29, the same as testnet today ([[soroban-versions-on-2026-10-25-9619]]).

Steps, verified 2026-10-25:
1. `cargo install soroban-sim-cli --locked` (about 1 min on this Mac; binary in `~/.cargo/bin/soroban-sim`).
2. `cd ~/.soroban-sim && soroban-sim serve --fork mainnet --report rehearsal` prints "fork of mainnet at ledger 65136929 (protocol 29)" and listens on 127.0.0.1:8000.
3. Point tools at it: `STELLAR_RPC_URL=http://127.0.0.1:8000`, `STELLAR_NETWORK_PASSPHRASE="Public Global Stellar Network ; September 2015"`, plus `STELLAR_CONFIG_HOME=~/.soroban-sim/config STELLAR_DATA_HOME=~/.soroban-sim/data` so that only throwaway keys are reachable.
4. Fund a throwaway key: `stellar keys generate rehearsal`, then the JSON-RPC `fork_setBalance {account, xlm}` (there is no friendbot).
5. Evidence: `stellar contract invoke` on the native XLM contract CAS3J7GY…OWMA returned `symbol` "native" and the real mainnet balance of GAAZI4TC…CWN7 (994338384 stroops). A `transfer` of 1 XLM came back Success, the balance read back as 1004338384 on the fork only, and `fork_report` gave passed True with no failures.

Gotchas: the stellar CLI prints a stellar.expert link for the transaction hash, but that transaction does not exist on mainnet. On a mainnet fork, an envelope signed by a real mainnet signer is refused (error -32001), so to act as a real account you use `fork_addSigner` with a throwaway key. Browsers cannot call it: any request with an Origin header gets 403. Not served: getLedgers, getTransactions, classic operations and history before the fork. To deploy our own wasm on mainnet state, the same `stellar contract deploy` works against it. The Radox backend read pattern in [[serve-a-read-only-soroban-contract-1aab]] can point at this URL for local tests.

Compared: [[serve-a-read-only-soroban-contract-1aab]] coexists (that note is the backend read view, this one is a local mainnet RPC tool)

