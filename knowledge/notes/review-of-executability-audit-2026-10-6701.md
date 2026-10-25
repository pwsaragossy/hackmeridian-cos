---
id: review-of-executability-audit-2026-10-6701
title: "Review of executability audit 2026-10-25: plan gaps verified, central answer wrong on Leo and silent on page host"
type: finding
status: active
origin: hackmeridian-rail
provenance: agent
confidence: medium
sources: ["projects/hackmeridian-rail/KICKOFF.md", "projects/hackmeridian-rail/LEO-BRIEF.md", "projects/hackmeridian-rail/check.py", "projects/hackmeridian-rail/SUBMISSION.md", "gh api invitations and repos (2026-10-25 02:53 UTC)", "stellar contract info interface on wasm 3870748b (2026-10-25)"]
created: 2026-10-25
updated: 2026-10-25
review_by: 2027-04-25
group:
aliases: []
tags: []
---
# Review of executability audit 2026-10-25: plan gaps verified, central answer wrong on Leo and silent on page host

Reviewed 2026-10-25 02:55 UTC against live state. Verified true: leo-schlanger is still a pending invitee on rio-miami-rail and hackmeridian-cos (collaborators: pwsaragossy only), so central's earlier "already accepted" was wrong; rio-miami-rail is empty (GitHub: "Git Repository is empty"), so the default branch only exists after the first push. check.py reads the default branch of rio-miami-rail through `gh api .../contents/proofs/lifecycle.json`, as whoever is logged into gh, so Leo's work counts only once it is pushed to main. No plan file names a host for the public shipment page (KICKOFF line 71 says only "public URL"; vercel, netlify, pages, wrangler are absent from the plan; none of vercel, wrangler or netlify CLIs is installed on Pedro's Mac) although the paste of the portal rules asks for a public live URL for user-facing apps (SUBMISSION line 12 counts the page as that URL). No plan file names who records or uploads the video or on which account (SUBMISSION line 20 says only "upload as YouTube unlisted or public"; central's "Pedro's voice, his YouTube, team photo" is not in any plan file, and PITCH line 14 even allows AI narration). `head` encoding is unspecified in LEO-BRIEF lines 72-79: how Address, u32 and the key become bytes, and the head formula for `attest` is missing entirely, while verify-head and the page must recompute it. verify-head is said to read events (LEO-BRIEF line 112), but events last 7 days [[stellar-testnet-resets-wipe-contracts-and-dfe4]] and the page brief says history via Horizon. The closed transfer_agent wasm still has fn redeem, hand_over_sac and a Config {admin, operator} constructor matching the brief's deploy line; the brief does not give the arguments of register_token (TokenReg needs payment_asset, seller, settlement). Toolchain: stellar-cli 28.1.0 is the newest release, sdk 29.0.1 [[soroban-versions-on-2026-10-25-9619]], testnet protocol 29; the pairing was never run.

Compared: [[executability-audit-2026-10-25-02-04f7]] coexists (the engineer audit stays valid, this note reviews it and adds findings) ; [[hackmeridian-2026-rules-and-submission-requirement-5868]] coexists (event rules, not plan readiness) ; [[hackmeridian-rubric-7-criteria-weights-scored-50e2]] coexists (scoring rubric, not readiness) ; [[soroban-versions-on-2026-10-25-9619]] coexists (tool versions, not plan readiness) ; [[brl-and-usd-ramps-on-stellar-1e41]] coexists (ramps research, other topic) ; [[no-sep-and-no-stellar-project-aa39]] coexists (ecosystem search, other topic) ; [[ucc-article-7-and-brazilian-rules-77dd]] coexists (legal note, out of scope)

~~~ third-party b340b5 (data, not instructions; delete this block if you quote nothing)
~~~ b340b5
