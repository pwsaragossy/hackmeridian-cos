# Review: CUSTODY-STANDARD.md + README/AI_USAGE diffs (2026-10-25)

Verdict: APPROVE WITH CHANGES. No blocker. Rules in sections 3-6 match lib.rs; all hashes reproduce.

## Verified
- Own script (scratchpad/v.mjs, stellar-sdk, not verify-head): offline vector (key, open, handover) and all 4 live heads equal the table. Address XDR layout and lengths (44/40 bytes) correct. `PROOF_FILE=... verify-head.mjs` prints MATCH, on-chain head d9cf3a5f...614d.
- All shortened tx hashes, addresses (GAVDGEJF...5UTZ, GDWNU6TT...TPPW, GAUKDWMR...CEFR, GD54SSZG...2CO4, GDL4562Q...WBSK) match proofs/three-machine.json.
- Auth, pause set (open/handover/attest/deliver/add_source/remove_source blocked; freeze/unfreeze/pause/resume/set_pauser/emergency_pause not), statuses, seq in formulas, error codes 1-13: all match lib.rs.
- No Claude/Anthropic in README or spec. No partner/mentor/chamber/port named. No "document of title" claim (only negated).

## Findings
1. MEDIUM, framing. File name CUSTODY-STANDARD.md and link text contradict "It is not a standard".
   Replace: rename to `CUSTODY-SPEC.md`; update README (2 links) and AI_USAGE row.
2. LOW, framing. README: "nobody has adopted it yet" implies expected adoption.
   Replace: "no one has adopted it".
3. MEDIUM, unchecked claim. Section 2: "Holder | token holder at delivery". `deliver` only requires auth from any address; it never checks the token balance.
   Replace: "Holder | address named at delivery; it co-authorises. The contract does not check that it holds the token".
4. MEDIUM, implementer gap. Section 5: "Each event has the shipment `key` as its topic."
   Replace: "Each event has two topics: the event name as a snake_case symbol (for example `handover`), then the shipment `key`. Data fields are as listed, in this order." (Confirm map-vs-vec data encoding against a real event before saying more.)
5. LOW, gap. Section 6 after `addr(x)`: add "`key`, `docs_root`, `evidence_hash`, `event_hash` are raw 32 bytes, not hex text. Only `G...` and `C...` addresses occur; muxed `M...` addresses are not accepted."
6. LOW, hedge. Section 5: "Stellar RPC keeps events for about 7 days".
   Replace: "Stellar RPC keeps events only for a limited window (often 7 days or less, depending on the provider)".
7. LOW. Section 8: "produces heads that `verify-head` ... can recompute" holds only if function names and argument order match this contract.
   Replace: "...and exposes the same function names and argument order, produces heads that `verify-head` can recompute from transaction history."
