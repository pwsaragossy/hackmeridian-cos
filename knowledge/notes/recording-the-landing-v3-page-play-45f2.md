---
id: recording-the-landing-v3-page-play-45f2
title: "Recording the landing v3 page: ?play at 1080p hides the Verify button and MATCH, and headless needs software WebGL flags"
type: finding
status: active
origin: hackmeridian-rail
provenance: agent
confidence: medium
sources: ["https://rio-miami-rail.vercel.app (commit 0c7dd19) opened with Playwright 1.58 at 1920x1080 on 2026-10-26 ~05:10 UTC", "rio-miami-rail origin/landing-v3 page/main.js lines 374-415"]
created: 2026-10-26
updated: 2026-10-26
review_by: 2027-04-26
group:
aliases: [play mode, landing recording]
tags: [hackmeridian, video, landing]
---
# Recording the landing v3 page: ?play at 1080p hides the Verify button and MATCH, and headless needs software WebGL flags

[FACT, measured 2026-10-26 ~05:10 UTC, Playwright at 1920x1080 on the production page 0c7dd19] Three things decide how the landing page can be recorded for the demo video.

1. `?play` (main.js line 405) scrolls the 8 scenes by itself and clicks `#verify` at 2.5 s into scene 6, but the scene 6 card is 1210 to 1273 px tall and starts about 80 px from the top, so at 1080 px the "Check the fingerprint" button and the MATCH badge sit below the fold and a plain `?play` recording never shows MATCH. After a click the page does scroll the button into view (a non-play run showed MATCH at y=592), so scene 6 needs its own choreography: hold the top, scroll the card, click, hold MATCH. CSS zoom 0.8 would fit the card but shrinks the text to about 11 px.
2. In headless Chromium the globe (three.js) draws nothing unless it is launched with `--use-gl=angle --use-angle=swiftshader --enable-unsafe-swiftshader --ignore-gpu-blocklist`; without them scenes 0, 3 and 7 show an empty dark screen. On Pedro's Mac a headed Chromium with the real GPU is the alternative.
3. `?play` runs the scenes for 8, 8, 10, 8, 7, 9, 9, 9 s (68 s in all); scene 5 ends on a simulated answer `GET /api/custody/shipments/COFFEE-0042` tagged "Practice run", which must not be shown as the real API (the real one is the 08b clip, [[claims-hackmeridian-material-may-and-may-3e4f]]).

Scene 7's paragraph names ZIS, Cisbra and Camacol (commit f4319e6, 2026-10-26 02:33 UTC), which [[zis-in-public-material-radox-is-bc05]] forbids in public material without Paulo's written OK; the video must not show that paragraph.

Compared: [[wording-the-rio-miami-deck-readme-ef38]] coexists (wording rules for the same video, this note is about how the page can be captured) ; [[deck-and-video-rules-for-async-8b70]] coexists (generic async-judging rules, this one is the page-capture facts) ; [[zis-in-public-material-radox-is-bc05]] coexists (the naming rule this note applies to scene 7).
