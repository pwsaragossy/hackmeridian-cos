# Review: User Value and Ecosystem wording (README + FORM-ANSWERS)

Reviewer: independent. Date: 2026-10-25. Scope: uncommitted README diff in ~/code/rio-miami-rail, and the matching FORM-ANSWERS.md text (the form diff was empty when run: the change is already in commit dad26c8, so I reviewed the current text at the lines below). Source wording: COPY-V13.md section 4 and 5.

## Verdict
Approve with changes. No false factual claim and no name, deal, customer or revenue claim. Four wording changes are needed so every sentence is checkable. Two are major.

## Claim checks

| Claim | Result | Evidence |
|---|---|---|
| "stores a token address and never calls the token" | TRUE | contracts/custody_registry/src/lib.rs:62, 87 (field), 278 (stored in `open`). No token client, no `invoke_contract`, no `token::` in the file. Mint/burn are done by scripts/lifecycle.mjs against Radox transfer_agent (lib.rs:8-10). Apache-2.0: LICENSE and Cargo.toml:6 agree. Caveat the README itself states at README:233: `open` never checks that the address is a real token. "Any tokenized Stellar asset can carry a record" is true; so can any address. |
| "about US$4 billion ... (SDF, as of 1 Sep 2026)" | TRUE to its source, weak source | Note a455: SDF page "4 billion dollars ... as of September 1, 2026", confidence low, medium evidence, SDF is an interested party, the note says "my fetch tool paraphrases; re-open before quoting". A newer, lower figure exists (rwa.xyz US$3.75B, 25 Oct). Table leaders (Spiko, Ondo, Franklin Templeton) are financial assets, not goods in transit. |
| "found no Stellar project that records a handover signed by two custodians (LumenLoop, SCF and Scout, searched 24-25 Oct 2026)" | TRUE, one imprecision | aa39: LumenLoop/SCF/Scout searched 2026-10-24; Kutana added 25 Oct (LumenLoop + SCF data). 05ea: 25 Oct, LumenLoop + SCF, no Scout. RESEARCH-raven.md:3, 72-73: asOf 24-25 Oct; Scout was queried for SEPs (source=sep), not for projects. Dates are right. The note says "not found in these directories, not 'does not exist'", and the sentence keeps that scope. |
| "Radox will open API access to Stellar issuers, from onboarding to delivery" | FUTURE, not backed by present code | Claims table (COPY-V13:103) labels it a plan, "owner's words". Present state: one read-only endpoint `GET /api/custody/shipments/<key>`, private backend, local dev run only (README:112). No onboarding or delivery endpoint exists in the repo. |
| "a financier can see who holds the goods before paying" | PARTLY TRUE | `get(key)` returns `current_custodian` and `holder` (lib.rs:483, struct 60-69), and the page reads it. What it shows is who last signed as custodian, not a check of physical possession. No financier has used it and no payment step exists. The README's own table (README:233) says the registry does not verify the token holder. |

## Findings

### F1. [FACT] major. "a legacy system will join through one adapter to the Radox API" and "each company integrates once"
README.md:13 and FORM-ANSWERS.md:52 (identical text).
Quote: "With the rail, each company integrates once, not pair by pair: a legacy system will join through one adapter to the Radox API, and a financier can see who holds the goods before paying."
Problem: no company has integrated and no adapter exists; "integrates once" is present tense. The Radox API is private and exposes one read-only endpoint, so a judge who checks the repo finds no way for a legacy system to write. "Who holds the goods" claims possession; the record shows who last signed for custody.
Replacement:
"With the rail, each company will integrate once, not pair by pair: a legacy system will join through one adapter to the Radox API, and a financier can read which custodian last signed for the goods before paying."

### F2. [FACT] major. "from onboarding to delivery"
README.md:196 and FORM-ANSWERS.md:40.
Quote: "Radox will open API access to Stellar issuers, from onboarding to delivery."
Problem: future tense is correct and allowed (COPY-V13:103), but the span "onboarding to delivery" describes a full lifecycle API. Only one read-only endpoint exists, in a local run. A judge cannot tell plan from product, and the team cannot back the span today.
Replacement (no hedge, states present fact beside the plan):
"Radox will open API access to Stellar issuers, from onboarding to delivery; today one read-only endpoint reads this registry, in a local development run."
If the owner wants the shorter text, cut to: "Radox will open API access to Stellar issuers." and drop the span.

### F3. [FACT] major. Chambers "engaged" plus "their systems" reads as an endorsement or integration under way
README.md:239 and FORM-ANSWERS.md:68.
Quote: "Radox has openings with ports and airports, and chambers of commerce are opening doors: chambers of commerce in Brazil and in Miami are engaged with Radox on the corridor. Our goal is to integrate their systems with the rail."
Problems:
1. "engaged with Radox" is the owner-approved wording (board lines 56-57), but placed right before "integrate their systems", it reads as a relationship in which the chambers' systems are being connected. Chambers have no systems here; the claim table (COPY-V13:102) says "no deal, no endorsement".
2. The sentence says the same fact twice ("opening doors" and "engaged"), so the second clause adds risk and no information.
3. Central removed "their" before "legacy systems" in line 13 but "their systems" stays here.
Replacement (uses decision 1 and decision 2 once each, names nobody, no ask):
"Radox has openings with ports and airports, and chambers of commerce in Brazil and in Miami are engaged with Radox on the corridor. Our goal is to integrate ports' and airports' systems with the rail."
This keeps "engaged" (owner decision 2) and drops "opening doors" duplication and the ambiguous "their". If the owner prefers the softer verb only, use "are opening doors on the corridor" and drop "engaged".

### F4. [FACT] minor. Search scope in the novelty sentence
README.md:196 and FORM-ANSWERS.md:40.
Quote: "(LumenLoop, SCF and Scout, searched 24–25 Oct 2026)"
Problem: Scout was queried for SEPs, not for projects (RESEARCH-raven.md:72-73). A judge reading "no project ... Scout" may think Scout lists projects.
Replacement: "(LumenLoop directory and SCF submissions, plus Scout for SEPs, searched 24–25 Oct 2026)"

### F5. [FACT] minor. US$4 billion is one-sided and stale next to a lower, newer figure
README.md:196 and FORM-ANSWERS.md:40.
Quote: "Stellar holds about US$4 billion in tokenized real-world assets (SDF, as of 1 Sep 2026)"
Problem: note a455 holds both figures and says never mix. Quoting only the larger, older, interested-party figure invites a check on rwa.xyz that shows US$3.75B on 25 Oct. Also, most of the value is financial assets, so it does not size physical goods.
Replacement: "Stellar holds about US$4 billion in tokenized real-world assets (SDF, as of 1 Sep 2026; rwa.xyz shows US$3.75 billion on 25 Oct 2026), mostly financial products, and we found no Stellar project ..."
Before publishing, re-open stellar.org/solutions/real-world-assets: a455 says the fetch paraphrased the quote.

### F6. [FACT] note. Repetition
- README.md:239 repeats its own point twice (see F3).
- README.md:13 is word for word FORM-ANSWERS.md:52, and README.md:196 is word for word FORM-ANSWERS.md:40. That is intended (two documents) but any fix must be applied to both.
- Nothing in the README repeats the sentences between sections: "never calls the token" appears once, "legacy" once (line 13), "Radox will open API access" once.

## Hard-line check
- No partner named: pass (no CISBRA, Camacol, ZIS, Paulo in either file; grep clean).
- No signed deal, user, customer or revenue claim: pass.
- No concrete ask invented: pass.
- Founder voice, no self-deprecating hedge: pass. F2 adds a fact, not a hedge.
- Cross-check with [[claims-hackmeridian-material-may-and-may-3e4f]]: its table forbids "any name (... chamber ...)" and "endorsement"; the owner decision of 2026-10-25 19:59 UTC adds the first-hand fact, so "chambers of commerce in Brazil and in Miami" is allowed. [[zis-in-public-material-radox-is-bc05]]: no ZIS mention, pass. That note still lists chambers under "must not say" for names only; the library note 3e4f should get a line recording the owner's 19:59 decision so a later reviewer does not flag it.

## Strongest contrary case
A judge asks "who are the chambers and what did they do?" and the team cannot say. "Engaged with Radox" invites exactly that. The defence is the plain claim without a number or a name, and F3 shrinks the surface to one sentence.

## Pre-mortem
Most likely failure: a judge opens the repo, finds no adapter and no write API, reads "will join through one adapter" and "from onboarding to delivery" as a product that does not exist, and scores Ecosystem and User Value down for overreach. F1 and F2 fix that.

## Not checked
The live SDF page (a455 asks for a re-open); the text of the video and deck (only README and FORM were in scope).
