# Review: founder-voice narration, DEMO-SCRIPT.md (uncommitted diff)

Verdict: APPROVE WITH CHANGES. No outright falsehood found. Three changes needed, two optional. No self-deprecating hedge remains. Testnet is still spoken at 0:20, 1:05 and 2:30.

## Checked and true
- Redeem "signed by the holder": proofs/tx/864fd164....json envelope carries an address-credential auth entry for the key 5e54b33f... (holder GBPFJMZ7...) with a signature, beside the operator source account. README line 21/172: burn is not enforced by the registry, and the narration no longer claims it is. True.
- "Seven successful transactions" and "first piece runs on testnet today": README table rows 1-7. True.
- "Four of four handovers", match, exit zero: unchanged, true.
- Hard line: no partner named, no deal, no users or revenue. Held.

## Findings
1. MEDIUM, 2:30. Quote: "The Radox backend reads the same record and returns the same head." Heard alone, it sounds deployed. API-PROOF.md: NODE_ENV=development, localhost:3111. The caption "local test run" is on screen only and shows for 4 s. Replace: "The Radox backend, running locally, reads the same record and returns the same head."
2. MEDIUM, 2:30 timing. The row went from 71 to 75 words. Old speech ran 26.8 s and ended 2:57.4, so the new one ends about 2:59. Finding 1 adds 1 word, so it ends near 2:59.5, too tight. Dropping "In a local test run," also moves "backend reads" about 1.7 s earlier than the terminal clip at 2:38-2:42, and "Verify head: match" lands before the click at 2:44. Fix: cut "design" is not enough. Cut "for the first live shipment" (5 words) and keep the rest: "Our ask: introductions to a financial institution and a port or logistics operator, and a Stellar engineer's design review." Then regenerate row 2:30 and re-check the timestamps (backend line on screen 2:38-2:42, MATCH at 2:44).
3. LOW-MEDIUM, 0:00. Quote: "puts every handover on a public record, on Stellar." Testnet is only in the on-screen label here. Replace: "puts every handover on a public record, on Stellar testnet." (+1 word; the row has about 6 words of slack after the cuts.)
4. LOW, 0:40. Quote: "two teammates authorised from their own computers, with their own keys." Presented as fact; the repo (README, Second shipment) only says "by their account" the keys never left their computers. It is a factual attribution, not a hedge, and the judge cannot check it on Horizon. If you keep the rule strictly, use: "two teammates authorised from their own computers, with their own keys, and only signed entries were exchanged." Otherwise restore "by their account".
5. LOW, 0:40. Quote: "No project in the Stellar directories we searched does dual-signed custody." RESEARCH-raven.md §5 says only that no candidate is "custódia física com dupla assinatura" (semantic similarity, asOf 2026-10-24). Scope is physical goods. Replace: "No project in the Stellar directories we searched does dual-signed custody of physical goods." (+4 words; the row is 5 words shorter, so it fits.)
6. NOTE, 2:30. Quote: "Radox is in conversations with ports, airports and chambers of commerce." It is Pedro's own statement and nothing in the repo supports or contradicts it. It sits next to the ask for "a port or logistics operator" introduction; a judge may ask why. Keep, but have the Q&A ready with no names.

## Not issues
- "a shared, SWIFT-like custody standard for every company along a supply chain" is stated as the goal ("We are building"), not as a delivered thing. OK.
- 1:50 row is now 21 words in a 25 s slot; fine.
