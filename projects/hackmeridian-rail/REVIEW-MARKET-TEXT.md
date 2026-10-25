Role: reviewer
Reviewing: README "## Market and business model", FORM-ANSWERS "Problem solved" and "What's next" (Business model), AI_USAGE.md README row
Verdict: approve with changes
Reason: wording matches the approved sentences and no SWIFT amounts, PortMiami, TEU or traction appear; one rule clash (value and document count in one sentence) and one overclaim in AI_USAGE.

## Findings
1. [minor] README joins a value figure and a document count in one sentence, against MARKET-NUMBERS section 4 last bullet. Quote: "World merchandise exports were US$26.26 trillion in 2025 (WTO, Mar 2026), and ocean carriers issue around 45 million bills of lading a year (DCSA, Feb 2023)." The approved README sentence itself has this join, so section 4 contradicts itself. Not misleading ("and", separate sources), but it breaks the literal rule. Fix: "World merchandise exports were US$26.26 trillion in 2025 (WTO, Mar 2026). Ocean carriers issue around 45 million bills of lading a year (DCSA, Feb 2023)." Confidence: high. [FACT] (README, Market section).
2. [minor] AI_USAGE.md claims the market section was "checked by independent reviewer agents ... (market and business model, 2026-10-25)". True only for the numbers (MARKET-NUMBERS) and this pass. Claim becomes accurate once this file exists and finding 1 is applied, so edit and re-run first. Confidence: medium.
3. [note] The multi-chain row now says "9 hashes checked on Horizon" while the file list says 10 tx files. Out of scope, not verified here. Check that 9 vs 10 is intended.

## Checks (all pass unless listed above)
- (a) README: both paragraphs identical to the approved sentences (section 4 README, section 5 long). "market figures, not our volumes" and "no pilot or traction yet" present. "We are not affiliated with Swift." present. No SWIFT amount. No PortMiami/TEU (grep empty). "gap": only line 205 "Known gap" (contract limitation), no trade-finance gap at all. "{{": only the video URL, lines 7 and 29.
- (b) Problem solved: corridor sentence follows the form wording, with "These are market figures, not our traction." The 45M count and US$94.2B sit in different sentences. Text is exactly 880 chars (header limit 880). What's next: Business model sentence identical to the section 5 long sentence, "Our prices are not set", "not affiliated with Swift" present. Exactly 1334 chars (limit 1334); no room for edits.
- (c) see findings 2 and 3.

## Not checked
Sources behind the numbers were not re-opened; that was done in MARKET-NUMBERS. The 11% eBL and 22% insider figures in Problem solved are outside this brief.
