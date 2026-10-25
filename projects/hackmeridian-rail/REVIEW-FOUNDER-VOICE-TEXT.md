Role: reviewer
Reviewing: uncommitted founder-voice edits in ~/code/rio-miami-rail/README.md (+ threat model b790cdf), CUSTODY-SPEC.md, and projects/hackmeridian-rail/FORM-ANSWERS.md (as it stands on disk; `git diff FORM-ANSWERS.md` was empty at review time, so the file was reviewed whole)
Verdict: approve with changes
Reason: no false hard-line claim found, all hashes/numbers reproduce, but one claim points judges at evidence that is not in the repo, test counts disagree inside the README, two sentences go past what was checked, and note d820's Compared line is mislabelled.

## Findings (ranked by severity)

1. [major] [FACT] FORM-ANSWERS.md:36 - "returned the same head as `verify-head` (curl output in the README)". README.md has no curl output of the Radox API (only the Horizon curl at line 63). The only copy is API-PROOF.md, which is not in the repo. The edit also removed the README sentence "Only the curl output is evidence here; judges cannot reproduce it" (README.md:110), so the claim is now unmarked and the pointer is false. Confidence: high (grep `curl` README.md). Fix, two parts:
   - FORM-ANSWERS.md:36 replace `(curl output in the README)` with `(response excerpt in the README, Architecture)`.
   - README.md:110 append after "the same head as `verify-head` above.": 
     ` Response excerpt (GET /api/custody/shipments/31b4cff7…5e37, 2026-10-25 13:23 UTC): {"success":true,"data":{"status":"Delivered","seq":4,"head":"2d74fec064a6796c34be93ede6241e0e067650dcfb2e058382f2f9cf83195414", …}}.` (values checked against API-PROOF.md "Full backend boot"; the full-backend wording in README is true).

2. [major] [FACT] README.md:79 and README.md:180 - "`cargo test` # 24 contract unit tests (24 passed on 2026-10-25)" and "the contract, 24 unit tests and their snapshots". I ran `cargo test` (/tmp/rv-ct.log): `26 passed; 0 failed` (24 in `test::`, 2 in `prop_test::`). README.md:229 and FORM-ANSWERS.md:42 say 26. A judge who runs the line-79 command sees 26, not 24. Fix:
   - :79 `cargo test                     # 26 contract tests: 24 unit, 2 seeded property (26 passed on 2026-10-25)`
   - :180 `- \`contracts/custody_registry\`: the contract, 24 unit tests, 2 property tests and their snapshots.`

3. [minor] [FACT] README.md:204 - "**Audit.** Through the SCF Audit Bank, which opens to SCF-awarded projects." Raven (lumenloop, stellar.org blog 2024-03-28) says Audit Bank projects were chosen on "ecosystem participation, readiness for audit, and involvement in the Stellar Community Fund", not "awarded"; the Stellar docs (threat-modeling page) add that a threat model is a precondition for audits requested from the SDF Audit Bank. The 2024 source may be out of date, and the old wording ("only after an award") is also not in the source. The new line reads as a statement of eligibility fact that the source does not give, and the claims note says never "SCF-eligible". Confidence: medium. Replace with: `3. **Audit.** We plan to request an audit through the SDF Audit Bank, which prioritises projects in the Stellar Community Fund and requires a threat model first (see below).`

4. [minor] [FACT] README.md:131, README.md:218, CUSTODY-SPEC.md:107 vs note d820 - d820 says "two teammates signed with their own keys" is checked from the signatures, but "on their own computers" is not (only the proof file's own text says it). Lines still assert "from their own computers" / "teammates' own keys on their own computers" / "signed on their own computers". The remote-auth flow cannot prove the machine. The heading at :129 and :183 say the same. Fix:
   - :131 `In a second testnet shipment, two team members authorised their own handovers, each with their own testnet key. Only public keys…` (drop "from their own computers").
   - :218 last sentence `In the second shipment, two of the four custodians (Leo and Vhendala) signed with their own keys; the other keys were ours.` This also fixes an overclaim: warehouse, recipient, holder and operator keys stayed on one machine (README:131), so "used teammates' own keys" read as a cure for the "keys held by one party" row.
   - CUSTODY-SPEC.md:107 `where two custodians signed with their own keys.`
   - :129 heading `### Second shipment: two custodians with their own keys`. (If the owner confirms the machines in writing, keep the originals; the owner's words are then the source, say "by their account".)

5. [minor] [FACT] README.md:233 and FORM-ANSWERS.md:66 - "Radox is in conversations with ports, airports and chambers of commerce, and the next step is integrating their systems with the rail." Only the first clause is the allowed founder sentence. "The next step is integrating their systems" states a step involving those parties that nobody agreed to; a judge reads it as an agreed path. It names nobody and claims no deal, so not a hard-line break, but it is the one clause the allowance does not cover. Replace with: `Radox is in conversations with ports, airports and chambers of commerce, and our goal is to integrate their systems with the rail.` Same replacement in FORM-ANSWERS.md:66 (same phrase).

6. [minor] [FACT] FORM-ANSWERS.md:66 - "(a read-only Radox API endpoint already reads this registry)". "Already" in a forward-looking section reads as deployed. It ran only on a local development backend, on a private branch (README:110, FORM:108). Replace with: `(a read-only Radox API endpoint reads this registry in a local development run)`.

7. [minor] [FACT] FORM-ANSWERS.md:58 vs README.md:229 - FORM challenge 3: "An AI reviewer agent found two major bugs before deploy". README now says the review "led to the fixes in commit `9b66e00`" (REVIEW-THREAT-MODEL finding 4: the commit lists five fixes, "2 major" has no source). The two bugs named (revisit address let `deliver` succeed with zero handovers; instance TTL never extended) both appear in the commit message, so they are real, but "two major" is a label nobody can check and the text reads as the whole review. Replace: `3. An AI reviewer agent found, before the testnet deploy, that a route that revisits an address let \`deliver\` succeed with zero handovers, and that the contract instance TTL was never extended, so it could have archived about a week after deploy, possibly during judging. Both were fixed with tests (commit \`9b66e00\`, together with three more review fixes).` Length drop is small; the field has no stated limit but the header "1279 chars" must be recounted (rerun the length script).

8. [minor] [FACT] library: note d820 `Compared:` line, worse-note rule. It labels four older notes `coexists` while saying parts of them are superseded or dropped: 89a2 ("its 'None signed…' label is superseded"), ef38 ("its hedge rules are superseded where they conflict"), 34f9 ("the 'no such standard exists today' sentence dropped"), dadf ("the 'not our volumes' tag is dropped"). `coexists` is only for two notes that are both valid choices. Where they conflict, the older one is worse and must be marked, merged or retired. State on disk: 89a2 and ef38 carry a "Superseded in part" paragraph; 34f9 and dadf do not (grep "Superseded" finds neither). dadf rule 7 still orders "End with 'Market figures, not our volumes' … 'we have no pilot or traction yet'", which the README market section now contradicts; 34f9 line "Never write … that a standard exists" still binds and is not in conflict. A later session following dadf will re-add the hedge. Fix: change d820 entries for 89a2, ef38, dadf to `replaces in part (…)` with the conflicting rules named, add the same "Superseded in part (2026-10-25 19:40, owner)" paragraph to dadf rule 7 and to 34f9's "no such standard exists today" line, keep 34f9's no-names/no-adoption rules.

9. [note] [FACT] README.md:3 - "a shared, SWIFT-like standard for every company along a supply chain". Aspiration stated as fact of intent; no false claim ("We are building"). Keep, but "for every company" can be read as reach already claimed; optional: `for the companies along a supply chain`. Not required.

10. [note] [FACT] README.md:239 - "Vhendala, supervision and product review"; the claims note table allows "QA and review". Unchanged by this diff; owner to confirm the title (card question).

## Premises tested
| Premise | Evidence | Result |
|---|---|---|
| "26 tests" | `cargo test > /tmp/rv-ct.log`: 26 passed (24 unit + 2 prop) | true; README:79/180 still say 24 (finding 2) |
| Every tx hash in README/FORM | 38 full-length hash strings checked against proofs/*.json lifecycle+attest; all tx hashes match, remaining unmatched hex are keys/heads (31b4cff7, 8f32b176, 404c2ca9, 836ec9f9) and the deploy hash 328ceaa9 (present in multi-chain setup) | true |
| Shipment counts | lifecycle: 7 steps + 1 attest; three-machine: open + 3 handovers + deliver; multi-chain: deploy + 9 = "Ten successful transactions" (FORM:38) | true |
| "nine refused calls" | `failures` has 9 entries, hash_or_sim "simulation" | true |
| heads MATCH | `verify-head --selftest` ok; `--offline` MATCH for 31b4…, 8f32…, 404c…, 836e… (2d74fec0…5414, d9cf3a5f…, f4b1c906…, cb46738d…) | true |
| "both custodians' authorisation enforced by the contract" | lib.rs:310-311 `from.require_auth(); to.require_auth();`; deliver :377-378; `handover-signers.mjs` exit 0 "both signed" | true |
| Threat model cells vs lib.rs | errors #1/#2/#10 = WrongCustodian/OutOfRoute/NotFinal; pause covers open/handover/attest/deliver (require_not_paused) but not freeze; attest has no `require_open` (any status); no set_admin/set_operator; TTL 120_960/518_400 only in save/load/bump_instance/add_source/attest; "64 seeded cases" = `cases()` default 64; both single-signer unit tests exist | all cells true |
| REVIEW-THREAT-MODEL corrections applied | findings 1-7 and the new rows (operator route, refusal, sources, attests, read) all present in README:214-229 as proposed; row "Final custodian is also the holder" was correctly NOT added; "What the head proves" renamed "What a handover attests" with same content; "Who can read" cell "Public" instead of "Not private" | applied correctly |
| Hedge removal left no false sentence | Radox API local run: full backend boot is documented (API-PROOF.md, 13:23 UTC) so README:110 is true; second shipment: see finding 4; "Production path": item 1 (Radox mainnet gating) rests on KICKOFF.md note "re-check against origin/main before publishing" | see findings 1,3,4; item 1 not re-verified |
| Hard line | grep README/CUSTODY-SPEC/DEPLOYMENTS/page for Claude/Anthropic: none; no partner, port, airport, chamber, person or company named beyond the allowed sentence; no deal, users, customers or revenue; testnet, prior work and AI usage disclosures kept (README:168-174, 190; FORM:42, 108, 114) | pass |
| FORM field lengths | Title 72, Tagline 25 (<=120), Description 3773 (<=8000), Problem 775, Challenges 1279, What's next 1067, Prior work 1306, AI note 1083 all equal the stated numbers; tech stack 20 items (<=25) | pass (recount after finding 7) |
| "each with their own testnet key" | proofs/three-machine.json lists distinct leo and vhendala addresses; signatures verified by handover-signers.mjs | key part true; "own computers" unchecked (finding 4) |
| multi-chain run counts | README table 10 rows, FORM "Ten successful transactions", "third registry", "second shipment sharing two stops" (A-terminal, B-vessel) | true |
| CUSTODY-SPEC diff | removed "not a standard / no body reviewed / unaudited"; new Status line says "proposed open spec … Reference implementation … testnet" - nothing false; "unaudited" no longer in the Status line but README states it in the threat model | pass |

## Strongest contrary case
A hostile judge says: the new text sells a "rail" and "conversations with ports" while the repo is a single testnet contract with test keys, so the removal of every hedge is misleading. Answer in the text: the title still says testnet, "running on Stellar testnet" is in the first paragraph, the threat model states what is not enforced, prior work and AI usage are disclosed, and no number or partner is invented. The weak points a judge can still hit are findings 1, 2, 4, 5 (a checkable pointer that is false, a test count that disagrees with the command, and two statements about third parties/machines that nobody checked). Those are the real exposure; the tone is not.

## Pre-mortem
A judge runs `cargo test` as README:79 instructs and sees 26, not "24 passed"; opens the Radox API line, looks for the curl output FORM promises, finds none, and writes "evidence referenced but missing". With "the next step is integrating their systems" next to "conversations with ports" they ask the owner for the counterparty and get none. One credibility hit then colours the threat model, which is the strongest part. Missing control: a last-pass grep of every number and cross-reference between README and FORM (done here once; rerun after fixes).

## Never-skip checklist
- Library citations: done (d820, 89a2, 3e4f, ef38, bc05, 34f9, dadf opened); new finding not saved to library (see Library).
- Specialist's own checklist: not applicable (no specialist output reviewed; texts audited).
- Three premises tested: done (tests, hashes/heads, authorisation, hard line, threat-model cells, API evidence).
- Citations opened: done for SCF Audit Bank (Raven), API-PROOF.md, commit 9b66e00, proofs/*.json.
- Recomputed: test count, tx count, field lengths, tech-stack count, TTL arithmetic (120,960 x 5 s = 7 d; 518,400 x 5 s = 30 d).
- Contrary case, pre-mortem: done.
- Contradictions with library: done (finding 8).
- Owner manual work: none beyond one confirmation (question 1).
- Versions: not applicable.

## Not checked
- README:202 "Physical-asset offers on the Radox platform stay blocked outside testnet": source is KICKOFF.md ("re-check against origin/main before publishing"); radox-internal not opened.
- Market figures (US$94.2B, US$6.1B, US$26.26T) and the DCSA/TT Club numbers: source pages not re-opened; the diff did not change them.
- Which physical machines Leo and Vhendala used (not checkable from chain).
- Live Horizon: reviewed offline copies (`--offline`), not the live network.
- This review is not legal advice or a licensed audit; the contract is unaudited.

## Questions for the owner
1. Do Leo and Vhendala confirm in writing that they signed on their own computers? If yes, finding 4 changes to "by their account".
2. Is "Vhendala, supervision and product review" the title she approved (claims note says "QA and review")?

## Library
cited: [[founder-voice-in-public-text-sell-d820]] [[founder-statements-in-the-deck-open-89a2]] [[claims-hackmeridian-material-may-and-may-3e4f]] [[wording-the-rio-miami-deck-readme-ef38]] [[zis-in-public-material-radox-is-bc05]] [[product-framing-rio-miami-is-the-34f9]] [[wording-market-figures-in-the-deck-dadf]]
saved: none (read-only task; finding 8 is for the owner of d820 to apply)
