# Landing page v3: the whole project as an interactive film

Owner: Vhendala (and her agent). Asked by Pedro, Sun 25 Oct ~21:10 UTC, via /chief-of-staff:ambition:
"uma landing page com motion, visual effects, que o objetivo principal seja atrair a atenção pelo UI, e apresentar o projeto INTEIRO com movimentações e imagens, que sejam de fácil compreensão, utilizando os melhores simbolos, imagens, assets 3D e movimentos ... do inicio ao fim, de forma interativa."
Supersedes LANDING-V2-BRIEF.md. Keeps Pedro's 21:00 rule: almost no text (at most 120 visible words with the proof drawer closed).

## Goal behind the goal
The page is the product's first impression for judges, and it is also the new video: the video becomes a screen recording of someone scrolling this page, with narration. One build, two deliverables.
A person who never heard of Radox scrolls for 60 seconds and can retell the whole story: the problem, the SWIFT-like standard, the rail from start to end across companies, both companies confirming each handover, many supply chains on one rail, anyone can verify, any Stellar asset can plug in, how Radox earns.

## Judges (set by Pedro's session; do not pick your own)
1. People, cold: Pedro first, then one person Pedro picks. After 60 s of scrolling they retell the story; pass = at least 6 of the 8 beats below, and Pedro scores the UI 8/10 or more.
2. Automated, on the deployed preview: the 17 existing page cases (both shipments, live and offline, 375 and 1280 px, Verify MATCH); a word counter that fails above 120 visible words with the drawer closed; `prefers-reduced-motion` shows a complete static version; Lighthouse mobile performance 80 or more; no long task over 200 ms while scrolling on a laptop.
3. Design: only the Radox Signal tokens in LANDING-V2-BRIEF.md (dark graphite, one lime signal, Inter). Icons from Lucide, the same family the Radox app uses.

## Stack (smallest that gives real 3D and film-grade motion; all files vendored in page/, versions pinned, no runtime CDN)
- three.js (ES module build) for the 3D Earth, arcs, container and ship.
- GSAP 3 + ScrollTrigger for scroll choreography. GSAP and all its plugins are free, including commercial use, since Webflow's acquisition (GSAP README 3.15.0).
- Lucide SVG icons, inline.
- Earth: NASA Blue Marble / Black Marble textures (public domain), compressed to about 1 MB total.
- Container and ship: built in code from boxes and simple shapes in three.js (ribbed container in graphite with a lime stripe; low-poly ship). No downloaded models: no licence risk, tiny size.
- Remove d3-geo once the three.js globe works.

## The film: 8 scenes, pinned scroll sections, one idea each (word budget in brackets)
1. Hero (8 words). Dark 3D Earth slowly turning, city lights on the night side; Rio glows lime; a container rises from Rio. Title "Who holds the cargo?" One line: "One record for goods, from origin to delivery."
2. Problem (12 words). The camera follows the container past five stops (Warehouse, Port, Ship, Customs, Buyer). At each, a different paper stack or grey silo appears with a "?" Three numbers count up: "45M bills of lading a year", "9 in 10 still paper", "22% of thefts are inside jobs".
3. The standard (10 words). Five company nodes wired pair by pair: 10 tangled lines flicker. They collapse into one lime ring, 5 clean links. "One record. Every company. Like SWIFT."
4. The rail, end to end (15 words). The container flies the Rio–Miami arc on the globe. At each stop two key icons meet, a double check pops in lime, and a tiny hash ticks in (the real testnet transaction). Caption per stop at most 3 words ("Port → Ship. Both confirm.").
5. Many chains, one rail (10 words). A second company's route draws in and meets the first at the shared terminal and vessel; internal handovers in one shade, external handovers in lime. "Many supply chains. One rail."
6. Trust (8 words). A big "Verify" button. On press, the links of the hash chain light one by one and land on MATCH. "Don't trust us. Check it." The full proof (hashes, ledgers, contract IDs, how it works) sits in a closed "See the proof" drawer.
7. Stellar ecosystem (12 words). Token icons from different Stellar assets orbit the globe and plug into the rail through one API socket. "Any tokenized asset on Stellar can ride the rail."
8. Business and next (20 words). Two icons: a membership card and a per-shipment ticket: "Subscription + fee per shipment, the SWIFT model." Then corridors light up across the globe from Rio–Miami outward. "Rio–Miami first. Then every corridor." Testnet label, repo link.

Voice: confident, no hedges (Pedro's rule). Nothing false: no partner, port, airport or chamber named; no users or revenue claimed.

## Interaction
Scroll drives the film; the globe can be dragged at any time; the Verify button and the proof drawer are real and use the live testnet data (app.js logic kept). Keyboard and screen-reader users get the same story as text in order.

## Cut gates (UTC)
- 23:00: scenes 1 and 4 working (3D Earth, container on the arc, stops lighting up). Pedro looks. If three.js is not running by then, fall back to the current d3 globe with GSAP scenes and keep going.
- 02:00: all 8 scenes; automated judges green. Pedro's verdict.
- 04:00: polish, reduced motion, mobile. People test.
- 06:00: the new video recorded from this page with the narration rebuilt to the 8 scenes (Pedro's session handles narration and edit).
- 08:00: video uploaded by Pedro. Production page deploy only after Pedro approves.

## Where
Repo pwsaragossy/rio-miami-rail, branch landing-v2, folder page/. Push often; one line on your card with each commit. Pedro's session deploys previews from the branch. Set git user.email to your GitHub noreply address before committing.
