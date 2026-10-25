# For Leo's agent — setup, then everything Leo's side does today

Internal: contains Radox-internal references. Never copy into rio-miami-rail.

You are the agent working for Leo (leo-schlanger) on HackMeridian 2026, project hackmeridian-rail.
Written by Pedro's project session (session-hackmeridian-rail) on 2026-10-25 11:05 UTC. Leo's agents
do all of the work below; Leo only does what an agent cannot (a login, a 2FA code). Pedro's session
**confirms** every checkpoint from what you push, so each step ends with a line you push to the board.

How we talk: this file is my side; **your side is the card** `board/Leo contract and testnet proofs.md`
in this repo. Append dated lines under "## Sunday" (`- HH:MM UTC (leo-agent): …`, with the evidence:
command output, tx hash, commit). Never message Pedro; a question goes on the card with
`status: waiting-owner`. Lisbon = UTC today.

Read this file now with:
`gh api repos/pwsaragossy/hackmeridian-cos/contents/projects/hackmeridian-rail/LEO-SETUP.md --jq .content | base64 -d`

## A. Setup (target: done by 11:45 UTC)

1. `gh auth status` shows leo-schlanger. If not: `gh auth login` (Leo's login, the one human step).
   Then `gh auth setup-git` (so `git clone` of the private repos works) and check
   `gh api repos/pwsaragossy/hackmeridian-cos --jq .permissions.push` prints `true`; a 404 or `false`
   means the collaborator invite is not accepted: error on the card, stop.
2. The chief-of-staff plugin is installed (Leo did this). Find its script:
   `v=$(ls ~/.claude/plugins/cache/chief-of-staff/chief-of-staff/ | sort -V | tail -1)`.
   `~/hackmeridian` must be missing or empty (`ls -A ~/hackmeridian`); if it holds something that is
   not this workspace, `mv ~/hackmeridian ~/hackmeridian.old` first.
3. Connect the shared workspace (board, projects, library; it syncs at every session start and turn end):
   `sh ~/.claude/plugins/cache/chief-of-staff/chief-of-staff/$v/scripts/setup.sh join ~/hackmeridian https://github.com/pwsaragossy/hackmeridian-cos.git --member leo`
   Pass = `~/hackmeridian/projects/hackmeridian-rail/LEO-BRIEF.md` exists.
4. Git identity for the code (no history rewrite later, so do it before the first commit):
   `gh api user --jq '"\(.id)+\(.login)@users.noreply.github.com"'` → set it with
   `git config --global user.email <that>` and `git config --global user.name leo-schlanger`.
5. Clone the code repo **outside** the workspace: `git clone https://github.com/pwsaragossy/rio-miami-rail ~/code/rio-miami-rail`.
   It already has Pedro's `page/` commits; your work goes in `contracts/`, `scripts/`, `proofs/`.
6. Toolchain: check `stellar --version` (expect 28.1.0), `rustup --version`, `node --version` (≥ 20).
   Install what is missing: Rust with `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y; . ~/.cargo/env`;
   then `rustup target add wasm32v1-none`; Node and the CLI with `brew install node stellar-cli`
   (Homebrew's stellar-cli is 28.1.0, checked 2026-10-25 11:10 UTC).
7. Append your line under `## Sunday` in `~/hackmeridian/board/Leo contract and testnet proofs.md`
   (the workspace pushes it at turn end): `- HH:MM UTC (leo-agent): setup done — workspace ok, email <noreply>, stellar <v>, node <v>, rio-miami-rail cloned at <commit>`.
   If any step fails: the exact error on the card, then stop that step.

## B. The work — all in [LEO-BRIEF.md](LEO-BRIEF.md)

Open a Claude Code session in `~/hackmeridian/projects/hackmeridian-rail` and give it LEO-BRIEF.md as
its first instruction. Its hard rules hold (no secrets in git, no partner names, AI_USAGE.md, small
commits, Apache-2.0 LICENSE in the first commit, Stellar facts looked up live).

Times moved because we start late (the 18:00 stop line and the 16:00 alarm do not move):

| By (UTC) | What | Line you push to the card (Pedro's session checks it) |
|---|---|---|
| 11:45 | A. setup | setup line above |
| 12:00 | Brief Step 0: hello contract on testnet | CLI version, sdk version, tx hash, and whether Horizon `parameters[1]` is the function name |
| 12:45 | Two-signature spike (two `require_auth`, two `authorizeEntry`) | tx hash, or the exact error |
| 13:30 | Brief Step 0b: transfer_agent spike | "register_token auth: …; redeem auth: …; set_admin before register_token: yes/no; trustline auth: issuer flag / set_authorized" + hashes |
| 14:00 | Contract + unit tests (`cargo test` green, `head` test vector), first commits in rio-miami-rail | commit hash; a mentor or the plugin reviewer reads the contract |
| 16:00 | **Alarm**: a dual-signed `handover` SUCCESS on testnet | tx hash, or say at once it is not there |
| 18:00 | **Stop line**: 7 lifecycle hashes in `proofs/lifecycle.json` pushed to `main` | "check.py should be 7/7" |
| after 18:00 | Failure branches, `scripts/verify-head.mjs <key>` exit 0 | output |

## C. What Pedro's session confirms (so you know what counts)

- Setup: your card line, and your commits appearing in this repo.
- Every tx hash: looked up on `https://horizon-testnet.stellar.org/transactions/<hash>` (must be `successful: true`).
- Code: the rio-miami-rail commit history (first contract commit after Sun 09:00, LICENSE present, no `S…` secret: `grep -rE "S[A-Z2-7]{55}"` empty).
- Target: `python3 check.py` in this folder reads `proofs/lifecycle.json` from rio-miami-rail `main` and must exit 0 (7 distinct SUCCESS hashes).
- `node scripts/verify-head.mjs <key>` exits 0 on a fresh clone.

A line without evidence counts as not done.
