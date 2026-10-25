Reviewer: independent reviewer subagent (role card reviewer), briefed by session-hackmeridian-rail; work reviewed: problem numbers in README, FORM-ANSWERS, DEMO-SCRIPT 0:00

Time: 2026-10-25 17:22 UTC

## Verdict
PASS WITH FIXES. All numbers, dates and links match the sources (I opened the two DCSA pages and the BSI page; via a summarising fetch tool, so quotes are as returned by it). Three wording problems let a judge read more than the sources say: the video line "is an inside job", the video sequence that runs from theft straight into "We built", and the FORM line "on paper". No mentor, ZIS or Paulo is named in any of the three; DEMO-SCRIPT line 21 even bans them.

## Source check
- DCSA Feb 2023: "Ocean carriers issue around 45 million bills of lading a year." / "In 2021, only 1.2%of these were electronic." Matches.
- DCSA soft-barriers page: "As of 2025, around 11% of bills of lading are issued electronically." The page does NOT say "ocean" for this figure and does not say "paper". Page undated (footer 2026).
- BSI 21 Apr 2026: "more than a fifth (22%) of global cargo theft incidents involved the cooperation of insiders", 2025 data, global. Matches.
- README links: first DCSA link = 45m page, second = 11% page, BSI link = correct page. All right. Weakness: the two "[DCSA]" labels look identical; the 45m figure carries no date.
- FORM table count: Problem solved = 589; I counted 589 characters. Matches.

## Findings
1. DEMO-SCRIPT, "More than one in five cargo thefts is an inside job." Overstates. Source: insiders cooperated in 22% of incidents (involved, global, 2025). "Inside job" says the theft was done by insiders. Replace: "In more than one in five cargo thefts, insiders were involved."
2. DEMO-SCRIPT, "We built a public record..." follows the theft sentence with no break, so it implies our build fixes theft and paper. The guard in PROBLEM-NUMBERS.md forbids that. Replace the last sentence with: "Those are market figures, not our results. We built a public record of each handover, on Stellar testnet."
3. DEMO-SCRIPT, "roughly nine in ten are still not electronic" with "45 million ... cross the oceans". The 45m is ocean (2021 data, Feb 2023); the 11% is unscoped "bills of lading" as of 2025. Joining them reads as one population. Fix: "About 45 million ocean bills of lading are issued a year, and DCSA says only about 11% were electronic in 2025." Keep "not electronic"; do not write "paper".
4. FORM-ANSWERS, "Goods in transit change hands on paper". "Paper" is in no source (PROBLEM-NUMBERS row 2 says so). Replace the opening with: "About 45 million ocean bills of lading are issued a year, and DCSA reports only about 11% were electronic in 2025; TT Club & BSI report that insiders were involved in 22% of global cargo thefts in 2025 (report published April 2026). These are market figures, not our traction." Also the heading "Problem solved" is the portal's field name; fine, but the next sentence must not say we solve them (it does not).
5. README, following sentence "In our working assumption ... many times" is still coherent, but it now follows hard numbers and reads as if the assumption covers them. Insert before it: "These are market figures, not our traction." Optionally label links "DCSA, Feb 2023" and "DCSA, 2025 figure", and add "(2023)" after the 45 million.
6. DEMO-SCRIPT line 21 says "No ... bill-of-lading claims" while the narration now talks about bills of lading. Reword line 21 to "No claim that our build handles bills of lading", otherwise a later reviewer will flag the row.

## Timing and layout (DEMO-SCRIPT 0:00-0:20)
- Words: 42 as written (about 13 s at 3.2 words/s, fits 20 s). With fixes 2 and 3 the line is about 52 words (about 16 s), still fits; cut "Every year" if the voice runs slow.
- Collision: none. Lower third 0:00-0:08, source line 0:08-0:20, same on-screen place is free. But the numbers are spoken at about 0:00-0:10 while the source line only appears at 0:08; the DCSA figures are said before their source shows. Better: show the source line from 0:03 and move the lower third to the bottom-left, or accept it. Not a blocker.
- The source line "DCSA 2023, 2025 · TT Club & BSI 2026" is correct; keep it.

## Not checked
Rendered video; real narration speed; the rest of FORM-ANSWERS and the deck; DCSA/BSI text beyond what the fetch tool returned (no raw HTML).
