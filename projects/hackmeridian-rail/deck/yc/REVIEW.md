# deck/yc review, 2026-10-26

Reviewer subagent (role card reviewer, claude-sonnet-5-5), ~04:40 UTC: approve with changes. No hard-limit breach (no partner, port or chamber named; no customers or revenue; no mainnet claim for custody_registry; no Hin Leong; no hosted-API claim). Numbers recomputed from proofs/*.json and contract sources: 7 tx, 9 refusals, 15 rehearsal tx, 26 tests, 13.72 XLM.

Applied (build.py), then check.py OK:
1. Slide 10: Leo "reviewed the contract, the signing logic and the proofs" (AI_USAGE.md: an AI agent wrote it); Vhendala "Supervision and product review" (README); Pedro's mainnet contracts marked "before the event ... (prior work)".
2. Slide 6: refusals "rejected in simulation"; rehearsal "Dry run on a local copy of mainnet state, nothing sent to mainnet ... simulated fees".
3. Slide 5: lender line in future tense.
4. Slide 7 headline no longer says trade runs on our records.
5. Slide 4 "customs" (not brokers); slide 2 "five parties"; slide 9 drops "to the Radox API"; cover adds "Running on Stellar testnet."
6. check.py BANNED gained the signed/agreed-partner, "ran on mainnet" and "customs brokers" patterns.

Open: name on slide 10 is "Pedro Wakigawa Saragossy", README says "Pedro Saragossy" (kept; both are the founder). check.py's number trace accepts small integers anywhere (ceiling: string filter, not a claims judge).

## Slide 5 rewrite, 2026-10-26
Owner rejected the connections slide. Marketing specialist drafted per-user values from FORM-ANSWERS and the contract; reviewer (approve after changes) cut "carries its own history" (the record points to the token), "when the goods left you" (no timestamp in the record) and "money can rely on" (no lender uses it yet). Applied; check.py OK.

## Specialist pass on slides 1-4, 6-10, 2026-10-26 ~05:00 UTC
Owner asked for pitch-deck-architect + specialists on every slide. Product (2-4, why-now), marketing (1, 9, 10), researcher (7), finance (8), engineer (6; 5 three-machine hashes re-checked on Horizon testnet). Main session kept the mainnet-fork dry-run line on slide 6 (brief requires it) against the engineer, and used the contract fact on reads instead of "free" (pricing is the owner's). Reviewer: 6 fixes applied (DCSA 5.7% Jan 2025 instead of 1.2%->11%, founder-only mainnet headline, pricing-neutral slide 8 headline, gross fee, per-bill wording, SCF Build application). check.py OK.
Open for the owner: repo link on slide 10 is dead until the repo is public.
