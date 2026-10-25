# Demo recordings (backup for DEMO-SCRIPT.md)

Recorded 2026-10-25 between 13:00 and 13:30 UTC, headless Chromium (Playwright 1.58.2), 1920x1080, 30 fps, H.264. The `.mp4` files stay out of git (about 16 MB); re-record with the commands below.
Each clip is cut to its row of DEMO-SCRIPT.md, so the editor lays the AI narration over them in order. No narration and no overlay are burned in: the lower third and the bottom label "Testnet - test keys - not real custodians" go on in the edit.

| File | Script row | Length | What it shows |
|---|---|---|---|
| 02-terminal-list.mp4 | 0:20-0:40 | 20 s | `jq` listing of the 7 lifecycle steps |
| 03-explorer-handover.mp4 | 0:40-1:05 | 25 s | stellar.expert tx 635c99ac (Warehouse to Port): summary 5 s, then the `handover(...)` call outlined in lime with the two custodian addresses GAJT…F3K2 and GCRB…SH4D, at the bottom of the frame |
| 03b-terminal-signers.mp4 | optional, inside 0:40-1:05 | 10 s | `node scripts/handover-signers.mjs`: for each handover and the deliver, the signed Soroban auth entries of both custodians, read from the saved envelopes |
| 04-explorer-cuts.mp4 | 1:05-1:25 | 20 s | attest 333792 (8 s), deliver 919def (8 s), handovers 56a0f0, ac268a, 5199d4 (1.33 s each) |
| 05-terminal-verify.mp4 | 1:25-1:50 | 25 s | `verify-head.mjs` output ending MATCH, then `echo $?` = 0 |
| 06-explorer-redeem.mp4 | 1:50-1:58 | 8 s | tx 864fd164, `redeem(...)` call outlined (Radox transfer_agent, prior work) |
| 06b-terminal-balance.mp4 | 1:58-2:15 | 17 s | holder balance `"0"` |
| 08-page-live.mp4 | 2:30-3:00 | 30 s | https://rio-miami-rail.vercel.app at 225% zoom (150% of a 1280 frame): top, "Live from Stellar testnet" and state, history, click "Verify head" at 20 s, MATCH held to the end |
| 09-page-snapshot.mp4 | fallback for 2:30-3:00 | 30 s | same take with horizon-testnet and soroban-testnet blocked: "Snapshot, not live: testnet could not be reached", then MATCH against the saved head |

Row 2:15-2:30 (GitHub README) is not recorded: the repo is private until submission.

## What is real and what is replayed

- Explorer and page clips are live captures of the public sites. The page clips (08, 09) show the page before rio-miami-rail commit be4bcb9; re-record them after that commit is deployed (it adds the transfer_agent prior-work line, the assurance level per handover and the self-hosted SDK).
- The terminal clips replay real output: the four commands ran at the time in `tools/term-time.txt` from the rio-miami-rail commit in `tools/term-commit.txt`, and their output is in `tools/t1.txt` to `tools/t4.txt`. Each terminal clip carries the caption "Recorded output, replayed · run <time>" in its corner, so the video discloses it on screen. Commands are shown in full; only the per-step heads of verify-head are shortened for width.
- Signatures: stellar.expert's "Signatures" box lists only the envelope signature of the transaction source (the operator). The custodians sign Soroban authorization entries inside the call, which the explorer does not list. The explorer clips therefore end with the outlined call at the bottom of the frame; only the "Signatures" heading shows under it, never its entry. Proof of both custodian signatures is clip 03b (`scripts/handover-signers.mjs`, rio-miami-rail commit 5069654, exit 1 if any is missing).
- Zoom: the page is shown at 225% of a 1920 px frame, which equals the script's 150% of a 1280 px frame; the explorer at 187.5% (= 125%).

## Re-record

```sh
PW=~/.npm/_npx/ec0ab2283efe73f6/node_modules/playwright-core node tools/record.cjs "$PWD"          # explorer + page clips
PW=~/.npm/_npx/ec0ab2283efe73f6/node_modules/playwright-core node tools/term.cjs "$PWD" "$PWD/tools" # terminal clips
```

`record.cjs` takes clip names to record only some (for example `08-page-live`). It fails if the page source line does not say what the take expects.
