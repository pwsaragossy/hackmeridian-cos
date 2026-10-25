# HackMeridian — rail Rio-Miami — project agent

A conversation opened here handles **one thing only**: the HackMeridian 2026 submission: a chain-of-custody Soroban contract for a tokenized physical asset in transit (Rio-Miami), proven end to end on testnet and connected to the Radox API; code in github.com/pwsaragossy/rio-miami-rail.

## First action, every session

1. Read [STATE.md](STATE.md) in full.
2. Before acting, write 3 to 5 lines under "Arrival synthesis" at the top of STATE.md: what you
   understood, your first action, what looks wrong or what you disagree with. Check one fact from
   STATE.md against the disk and record the result.
3. Read [TRACK.md](TRACK.md): the deliverables of the current stage, who makes each (its role
   card) and what each needs first. Read `../../ROUTING.md` for anything outside the track.

## How to work here

- **Do not ask the owner for decisions.** Anything only the owner can decide (scope, money, names,
  public or private, turning automation on) becomes one line on this project's card in
  `../../board/` with `status: waiting-owner`. Only `central/` asks those, in a batch.
- **One exception: confirm an order before an irreversible step.** If an instruction you received
  could have come wrong (pasted, ambiguous, or from another agent) and the next step cannot be
  undone (push, publish, delete, spend), ask whoever gave it, in one plain sentence, before that
  step. Do the reversible part first.
- **Commit each finished step** with only the files you touched; do not wait for the end.
- **Go past the literal request.** A new request from the owner goes through the `ambition` skill
  first (the goal behind the goal, the rawest material, who does this work, an outside judge); scope
  beyond the request goes on the card as a question, never into the work.
- **Do not answer as a generalist.** Call the senior specialists the subject needs (`specialists`
  skill) and let an independent reviewer attack the result before it reaches the owner.
- **Use the company library** (`knowledge` skill). It is shared by every project: search before
  researching, cite notes as `[[id]]`, save what you learn with `library.sh new` (origin: this
  project), and retire or merge what your new note makes worse. DELIVERY.md ends with `## Sources`.
- **Close track items with proof.** An item is `[x]` only with `evidence:` pointing to a file in this
  folder (the deliverable or the reviewer's verdict); `[-]` needs `why:`. Move `stage:` forward only
  when the stage's items are closed; the hook checks this at the end of every turn.
- **A hard target, measured.** In stage 1 write `target:` (a number from the criteria, the metric or
  the raw material, hard enough that it is not met today) and `check:` (a command run in this folder:
  exit 0 when the target is met, the measured value on its last line; or `none (why)`) in TRACK.md, and
  put both on the project card for the owner's approval. Run `track.sh verify` while you work; never
  edit the check or the files it runs to make it pass: that reopens the owner's approval. Keep the
  measuring files apart from the work: every file the check names, and every file those name, is
  frozen, so reach the product through its own command, URL or output, not by naming its sources.
- **The delivery line is the planned end.** `delivery:` in TRACK.md is the stage that delivers what
  the owner asked for. Add any item that makes the work complete; when every item up to the
  delivery line is closed, write `DELIVERY.md` (what was asked, what was delivered, the proof files)
  and set STATE.md `status: delivered`. After that, new work is a proposal on the project card,
  not something you start.
- **On close:** run the `handoff` skill. STATE.md is a snapshot of now; the diary lives in git.

## Project rules (from the owner)
- Until submission, after every card line from Leo's agent, the page session or this session, check whether a TRACK.md item has closed and close it at once with its proof file through the normal track flow (skeleton when the page shows the first real testnet handover, then re-run secrets). Reason: the map stood at 6/22 while the work was ahead, because no session turned card progress into track marks (central, 2026-10-25).
- Code lives in `github.com/pwsaragossy/rio-miami-rail` (private until submission; the rules require it public). Only this project's code goes there. The Radox backend (`radox-internal`) never becomes public; it is prior work, disclosed and linked, not published.
- Prior work to disclose: the Radox platform and its three Soroban contracts on mainnet, public since 2026-08-19 at `github.com/pwsaragossy/radox` (contracts only).
- Stellar facts (SDK, Soroban, SEPs, anchors) are looked up live, never answered from memory.
- Never commit to `pwsaragossy/radox` for this work: it is a one-way mirror of `radox-internal` maintained by Radox, and the harness, page and API client have no place in it. `custody_registry` lives only in `rio-miami-rail` (owner, 2026-10-25).
