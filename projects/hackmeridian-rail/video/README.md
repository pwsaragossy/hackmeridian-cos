# Demo recordings (backup for DEMO-SCRIPT.md)

Recorded 2026-10-25 around 13:00 UTC, headless Chromium (Playwright 1.58.2), 1920x1080, 30 fps, H.264. The `.mp4` files stay out of git (about 16 MB); re-record with the commands below.
Each clip is cut to its row of DEMO-SCRIPT.md, so the editor lays the AI narration over them in order. No narration and no overlay are burned in: the lower third and the bottom label "Testnet - test keys - not real custodians" go on in the edit.

| File | Script row | Length | What it shows |
|---|---|---|---|
| 02-terminal-list.mp4 | 0:20-0:40 | 20 s | `jq` listing of the 7 lifecycle steps |
| 03-explorer-handover.mp4 | 0:40-1:05 | 25 s | stellar.expert tx 635c99ac (Warehouse to Port): summary 5 s, then the `handover(...)` call outlined in lime with the two custodian addresses GAJT…F3K2 and GCRB…SH4D |
| 04-explorer-cuts.mp4 | 1:05-1:25 | 20 s | attest 333792 (8 s), deliver 919def (8 s), handovers 56a0f0, ac268a, 5199d4 (1.33 s each) |
| 05-terminal-verify.mp4 | 1:25-1:50 | 25 s | `verify-head.mjs` output ending MATCH, then `echo $?` = 0 |
| 06-explorer-redeem.mp4 | 1:50-1:58 | 8 s | tx 864fd164, `redeem(...)` call outlined |
| 06b-terminal-balance.mp4 | 1:58-2:15 | 17 s | holder balance `"0"` |
| 08-page-live.mp4 | 2:30-3:00 | 30 s | https://rio-miami-rail.vercel.app at 225% zoom (150% of a 1280 frame): top, "Live from Stellar testnet" and state, history, click "Verify head" at 20 s, MATCH held to the end |
| 09-page-snapshot.mp4 | fallback for 2:30-3:00 | 30 s | same take with horizon-testnet and soroban-testnet blocked: "Snapshot, not live: testnet could not be reached", then MATCH against the saved head |

Row 2:15-2:30 (GitHub README) is not recorded: the repo is private until submission.

## What is real and what is replayed

- Explorer and page clips are live captures of the public sites.
- The terminal clips replay real output: the three commands ran at 2026-10-25T12:59:47Z from rio-miami-rail commit 262ab17, and their output is in `tools/t1.txt` to `tools/t3.txt`. The clips type the command and print that output at a fixed pace; hashes in the verify-head per-step lines are shortened for width, the recomputed and on-chain heads are shown in full. If the video must show a live terminal, record it by hand.
- The explorer's "Signatures" section shows only the operator (the transaction source). The two custodian signatures of each handover are Soroban authorization entries in the envelope, which stellar.expert does not list; the 635c99ac envelope holds two signed address credentials, GAJT…F3K2 (warehouse) and GCRB…SH4D (port). That is why clip 03 frames the call arguments and never the Signatures box.

## Re-record

```sh
PW=~/.npm/_npx/ec0ab2283efe73f6/node_modules/playwright-core node tools/record.cjs "$PWD"          # explorer + page clips
PW=~/.npm/_npx/ec0ab2283efe73f6/node_modules/playwright-core node tools/term.cjs "$PWD" "$PWD/tools" # terminal clips
```

`record.cjs` takes clip names to record only some (for example `08-page-live`). It fails if the page source line does not say what the take expects.
