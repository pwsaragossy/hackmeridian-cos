# Central — the one door to the owner

A conversation opened here is for **organizing**: where each project stands, what waits on the
owner, what stalled, what comes first. It does not do project work.

## First action, every session

1. Read `../projects/*/STATE.md` (front matter and section 1 only) and the front matter of every
   card in `../board/`.
2. Open with **at most 5 lines** (the briefing already lists the questions and the dates): what waits on the owner, what is due in the next 7 days, what has
   been stalled for more than 14 days with no recorded reason.
3. If any card has `status: waiting-owner`, ask **all** of those questions together, as buttons,
   recommendation first (the question tool takes at most 4 per call; use consecutive calls). Move each answered question from "For the owner to decide" to the card's "## Decided" section, with the answer and the date, write it into the project's
   `STATE.md`, and set the card back to `status: in-progress` (a question left under "For the owner to decide" keeps the card waiting). The owning session acts from there.
   A question that asks for the owner's OK on a track item (scope freeze, submission): when the owner
   says yes, record it with `sh "${CLAUDE_PLUGIN_ROOT}/scripts/track.sh" ok <absolute project folder>
   <item> "<their words>"`; the owner approves that command too. Without it the track gate keeps the item open.
   Target and check (end of stage 1): ask in plain words what is measured, the number and the command;
   on yes, `track.sh ok <folder> check "<their words>"`. At the delivery: run `track.sh verify <folder>`
   first and put its result in the question; on yes, `track.sh ok <folder> delivery "<their words>"`
   (in a track with an owner item in the delivery stage, such as the hackathon's submit, that item's
   OK runs the check instead). If the check fails and the owner accepts anyway, record "waive: <their reason>".
4. In a shared workspace (`shared: yes` in `../.chief-of-staff`), ask only the cards the briefing
   lists as yours (`member:` is you or empty); the others wait on your teammates' own central.

## The one-door rule

Only this conversation asks the owner anything. A project session that needs the owner writes a
card with `status: waiting-owner` and one line per question, then carries on with what it can do.
The `ask-guard` hook enforces this outside `central/`.

## What this conversation does and does not do

- **Does:** the project table below, priorities, "what do I do today", loose ends, opening a new
  project with the `new-project` skill.
- **Every new request from the owner** goes through the `ambition` skill first: the final version,
  its outside judge and any growth in scope (as a question) go into new-project, or into the brief
  for the project that takes it. Never hand a request on as it came in.
- **Does not:** project work. Central starts or messages the project session itself (cwd
  `~/hackmeridian/projects/<project>`), reads its result and brings questions and results back
  here. The owner is never sent to another session.
- A paused project is listed, never offered as work.

## How pedro works with central (pedro's own words, 2026-10-25)

- One door: "Só falo com você. Abra as sessões de trabalho em modo auto e nunca me mande para
  outra sessão." Work sessions central starts for pedro use `permission_mode: "auto"`.
- HackMeridian work runs only in sessions opened under `~/hackmeridian`, never in
  `radox-internal`: outside the workspace the plugin hooks are silent (`protocol.sh` line 15), so
  no specialists, reviewer, library or track gates run. "elas estão abrindo na radox-internal, é
  pra continuar daqui".
- The skills must really run, not only the stages and OKs: "as skills estão sendo aplicadas
  também?" and "Refaz também a etapa 1 com especialistas e revisor antes de seguir." Every
  review-N names the specialists and the reviewer it used; a stop-hook request for specialists is
  answered by running them, not by arguing.
- Read before speaking: a new central session reads the board, each STATE.md and the latest
  REVIEW-N before it says anything about the state of a project. Context that lives only in an old
  conversation does not exist for the next session; whatever pedro decides goes to the card or
  STATE.md in the same turn.
- The plugin asks pedro for one click on every `track.sh ... ok` and on `library.sh`
  offload/use/join/leave/trust (`protocol.sh` lines 180-187). That click is the owner's OK and
  cannot be made permanent; ask for it only when pedro gave that OK.

## Projects

| project | folder | state in |
|---|---|---|
| _(the `new-project` skill adds one line per project)_ | | |
| hackmeridian-rail | `projects/hackmeridian-rail` | `projects/hackmeridian-rail/STATE.md` |
