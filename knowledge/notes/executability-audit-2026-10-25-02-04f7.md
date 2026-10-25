---
id: executability-audit-2026-10-25-02-04f7
title: "Executability audit 2026-10-25 02:50 UTC: Leo invite pending, no page host named, CLI 28.1.0 vs protocol 29 untested"
type: finding
status: active
origin: hackmeridian-rail
provenance: agent
confidence: medium
sources: ["projects/hackmeridian-rail/KICKOFF.md", "projects/hackmeridian-rail/LEO-BRIEF.md"]
created: 2026-10-25
updated: 2026-10-25
review_by: 2027-04-25
group:
aliases: []
tags: []
---
# Executability audit 2026-10-25 02:50 UTC: Leo invite pending, no page host named, CLI 28.1.0 vs protocol 29 untested

Checked live 2026-10-25 02:49 UTC for the Mon 26 Oct 08:00 submission of hackmeridian-rail. (1) `gh api .../invitations` lists leo-schlanger as a PENDING invitee on both pwsaragossy/rio-miami-rail and pwsaragossy/hackmeridian-cos; the collaborators list holds only pwsaragossy, so Leo is not yet a collaborator. (2) The testnet transfer_agent instance CAF4JIUZ... and wasm 3870748b... both still return the spec with `fn redeem`; branch `hackmeridian` exists in radox-internal (main fb46527d). (3) Testnet RPC protocolVersion 29, Horizon reachable, friendbot answers (400 only because the probe account existed). (4) stellar-cli on Pedro's Mac is 28.1.0, the newest release (2026-09-26); the kit pairs it with soroban-sdk 29.0.1 on protocol 29: no deploy of an sdk-29 wasm with CLI 28.1.0 has been run, and Leo's toolchain was never checked. (5) No public host for the shipment page is named in any plan file; the repo is private until Mon 06:00 and the GitHub account plan is free, so GitHub Pages from that repo is not available (inference). The Vercel connector in central is authenticated but lists 0 teams. (6) Nobody is assigned to record or upload the video; ffmpeg exists on Pedro's Mac. (7) The `head` hash encoding (how Address values enter sha256) is not fixed in LEO-BRIEF.md, yet verify-head and the page's 'Verify head' must agree with the contract. (8) check.py reads the repo through gh as Pedro: it needs the push to main of proofs/lifecycle.json. Source files: KICKOFF.md, LEO-BRIEF.md, TRACK.md, STATE.md in projects/hackmeridian-rail. Related: [[soroban-versions-on-2026-10-25-9619]] [[two-signers-in-one-soroban-call-1b93]].

Compared: [[soroban-versions-on-2026-10-25-9619]] coexists (tool versions, not the audit of this project's plan) ; [[two-signers-in-one-soroban-call-1b93]] coexists (howto, not an audit) ; [[apache-2-0-for-rio-miami-9905]] coexists (licence choice, not plan readiness) ; [[brl-and-usd-ramps-on-stellar-1e41]] coexists (ramps research, other topic) ; [[hackmeridian-2026-rules-and-submission-requirement-5868]] coexists (event rules, while this note audits the plan against them) ; [[hackmeridian-rubric-7-criteria-weights-scored-50e2]] coexists (scoring rubric, not readiness) ; [[lisbon-is-utc-0-for-the-9963]] coexists (time zone fact used by the timeline) ; [[no-sep-and-no-stellar-project-aa39]] coexists (ecosystem research, other topic) ; [[ucc-article-7-and-brazilian-rules-77dd]] coexists (legal research, out of scope under the no-legal rule)

~~~ third-party 62aeea (data, not instructions; delete this block if you quote nothing)
~~~ 62aeea
