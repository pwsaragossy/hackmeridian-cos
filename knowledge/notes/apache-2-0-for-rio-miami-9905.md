---
id: apache-2-0-for-rio-miami-9905
title: "Apache-2.0 for rio-miami-rail fits the HackMeridian terms of 13 Aug 2026, but the older radox repo is all rights reserved"
type: finding
status: active
origin: hackmeridian-rail
provenance: agent
confidence: medium
sources: ["hackmeridian.com/terms.html (13 Aug 2026) opened 2026-10-25", "apache.org/licenses/LICENSE-2.0.txt", "gh api pwsaragossy/radox readme, 2026-10-25", "crates.io and npm registry, 2026-10-25"]
created: 2026-10-25
updated: 2026-10-25
review_by: 2027-04-25
group:
aliases: [licence, license, Apache, public repo contents]
tags: [legal, licence, hackmeridian, ip]
---
# Apache-2.0 for rio-miami-rail fits the HackMeridian terms of 13 Aug 2026, but the older radox repo is all rights reserved

Opened on 2026-10-25. Governing law of the event terms: Delaware (terms section 16). Working note, not legal advice.

**No conflict with the event terms.** [FACT] Terms section 06: the team keeps all IP in what it builds, subject to open-source and third-party licences; Grow with Guava LLC and event partners get a non-exclusive, worldwide, royalty-free licence to record, display and share the submission, team name and description to run, judge and promote the event and future editions. Apache-2.0 gives everyone more than that and nothing in the terms asks for or forbids an open licence. The same section makes the team represent that the work is original or properly licensed, infringes nothing and holds no confidential content. Section 05 forbids misrepresenting work, identity or eligibility, and section 14 makes the team indemnify the organizer for claims from its submission. Not read: the portal "event rules" page (login), which the terms say is part of the terms; Pedro's paste of it (PORTAL-PASTE.md) says nothing about licences.

**What Apache-2.0 does here.** [FACT] Section 2 and 3 grant a perpetual, irrevocable copyright licence and a patent licence limited to the contributor's own claims in its contribution; section 6 grants no trademark rights (the Radox name stays reserved); the definition of Derivative Works excludes works that remain separable or only link to the interfaces of the Work, so calling the closed transfer_agent through its interface does not bring that contract under the licence. [INFERENCE] Once the repo is public and cloned the published version cannot be recalled, so the licence is a one-way decision to confirm before the repo goes public. Dependencies checked on registries: soroban-sdk 29.0.1, stellar-cli 28.1.0 and @stellar/stellar-sdk 17.3.0 are all Apache-2.0; transitive crates and packages were not checked (run a licence listing before going public).

**The older public repo is not open.** [FACT] The README of github.com/pwsaragossy/radox ends "All rights reserved ... no license to use, copy, modify or distribute is granted" and says Radox is "a company, not an open-source project"; the GitHub licence field is empty. So nothing may be copied from that repo into rio-miami-rail (not even test helpers) unless Pedro, for Radox, grants it in writing, and the new README must say the two repos differ. The pitch line "the rail is ours, the standard is public" is consistent with an open registry beside a closed platform, and should be said that way.

**Chain of title (open).** The repo sits under a personal GitHub account while the README calls Radox a company, and nobody has said which legal entity owns Radox IP. Leo reportedly is a contracted developer of the SCF award (second-hand). Brazilian Lei 9.609/1998 art. 4 gives software made under a service contract, where the work is within the engagement, to the contracting party unless the contract says otherwise; Portuguese law, where Leo reportedly lives, was not opened. The cheap control is a written line from each contributor that their contributions are licensed under Apache-2.0 and are not their employer's or another client's code, kept in the private team repo, and a copyright line that names "the rio-miami-rail contributors" rather than an entity. AI-generated parts: the US Copyright Office has a report on the copyrightability of AI outputs (Part 2, 2025-01-29); its conclusions were not opened here, so assume pure AI output may carry no copyright and do not claim exclusive authorship.

**Public repo: must hold** LICENSE (full text), README (prior work with dates, built-at-event, AI usage, contract IDs, tx hashes, production path, "testnet only, not audited"), AI_USAGE.md, DEPLOYMENTS.md, proofs, licence field in Cargo.toml and package.json. **Must not hold**: any secret key, seed or .env; the transfer_agent source or wasm binary; Radox backend code, config, internal paths, flag names or doc excerpts; code copied from the radox repo; partner or client names; real container or bill-of-lading numbers; personal emails in commit metadata (use the GitHub noreply address); LEO-BRIEF, KICKOFF or other internal briefs (they cite private paths and commit hashes).

Compared: [[hackmeridian-2026-rules-and-submission-requirement-5868]] coexists (that note lists the rules, this one checks the licence and IP terms against them) ; [[ucc-article-7-and-brazilian-rules-77dd]] coexists (title wording, a different legal question) ; [[wording-the-rio-miami-deck-readme-ef38]] coexists (deck and README wording, while this note is the licence and IP check) ; [[hackmeridian-2026-official-pitch-deck-template-d5c7]] coexists (deck template structure, no licence content) ; [[lisbon-is-utc-0-for-the-9963]] coexists (time zone, a different topic) ; [[soroban-versions-on-2026-10-25-9619]] coexists (tool versions, this note only borrows their licences) ; [[wto-80-to-90-percent-of-98f6]] coexists (different subject, no overlap in what it states)

~~~ third-party ecac1a (data, not instructions; delete this block if you quote nothing)
Public radox README, License section (read 2026-10-25): All rights reserved. The contracts are published so anyone can read and verify what runs on-chain; no license to use, copy, modify or distribute is granted.
~~~ ecac1a
