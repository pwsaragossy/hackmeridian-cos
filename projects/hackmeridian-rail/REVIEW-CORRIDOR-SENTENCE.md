Role: reviewer
Reviewing: the corridor sentence (deck slide 4) as placed in rio-miami-rail README Future, FORM-ANSWERS What's next (line 68), DEMO-SCRIPT row 2:30 (line 16)
Verdict: approve with changes
Reason: no adapter exists and no port or airport has joined, so the present tense "joins ... through one adapter" can be read as a delivered integration; one word-level tense fix ("will join") removes it and matches the owner's own 20:07 UTC wording.

## Findings (ranked by severity)
1. [major] The sentence reads as if the adapter exists today. [FACT] No adapter in ~/code/rio-miami-rail: `grep -rli adapter` over the repo (without node_modules, target, .git) hits only README.md and the minified page/stellar-sdk.min.js (a third-party library); scripts/ holds handover-signers, lifecycle, multi-chain, page-snapshot, remote-auth, verify-head; contracts/ holds only custody_registry. The only Radox API link is one read-only GET `/api/custody/shipments/<key>`, run on a local throwaway backend (README line 112); the backend is private. "joins the rail, through one adapter to the Radox API" is present tense and names the adapter with the article "one", so a judge will take "adapter" as a thing that exists. Confidence: high on facts, medium on how a judge reads it. Fix: tense change below.
2. [major] Inconsistent tense inside the README. [FACT] README line 13 (Problem) says "a legacy system will join through one adapter"; README line 239 (Future) says "joins the rail, through one adapter". The earlier review fixed the first and the new sentence reintroduces the claim in the second. Same sentence in FORM-ANSWERS line 68 is partly saved by the next sentence ("Next we connect the rail to the Radox platform's physical-asset flow (a read-only ... endpoint ... local development run)"). In the README Future and in the video nothing next to it says "not built yet". Fix: same tense change.
3. [minor] "joins it joins the rail" does not say ports or airports have joined: "every ... that joins" is generic. But it is not strictly future either, and with finding 1 a listener can read "joins" as "already joins". Board, same owner decision (Sessions build and submission, line 56, 20:07 UTC): "Every port, airport and chamber that joins the initiative will join the rail." The owner used "will". Restoring it is faithful, not an edit of intent.
4. [minor] "the Rio–Miami trade-corridor initiative" with "the" names one specific initiative a judge cannot identify or check ([[zis-in-public-material-radox-is-bc05]]: "a judge cannot check the statement"). Board line 56 says "a Rio–Miami trade-corridor initiative". "is its technology rail" is also stronger than the unnamed bridge sentence in that note ("a Rio–Miami trade-corridor initiative"); the owner chose it on purpose at 20:07 UTC and asked the reviewer to check it. Check result: allowed only because nothing is named, and only while it stays a statement of Radox's role, not of an agreement. Risk: if the initiative's own people read "the technology rail" as an appointment that was never made. Not changed here because the owner fixed the words; ask below. Confidence: medium.
5. [note] "Radox is in conversations with chambers of commerce in Brazil and Miami" matches board line 56 ("direct conversations are with chambers of commerce") and [[claims-hackmeridian-material-may-and-may-3e4f]] (owner override, chambers allowed unnamed, no ask). No chamber, ZIS or Paulo named in any of the three places (checked by reading the three texts). OK.

## Answer 1: tense fix (smallest change)
Replace "every port, airport and chamber that joins it joins the rail, through one adapter to the Radox API" with:
"every port, airport and chamber that joins it will join the rail, through one adapter to the Radox API"
Full sentence: "Radox is the technology rail of the Rio–Miami trade-corridor initiative: every port, airport and chamber that joins it will join the rail, through one adapter to the Radox API. Radox is in conversations with chambers of commerce in Brazil and Miami."
One word added, nothing else. Apply in README line 239, FORM-ANSWERS line 68, DEMO-SCRIPT row 2:30 narration (and the deck slide 4, which holds the same text, to keep the four places equal). Spoken, "will join" costs 0.4 s.

## Answer 2: repeat or contradict the README
- Repeats: the adapter idea is stated twice (line 13 Problem, line 239 Future). Not a contradiction once both are future. After the fix the two lines agree; the repetition is acceptable (problem, then roadmap) but line 239 could drop the adapter clause if the owner wants the shortest text. His words are fixed, so leave it.
- Without the fix it contradicts line 13 (will vs joins), see finding 2.
- "Stellar ecosystem" section (line 194-): [FACT] "Radox will open API access to Stellar issuers." Consistent: the Radox API is not open today, which is another reason an unqualified present-tense "adapter to the Radox API" misleads. It is a different audience (issuers) from the adapter (ports, airports, chambers); no contradiction, but a reader may ask which API is meant. No change needed.
- Line 112 (Architecture): "private, closed and not in this repo", local run. The sentence does not contradict it once "will".

## Answer 3: DEMO-SCRIPT row 2:30
[FACT] Narration is 95 words (counted), of which the sentence pair is 40 words (the owner-fixed two sentences). The row was committed in f3706e4; the claimed "about 21 words" growth is not what I count for the two corridor sentences (40), so the rest of the row was probably trimmed too; I did not see the earlier version in git for this row beyond the HEAD text.
Timing at 2.6 words/s:
- 2:30 to about 2:38: page sentence (about 20 words, 7.7 s). Fits the page shot.
- about 2:38 to 2:43: backend sentence (14 words, 5.4 s). Fits the 2:38-2:42 terminal replay.
- "Verify head: match." (3 words) ends at about 2:44.5, when the click is made at 2:44. Coherent: the 36 words up to there take 13.8 s.
- Corridor sentences: 40 words, 15.4 s, about 2:45 to 3:00, spoken over the held MATCH.
- "Our ask" sentence: about 19 words, 7.3 s, ends at about 3:07.
New end of narration: about 3:07 (95 / 2.6 = 36.5 s from 2:30). With the 3 s silence on MATCH (DEMO-SCRIPT line 35) the video ends at about 3:10. This is inside the 2:00-4:00 rule (line 35), but past the row header "2:30-3:00" and the "target 3:00" in line 35.
Coherent with the screen timings: yes, the claims land after the click and the screen holds on MATCH to the end. Two points: (a) the 22-second hold on a static MATCH is long but not wrong; (b) the corridor sentence is the claim most exposed to a judge and it plays after the proof, over a still image; the "will join" fix matters most here because the viewer has just seen the local backend, which makes "through one adapter to the Radox API" sound shown. Fix: header "2:30-3:10" and line 35 "target 3:10 (rules allow 2:00 to 4:00)".

## Premises tested
| Premise | Evidence | Result |
|---|---|---|
| An adapter exists | grep of repo, scripts/ and contracts/ listing | false: none |
| The Radox API is connected to ports/airports | README line 112: one GET, local run, throwaway database | false |
| Any port/airport has joined | no file or board line says so; board line 56 says "will join" | false |
| No name leaks (ZIS, Paulo, chambers) | read README Future, FORM line 68, DEMO row 2:30 | holds |
| Owner wording is the sentence | board line 56, 20:07 UTC (newer than 19:59) | holds, except the owner wrote "will join" |
| Video within 2:00-4:00 | 3:07 narration + 3 s | holds |

## Never-skip checklist
- Library cited: done (two notes opened). Findings saved with library.sh new: not done (read-only brief; see Library).
- Specialist's checklist audit: not applicable, the author is the owner's fixed sentence, not a specialist's report.
- Three premises tested: done (six above). Citations opened: done. Numbers recomputed: done (word counts by script, timing arithmetic).
- Contrary case: below. Contradictions with library and other files: done (finding 2, 4). Pre-mortem: below. Owner's hand work: none, four one-word edits.

## Contrary case
Leave it as is: "joins it joins the rail" is generic and conditional, nobody is said to have joined; the Radox API exists; "one adapter" describes the design, and slide 4 is a vision slide. Answer: the reading that counts is the judge's, who sees a local backend and the word "adapter" and has no repo file to check. A generic present tense about an unbuilt thing is the usual overclaim; the terms (section 05) allow removal without refund. The cost of "will" is one word; the cost of the stretch is the entry.

## Pre-mortem
A judge opens the repo to look for the adapter, finds none, and reads the Future sentence next to a "delivered" proof pack as a claim that failed. Missing check: a tense check on every sentence in the Future section. A second story: the initiative's people read "the technology rail of the initiative" as a title nobody gave Radox. Missing check: the owner's confirmation that this role statement is true as he states it.

## Not checked
- The deck itself (slide 4 text) was not opened; I rely on the brief that it is the same text.
- Whether the words "the ... initiative" are true: no document available to me; it is the owner's first-hand statement (board line 56).
- The previous version of the 2:30 row from before f3706e4, so the "21 words" figure is unverified.
- Whether Paulo's written OK arrived (board line for the 18:00 cut-off); the sentence names nothing either way.

## Questions for the owner
1. Keep "the Rio–Miami trade-corridor initiative", or use "a" as in your own board line 56? Only you can say what is true; the unnamed text is safe either way.
2. Update the video header and target to 3:10?

## Library
cited: [[claims-hackmeridian-material-may-and-may-3e4f]] [[zis-in-public-material-radox-is-bc05]]
saved: none

---
# Addendum: corrected sentence (deck commit eb7d0a3, applied in all three files)
Version reviewed: "Radox is part of the Rio–Miami trade-corridor initiative and its technology rail: every port, airport and chamber that joins it joins the rail, through one adapter to the Radox API. Radox is in conversations with chambers of commerce in Brazil and Miami." (README line 239, FORM line 68, DEMO row 2:30 confirmed by grep.)

Q1 (adapter / joined): unchanged. Findings 1-3 still stand; the sentence is still present tense. Now "it" is the initiative, which is more accurate (ports join the initiative, per board 20:07), but "joins the rail, through one adapter" is still read as existing. Smallest fix, one word: "...that joins it will join the rail, through one adapter to the Radox API." (the owner's own board line 56 says "will join").

Q2 (README): same as before. Line 13 says "will", line 239 says "joins": still inconsistent until the fix. No contradiction with "Stellar ecosystem" or line 112.

Q3 (timing): narration now 97 words (counted). Up to "Verify head: match." still 36 words, 2:44 as before; the rest 61 words, 23.5 s, so narration ends about 3:08, video about 3:11 with the 3 s silence. Inside 2:00-4:00; row header and line 35 target should read 3:10. Coherent with the click at 2:44 and the hold on MATCH.

Q4 (new): does "is part of the … initiative" read as partnership or endorsement under the hard line?
- [FACT] The hard line ([[claims-hackmeridian-material-may-and-may-3e4f]]): partners "roles only ... any name (any partner, programme, chamber or person), endorsement, 'in partnership with'" must not be said. [[zis-in-public-material-radox-is-bc05]]: "part of the ZIS project" needs Paulo's own signature; the fallback for no OK is the unnamed "a Rio–Miami trade-corridor initiative", which does not contain "part of".
- [FACT] "Is part of" is a membership claim. It reads as partnership with the initiative's people, not as endorsement words: the sentence has none of "supports", "backs", "endorses", "validates", "pilot". It names nobody. So it does not break the table's named-party ban or the endorsement ban, but it is the unnamed twin of the "part of" phrase that note reserves for a signed text.
- [FACT] Basis: Pedro's first-hand statement (zis note, board). A judge cannot check it. The note says Pedro's statement alone did not allow it; the owner has since decided this wording explicitly (board 20:07-20:09) and only he can relax a hard line, so I treat it as approved, not as an error.
- Severity: major risk, not a blocker. If the initiative's own people say Radox is not part of it, the sentence becomes a misrepresentation under terms section 05 (removal without refund). Mitigation inside the owner's words: article "the" claims one definite, known initiative; "a" (board line 56) is weaker and still true. Question below. No change forced.
- Also: "its technology rail" is a role claim on top of membership; same risk, same owner approval.

Questions for the owner (add to card): (1) keep "the" or "a" before "Rio–Miami trade-corridor initiative"? (2) is the "part of" claim confirmed with Paulo in writing before the form is submitted, or do you accept the risk? (3) header and target 3:10.
Library: cited [[claims-hackmeridian-material-may-and-may-3e4f]] [[zis-in-public-material-radox-is-bc05]]; saved: none.

---
# Addendum 2: Vhendala's two additions in FORM-ANSWERS.md (lines 110 and 116)
1. redeem signature and instance: [FACT] scripts/lifecycle.mjs lines 37-38 give `redeem(token: Address, from: Address, amount: i128, ref_id: u64)`, matching `redeem(token, from, amount, ref_id)`; proofs/lifecycle.json line 4 `transfer_agent_instance` = CAYD3EFTN6YO...XSJWH, matching `CAYD3EFT…SJWH`; README lines 23, 127, 174 agree (transaction 7, prior work, closed source). Match. Confidence high. (The README and the hash line say the wasm is existing; the form says the same.)
2. `GET /api/custody/shipments/:key` calling `get(key)`: [FACT] README line 112 and lifecycle.mjs header (lines 41-47) agree: closed backend, read-only simulateTransaction of `custody_registry.get(key)`, local run 2026-10-25. Match. Note the form also says the endpoint "was written during the event, on a private branch"; README line 112 says only "exposes". Not a contradiction, but a judge reading both could ask where it is; the form wording is the honest one.
3. Antigravity line: [FACT] source is Vhendala's agent (board card line 28), not Vhendala herself. [FACT] grep: "Antigravity" appears nowhere in ~/code/rio-miami-rail (README, AI_USAGE.md) and in no other board file. Not enough as it stands: (a) a tool-use disclosure is a statement about a person's work, and the terms forbid misrepresenting your work; the cost of a false line is small but the check is one message; (b) the form would now disclose a tool the public repo's AI_USAGE.md does not, which is an inconsistency a judge can see. Fix: Vhendala (the person) confirms in one line that she used it and for what, and AI_USAGE.md gets the same line; else delete the clause. Severity minor.
4. Limits: [FACT] PORTAL-SEEN.md line 7 lists "prior work disclosure" and "AI tooling note" as optional with no character limit stated; only description (8000 chars), tagline (120) and tech stack (25 items) have limits. "No limit stated" is not "no limit": the page was pasted by Pedro, may omit it. Line 110 is about 2,000 characters; keep it, check the live form counter before submission.
Library: cited none new; saved none.
