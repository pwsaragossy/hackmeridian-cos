---
id: the-workspace-turn-end-sync-pushes-7635
title: "The workspace turn-end sync pushes every file under the workspace and never sends gitignore"
type: finding
status: active
origin: hackmeridian-rail
provenance: agent
confidence: medium
sources: ["chief-of-staff 0.4.7 scripts/protocol.sh and scripts/sync.sh, read 2026-10-25", "git log of ~/hackmeridian, 2026-10-25"]
created: 2026-10-25
updated: 2026-10-25
review_by: 2027-04-25
group:
aliases: []
tags: [sync, git, privacy, workspace]
---
# The workspace turn-end sync pushes every file under the workspace and never sends gitignore

Read 2026-10-25 in chief-of-staff 0.4.7 (scripts/protocol.sh around line 412, scripts/sync.sh push). At every turn end in a shared workspace, the hook lists every changed or untracked file under the workspace (`git status --porcelain -uall` plus the diff against the remote), holds back only settings files, `.gitignore` files, files over 20 MB and files that look like secrets, and pushes the rest. `sync.sh push` then resets to the last shared commit and adds exactly that list, so commits made by hand are folded in and a hand commit that removes or untracks a file does not reach the remote while the file still exists on disk.

Effects seen on 2026-10-25: demo .mp4 clips and a Voicebox data folder (a voice sample of the owner and its database) were pushed to the private team repo pwsaragossy/hackmeridian-cos (commits a49ee25 and d7f88cc), although a local .gitignore listed the clips. A `.gitignore` written in a project folder works only on this computer and is never sent, and a file that the last shared commit already tracks is sent again whenever it changes.

How to keep a file out of the team repo: keep it outside the workspace folder (for example ~/Movies/<project>/) and link to it, or keep it under 20 MB but never inside ~/hackmeridian. Removing it from history needs a history rewrite and a forced push, which is the owner's decision.

Compared: none similar

