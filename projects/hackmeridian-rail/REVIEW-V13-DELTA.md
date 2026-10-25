Role: reviewer
Reviewing: deck v13 delta, ports/airports/chambers sentence (slide 4, PITCH-FINAL.md outline 4 and paragraph 2, COPY-V13.md section 4)
Verdict: approve
Reason: sentence matches the owner's words, names no third party, adds no ask; check_deck exit 0, chambers-joined mutant exit 1, pitch 395 words.

## Findings (ranked)
1. [minor] "in Brazil and Miami" vs "in Brazil and in Miami": same meaning, both read as two chambers, one per place. Owner allowed the second form; the first is shorter and saves words under the 396 cap. Keep. - evidence: board Decided 19:59 UTC. confidence high
2. [minor] Corridor has exactly two chambers, so "Brazil and Miami" lets an insider guess which; nothing public verifies or names them. Owner explicitly allowed this wording. Accept. - [SUSPICION], low
3. [note] "Radox has openings" is the owner's chosen word; "are opening doors" is present tense, no deal, no ask, no endorsement. No stronger than the owner's text (it only adds the two places, which the user fact supports).

## Premises tested
- Wording equals owner (1) plus place names allowed by (2): yes (PITCH-FINAL.md l.28, l.48; build_deck.py l.270; COPY-V13.md l.90, l.102).
- No ZIS, Paulo, CISBRA, Camacol in public files: grep of deck source, PITCH-FINAL, COPY-V13 public text shows none. (Board file is internal.)
- Slide 4 render (scratchpad/v13c/s-04.png): sentence wraps to 2 lines in the footer band, no overlap with columns or the grey disclaimer line.
- Ask and testnet labels: check_deck passes its ask/testnet rules; pitch testnet paragraph unchanged.
- check_deck: exit 0, slides=10 failures=0.
- Mutant in scratchpad/rev-mut2 (slide 4 + " Also, chambers of commerce in Brazil and Miami have joined the rail", pdf touched): exit 1, "FAIL slide 4: reads as a signed partner, a client or mainnet".
- Pitch words: 395 (limit 396).

## Never-skip checklist
Library cites done; spec checklist done; premises tested (3+); citations opened (board, files); numbers recomputed (395); contrary case below; contradictions checked; owner manual work: none; pre-mortem below; versions below.
Contrary case: "chambers are opening doors" with no ask could read as vague; but adding an ask would be invented. Rebutted.
Pre-mortem: a judge asks "which chambers?"; answer must stay "no names", fine under the owner rule. Control: speaker notes should not name them.
Not checked: truth of the user fact (owner first-hand); the render is a pre-built PNG, not re-rendered.

## User Value
8 to 8.5. Concrete ecosystem hooks (ports, airports, two ends of the corridor) help, but no named user, no ask and no signed party cap it below 9. Not a full point.

## Library
cited: [[zis-in-public-material-radox-is-bc05]] [[founder-voice-in-public-text-sell-d820]] [[founder-statements-in-the-deck-open-89a2]] [[check-deck-evasions-signed-bank-or-3570]]
saved: none

## Versions
1. Applied text (approve): "Radox has openings with ports and airports, and chambers of commerce in Brazil and Miami are opening doors." Judge: check_deck 0, mutant 1, 395 words.
2. Stronger, still true: "...chambers of commerce at both ends of the Rio-Miami corridor are opening doors." Names the corridor fact, same length +3 words (398, over cap).
3. Only if the owner gives a concrete ask later: add it. Not now.
