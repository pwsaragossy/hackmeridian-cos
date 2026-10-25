---
id: lisbon-is-utc-0-for-the-9963
title: "Lisbon is UTC+0 for the whole HackMeridian event"
type: finding
status: active
origin: hackmeridian-rail
provenance: agent
confidence: high
sources: [macOS date with TZ=Europe/Lisbon, run 2026-10-25]
created: 2026-10-25
updated: 2026-10-25
review_by: 2027-04-25
group:
aliases: []
tags: []
---
# Lisbon is UTC+0 for the whole HackMeridian event

EU summer time ended Sun 25 Oct 2026 at 01:00 UTC, so Lisbon is WET (UTC+0) before check-in at 09:00 on 25 Oct. The whole event, including the Mon 26 Oct 12:00 deadline and the team deadline of 10:00 +0000, is on UTC+0, so Lisbon time and UTC are the same during the build. Checked with macOS date for Europe/Lisbon on 2026-10-25 09:00 and 2026-10-26 10:00: both print WET +0000. The line in STATE.md that says UTC+0 only on 26/10 is imprecise.

Compared: none similar
