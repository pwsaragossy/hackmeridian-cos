# Review v13 delta 2 (corridor sentence)

Verdict: PASS, no must-fix. One optional tightening below.

1. Claims vs owner words. "Every port, airport and chamber that joins it joins the rail" is a true conditional: owner said "a zis fechando, nos fechamos" and "se adotar a zis, nos somos consequencia". It asserts no joiner exists. "In conversations with chambers of commerce" matches answer (1); ports and airports are not attributed to Radox. Weak point (not false): "the technology rail of" is the chief of staff's wording; the owner said "part of" and "grow together". Exclusivity is not in his verbatim words. If a judge asks "the only one?", answer "we are its technology rail, others may join". No text change required by the owner rule (no hedges).
2. Identifiability: "Rio-Miami trade-corridor initiative" plus "technology rail" lets insiders infer the initiative, no name, person or chamber is given. Allowed by the owner. "Custody layer" (slide 2) and "technology rail" (slide 4) agree: custody layer is this project, rail is Radox's role.
3. Slide 4 fits: render s-04.png, bottom paragraph two lines, no overflow, nothing under 18 pt flagged.
4. Ask and testnet labels untouched (pitch lines "Testnet, test keys" and the ask intact).
5. check_deck: exit 0, failures=0. Mutant in scratchpad/rev-mut3 (added "Ports and airports in the corridor have signed on to the rail" to slide 4, pdf touched): FAIL "slide 4: reads as a signed partner" (failures=1).
6. Spoken pitch: 392 words (limit 396), matches the stated count.
7. User Value: 8.5 (up from 8). The corridor line gives a channel and a market path with only true words; 9 still needs one first-hand "we spoke" line from a named-type counterparty.

## Versions
- v1: sentence as applied. Outside judge: check_deck 0, mutant fails, 392 words. Passes.
- v2: swap "the technology rail of" for "part of ... and its technology rail" (owner-verbatim safe). Costs 3 words (395), still under 396. Optional.
- v3: add "Brazil and Miami" chamber count only if the owner supplies a number or a one-line written "we spoke"; this is the step to 9, not a rewrite.
