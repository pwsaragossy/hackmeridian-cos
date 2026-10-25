# Scope freeze — proof for the track item `scope`

Owner's OK, recorded with track.sh on 2026-10-25 01:26: "Sim, inclui a página pública do embarque
como terceira entrega obrigatória; a ligação com a API fica como quarta condicional."

Must-haves (3), full text in IDEA.md "Scope":
1. `custody_registry` + tests, deployed on testnet (Leo's agents, LEO-BRIEF.md).
2. Lifecycle harness with the 7 txs + `verify-head` + failure branches (Leo's agents).
3. Public read-only shipment page reading the contract on testnet (Pedro's sessions).

Conditional 4th: the Radox API connection, cut if no dual-signed handover runs on testnet by
Sun 25 Oct 18:00 Lisbon (owner's stop criterion, STATE.md §2).

Cut: TokenSale escrow / DvP (prior work), passkey signing in a phone UI, event-source adapters, the USD leg.

Time boxes (clock times, Lisbon = UTC): LEO-SETUP.md §B and KICKOFF.md §5; 16:00 alarm and 18:00
stop line for the dual-signed handover; submit Mon 26 Oct 08:00 (portal closes 12:00 WET).
