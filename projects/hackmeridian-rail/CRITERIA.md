# Judging criteria → where each one is won

Source: hackmeridian.com/build, read 2026-10-25 [[hackmeridian-rubric-7-criteria-weights-scored-50e2]].
Seven criteria, weights sum to 100, **each scored 1–5** (the first draft said 1–10; wrong). The portal
tracks PDF has no weights. Judging priority order on the site: Adoption → Discovery → Continuation
(undefined there). Scale is also described as judged on: milestone completion against the intake,
SCF eligibility, production readiness, ecosystem impact — the "Ecosystem Alignment" row below carries
that, including a README "Production path" section. Read directly (DOM text) by the reviewer on
2026-10-25: scale 1–5 and the weights confirmed. Judges review video, deck, repo and answers; AI tools may help, humans decide.

Video moments are the PITCH.md outline (2–4 min, target 3:00).

| Criterion | Weight | What the judge must see | Where (demo moment / artifact) |
|---|---|---|---|
| Ecosystem Alignment (Scale) | 20 | multi-party `require_auth` of two custodians in one call; SAC clawback burning the title; contract events + on-chain `head` | video 0:20–1:30 (first handover, both auth entries on the explorer) and 2:00–2:30 (burn); deck slide 4; README architecture and the intake-milestone table; README "Production path" (mainnet plan, audit status, what is testnet-only, SCF Build eligibility) — covers Scale's "production readiness" and "SCF eligibility" |
| User Value & Problem | 20 | a real party with a real pain: the financier and buyer cannot see who holds the goods | video 0:00–0:20; deck slides 2 and 6. **Evidence is an assumption today** (IDEA.md) |
| Technical Execution | 15 | 7 SUCCESS testnet txs, failure branches refused on-chain, `verify-head` exit 0, tests green | video 0:20–1:30 and 1:30–2:00; `proofs/lifecycle.json`; test output in README |
| Innovation | 15 | dual-signed handover with assurance levels; no SEP covers it, and none of the ecosystem projects found does it (RESEARCH-raven.md §5, a directory search, not proof of absence) | video ~0:30 (the first dual-signed handover, voiced over); deck slide 3 |
| Hackathon Progress | 10 | clear prior/new split; commits only after Sun 09:00 | deck slide 5; README "Prior work" / "Built at HackMeridian" / "AI usage"; no video moment yet (proposal: 5 s of the README table at 2:50) |
| Market & Ecosystem Potential | 10 | one corridor → public record format others adopt (SWIFT model); USD leg via a ramp (future) | deck slides 7–8; no video moment (the weakest mapping) |
| Product Design & UX | 10 | a legible public screen, not only a terminal | video 2:30–3:00: the public shipment page (a must-have); the public URL itself |

Changes from the first draft: scale 1–5; passkey smart accounts removed (cut from scope, not built);
UX gap closed by the approved shipment page; moments now match PITCH.md; innovation and progress
no longer point at "voice-over" or nothing.

Idea, self-score and scope: IDEA.md.
