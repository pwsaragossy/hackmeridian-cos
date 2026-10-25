# Demo recordings (backup for DEMO-SCRIPT.md)

Recorded 2026-10-25 between 13:00 and 13:30 UTC, headless Chromium (Playwright 1.58.2), 1920x1080, 30 fps, H.264. The clips live outside the workspace, in `~/Movies/hackmeridian-rail-video/` on Pedro's Mac (the workspace turn-end sync sends every file under ~/hackmeridian to the team repo and ignores .gitignore, so large or private media cannot stay here). Re-record with the commands below, run from this folder with the output folder as argument.
Each clip is cut to its row of DEMO-SCRIPT.md, so the editor lays the AI narration over them in order. No narration and no overlay are burned in: the lower third and the bottom label "Testnet - test keys - not real custodians" go on in the edit.

| File | Script row | Length | What it shows |
|---|---|---|---|
| 02-terminal-list.mp4 | 0:20-0:40 | 20 s | `jq` listing of the 7 lifecycle steps |
| 03-explorer-handover.mp4 | 0:40-1:05 | 25 s | stellar.expert tx 635c99ac (Warehouse to Port): summary 5 s, then the `handover(...)` call outlined in lime with the two custodian addresses GAJT…F3K2 and GCRB…SH4D, at the bottom of the frame |
| 03b-terminal-signers.mp4 | optional, inside 0:40-1:05 | 10 s | `node scripts/handover-signers.mjs`: for each handover and the deliver, the signed Soroban auth entries of both custodians, read from the saved envelopes |
| 03c-page-shipment-2.mp4 | 0:40-1:05, after 03b (replaces 03c-terminal-signers-3m.mp4, same 119 frames, 3.97 s) | 4 s (119 frames) | Held still of https://rio-miami-rail.vercel.app/#shipment-2 (deploy of rio-miami-rail cbd0dd3, captured 2026-10-25 17:14 UTC, source line "Live from Stellar testnet") at 150% zoom: the Handovers list with both keys per row (Warehouse → Leo GAVD…5UTZ + GDWN…TPPW, Leo → Vhendala GDWN…TPPW + GAUK…CEFR, Vhendala → Recipient, deliver) and "Verify head" already clicked, MATCH d9cf3a…a9614d from 5 transactions; the three handovers with Leo or Vhendala are outlined in lime. A still because the frame does not move. In the edit it carries the label "Testnet - test keys - not real custodians" and the caption "Public page, captured 2026-10-25 17:14 UTC"; do not say "live" over it. The earlier terminal take (`PROOF_FILE=proofs/three-machine.json node scripts/handover-signers.mjs`, `t6.txt`) stays in the folder as a spare. |
| 04-explorer-cuts.mp4 | 1:05-1:25 | 20 s | attest 333792 (8 s), deliver 919def (8 s), handovers 56a0f0, ac268a, 5199d4 (1.33 s each) |
| 05-terminal-verify.mp4 | 1:25-1:50 | 25 s | `verify-head.mjs` output ending MATCH, then `echo $?` = 0 |
| 06-explorer-redeem.mp4 | 1:50-1:58 | 8 s | tx 864fd164, `redeem(...)` call outlined (Radox transfer_agent, prior work) |
| 06b-terminal-balance.mp4 | 1:58-2:15 | 17 s | holder balance `"0"` |
| 08-page-live.mp4 | 2:30-3:00 | 30 s | https://rio-miami-rail.vercel.app (deploy of rio-miami-rail 54dc401, recorded 2026-10-25 14:50 UTC) at 225% zoom (150% of a 1280 frame): label and title from 0 s, the "Live from Stellar testnet" line, state and assurance per handover on screen by 7 s; page under the 08b overlay 8-15 s; "Verify head" in view at 15 s, click at about 16 s, MATCH on screen from 16.2 s (2:46.2) and held to the end |
| 08b-terminal-radox-api.mp4 | 2:38-2:45, over 08 | 7 s | Replay of the Radox backend response recorded in `API-PROOF.md` ("Full backend boot", 2026-10-25 13:23 UTC; backend not run for the clip): `curl -s …/api/custody/shipments/31b4…5e37 | jq .` with `"status": "Delivered"` and `"head": "2d74fec0…95414"` highlighted; caption "Radox backend (private), local test run · recorded output, replayed · 2026-10-25 13:23 UTC". `t5.json` is that response body. |
| 09-page-snapshot.mp4 | fallback for 2:30-3:00 | 30 s | same take and timing with horizon-testnet and soroban-testnet blocked: "Snapshot, not live: testnet could not be reached", then MATCH against the saved head |

Row 2:15-2:30 (GitHub README) is not recorded: the repo is private until submission.

## What is real and what is replayed

- Explorer and page clips are live captures of the public sites. The page clips (08, 09) show the page before rio-miami-rail commit be4bcb9; re-record them after that commit is deployed (it adds the transfer_agent prior-work line, the assurance level per handover and the self-hosted SDK).
- The terminal clips replay real output: the four commands ran at the time in `tools/term-time.txt` from the rio-miami-rail commit in `tools/term-commit.txt`, and their output is in `tools/t1.txt` to `tools/t4.txt`. Each terminal clip carries the caption "Recorded output, replayed · run <time>" in its corner, so the video discloses it on screen. Commands are shown in full; only the per-step heads of verify-head are shortened for width.
- Signatures: stellar.expert's "Signatures" box lists only the envelope signature of the transaction source (the operator). The custodians sign Soroban authorization entries inside the call, which the explorer does not list. The explorer clips therefore end with the outlined call at the bottom of the frame; only the "Signatures" heading shows under it, never its entry. Proof of both custodian signatures is clip 03b (`scripts/handover-signers.mjs`, rio-miami-rail commit 5069654, exit 1 if any is missing).
- Zoom: the page is shown at 225% of a 1920 px frame, which equals the script's 150% of a 1280 px frame; the explorer at 187.5% (= 125%).

## Re-record

```sh
OUT=~/Movies/hackmeridian-rail-video
PW=~/.npm/_npx/ec0ab2283efe73f6/node_modules/playwright-core node tools/record.cjs "$OUT"            # explorer + page clips
PW=~/.npm/_npx/ec0ab2283efe73f6/node_modules/playwright-core node tools/term.cjs "$OUT" "$PWD/tools"  # terminal clips
```

`record.cjs` takes clip names to record only some (for example `08-page-live`). It fails if the page source line does not say what the take expects.

## Narration voice (Voicebox, local)

- Profile "Pedro (cloned, rail video)" in a Voicebox data folder at `~/Movies/hackmeridian-rail-video/voicebox-data/` (not the app's default folder). Start the server on it with `/Applications/Voicebox.app/Contents/MacOS/voicebox-server --host 127.0.0.1 --port 17493 --data-dir ~/Movies/hackmeridian-rail-video/voicebox-data`, then `POST /generate` with the profile id, `engine: qwen`, `model_size: 1.7B`.
- Reference sample: 18.6 s cut from `~/Movies/FINAL youtube.mp4` (0.2-18.8 s, Pedro narrating the Agent Pay demo in English), with its transcript. Nothing was uploaded; the model runs on the Mac (mlx-community/Qwen3-TTS-12Hz-1.7B-Base-bf16).
- Test line: `~/Movies/hackmeridian-rail-video/voice-test-15s.wav`, 12.6 s, the first three sentences of row 0:00; a local transcription reads back the exact words. About 177 words per minute, so the 325-word script runs about 1:50 of speech inside 3:00.
- Full narration (DEMO-SCRIPT.md at e1059c0; row 0:00 re-taken 17:29 UTC with the reviewed problem numbers, seed 23, 16.4 s, "11%" and "DCSA" passed to the voice as "eleven percent" and "D C S A"; row 1:05 regenerated 2026-10-25 14:31 UTC, row 2:30 at 14:45 UTC, row 0:40 at 16:20 UTC and again at 17:19 UTC with the 'by their account' hedge, seed 42, 23.4 s, speech 40.3-63.4 s in the mix): one wav per row in `~/Movies/hackmeridian-rail-video/narration/` (01-000 to 08-230; speech 16.4, 12.0, 23.4, 13.4, 12.2, 13.9, 11.9, 25.5 s, each inside its row) and `~/Movies/hackmeridian-rail-video/narration-full-3m00.wav` (180.0 s, each row placed at its start time, loudness -16.7 LUFS, peak -1.5 dB; silencedetect shows speech starting at 0, 20, 40, 65, 85, 110, 135 and 150 s). Made with `tools/narrate.py`, then mixed with ffmpeg `adelay` per row (an earlier mix that used a 1-indexed zsh array shifted every row one slot early and was rebuilt); the identifiers are spoken as words (custody registry, require auth, the container number digit by digit). A local transcription (parakeet-mlx) of every row reads back the script; the only differences left are the transcriber's spellings (authorize, Soroban read as "Sorob and" or "Sorobank", README as "RIDME"); an independent reviewer re-transcribed every window of the final mix and approved it. Row 2:30 by local transcription timestamps: "the Radox backend reads the same record…" at 2:38.6-2:43.5 (inside the 08b clip), "Verify head: match" at 2:54.5-2:56.2, after the click at about 2:47.
- Disclosure for the video credit, deck and README: "Narration: AI voice generated from Pedro's voice" (the DEMO-SCRIPT.md lower third; use this one string everywhere; Voicebox can be named in the README credits).

## Assembled cut

`tools/assemble.cjs <outdir> <rio-miami-rail clone>` writes `rail-demo-3m00.mp4` (180 s, 5400 frames): the clips in DEMO-SCRIPT row order under `narration-full-3m00.wav`. Row 0:40 is 03 (first 331 frames) + 03b + 03c; row 1:50 is 06 + 06b; row 2:15 is the README rendered by GitHub's markdown API from rio-miami-rail origin/main (three sections, 5 s each, captioned with the commit and "repo private until submission"; replace with a GitHub capture once the repo is public); row 2:30 is 08 0-8 s, 08b, 08 from 15 s, captioned "Public page, recorded … UTC" (08's recording time) and 08b's replay caption repeated in the strip. Row 0:40 after the independent review: 03 9 s, the last 5 s of 03b, then 03c held from 0:54 to 1:05 under the sentence about the teammates. The picture is scaled to 94% so the overlays sit in a 64 px strip at the bottom: the label for the whole video, the AI-voice lower third 0:00-0:08, the source line 0:08-0:20 (read from the 0:00 row of DEMO-SCRIPT.md), and the captions on 03c and the README row.

Offline copy: `~/Movies/hackmeridian-rail-video/final/rail-demo-3m00-2026-10-25-1741Z.mp4` with its `.sha256`, byte-identical to `rail-demo-3m00.mp4` at that time.
