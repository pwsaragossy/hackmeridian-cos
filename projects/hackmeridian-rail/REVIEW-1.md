# Review-1 — independent review of stage 1 (redo with specialists)

Date: 2026-10-25. Specialists (subagents with role cards): researcher → RULES.md, SUBMISSION.md;
product → CRITERIA.md, IDEA.md, KICKOFF.md. Reviewer (subagent, `specialists/reviewer.md`) read both
cards and both full outputs, opened the portal tracks PDF (all 4 pages), hackmeridian.com /build, home,
/schedule, /faq, /terms.html as page text, and the live testnet RPC.
Final pass: Vhendala's human review (not yet done). This review is the same model with a different
brief; it is not legal or tax advice on prize, KYC or IP terms.

**Verdict: approve with changes.** The facts the specialists verified hold against primary sources; no
critical error. Fixes applied by the project session the same day (column "Applied").

| # | Sev. | Finding | Applied |
|---|---|---|---|
| 1 | major | Submission form and its "project editing window" never seen; first contact planned at Mon 08:00 | KICKOFF §5 Sun 09:00: Pedro saves rules, form fields and window dates to `PORTAL-SEEN.md`; form dry-run in Sun 18:00–22:00; SUBMISSION.md says so |
| 2 | major | Scale's "production readiness" and "SCF eligibility" had no artifact | CRITERIA row 1 and SUBMISSION: README "Production path" (deck slide only if the owner says so); KICKOFF README line |
| 3 | major | Score 72/100 hid the API-cut case | IDEA.md: 66/100 if the API connection is cut (first applied as 64, an arithmetic slip caught by a second reviewer pass); "72 is the ceiling, not the forecast" |
| 4 | major | Timeline ignored the event programme; 14:00 gate had no action | KICKOFF §5: programme lines (≈3 h not building), 14:00 checkpoint → line on the card |
| 5 | major | Mentors start 11:00, not 09:00 | KICKOFF: organizers at 09:00, mentor user test 11:00–12:00 and 13:30–14:00 |
| 6 | major (suspicion) | Burn depends on the `transfer_agent` wasm still being on testnet | Checked: `stellar contract info interface --wasm-hash 3870748b… --network testnet` returned the spec with `fn redeem` (01:02 UTC); Leo re-runs it at Sun 09:00 (STATE §5) |
| 7 | minor | check.py passes with 7 copies of any successful hash (no uniqueness, no contract check) | Frozen: question on the board card (waiting-owner) |
| 8 | minor | Stale text outside the five files | PITCH.md: scale 1–5, passkey claims removed, page "must-have", track "Scale"; STATE.md §2–3 updated. Slide 2 fill marker (cost of today's alternative) still open |
| 9 | minor | Thematic-track conflict | Settled in RULES.md: Scale needs none (/build, home); optional and unscored |
| 10 | minor | "Plan to the paste" is right; the paste is in the central session transcript | SUBMISSION.md notes it; Pedro's copy at check-in (`PORTAL-SEEN.md`) replaces it |
| 11 | minor | Library: rubric note confidence and Compared: line; rules note "Open" settled | Notes updated; `library.sh doctor` clean |

Premises tested: rubric 1–5 with 20/20/15/15/10/10/10 (confirmed on /build); video/deck specs, AI duty and
the disqualifier are on no public page (confirmed); deadline Mon 12:00 Lisbon = 12:00 UTC (confirmed);
testnet protocol 29, soroban-sdk 29.0.1, stellar-tokens 0.8.0 needs ^28 (confirmed); 72 = 360/5 (correct).

Pre-mortem: Mon 08:00, Pedro opens the form for the first time and it wants something not prepared, or the
editing window is closed. Control now in place: the Sun 09:00 portal copy and the Sun evening dry run.

Not checked: portal rules, submission form and window (login); SCF eligibility criteria themselves; the
full text of the paste.

Sources: [[hackmeridian-rubric-7-criteria-weights-scored-50e2]] [[hackmeridian-2026-rules-and-submission-requirement-5868]]
[[lisbon-is-utc-0-for-the-9963]] [[soroban-versions-on-2026-10-25-9619]]
