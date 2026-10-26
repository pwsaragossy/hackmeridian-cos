---
status: in-progress
updated: 2026-10-25
next: video final cut with the rail reframe (rows 0:20 and 2:30, rail-page-host) → Pedro uploads tonight → video URL into README and FORM → Leo's scrub by 23:00, scrub re-run on the final commit → Pedro's OK: repo public → Vhendala's two timed plays (pitch) → deck → review-3 → package → review-4 → Pedro submits by Mon 08:00 (portal edits allowed until 12:00).
dispatch: off
member: pedro
---

# HackMeridian — rail Rio-Miami — state

## Arrival synthesis
- 2026-10-25 (soroban-sim session, owner request): set up github.com/theahaco/soroban-sim so we can call a Stellar RPC that is a local fork of mainnet (`soroban-sim serve --fork mainnet`). Nothing is submitted to mainnet; it is a local tool, outside the frozen submission scope (owner: custody_registry stays on testnet).
- First action: build the CLI from source (no crates.io release yet per its README), start `serve`, prove getLatestLedger/getLedgerEntries answer with mainnet data.
- Disagree: none. It does not touch the submission track.
- Fact checked on disk: the soroban-sim README pins soroban-env-host 29.0.2 (protocol 29), consistent with [[soroban-versions-on-2026-10-25-9619]] (testnet protocol 29).
- 2026-10-25 17:16 UTC (problem-numbers session, started by the rail session): I own PROBLEM-NUMBERS.md, 4-6 market numbers on the custody/handover problem, each re-opened at its primary source by an independent reviewer; deadline 17:55 UTC.
- First action: library search (only the ADB note has content; the DCSA, ICC FIT and TT Club notes are empty stubs), then 3 researchers in parallel.
- Disagree: none; the numbers describe the market, never our traction (Claims guard).
- Fact checked on disk: `date -u` gave 17:15 UTC; library note adb-trade-finance-gap-survey-dec-d033 exists with the US$2.5T Dec 2025 figure, as the brief said.
- 2026-10-25 (deck session, started by central): I own the pitch deck. Understood: rebuild the 9-slide deck on DECK-TEMPLATE.pptx, max 10 slides, Claims guard binding, real testnet hashes, no partner names, ZIS only if Paulo's written OK lands, AI line required; done = PDF + deck/REVIEW.md + `deck` [x].
- First action: read PITCH-FINAL.md, LOOK.md and the current deck render, then research winning decks.
- Disagree: the brief asks for a legal specialist on claims, but STATE §6 says no legal work during the hackathon (owner); the reviewer checks claims against the Claims guard instead. `deck` needs `pitch`, which is still open while PITCH-FINAL.md exists; I close `deck` only and flag `pitch` (needs two timed rehearsals).
- Fact checked on disk: deck/radox-custody-rail.pdf is 677768 bytes (0.65 MiB), as the brief said.

## 1. State in one line
green, stage 3 (Demo and pitch), track 15/22 at 2026-10-25 18:2x UTC. Done: both shipments on testnet (7 lifecycle txs, check.py 7; second shipment with teammates' own keys, verify-head MATCH both), page live, README and FORM-ANSWERS reviewed, private main pushed, fresh-run PASS on Windows (FRESH-RUN.md). Open: final video cut, pitch (two timed plays of the final video, TRACK.md rule), deck, review-3, repo public (after Leo's scrub and Pedro's OK), package, review-4, submit. Paulo's letter: past the 18:00 cut-off, unsigned wording locked (no ZIS anywhere; the only bridge is the deck's unnamed line); a signed letter becomes an edit before the deadline.

## 2. Intent (what counts as "done")
- What the owner wants, in their words (Scale intake, sent 2026-10-21 about 14:25 UTC, before the event): "a chain-of-custody contract for a tokenized physical asset in transit (Rio-Miami). Each handover between custodians (warehouse, port, carrier, customs) is signed by both the outgoing and incoming custodian with an event attestation; ownership stays with the token holder and final delivery burns the token. Proven end to end on testnet with signed transactions and connected to our API."
- Also wanted at the event: Stellar engineers review the design; meet anchors/ramps for the USD leg and logistics / trade-finance partners; improve the pitch.
- Kind: real project. Track: hackathon (builder track Scale; thematic track Stellar Unlocked (optional for Scale), chosen by Pedro 2026-10-24).
- Investment: the weekend (Sun 25 09:00 to Mon 26 10:00 Lisbon), team Pedro, Leo, Vhendala (3); money: zero (testnet only).
- "Done" for the current stage: stage 1 of TRACK.md closed (done 2026-10-25); stage moves to 2 after Vhendala's manual product review.
- Stop criterion (owner, 2026-10-25): if by Sun 25 18:00 Lisbon no handover signed by two custodians has run on testnet, cut the API connection and deliver contract + harness + recorded demo only.

## 3. What is true now
- Deadline: the portal form (PORTAL-SEEN.md, Pedro's paste 2026-10-25 ~10:50 WET) says submissions open Sun 25 Oct 11:30 WET and the deadline is Mon 26 Oct 12:00 WET, editing allowed until close after submitting. Pedro's "10am do dia 26" stays our internal target; submit at 08:00. Nobody but Pedro checks the terms box or submits (his OK at delivery). Rubric: 1–10 per criterion (portal rules page, settled 2026-10-25). Lisbon is UTC+0 for the whole event (summer time ended Sun 25 Oct 01:00 UTC). Field-by-field plan: SUBMISSION.md "Portal form, field by field".
- Rubric: 7 criteria, weights 20/20/15/15/10/10/10; scale 1–5 on hackmeridian.com/build but 1–10 in the portal rules (PORTAL-PASTE.md), checked at Sun 09:00. Self-score 72/100 ceiling, 66 if the API connection is cut (IDEA.md).
- Requirements verified in the portal PDF and public pages: RULES.md, SUBMISSION.md. Video 2–4 min YouTube/Vimeo, deck ≤20 MiB, mandatory AI attribution and the prior-work disqualifier come from Pedro's paste of the portal rules, now verbatim on disk in PORTAL-PASTE.md; binding.
- Portal rules page and submission form need login: not seen by any agent.
- The burn's `transfer_agent` wasm (`3870748b…`) is on testnet with `fn redeem` (rechecked by leo-agent 11:10 UTC; redeem burned on testnet).
- check.py names only the proof file it reads and requires 7 distinct hashes; check OK re-recorded by central (owner: "Sim, travar"). Do not edit it without a new OK; propose the "each tx calls our contract" check after deploy.
- Library: library notes tagged hackmeridian-rail.
- Repos: `pwsaragossy/rio-miami-rail` (private, empty, created 24/10); team board `pwsaragossy/hackmeridian-cos`. leo-schlanger invited with write to both on 24/10.
- `radox-internal` branch `hackmeridian` exists (from main), only for a backend change the API connection may need; never public.

- custody_registry on testnet: CCBJVXMJYWPHTDJHDFPRGKPGXGEP24JOPJAMUS5C3BMZJTRTWR2H4LII, wasm 8230ed93…, 24/24 unit tests, reviewer verdict approve with changes, fixes applied (REVIEW-contract.md; rio-miami-rail DEPLOYMENTS.md).
- Target met: `python3 check.py` → 7, exit 0 (leo-agent, 2026-10-25 12:15 UTC); hashes and shipment key on the Leo card. `node scripts/verify-head.mjs <key>` → MATCH; README run commands on the Leo card (12:01 line).
- Library relied on this session: [[executability-audit-2026-10-25-02-04f7]].
- 2026-10-25 12:20 UTC (central, owner answers): Joe Chi liking the videos is secondhand from Paulo, unwritten; never public. Paulo received the PT videos ZIS Rio–Miami and ZIS Rio–Peru (vertical axis) on 23/10; his "Nada a alterar" covers those two; no endorsement in public material. EN v2 approval unconfirmed.

- 2026-10-25 12:40 UTC (central, owner): Radox is part of the ZIS project with Paulo, not outside support ("paulo não só apoia, como fazemos parte do projeto ZIS"). Public use waits on the reviewer and on Paulo's written OK.

- 2026-10-25 14:29 UTC (owner): custody_registry stays on testnet; no mainnet deploy before submission ("Não, fica na testnet").

- 2026-10-25 23:45 UTC (owner): after judges asked for mainnet, custody_registry is rehearsed on a local mainnet fork only; no real mainnet deploy ("Fica só o ensaio no fork; não publica em mainnet"). Rehearsal (clean re-run fd84b68 by the rail session): 15 tx, 9 refusals, 13.72 XLM charged, custody lifecycle only, no burn.

- 2026-10-26 ~04:00 UTC (owner): landing v3 in production (deploy enj4j30gv, landing-v3 0c7dd19) was his request; keep it ("Fui eu que pedi a landing v3 em produção. Mantém.").

- 2026-10-25 18:26 UTC: no early submission and edit. Every portal field is prepared outside the portal, in FORM-ANSWERS.md, in portal order and as final text only, so Pedro pastes once on Monday. Owner: "vamos preparar tudo por fora, organizado, e depois copiamos."
- 2026-10-25 18:26 UTC: the repo goes public at 06:00 Mon as planned, not earlier. Owner: "Manter 06:00".

- 2026-10-25 19:17 UTC: commit 67c2b13 in rio-miami-rail names radox-internal and one route path in code comments (no secret). The tree is fixed in a follow-up commit, and the history is not rewritten, so the cited commit hashes stay valid. Owner: "Deixar como está (Recomendado)".

- 2026-10-25 19:18 UTC: no payment demo and no new money flow. The Innovation lever is interoperability: many supply chains on one rail, with internal and external handovers. Testnet only, timeboxed to Mon 04:00. If it does not close, it stays a future-tense design line. Owner: "não funciona assim, a ideia é poder conectar múltiplos supply chains dentro do mesmo rail, com passadas de mão interna e externa. não vejo necessidade de pagamento no meio. a carga já foi paga para estar em transito".
- 2026-10-25 19:18 UTC: the pricing model is a subscription per connected institution plus a fee per shipment, after SWIFT. Public text names the model with no values, and the SWIFT comparison is checked against a primary source. Owner: "assinatura + embarque, como uma maquininha + taxa. precisamos copiar o modelo swift".
- 2026-10-25 19:18 UTC: Pedro asks a Stellar engineer at the venue for a review. The rail session prepares a one-page brief by 21:00. What the engineer says goes in the README only with that person's OK.
- 2026-10-25 19:18 UTC: Pedro chases Paulo's letter himself today. If it arrives signed by Mon 08:00, we quote only what it says.

- 2026-10-25 19:40 UTC: until submission, central pushes to the private rio-miami-rail main whatever has passed the tests and the independent reviewer, and tells Pedro in one line. Making the repo public and sending the submission still wait for his OK. Owner: "Sim, até a submissão (Recomendado)". First use: 7dd63f7 (verify-head offline fix). All 4 shipments MATCH offline and live.
- 2026-10-25 19:40 UTC: judge 1 verdict on globe page v1: UX 3/10, so v1 is NOT deployed. The v2 scroll story is briefed to rail-page-host. Owner: "ninguém entendeu nada e não motivou ninguém".

- 2026-10-25 19:40 UTC: we do not lowball the project in public text. README, FORM-ANSWERS, DEMO-SCRIPT narration, the page and the deck sell only the strong part, in the founder's voice, with no self-deprecating caveats. Strengths are stated as facts, for example "Radox is in conversations with ports, airports and chambers of commerce" (no names), and the roadmap is said with confidence. The hard line stays: nothing false, no partner named, no signed deal, no users or revenue claimed. Only the required disclosures stay: prior work, AI usage, testnet. Reviewers apply this rule from now on, and the earlier hedge rules in the wording notes are superseded where they conflict. Owner: "NÃO É PRA LOWBALL NOSSO PROJETO, VENDA APENAS A PARTE BOA".

- 2026-10-25 19:59 UTC (owner via central): wording in deck, README and form is "Radox has openings with ports and airports, and chambers of commerce are opening doors". Owner chose "Usar \"openings\"".
- 2026-10-25 19:59 UTC (owner via central): first-hand user fact. Two chambers of commerce, one at each end of the Rio–Miami corridor, are engaged with Radox on this through the corridor initiative. Internal only: the chambers are CISBRA and Camacol, via Paulo Protásio's ZIS. Public text names neither the chambers nor ZIS nor Paulo ([[zis-in-public-material-radox-is-bc05]]). It may say "chambers of commerce in Brazil and in Miami". No "asked for X", because Pedro named no concrete ask. Owner: "sim, cisbra, camacol, pelo zis do paulo protasio".

- 2026-10-25 20:07 UTC (owner via the status session, newer than the 19:59 answer and more precise, so it wins where they differ): Radox's direct conversations are with chambers of commerce. Ports and airports come through the Rio–Miami corridor initiative that Radox is part of. Public wording: Radox is part of a Rio–Miami trade-corridor initiative and is its technology rail (unnamed until Paulo's letter). Every port, airport and chamber that joins the initiative will join the rail. Radox is in conversations with chambers of commerce. Do not write "openings with ports and airports". The deck session sends the final sentences, and the independent reviewer checks "its technology rail" against [[zis-in-public-material-radox-is-bc05]]. Owner: "a zis fechando, nós fechamos. estamos juntos"; "se adotar a zis, nós somos consequência".

- 2026-10-25 20:12 UTC: the corridor sentence keeps "the" ("Radox is part of the Rio–Miami trade-corridor initiative and its technology rail ... will join the rail"). Pedro accepts the reviewer's risk that this is a membership claim a judge cannot check. Reviewers do not raise it again. Owner: "Manter como está".

- 2026-10-25 20:57 UTC: the 20:47 video cut is rejected and will not be uploaded. Order now: (1) landing page v2 until Pedro approves it, with Leo's agent as the single writer; (2) only then a new video built around the approved page, from a fresh brief (no re-cut). The video deadline stays Mon 08:00. Owner: "O VIDEO ESTÁ UMA MERDA, NÃO VAI SUBIR ASSIM! vamos resolver a landing page primeiro."

## 4. What was done and how
- 2026-10-25 12:15 UTC (leo-agent): Leo's work runs in the session opened with the plugin active (window «hackmeridian-rail (leo)»); the old Leo session no longer writes, so pushes do not cross.
- 2026-10-25 (central, owner's answers): pushes to both repos and testnet deploys of the shipment page are pre-authorized for the weekend (repo public and submission still need the owner's OK); Vhendala does a manual product review, not code; the Mon 00:00 fresh-run is an independent agent on a clean clone.
- 2026-10-25 (central, owner's answers): `check.py` requires 7 distinct hashes, check OK re-recorded with track.sh; README gets a "Production path" section; Pedro pastes the portal rules, form fields and editing-window dates into `PORTAL-SEEN.md` at Sun 09:00.
- Workspace created with `setup.sh create ~/hackmeridian --share <hackmeridian-cos> --member pedro`.
- Stage 1 redo: researcher and product subagents with role cards rewrote the five files; reviewer subagent attacked them; fixes applied (REVIEW-1.md lists each).

## 5. Next actions
1. **Pedro (via central), Sun 09:00:** portal rules + form fields + editing window into `PORTAL-SEEN.md`; organizer question on the closed-platform repo.
2. **central, Mon 00:00:** independent fresh run of `npm install && node scripts/lifecycle.mjs` on a clean clone (own-registry path already passed for leo-agent 12:01 UTC); done when it ends 7/7 and verify-head MATCH.
3. **Vhendala:** manual product review of REVIEW-1.md and, later, the page, deck, video and README as a judge would (no code review, no repo invite); then stage → 2. The Mon 00:00 fresh run of the README on a clean clone is an independent agent that wrote none of the code, launched by central. The contract is read by a Stellar mentor or the plugin reviewer by 14:00.
4. **Leo:** contract and proofs done. Left: by Sun 22:00 one line per real breakage on his card (portal Challenges field); by Mon 05:30 AI_USAGE.md per-file list matches the repo and the Claude model names (done when both lines are on the card).
5. **session-hackmeridian-rail:** shipment page against CCBJVXMJ…; `skeleton` [x] when it shows a real testnet handover, then `secrets` (re-run SECRETS-SCAN) and `review-2`; propose the "each tx calls our contract" check (every lifecycle tx but redeem has parameters[0] = the registry).

## 6. If X, then Y
- Paulo's letter (owner, 2026-10-25: "você sabe que nossa força vem da carta do paulo, certo?"): unsigned draft, due Sun noon, fallback Sun 18:00; base case is unsigned. Marketing specialist + reviewer (2026-10-25): it is context for User Value, Market and possibly Ecosystem (1–2 of 100 per point), not the strength; the 7-tx demo is. Public material names ZIS only after Paulo's written OK; never the video's "Backed by" clip, G20 line or trade figures. Full rules on the card and in [[which-zis-video-versions-paulo-saw-1bb9]].
- Video and team photo belong to Vhendala (owner, 2026-10-25): account and test upload now, narration, final upload; card `board/Vhendala video and team photo.md`.
- No legal work during the hackathon (pedro, 2026-10-25): "regra daqui pra frente no hackathon: não é momento de envolver jurídico." No legal specialist, no legal research (UCC, Brazilian law, KYC, IP terms), no legal questions to pedro. The track's `licences` item is done by the engineer card as a plain list of dependency licences (the repo is Apache-2.0), with no legal analysis. Legal library notes already written stay as they are and are not used.
- If something needs the owner, it becomes a line on the card with `status: waiting-owner`. Do not ask.
- If the rules forbid code written before the event, list exactly what reused code comes from the public radox repo.
- If the portal rules contradict RULES.md or SUBMISSION.md, the portal wins: fix the files the same hour.
- If check.py is below 7/7 when Pedro gives the submit OK (Mon 08:00), track.sh refuses unless the OK words start with 'waive: <reason>' (track.sh:289-298); central runs track.sh verify first and puts the count in the question; Leo must push proofs/lifecycle.json to main.
- If the portal shows the editing window closing earlier than Mon 10:00: ask an organizer at ONE16 the same hour and email meridian@growwithguava.com how a late edit is submitted; write the answer in PORTAL-SEEN.md.
- If an organizer refuses a Scale repo without the closed backend: cut the API connection and deliver the registry as infrastructure; do not publish the backend.
- Vhendala's manual product review does not block Leo's start at 09:00; if she cannot be reached Pedro closes the pass himself.

## 7. What I did not verify
- Fresh run by someone who did not write the code (Mon 00:00, central).
- Whether the old Leo session (without the plugin) is closed; the owner sees that window, this session cannot.
- Whether the organizers accept a Scale repo that holds only the new work, with the platform backend closed. Ask an organizer at check-in.
- Portal rules, submission form and its editing window (login).
- Any evidence that a financier or buyer has the custody-visibility pain (IDEA.md: assumption; mentor test planned).
- SCF Build eligibility criteria themselves.
- PITCH.md slide 3 (problem) still has a {{source needed}} marker for how handovers are documented today.
- Open-slot markers in PITCH use {{fill}}; double square brackets are parsed as a library citation by the checker.
