# Product decisions: User Value and Ecosystem (deck v12 -> v13)

Role: product. Date 2026-10-25. Decisions, not final copy. Deck stays at 10 slides.
Library used: [[claims-hackmeridian-material-may-and-may-3e4f]], [[zis-in-public-material-radox-is-bc05]], [[product-framing-rio-miami-is-the-34f9]], [[hackmeridian-rubric-7-criteria-weights-scored-50e2]], [[hackmeridian-scale-intake-as-submitted-the-7fb5]], [[iata-one-record-is-a-live-e27f]], [[wording-the-rio-miami-deck-readme-ef38]]. Saved: [[founder-statements-in-the-deck-open-89a2]].

Answer: change slides 2, 4, 7 (and one line each on 5 and 9); test first, then ship. Ecosystem can plausibly reach 9; User Value will not reach 9 without a third party confirming the pain, so the ambition is met for Ecosystem only.

## 1. Which slides change, and why (per rubric criterion)

Rubric: User Value and Problem (20), Ecosystem Alignment (20) ([[hackmeridian-rubric-7-criteria-weights-scored-50e2]]). Reviewer today: User Value 7, Ecosystem 8 (deck/REVIEW.md "v11 rubric per criterion").

| Slide | Change | Criterion it moves | Why |
|---|---|---|---|
| 2 Problem | Add "why it stays on paper": legacy systems at ports and airports are hard to integrate | User Value | Today the slide proves the problem exists (45M, 11%, 22%) but not why nobody has fixed it. A hard-to-integrate installed base is the missing "why not solved" |
| 4 Proposal | Replace "none confirmed" line with the founder-statement line on open conversations; add one clause tying "integrate once" to legacy systems | User Value, Ecosystem | This is where the standard and the buyer's integration cost already sit. The founder statement belongs next to the claim it supports |
| 5 Rail | One future-tense line: port and airport systems would connect by API | User Value | Pedro's "supply chain de ponta a ponta": slide 5 is already origin-to-delivery; it only lacks the how-do-legacy-systems-join line |
| 7 Why Stellar | Row 03 (burn) becomes "Any Stellar asset, one record format" | Ecosystem | Row 03 repeats slide 5. The new row is the only place the ecosystem-reuse argument is made as a feature, not a footer sentence |
| 9 Market/Ask | Now/Next line gains one "Next" item; ask untouched | Ecosystem | Next list is where future-tense adoption belongs |
| 1, 3, 6, 8, 10 | None | | Slide 6 and 8 carry Technical, Progress and disclosure; touching them risks regressions |

## 2. Per changed slide: job, claims, labels, cuts

Labels: S = sourced (footnote), F = founder's statement (says "per the founder, 25 Oct"), P = proven by our own artefact (file named), FUT = future tense.

### Slide 2: job = prove the pain and why it persists
| Claim | Label | Notes |
|---|---|---|
| "Ports and airports run legacy systems that are hard to integrate" | S once the researcher lands it: {{R: legacy-systems figure}}. Until then F | Never state without one of the two labels. A figure plus its source beats the founder label |
| "A corridor like this needs a shared custody record to move off paper" | F, held for owner OK | Pedro said the corridor project "could not leave paper without this". That is a claim about a third party's dependency; it implies a relationship ([[zis-in-public-material-radox-is-bc05]]). Default: leave out of the slide, say it in the spoken pitch as "in the founder's view". Fallback line is drafted in Open questions |
| Existing hypothesis line, 45M, ~11%, 22% | S, unchanged | |
Cut for room: the "Jan 2025 guide: 5.7%" parenthetical (move to notes); shorten the bridge "Context" line to one sentence, same unnamed wording as today.

### Slide 4: job = say what the standard is and who it is for, honestly
| Claim | Label | Notes |
|---|---|---|
| Integrate once: 10 links vs 5 | P arithmetic, unchanged | |
| "Per the founder (25 Oct): conversations are open with several ports, airports and chambers of commerce. None signed, none named, none confirmed." | F | Keeps the string "none confirmed" that check_deck REQUIRED needs. Do not use "in talks", "partners", "working with", "doors open", "receiving our technology" (all banned or traction-smelling) |
| "A legacy port or airport system would reach the rail through one adapter to the Radox API" | FUT | The API is Radox's and closed; say so in the same box (already in the right column) |
Cut for room: the "Radox is the rail, never the issuer. Regulation stays with the client" line moves to slide 8 notes; merge "still need a key and one connection" into the integrate-once sentence.

### Slide 5: job = origin-to-delivery chain, built vs design
| Claim | Label |
|---|---|
| Lifecycle on testnet, test keys | P, unchanged |
| "Port and airport systems would connect through an API, not a rewrite" | FUT, design |
Cut: the keyed-by/bill-of-lading footnote shrinks to its bill-of-lading half; sha256 detail already lives in CUSTODY-SPEC.md.

### Slide 7: job = why this belongs on Stellar and why other Stellar projects gain
| Claim | Label | Notes |
|---|---|---|
| "The record stores a token address and never calls the token, so it is not tied to Radox's token" | P: `contracts/custody_registry/src/lib.rs` lines 62, 87, 278; grep finds no token call | Present tense is allowed here as a design property |
| "Another Stellar issuer could use the contract or implement the spec today (Apache-2.0, CUSTODY-SPEC.md)" | P (licence, spec); "could", not "does" | Add "No one else has yet" in the same breath |
| "Any tokenized Stellar asset would get access through the Radox API: onboarding, then API calls, from open to delivery" | F + FUT | Pedro: "acesso para qualquer ativo stellar tokenizado seguindo nosso padrão ... por meio de APIs". Say "would", name it "the plan", and add "API not connected in this build" unless a hash proves otherwise ([[hackmeridian-scale-intake-as-submitted-the-7fb5]] makes the API connection the conditional must-have) |
| "Adoption would be large" | CUT | Pedro's word "absurda" is a forecast. It cannot be sourced; it scores as hype |
| Neighbours line, "found none", no SEP | S, unchanged | Keep Pipeline ([[iata-one-record-is-a-live-e27f]] also supports citing existing standards; consider one clause "can reference IATA ONE Record for air" only if the owner wants it, low confidence) |
Cut for room: row 03 (burn) and the second sentence of row 02; slide 6 already shows the head check.

### Slide 9: job = market, model, ask
Only the Now/Next line changes: Next gains "open the rail to other Stellar tokenized assets through the API". The ask stays word for word. No pricing text added, no flow of funds drawn.

## 3. The two stories

User Value (3 sentences). Goods change hands across companies whose records stop at their own door, and the systems at ports and airports are legacy and hard to integrate, so a shared record has stayed on paper {{R: legacy-systems figure}}. We built the record and proved it on testnet with test keys, and the founder says conversations are open with several ports, airports and chambers of commerce, none signed and none named. The first user is the person who must trust the chain before paying, and the first test is one Rio-Miami shipment, none agreed yet.

Ecosystem (3 sentences). The record is a small open contract and a proposed spec, and it stores a token address without ever calling the token, so any Stellar tokenized asset could carry a custody record. The managed way in would be the Radox API, which stays closed, so another issuer would onboard and call it instead of building adapters. None of this is used by anyone else yet: it is the plan, and the next step is one pilot shipment.

## 4. The three biggest overclaim risks and their guards

1. "Open conversations" read as a partnership or traction (a judge sees "ports, airports, chambers" and counts them as relationships).
   Guard: fixed wording with the label and the three negatives in one sentence; one sentence only, on slide 4, repeated nowhere else; never in the title, cover or ask. check_deck: any slide containing "conversations" must also contain "per the founder" and "none signed" (REQUIRED-together rule). New banned regex (case-insensitive; it does not match "both sides sign", "dual-signed", "signed by both custodians", "none signed"; tested on 6 bad and 8 good strings):
   `\b(?:(?:signed|agreed|confirmed|committed|onboarded|joined)\s+(?:partners?|ports?|airports?|chambers?|carriers?|banks?|institutions?|operators?)\b|(?:ports?|airports?|chambers?(?:\s+of\s+commerce)?|carriers?|banks?|institutions?)\s+(?:have|has|had)\s+(?:signed|agreed|joined|committed|confirmed)\b|(?:signed|agreed)\s+with\s+(?:a|an|the|several|one)?\s*(?:ports?|airports?|chambers?|banks?|institutions?|operators?))`
   (check_deck already bans bare "partner(s)", "in talks", "working with", "partnership".)
2. "Any Stellar asset can use it, easily, end to end" read as a live product, or the closed API read as open.
   Guard: present tense only for the verified property (token address stored, never called); everything about the API and other issuers uses would/plan; the same slide states "API closed, Radox's" and "no other issuer has used it". Add banned regex `\b(any|every|all)\s+(tokenized\s+)?(stellar\s+)?assets?\s+(can|already|now)\b`, and `\bcomplete ease\b|\bseamless\b|\badoption (will|would) be\b`. If no API-connection hash exists, the slide says "API not connected in this build" (STATE.md has the cut rule).
3. The corridor initiative or its leader implied as dependent on us, or as our customer ("the project could not leave paper without us"), through the unnamed bridge line.
   Guard: not on the slides unless Pedro approves the softened line; the existing bridge line is not extended; no "needs", "depends on", "relies on" within a sentence that contains "initiative" or "corridor". Regex: `(initiative|corridor)[^.]{0,80}\b(needs?|depends?|relies|could not|cannot)\b`.
   Also: the legacy-systems claim must carry S or F; a "legacy" sentence with neither label fails (`\blegacy\b` requires a footnote digit or "per the founder" in the same text box).

## 5. Predicted scores (my estimate, not a judge's)

| Criterion | Now | Predicted | Why |
|---|---|---|---|
| User Value and Problem (20) | 7 | 8 (range 7-8) | Gains: a "why it persists" reason with a source, the first user and test named, founder statement visible and honest. Held back: no customer, no written confirmation, and the reviewer already marked it capped near 7 until one exists. Founder-statement text counts as weak evidence ("owner opinion is a hypothesis, not evidence", product card). 9 needs one third-party confirmation (a shipper, forwarder or bank, in writing) |
| Ecosystem Alignment (20) | 8 | 9 (range 8-9) | Gains: the token-agnostic property is verifiable in code, the spec is open, reuse by other issuers is a concrete feature on slide 7, neighbours are named honestly. Held back: no issuer has adopted it and the API route is closed and possibly unconnected; reviewer's 10 asks for one named ecosystem partner, which we cannot get |

Ambition check: target "9 or more on both" is likely met for Ecosystem and not for User Value. Reaching 9 on User Value needs a fact only the owner can produce.

## What would change the conclusion
A sourced figure on legacy port/airport integration (researcher) raises User Value by about one point. A written confirmation from any real shipper or bank, or a signed letter from a port or chamber with the wording they approve, lifts the cap. A finding that the API connection was cut removes the "via API" line from slide 7 and lowers Ecosystem to 8.

## Versions (lenses run on my own draft, judge = rubric note applied slide by slide + claims table)
- v1, lens "goal behind the goal" (what does a judge need to believe): Pedro's two statements placed as bold claims on slides 2, 4, 7. Judge: fail. Reads as traction on slide 4 and as a live product on slide 7; "adoption absurda" is unsourced.
- v2, lens "rawest material": built on what exists in the repo (the token is never called; spec is open; REVIEW.md ban list). Moved the ecosystem claim to a verified present-tense property and the rest to future tense. Judge: pass on claims table, but User Value still just a statement.
- v3, lens "outside judge, hostile reader of the founder line": added label "per the founder, 25 Oct", the three negatives, and the REQUIRED-together and regex guards; cut "complete ease" and "absurda". Judge: pass, 12 claims checked, none reads as signed or endorsed.
- v4, lens "who does this work / skim test": cut the corridor-dependency sentence from slides (third-party claim); made legacy sentence need a source slot; cut duplicate rows (burn on slide 7, 5.7% parenthetical). Judge: pass; UV predicted 8, Ecosystem 9.

## Never-skip checklist (product card)
- [x] Library claims cite [[id]]; one new note saved ([[founder-statements-in-the-deck-open-89a2]]) with Compared lines.
- [x] Target user in behavioral terms: the financier who must see who holds goods before paying, and the port/airport/carrier operator who must integrate a record. Access path: none confirmed; founder says conversations are open (F).
- [ ] Problem has behavior evidence: partial. DCSA 11% electronic and TT Club insiders 22% are behavior data; the pain for a named user is still hypothesis, stated on slide 2.
- [x] Existing alternative with cost: paper and each company's own system; cost via R$900M, US$85M on slide 3; legacy-systems cost pending {{R: legacy-systems figure}}.
- [x] Out of scope: no USD leg, no prices, no named parties, no mainnet, no other issuers live.
- [x] Empty/error/first-use states: not applicable to a deck; the demo page states are Leo's.
- [x] Effort: unvalidated estimate; text-only edits to build_deck.py, check_deck.py new rules about 1 hour.
- [ ] Success metric: baseline 0 users, 0 pilots; target one pilot shipment by the SCF round (Nov 8 is the SCF close, not a promise); kill criterion: no institution agrees to a pilot by end of 2026 means the standard story is dropped. Needs owner confirmation of the dates.
- [x] Riskiest assumption: that ports and airports will connect at all. Cheapest test: one written yes/no from one port or chamber on a one-page ask.
- [x] Accessibility basics: slide text stays at 18 pt or more (check_deck already enforces); no colour-only meaning added.

## Not checked
The researcher's figures (not yet landed). Whether the Radox API connection delivered (no hash found). I did not edit build_deck.py or check_deck.py. I read slide text from the PDF, not the PNGs. IATA ONE Record spec read only as summaries (low confidence).

## Open questions for the owner (project card)
1. May the unnamed corridor initiative be described as "needing a shared custody record to leave paper", labelled "founder's view"? Default: no. Fallback line if yes: "In the founder's view, a Rio-Miami corridor needs a shared custody record to move beyond paper."
2. Is the Radox API connected for this build (hash)? Decides whether slide 7 says "API not connected in this build".
3. Confirm the pilot target date and the kill criterion in the checklist.
4. Which chambers, ports and airports could give a one-line written "yes, we spoke" with permission to say "one port"? That is the only route past User Value 8.

## Library
cited: [[claims-hackmeridian-material-may-and-may-3e4f]] [[zis-in-public-material-radox-is-bc05]] [[product-framing-rio-miami-is-the-34f9]] [[hackmeridian-rubric-7-criteria-weights-scored-50e2]] [[hackmeridian-scale-intake-as-submitted-the-7fb5]] [[iata-one-record-is-a-live-e27f]] [[wording-the-rio-miami-deck-readme-ef38]]
saved: [[founder-statements-in-the-deck-open-89a2]]
