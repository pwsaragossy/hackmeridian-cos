# Brief for Vhendala — supervise HackMeridian rail from the panel

Paste this whole file as the first prompt of Vhendala's Claude Code session, opened in `~/hackmeridian/central` after the setup below. Written by Pedro's central on 2026-10-25.

## Setup (once)
1. Accept both GitHub invites (rio-miami-rail and hackmeridian-cos) at github.com/notifications.
2. In Claude Code: `/plugin marketplace add pwsaragossy/chief-of-staff`, then `/plugin install chief-of-staff@chief-of-staff`.
3. `setup.sh join ~/hackmeridian https://github.com/pwsaragossy/hackmeridian-cos.git --member vhendala`.
4. Open a session in `~/hackmeridian/central` and run `/chief-of-staff:panel`.

## How the connection works
- The team board repo (hackmeridian-cos) is the shared state: cards in `board/`, `projects/hackmeridian-rail/STATE.md`, the library in `knowledge/`. Every turn end syncs it, so Pedro's central, Leo's sessions and yours see the same cards.
- Your central asks you only the cards with `member: vhendala`. Pedro's central asks Pedro; Leo's asks Leo.
- Something red or stuck: write one line on the card it belongs to (or on `board/HackMeridian rail.md`). Pedro's central reads it and acts. Do not message Pedro or Leo outside the cards for project decisions.

## What you supervise
- The panel: red = a gate or protocol problem, yellow = waiting on someone. Check it at 09:00, 14:00, 18:00 (Leo's stop line), 22:00 and Mon 06:00.
- Leo's checkpoints on his card: 09:00 wasm check, 14:00 redeem path on testnet, 18:00 seven lifecycle hashes on main (`python3 projects/hackmeridian-rail/check.py` prints the count).
- The public page https://rio-miami-rail.vercel.app opens logged out.
- Manual product review: read the page, deck, video and README as a judge would ([REVIEW-1.md](REVIEW-1.md), [SUBMISSION.md](SUBMISSION.md)).
- Your own items: video account and test clip, team photo, narration (your card "Vhendala video and team photo").

## Rules
- You do not change code in rio-miami-rail.
- No legal work during the hackathon.
- The submission is Pedro's OK on Mon 08:00; nobody else checks the terms box or submits.
