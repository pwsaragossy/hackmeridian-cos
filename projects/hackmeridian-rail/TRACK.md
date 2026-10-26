---
track: hackathon
stage: 3
delivery: 4
stale_hours: 3
owner_wait_minutes: 20
deadline: 2026-10-26 10:00 +0000
target: a judge, logged out, opens the public repo, the site, the live testnet API and its docs, the video and the deck from the form (7 gates in check.py)
check: python3 check.py
baseline: 22
baseline_delivery: 4
---
# Track: hackathon
For a 24-48 hour build event judged by a panel. Pick it when the deadline is hours away and the goal is a working demo plus a complete submission.

## Stage 1: Rules and plan
Gate: rules, criteria, submission requirements and deadline are written down, and one idea is chosen against the criteria.
- [x] rules | Rules and eligibility read in full: allowed tools and code, team size, IP terms, prize conditions, disqualifiers | card: researcher | needs: - | evidence: RULES.md
- [x] criteria | Judging criteria extracted with weights, each mapped to one planned moment in the demo | card: product | needs: rules | evidence: CRITERIA.md
- [x] submission-reqs | Submission package requirements listed: form fields, video length, repo, deck, links, file formats, platform | card: researcher | needs: rules | evidence: SUBMISSION.md
- [x] deadline | Deadline written as `deadline: YYYY-MM-DD HH:MM` in this file's front matter, in local time, or with the offset when teammates are in other time zones (`2026-10-25 18:00 -0300`); the panel counts down to it, and a backward timeline with at least 2 hours of buffer before it (default, adjust to the case) | card: product | needs: submission-reqs | evidence: KICKOFF.md
- [x] idea | One-sentence idea, user and problem, scored against the criteria | card: product | needs: criteria | evidence: IDEA.md
- [x] review-1 | Independent review of stage 1: verdict and fixes | card: reviewer | needs: rules, criteria, submission-reqs, deadline, idea | evidence: REVIEW-1.md
## Stage 2: Scope and build
Gate: scope is frozen, the thinnest end-to-end path runs, and nothing in the build breaks the rules.
- [x] scope | Scope freeze: at most 3 must-have features for the demo, everything else listed as cut, time-boxed with a clock time | card: product | needs: idea, deadline | owner: ok | evidence: SCOPE.md
- [x] skeleton | Thinnest end-to-end path running (input to visible output) before any extra feature is built | card: engineer | needs: scope | evidence: SKELETON.md
- [x] licences | Licences of dependencies, datasets and third-party assets checked against the rules and the intended licence | card: legal | needs: rules | evidence: LICENCES.md
- [x] secrets | No keys or personal data in the repository or demo, keys in environment variables, keys rotated if exposed | card: security | needs: skeleton | evidence: SECRETS-SCAN.md
- [x] look | Name and one consistent visual style across product screens and deck, readable at projector size | card: designer | needs: scope | evidence: LOOK.md
- [x] review-2 | Independent review of stage 2: verdict and fixes | card: reviewer | needs: scope, skeleton, licences, secrets, look | evidence: REVIEW-2.md
## Stage 3: Demo and pitch
Gate: the demo runs without live dependencies, a recorded backup exists, and the pitch has been rehearsed against the clock.
- [x] demo-script | Demo script with timings under the time limit, following the criteria order, with the success path only | card: product | needs: criteria, scope | evidence: DEMO-SCRIPT.md
- [x] demo-offline | Demo runs without internet or live third-party services (cached or local data), and a screen recording of the full flow exists as backup | card: engineer | needs: skeleton, demo-script | evidence: video/README.md
- [x] fresh-run | Product runs from the README on a clean machine or account by someone who did not build it | card: engineer | needs: demo-offline | evidence: FRESH-RUN.md
- [ ] pitch | Pitch covering problem, solution, demo, why this team, next step, rehearsed at least twice with a timer | card: marketing | needs: demo-script | evidence:
  Evidence rule (central, 2026-10-25, from Leo's 18:06 line and Vhendala's 17:36 line): judging is async and only the demo video is required, so the pitch is the final 3:00 video; two timed full plays of the final cut by Vhendala, each logged with start, end and length, count as the two rehearsals. Proof file: PITCH-REHEARSALS.md.
- [ ] deck | Slide deck of at most 10 slides (default), one message per slide, readable at distance, exported as the format the rules require | card: designer | needs: pitch, look | evidence: deck/REVIEW.md
- [ ] review-3 | Independent review of stage 3: verdict and fixes | card: reviewer | needs: demo-script, demo-offline, fresh-run, pitch, deck | evidence:
## Stage 4: Submission
Gate: the submission is sent before the deadline, confirmed, and every link opens from a logged-out browser.
- [x] api | Public testnet API live: GET /api/shipments/<key> answers JSON read from the registry, /docs page with parameters and examples, request access, mainnet enabled in code but not deployed | card: engineer | needs: fresh-run | evidence: production rio-miami-rail.vercel.app deployed 2026-10-26 from rio-miami-rail branch public-api 36f3927 (Pedro yes); scripts/api-check.mjs 18/18 against production, proofs/api-check.json (commit 88bb31e), e.g. open 50e590db…f967, handover 8ecee4d6…545b, deliver 4d360579…98eb, refusal E_WRONG_CUSTODIAN; ?network=mainnet answers 503 E_MAINNET_NOT_DEPLOYED; check.py api PASS, docs PASS; reviewer + security reviews applied
- [ ] repo | Repository with README (what it does, how to run, team, licence), no secrets, set to the visibility the rules require | card: engineer | needs: fresh-run, secrets | evidence:
- [ ] package | Every item in the submission requirements prepared: video, deck, description, links, team details | card: product | needs: submission-reqs, deck, demo-offline, repo, api | evidence:
- [ ] review-4 | Independent review before sending: submission checklist walked item by item against the rules, every link opened in a logged-out browser, verdict and fixes | card: reviewer | needs: repo, package | evidence:
- [ ] submit | Submission sent at least 2 hours before the deadline (default, adjust to the case) and the confirmation saved | card: product | needs: review-4 | owner: ok | evidence:
