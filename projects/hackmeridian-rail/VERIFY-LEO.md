# VERIFY-LEO: independent check of Leo's agent claims (card lines 11:10 to 12:01 UTC)

- Repo HEAD verified: 79306469bf35bf9579027c90991f76f8c4b42ba8 (fresh clone of github.com/pwsaragossy/rio-miami-rail, 11 commits, all branches)
- Time: Sun 2026-10-25 12:17 UTC (clone) to about 12:25 UTC
- Who: engineer subagent of session-hackmeridian-rail. Nothing pushed, no transaction sent, no repo file edited.

## a. Contract exists on testnet: PASS
`stellar contract info interface --id CCBJVXMJ...H4LII --network testnet` lists: open, handover, attest, deliver, freeze, unfreeze, pause, resume, emergency_pause, set_pauser, is_paused, add_source, remove_source, head, get, version, __constructor. DEPLOYMENTS.md line 7 names the same ID.

## b. Lifecycle proof: PASS
7 entries in order open, handover x4, deliver, redeem; 7 distinct hashes (`sort -u | wc -l` = 7). Horizon `/transactions/<hash>` `.successful` = true for all 7. `/operations` parameters[0] decoded (ScVal): open, 4 handovers and deliver call CCBJVXMJ... (the registry); redeem calls CAYD3EFT...SJWH, equal to `transfer_agent_instance` in the proof file. Function names (parameters[1]) match the step names.

## c. Holder balance after redeem: PASS
`stellar contract invoke --id CBCWTIT5...Q22Z (token) --network testnet --source-account alice --send=no -- balance --id GBPFJMZ7...RIIGDJ (holder)` returns `"0"`. Simulation only, local key "alice" used as source, no tx sent.

## d. Failures: PASS
9 entries, matches the card: wrong_custodian Contract #1; out_of_route #2; wrong_signer Auth InvalidAction; early_delivery #10; bad_assurance #13; duplicate_key #4; after_freeze #7; while_paused #6; unknown_source #5. All recorded as `hash_or_sim: simulation` (refusals, not on-chain txs). Not re-run by me: I checked the file, not that each refusal reproduces.

## e. cargo test: PASS
`cargo test` in the clone: `24 passed; 0 failed` (exit 0). Matches the card's 24.

## f. verify-head: PASS
`npm ci` exit 0. `node scripts/verify-head.mjs 31b4cff7...5e37`: exit 0; last lines `recomputed 2d74fec0...5414`, `on-chain 2d74fec0...5414`, `MATCH`. Same head as `shipment.final_head` in the proof file.

## g. Secrets re-scan: PASS

### Secrets re-scan
HEAD 79306469bf35bf9579027c90991f76f8c4b42ba8, fresh clone, 12:2x UTC 2026-10-25.
- Tree: `grep -rnE "S[A-Z2-7]{55}" --exclude-dir=.git --exclude-dir=target --exclude-dir=node_modules .` returned 0 matches.
- History: `git log -p --all | grep -cE "S[A-Z2-7]{55}"` returned 0 (11 commits, all refs).
- Names: `grep -rniwE "ZIS|Paulo|Protasio|Protásio|CISBRA|CAERJ|Camacol|OAS|RITLA|Glocal|UpShift|radox-internal|CAF4JIUZ"` over the tree returned 0 matches; same terms (case-insensitive, subset) over `git log --all -p` returned 0.
- `.env`: `git check-ignore -v .env` gives `.gitignore:3:.env`; no .env file in the clone.
- No secret values were printed.
Limit: the regex catches Stellar secret seeds (S + 55 base32) only; other credential formats were not scanned.

Overall verdict: PASS. Every checked claim (a to g) was confirmed from the chain or the fresh clone; the only unreproduced items are the individual refusal simulations in d.
