# Review: submission opening reframe (2026-10-26)

Reviewer subagent (role card: reviewer), Sonnet, 01:10 UTC. Verdict: approve with changes.

Reviewed: FORM-ANSWERS.md (title, tagline, Description opening, new API and mainnet-rehearsal paragraphs, Problem solved) and rio-miami-rail README.md (same opening, Problem, Architecture, rehearsal section, Built at).

Findings and what was applied:
1. High. The Hin Leong sentence next to the product implied the rail stops forged-document fraud (GTR, 18 Nov 2024, says forged documents were used; a dual-signed record does not stop forgery by a signer). Applied: cut. The WTO line stays as the size of the problem.
2. High. "five companies", "Nobody can prove", "one shared record for every company", "saved where no one can edit it", "checks the whole history in one call" overclaimed. Applied: "several companies and agencies (for example ...)", "No record is shared among them", "a shared record that each company on the route signs into", "hash chain that no one can rewrite (an administrator can freeze a shipment but cannot change past steps)", "check the whole history against one 32-byte value stored on the contract". Not applied: the reviewer's "That is the size of the market, not something this repo claims to solve" and the Swift disclaimer inside the opening (founder-voice rule; the disclaimer stays in What's next).
3. Medium. Title "SWIFT for goods" reads as a claim of equivalence. Reviewer proposed "Radox Custody Rail: shared custody for goods in transit, on Stellar". Not applied: the title is the owner's call (asked).
4. Medium. ADB never says "requested and approved". Applied: "ADB estimates the global trade finance gap at about US$2.5 trillion, unchanged from 2023 (Dec 2025)" plus a market-figures line; WTO marked "page undated" in the README.
5. Medium. Radox API paragraph in present tense. Applied: "will be able to ask"; "ran only in a local development run on testnet".
6. Low. Rehearsal numbers recomputed from proofs/mainnet-rehearsal.json: 15 applied, 9 refusals, protocol 29, wasm 8230ed93, 13.7249693 XLM charged. Applied: "(without the token and burn steps)", "all 15 transactions applied".
7. Low. Character counts and four proof sets confirmed; counts recomputed after the fixes.

Sources opened by the reviewer: gtreview.com Hin Leong article (18 Nov 2024), wto.org trade finance page (undated), adb.org ADB Global Trade Finance Gap Survey (Dec 2025). Library: [[wto-80-to-90-percent-of-98f6]], [[adb-trade-finance-gap-survey-dec-d033]], [[product-framing-rio-miami-is-the-34f9]].
