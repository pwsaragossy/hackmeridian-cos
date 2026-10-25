Reviewer: independent reviewer subagent (role card reviewer), briefed by session-hackmeridian-rail; work reviewed: rail reframe (DEMO-SCRIPT 0:20 and 2:30, README lead, FORM Description lead)

Time: Sun Oct 25 17:48 UTC 2026 (`date -u`)

## Verdict
PASS WITH FIXES. No claim of use, partner, mentor, chamber, port or airport is made; the present tense is confined to what ran on testnet. Five wording or timing fixes below; none is a blocker, F1 to F4 should be applied before recording.
Notes consulted: [[wording-the-rio-miami-deck-readme-ef38]], [[claims-hackmeridian-material-may-and-may-3e4f]], [[product-framing-rio-miami-is-the-34f9]] (the owner's framing matches the new order).

## Checked and OK
- 0:20 narration: 50 words = 15.6 s at 3.2 words/s, in a 20 s slot (4 s slack for the command run). It fits the screen: goal and "none exists" (29 words, about 9 s) play while the command is typed and run; "seven successful transactions" (last 7 s) lands as the 7-line listing shows. Seven lines = open, 4 handovers, deliver, redeem: matches "from open to burn".
- 2:30 narration: 71 words = 22 s in a 30 s slot (8 s slack for the hold on MATCH).
- Ask: "introductions to one financial institution and one port, airport or logistics operator for a first pilot shipment, and a Stellar engineer's review of the design" is word for word the deck ask (build_deck.py l.363-364); the script only adds "Our ask:".
- "SWIFT-like" is the deck's own wording (slide 1 l.179, slide 9 l.349). A "-like" comparison states the model, not an endorsement; no logo, no SWIFT person or body named. Keep it.
- Nothing named: no partner, mentor, chamber, port, airport.
- Tense: "Our goal is" (goal), "could/would" (conditional), "exists yet" (negative present), "What ran" (past). "is a Soroban contract where every handover is authorised" in the README is present tense about something that ran on testnet: acceptable.

## Findings (ranked)

**F1 (medium) "None of that/it exists yet" next to "this repo is its first link" contradicts itself.** The contract exists; "none of it" includes the repo. In speech "that" is also ambiguous after a long sentence. Name the two things that do not exist.
- DEMO-SCRIPT 0:20 narration, replace with:
  "Our goal is an end-to-end rail for goods in transit: a shared, SWIFT-like custody standard that companies along a supply chain, from origin to destination, could use. Neither the standard nor the rail exists yet. What ran on Stellar testnet, with test keys held by one harness: seven successful transactions, from open to burn."  (52 words, 16.3 s)
- README line 3 and FORM "### Description" first paragraph (keep the two identical), replace with:
  "**Our goal is an end-to-end custody rail for goods in transit: a shared, SWIFT-like standard that companies along a supply chain, from origin to destination, could use. Neither the standard nor the rail exists yet. This repo is the first piece we built, run on Stellar testnet: a Soroban contract where every handover is authorised by both custodians, hash-chained, and checkable by anyone from public data.**"

**F2 (medium) "every company ... would join once".** "Every company" is a universal nobody can promise; "join once" is vague. It is conditional, so not a use claim, but it reads as a sales promise. The F1 texts replace it with "companies along a supply chain ... could use".

**F3 (medium) 2:30 row: MATCH is clicked at 2:47 but spoken at about 2:53.** At 3.2 words/s "Verify head: match" comes after the ask, while the click happens during the ask. Reorder so the ask plays over the held MATCH, and move the click earlier.
- Narration, replace with:
  "The public shipment page reads it from the chain, on Stellar testnet: container TEST4627832, delivered, four of four handovers. In a local test run, the Radox backend reads the same record and returns the same head. Verify head: match. Rio–Miami is our pilot corridor. Our ask: introductions to one financial institution and one port, airport or logistics operator for a first pilot shipment, and a Stellar engineer's review of the design."
- Screen cell: change "2:38–2:45" to "2:38–2:42", and "2:45: back to the page; at 2:47 click" to "2:42: back to the page; at 2:44 click".

**F4 (low-medium) Flow 0:00 to 0:20.** Row 0:00 ends "We built a public record of each handover" and 0:20 opens "Our goal is ...". The owner's order is problem, standard, rail, proof. Smallest fix, last sentence of 0:00: "Our answer starts with a public record of each handover, on Stellar testnet." Then 0:20 reads as "here is where it goes, here is what ran". Row 0:40 opens "The first handover" and follows 0:20 cleanly.

**F5 (low) README "## Future" duplicates the lead.** Line 179 ("Rio–Miami is the first corridor... We aim to grow this into a shared standard ... as SWIFT did ...") repeats the goal now in the bold lead. Keep only what the lead lacks. Replace with:
  "Rio–Miami is the first corridor, not the product. We intend to approach chambers of commerce, ports and airports about integrating their systems. No such standard, integration, adoption or partnership exists today."

## Smaller notes (no fix needed unless the owner wants)
- Vocabulary: deck and script say "pilot corridor"; README says "first corridor". Both pass, but "pilot corridor" implies a pilot, and deck slide 9 itself says "none agreed yet". Optional safer script wording: "Rio–Miami is the corridor we propose for a first pilot."
- The old lead said "proven on Stellar testnet"; the F1 text says "run on", which is safer.
- The bold lead is three sentences, about 75 words; the honest "Neither ... exists yet" sits in bold in sentence two. Deliberate; passes the honesty rule.

## Not checked
- Rendered slides 1 and 7 (read only the code strings in build_deck.py, l.179 and 347-364); FORM-ANSWERS.md fields other than the Description lead; real narration speed (counted, not timed); whether the 2:44 click and cuts fit the final edit.
