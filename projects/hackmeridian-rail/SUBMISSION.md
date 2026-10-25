# HackMeridian 2026 — submission requirements (re-checked 2026-10-25)

Tags as in RULES.md: [PDF] portal tracks PDF 2026-10-24 (read in full), [WEB] hackmeridian.com 2026-10-25
(second-hand summaries), [PASTE] Pedro's paste of the portal rules (not on disk): **not verified**.
Portal rules and the submission form need login: not reached. Library: [[hackmeridian-2026-rules-and-submission-requirement-5868]].

## Verified (PDF and/or web)
- Judges review asynchronously: demo video, pitch deck, GitHub repo, submission answers [WEB home, /faq, /build].
- Public GitHub repository with the project source code [PDF p4]. When it must be public: not stated. Not verified. Safe rule: public before 10:00 on Mon 26 Oct.
- README: project summary, problem, setup, installation, environment variables, demo instructions [PDF p4]. "A clear README ... including its specs, does most of the work for judges" [WEB home].
- Architecture overview: how Stellar is used, with assets, contract IDs, anchors, wallets, integrations, APIs [PDF p4].
- "Working live demo or video walkthrough showing core functionality and meaningful use of Stellar." User-facing apps must also give a public live URL; developer tools and infrastructure may use "an appropriate technical demonstration" [PDF p4]. Our contract is infrastructure; the public shipment page (scope, 3rd must-have) gives a live URL anyway.
- Evidence of an onchain transaction on testnet or mainnet "where applicable" [PDF p4]: tx hashes and contract IDs in the README.
- "Disclose prior work and show what you built during the event" [PDF p4].
- Scale deck content: problem, solution, target users, value proposition, team, future vision, business or sustainability model, market opportunity, go-to-market [PDF p1-2].
- Deadline: Mon 26 Oct 12:00 Lisbon time = 12:00 UTC, "No late submissions" [WEB /build, /schedule]. Judging starts 13:30 [WEB /schedule]. Our own cutoff: 10:00 +0000.
- Scale answers are scored against "goals set at pre-event intake" [WEB home]: keep the intake text (STATE.md §2) as the milestone list.

## Not verified (only in the paste, or nowhere)
- Demo video 2–4 minutes, YouTube or Vimeo: [PASTE] only. Public pages say nothing on length or host. Plan to it anyway (PITCH.md 2:30), upload as YouTube unlisted or public, check the form accepts the link.
- Deck as PDF, PPTX, PPT or HTML up to 20 MiB: [PASTE] only. Plan: PDF under 20 MiB.
- Form fields, number of questions, link fields, platform name: not seen. Not verified (home, /faq, /build, PDF). The form is inside the portal ("project editing window", PDF p4); when that window closes is not known. Pedro saves the field list and the window dates to `PORTAL-SEEN.md` at Sun 09:00, and the form is dry-run with placeholder links before Sun 22:00 (KICKOFF §5). The paste itself is only in the central session's transcript, not in this folder.
- AI attribution required and undisclosed prior work disqualifying: [PASTE] only (see RULES.md). Treat both as binding.
- Repo must stay open after the event, licence requirement: not found.

## What this means for us
- README fixed sections: **Prior work** (Radox before 25 Oct 09:00: public repo github.com/pwsaragossy/radox since 2026-08-19, 3 mainnet contracts, closed backend radox-internal, with dates), **Built at HackMeridian** (commit range from the first commit after Sun 09:00), **AI usage** (which parts Claude Code agents wrote), plus architecture with contract IDs and testnet tx hashes, and **Production path** (mainnet plan, audit status, what is testnet-only, SCF Build eligibility), which Scale judges as "production readiness" and "SCF eligibility".
- The closed Radox backend is declared prior work. Whether an entry without it in the repo is accepted is unanswered (RULES.md open items): ask at check-in; README says plainly what is not in the repo.
- Submit by Mon 10:00 +0000: repo link, video link, deck file, answers. Test the links logged out.
- Terms licence: the organizers may show the submission and team name publicly (terms.html sec 06): nothing secret in repo, video or deck.
