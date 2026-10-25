Role: designer
Answer: v2 is a solid engineering base but reads as a document (796 visible words measured, no image in the first screen). The v3 spec below fits the whole story into 103 words. It works by turning one graphite Earth into the narrator, scrubbing the 3D and triggering the text, and moving every number with a hash into a drawer that is really closed.

Reviewed: `origin/landing-v2` at `a235cb5` (no v3 commits pushed as of 2026-10-25, checked with `git fetch` + `git log`). For Vhendala, v3 owner. Read-only review: nothing in `page/` was changed.

## Analysis

### 0. Measured state of v2 (the starting point)

| Measure | Value | How | Tag |
|---|---|---|---|
| Visible words, drawer closed | **796** (154 of them inside the "closed" drawer) | Playwright, `document.body.innerText` split on whitespace, 390 and 1440 px | [FACT] |
| Focusable links inside the closed drawer | **9** | Playwright, `a,button` inside `#proof` | [FACT] |
| Lighthouse mobile (local static server, no compression) | Performance **76**, Accessibility 100 (one failed audit) | Lighthouse CLI, Chromium 1234 headless | [FACT] |
| LCP / TBT / CLS | 6.6 s / 100 ms / 0.02; LCP element `p.lead` (render delay) | same run | [FACT] |
| Bytes on load | 1,084 KiB; `stellar-sdk.min.js` 826,679 B raw / 176,655 B gzip, loaded at startup | Lighthouse + `gzip -9 \| wc -c` | [FACT] |
| Long tasks during 60 wheel steps on a laptop | 0 | PerformanceObserver `longtask`, 1280 px | [FACT] |
| Failed a11y audit | `label-content-name-mismatch`: hash links show `2b3d51f0…` but are named "Testnet transaction 2b3d…" (WCAG 2.5.3) | Lighthouse | [FACT] |
| Globe size at 390 px | **164 px** wide; first globe pixel at y = 3101 px (3.7 screens down) | Playwright bounding box | [FACT] |
| Globe in first fold at 1440 px | none, the hero is text only | screenshot `v2-1440-top.png` | [FACT] |

Screenshots: `/tmp/claude-1000/-mnt-c-Users-leosc-Desktop-hackaton-meridian/500eb7a6-e536-4de1-b7df-95280e80f86b/scratchpad/design/` (`v2-390-top.png`, `v2-1440-top.png`, `v2-390-globe.png`, full-page pair).

### 1. The system for all 8 scenes (build this first, once)

**Architecture: one fixed canvas, sticky scenes.** [INFERENCE, High]
- One `<canvas id="earth">` with `position: fixed; inset: 0; z-index: 0`, shared by every scene. The camera and the scene state change and the canvas never moves. This gives one WebGL context, no re-init, and a continuous "film".
- Each scene is `<section class="scene" style="height: Nsvh">` containing `<div class="stage">` with `position: sticky; top: 0; height: 100svh`. Use CSS sticky, not `pin: true`. Sticky has no pin-spacer reflow, no iOS jump when the URL bar collapses, and lets the browser scroll natively. ScrollTrigger only reads progress: `ScrollTrigger.create({ trigger: section, start: "top top", end: "bottom bottom", scrub: 0.6, animation: tl })`.
- **Rule: 3D, lines and counters scrub. Text triggers.** Drive text beats from `onUpdate: self => setBeat(Math.floor(self.progress * beats))` toggling a class, with a 320 ms CSS transition (`cubic-bezier(.2,.8,.2,1)`). When the visitor stops, words are never half faded. This is the biggest single "premium vs. student" difference.
- Remove `html { scroll-behavior: smooth }` (v2 line 25): it fights ScrollTrigger. Do not add Lenis or ScrollSmoother: native scroll keeps keyboard, screen reader and Lighthouse happy.
- `ScrollTrigger.config({ ignoreMobileResize: true })`. Use `svh` for section heights.
- Scene heights (desktop, total about 1200 svh, which is about 60 s of normal scrolling). Mobile = 0.85x.

| Scene | 1 Hero | 2 Problem | 3 Standard | 4 Rail | 5 Many chains | 6 Trust | 7 Stellar | 8 Business |
|---|---|---|---|---|---|---|---|---|
| Section height | 120svh | 160svh | 120svh | 280svh | 140svh | 120svh | 120svh | 140svh |
| Target seconds in the 60 s test | 6 | 8 | 6 | 14 | 7 | 7 | 6 | 6 |

**Grid and safe areas.**
- 390 x 844: 4 columns, 16 px side gutters (`max(16px, env(safe-area-inset-left))`), header 56 px. The **text zone** is the top band, from 72 px to 36% of `svh`. The **3D zone** is the lower 64%. In the bottom 24 px nothing is interactive (iOS home bar).
- 1440 x 900: 12 columns, 1200 px container, 24 px gutters. The **text zone** is columns 1 to 5 (x 120 to 600). The **3D zone** is centred at x of about 1000, and the globe diameter is about 78% of the viewport height (700 px).
- **Hard rule: text never sits over the lit globe disc.** The shader caps the brightest land pixel at `#303740`, but city lights reach `#C8CBD0`. Over those, even foreground text cannot be guaranteed. Where a mobile scene needs overlap, the globe dims to 35% opacity during that text beat.

**The Earth, in Signal.** [INFERENCE, High] This is the one move that makes it look designed and not downloaded. Grade the NASA textures to **graphite monochrome**: ocean `#0E0F11`, land `#1F2329` to `#303740`, night lights tinted to `#C8CBD0` (soft). The only colour on the planet is lime: Rio, the route and the checks. A blue Blue Marble breaks the token gate in spirit and turns the page into a stock-NASA screensaver. Pack it as **one** RGB texture: R = land albedo, G = night lights, B = land mask. A custom `ShaderMaterial` mixes it along a fixed sun direction, so the terminator crosses the Atlantic. Add a thin fresnel rim in `#303740` (lighting, not a CSS gradient; Signal forbids gradients and shadows in UI). No bloom, no post-processing.

**Camera.** `PerspectiveCamera` with FOV 30. A long lens means less distortion, which reads as "Apple product shot". Earth radius 1. Distance 3.6 at 1440 and 4.4 at 390, so the globe fits the width. All camera moves are eased by the scrub only (`ease: "none"` inside the timeline, `scrub: 0.6` for weight).

**Type scale (Inter, OFL 1.1, already vendored: 400/600/700 latin woff2 plus `fonts/LICENSE-Inter-OFL.txt`).** [FACT for the files; sizes are spec]

| Role | 390 px | 1440 px | CSS | Weight | Tracking | Line | Colour |
|---|---|---|---|---|---|---|---|
| Display (S1 H1) | 44 px | 96 px | `clamp(44px, 4.95vw + 24.7px, 96px)` | 600 | -0.035em | 0.98 | foreground |
| Scene title (H2) | 34 px | 64 px | `clamp(34px, 2.86vw + 22.9px, 64px)` | 600 | -0.03em | 1.04 | foreground |
| Big number | 56 px | 120 px | `clamp(56px, 6.1vw + 32.2px, 120px)` | 700 | -0.04em | 0.95 | foreground, `tnum` |
| Sub line | 19 px | 24 px | `clamp(19px, 0.48vw + 17.1px, 24px)` | 400 | -0.011em | 1.35 | soft `#C8CBD0` |
| Caption / legend | 16 px | 17 px | `clamp(16px, .1vw + 15.6px, 17px)` | 600 | -0.006em | 1.3 | foreground |
| Label (chip, number unit) | 14 px | 14 px | fixed | 600 | +0.06em, uppercase only for chips | 1.2 | muted-fg |
| Hash | 14 px | 15 px | fixed | 400 | +0.02em | 1.2 | muted-fg, `font-feature-settings: "tnum","zero"` |
| Button | 18 px | 18 px | fixed | 600 | -0.006em | 1 | text on lime |

- Leo's existing rule (commit a235cb5) stays: no grey text under 14 px. Max measure: H1 12ch, H2 16ch, sub 34ch.
- Fallback: `font-family: Inter, "Inter Fallback", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif` with `@font-face { font-family: "Inter Fallback"; src: local("Arial"); size-adjust: 107%; ascent-override: 90%; descent-override: 22%; }`. This keeps CLS under 0.02 when Inter swaps in (the metric values are [INFERENCE, Medium]; check visually).
- Preload only `inter-latin-600-normal.woff2`, since the H1 uses 600 (v2 preloads 700).

**Icons.** Lucide (ISC licence, [INFERENCE, High]; put the licence file in `page/vendor/`), inline SVG, `stroke-width: 1.5`, 24 px grid, `aria-hidden="true"` with the meaning carried by text or by the scene's label. Proposed names: `warehouse`, `anchor`, `ship`, `stamp`, `package-check`, `file-question` (check the exact name in the pinned version; recent Lucide renamed some to `file-question-mark`), `key-round`, `check-check`, `shield-check`, `plug-zap`, `coins`, `wheat`, `coffee`, `gem`, `building-2`, `id-card`, `ticket`, `chevron-down`, `wifi-off`, `circle-x`, `github`. **No real token logos** (no USDC, XLM or other issuer marks): a logo implies a partner ([[claims-hackmeridian-material-may-and-may-3e4f]]).

### 2. Scene by scene

Word counts use the same rule as the gate (whitespace-separated tokens). Write separators like "·" as CSS gaps, never as characters, because each one counts as a word.

**Persistent header (6 words, counted once).** Wordmark "Radox" (1) on the left. Chip "Stellar testnet, test keys" (4) on the right, 14 px, muted-fg, border `#303740`. Skip link "Skip to Verify" (3 words, visible on focus) is the first tab stop. 390: 56 px tall. 1440: 64 px. Header background is `#0E0F11` at 100% (no blur: no glass effects in Signal).

---

**Scene 1. Hero (8 words)**
- Words: H1 **"Who holds the cargo?"** Sub: **"One record. Every handover."**
- 390: H1 at the top of the text zone (y of about 96 px), sub under it. The Earth fills the lower 64% at diameter 1.1x the viewport width, so the bottom third bleeds off-screen (a planet horizon). Rio sits at about (50%, 70%).
- 1440: H1 and sub in columns 1 to 5, vertically centred. The Earth is on the right, full disc.
- Motion: on load, the canvas fades in over 600 ms (`power2.out`). The H1 is **visible at first paint**, and never `from({opacity:0})`, which would push LCP back. The Earth turns continuously at 0.03 rad/s. Rio pulses as a lime ring, 2.4 s period, scale 1 to 2.2 with opacity 0.6 to 0. Scrub 0 to 1: the camera dollies from 3.6 to 3.0, and the container (graphite with a lime stripe) rises 0.08 units off Rio. A scroll cue (Lucide `chevron-down`, `aria-hidden`) bobs 4 px, 1.6 s, `sine.inOut`, and disappears at progress 0.05.
- Reduced motion: the same frame, no spin and no pulse. The container sits on Rio and the ring is static.
- Premium detail: the **real terminator**. Rio is at dusk, half in light, with lime on the line between day and night.

**Scene 2. Problem (14 words; 2 over the 12 budget, see the note)**
- Words: **"45M"** with "cargo documents a year" · **"9 in 10"** with "not electronic" · **"22%"** with "of thefts: insiders". No title: the numbers are the title. The section has `aria-label="The problem"` (an attribute, so it costs no visible words).
- Claims note: PROBLEM-NUMBERS row 2 says the source supports "not electronic", **not** "paper". The brief's "9 in 10 still paper" overstates DCSA. Use "not electronic". "Cargo documents" is plain English for bills of lading. The sources live in the drawer and are linked from the footer.
- 390: the camera goes low over the Atlantic near Rio, and the container moves along a straight path at the bottom third. Five stop icons (warehouse, anchor, ship, stamp, package-check), 32 px, appear as DOM overlays projected from 3D (CSS `transform` updated in the same rAF). A grey "?" (`file-question`, muted-fg) stamps onto each. The numbers stack in the text zone, **one at a time** (one beat each).
- 1440: the same choreography, with the numbers in columns 1 to 5 stacked with 48 px between them, and the stops along the arc on the right.
- Motion: the camera and container scrub. The five "?" stamps trigger at progress 0.1, 0.25, 0.4, 0.55 and 0.7 (scale 1.12 to 1, 260 ms, `power4.out`, with a 2 px grey paper-stack extrude behind each). The numbers trigger at 0.15, 0.45 and 0.75 and count up over 1.1 s, `power2.out`, with `tnum` so the width does not jitter. Count up once; going back up the page shows the final value with no recount.
- Reduced motion: five icons in a row, each with its "?", and all three numbers visible.
- Premium detail: each stop's silo is a **different shade of grey**, which shows "five systems" without a word.

**Scene 3. The standard (10 words)**
- Words: H2 **"One record. Every company."** Sub: **"Like SWIFT: connect once, reach everyone."**
- 390 and 1440: the globe dims to 35% and recedes (distance 3.0 to 5.5). Five company nodes (32 px circles, `#303740` fill, a foreground icon each) sit on a pentagon in the 3D zone. Draw this as inline SVG over the canvas, not in WebGL, so it stays crisp and works in the static mode for free.
- Motion: beat A: 10 pairwise lines (`#7F848E` faint, 1 px) draw in via `stroke-dashoffset` (scrub) and flicker (opacity 0.4 to 1, 3 random steps). Beat B (progress 0.55): the lines **retract along their own paths** rather than fading out, and a lime ring (2 px, `#C7F250`) draws around the pentagon with 5 short spokes. The node outlines turn lime with a 40 ms stagger.
- Reduced motion: a side-by-side pair, "tangle" (10 grey lines) on the left and "ring" (5 lime spokes) on the right.
- Premium detail: lines that retract instead of fading. The count, 10 to 5, is seen, not read.

**Scene 4. The rail, end to end (11 words visible at once; 15 budget)**
- Words: H2 **"Every handover. Both confirm."** (4). Live caption, at most 3 words, one at a time: "Opens in Rio", "Warehouse → Port", "Port → Ship", "Ship → Customs", "Customs → Buyer", "Delivered", "Token retired". For shipment 2's teammate hops, use "Own laptop keys". Hash chip: `2b3d51f0…` (1). Switch: "Shipment" + "1" + "2" (3).
- 390: the H2 is in the text zone and the caption is under it at 17 px. The globe is at diameter 0.92x the width, centred at 60% `svh`, rotated so the whole Rio–Miami arc is visible. The **step rail** is 7 dots in a horizontal row above the home-bar safe area. The switch is a segmented control, 44 px tall, top right of the text zone.
- 1440: the text is in columns 1 to 5, and the step rail is a vertical column of 7 dots at x = 120, from y 40% to 80%. The globe is on the right.
- Motion: the container travels the arc with progress scrubbed (camera follows with a 0.15 lag). The arc behind it draws lime (`TubeGeometry` with `setDrawRange`). At each of the 7 thresholds (start of step n), these trigger:
  - two `key-round` icons slide in from both sides (180 ms, `power3.out`);
  - they meet;
  - a lime `check-check` pops (scale 0 to 1, 240 ms, `back.out(1.6)`);
  - the stop disc goes from muted-fg to lime;
  - the hash chip ticks in, with the last 4 characters cycling for 240 ms before landing on the real value;
  - the matching step dot fills.
- Reduced motion: the whole arc is lime, all 7 stops are checked, and the 7 captions and hashes are shown as a list (the 3-word captions keep this under budget: about 30 words. Count it in the reduced-motion budget too).
- Premium detail: the **step dots are the accessible list** (see Keyboard). Tabbing to dot 3 scrolls the film to step 3, so the keyboard drives the movie.

**Scene 5. Many chains, one rail (10 words)**
- Words: H2 **"Many supply chains. One rail."** (5). Legend: "Inside a company" (3) and "Between companies" (2). Company letters "A" and "B" are drawn in the canvas, not the DOM.
- 390 and 1440: the camera pulls back to distance 3.4. Shipment 1's route (already lime) stays. Shipment 2's route draws in from a second origin and merges at the shared terminal and vessel.
- Encoding, **never colour alone**:
  - inside a company: info `#9FB2CC`, 1.5 px, **dashed** (6/6), single check icon;
  - between companies: lime `#C7F250`, 3 px, **solid**, double check.
  - Shared nodes get a double ring.
  - Each legend item shows its own line sample, so the legend works in greyscale too.
- Motion: route 2 draws on scrub. At the moment both routes touch a shared node, a "handshake" double ring triggers (two rings 1 to 1.8, 400 ms, 80 ms apart).
- Reduced motion: both routes drawn, with the legend.
- Premium detail: the handshake ring at the shared terminal and vessel. That is the moment the idea clicks.

**Scene 6. Trust (13 words with the live/offline label; 8 budget)**
- Words: H2 **"Don't trust us. Check it."** (5). Button "Verify" (1). The `#source` label "Live from Stellar testnet" (4) stays as app.js writes it, because the live and offline tests read it. Drawer toggle "See the proof" (3). After a press: "MATCH" (1).
- Move `#about` and the long result detail ("recomputed … from 7 transactions …") **into the drawer**. They are about 30 words.
- 390: the Earth is pushed far back to 20% opacity. The H2 is in the text zone. A horizontal hash chain sits mid-screen: 7 linked rounded rectangles of 28 px, `#17191C` fill and `#303740` stroke. The Verify button is full width minus gutters, 56 px tall. The drawer toggle is below it, full width and 48 px.
- 1440: H2 on the left. Chain and button in columns 7 to 12, with a 320 px button.
- This scene is **interactive, not scrubbed**: `end` is short, and nothing moves while the visitor reads.
- Verify press:
  - each chain link lights lime as the **real recompute loop** reaches that transaction (hook a callback into app.js's loop, no fake timer), at least 90 ms per link;
  - then a MATCH pill appears: lime fill, text `#0E0F11`, `shield-check` icon, 22 px 700 with +0.08em tracking.
- Button and result states:

| State | Button | Result area |
|---|---|---|
| Loading (data not ready) | "Verify", lime at 100%, `aria-disabled="true"`, `cursor: progress`, small `loader-2` icon (spins only with motion allowed). Not `opacity: .5`: lime at 50% on graphite is `#6A8030`, 4.33:1, which reads as broken. | – |
| Ready | "Verify", lime | – |
| Hover | lime + 2 px lime outline at 3 px offset | – |
| Active | `scale(.97)`, 80 ms | – |
| Focus | 2 px lime outline, 3 px offset | – |
| Recomputing | "Checking…" with spinner, `aria-busy="true"` | chain links light one by one |
| MATCH | "Verify again", secondary style | lime pill with `shield-check` icon and the word MATCH |
| MISMATCH | "Verify again" | destructive `#F26969` text and 2 px border, `circle-x` icon, the word MISMATCH |
| Error | "Try again" | destructive text, the reason in plain words |
| Offline snapshot | – | `#source` in **warning `#F2930D`** with a `wifi-off` icon. v2 paints the warning in lime, the success colour (fix 6). |

- Drawer: **use `hidden`** (or `<details>`), not `max-height: 0`. Animate the reveal with `grid-template-rows: 0fr → 1fr` after removing `hidden`, 300 ms. When it opens, move focus to the drawer heading. Contents: how it works, sources (DCSA Feb 2023 and 2025, TT Club & BSI Apr 2026), state rows, history, contract IDs, and the prior-work disclosure (the transfer_agent note; keep it, since the portal rules require disclosure).
- Reduced motion: the chain is shown already lit after a press, with no per-link animation, and the result appears at once.
- Premium detail: **honest motion**. The light runs at the speed of the real check.

**Scene 7. Stellar ecosystem (11 words)**
- Words: H2 **"Any tokenized asset on Stellar can ride the rail."** (9). Socket label "One API" (2).
- 390 and 1440: the Earth comes back to 100%, distance 3.2. Six generic coins (`InstancedMesh`, graphite discs with a 1 px lime edge, each carrying a DOM-projected Lucide glyph: `coffee`, `wheat`, `gem`, `building-2`, `coins`, `package`) orbit at radius 1.35. One socket (`plug-zap`) sits on the rail near Rio.
- Motion: the orbit speed scrubs (fast to slow). At progress 0.35, 0.5 and 0.65, three coins detach, fly to the socket (500 ms, `power3.inOut`) and snap (`back.out(1.4)`). The socket ring flashes lime for 200 ms on each snap.
- Reduced motion: the coins sit parked in a row at the socket.
- Premium detail: the magnetic snap and a single 200 ms lime flash. Nothing else blinks.

**Scene 8. Business and next (17 words, footer included)**
- Words: **"Membership + per-shipment fee. The SWIFT model."** (7). H2 **"Rio–Miami first. Then every corridor."** (5). Footer: "Code" (GitHub link), "Sources" (opens the drawer at the sources), "Apache-2.0" (3). The testnet chip is already in the header.
- 390: two icon tiles (`id-card` and `ticket`, 48 px, `#17191C` card, `#303740` border) side by side in the text zone, with the business line under them. The Earth is below. The H2 enters on beat 2.
- 1440: tiles and line in columns 1 to 5, Earth on the right.
- Motion: beat 1 triggers the tiles (fade and 12 px rise, 400 ms, 60 ms stagger). Beat 2: 8 to 12 unlabeled corridors draw outward from Rio on scrub. They are **one merged tube geometry** with a per-vertex `progress` attribute (one draw call), staggered by great-circle distance. Endpoints are generic points with no labels (no port, airport or city other than Rio–Miami). The globe ends turning slowly.
- Reduced motion: all corridors drawn and the tiles shown.
- Premium detail: the **last frame is the first frame, grown**. The same Earth, now laced with lime. The video can end on it.

**Word total:** header 6 + skip link 3 + S1 8 + S2 14 + S3 10 + S4 11 + S5 10 + S6 13 + S7 11 + S8 17 = **103 ≤ 120** [FACT by count of this spec; re-measure on the build]. Open question 1 covers how the counter treats focus-only and canvas text.

### 3. Contrast table (WCAG 2.2 AA)

Method [FACT]: WCAG relative-luminance formula in Python (`scratchpad/design/contrast.py`), with tokens converted from the page's HSL. The page's `hsl(219 7% 57%)` renders `#8A8F99`; the brief says `#8A8F98`, and the difference is negligible. Thresholds: 4.5 normal text, 3.0 large text (24 px, or 18.66 px bold) and UI or graphics (1.4.3, 1.4.11).

| Pair (foreground on background) | Ratio | Used for | Verdict |
|---|---|---|---|
| foreground `#E6E8EA` on background `#0E0F11` | 15.61 | titles, captions | pass |
| foreground on card `#121416` | 15.03 | tiles | pass |
| foreground on muted `#17191C` | 14.34 | chain links, segmented control | pass |
| soft `#C8CBD0` on background | 11.79 | sub lines | pass |
| muted-fg `#8A8F99` on background | 5.91 | labels, hashes | pass |
| muted-fg on card | 5.69 | labels in tiles | pass |
| muted-fg on muted | 5.43 | drawer rows | pass |
| faint `#7F848E` on background | 5.11 | scene 3 tangle lines (graphic) | pass |
| faint on card | 4.92 | not for text under 18.66 px bold | pass (keep to graphics) |
| lime `#C7F250` on background | 14.83 | route, checks, focus ring, MATCH | pass |
| text `#0E0F11` on lime | 14.83 | Verify button, MATCH pill | pass |
| info `#9FB2CC` on background | 8.87 | internal-handover line | pass |
| success `hsl(160 60% 40%)` `#29A37A` on background | 6.04 | not needed (lime is success) | pass, unused |
| warning `#F2930D` on background | 8.18 | offline snapshot label | pass |
| destructive `#F26969` on background | 6.39 | MISMATCH, error | pass |
| destructive on card | 6.15 | error inside the drawer | pass |
| lime on land `#1F2329` | 12.21 | route over land | pass |
| lime on bright land `#303740` | 9.30 | route over land | pass |
| muted-fg on land `#1F2329` | 4.86 | unlit stop disc (graphic, 3.0 needed) | pass |
| muted-fg on bright land `#303740` | 3.71 | unlit stop disc | pass for graphics, **fail for text**: no grey text over the globe |
| info on bright land | 5.56 | internal line over land | pass |
| faint on bright land | 3.20 | no use over land | marginal, avoid |
| border `#1F2329` on background | 1.22 | card edges (decorative) | fail 1.4.11, allowed only where the border is not the only cue |
| border-hover `#303740` on background | 1.59 | tile and chain-link strokes | same rule |
| **v2 globe: land `#1F2329` on sphere `#121416`** | **1.17** | continents in v2 | **fail 1.4.11** (the map is meaningful) |
| **v2 route: muted-fg at 70% over land** | **2.91** | v2 dashed route | **fail 1.4.11** |
| **v2 unlit stops: border on land** | about 1.0 | v2 stops | **fail**, invisible |
| lime at 50% (v2 disabled) on background | 4.33 | v2 disabled Verify | exempt (disabled), but reads as broken |
| muted-fg on lime | 2.51 | never | fail, do not use |

Segmented control and border-only controls: the text label identifies the control, so a low-contrast border is allowed. The **selected** state must hold 3:1, and the lime fill (14.83) does. Lime's 14.83:1 on background makes the focus ring pass easily.

### 4. Focus, keyboard path, screen-reader order

**Tab order:**
1. Skip link "Skip to Verify"
2. Step dots 1 to 7 (scene 4)
3. Shipment switch 1 and 2
4. Verify
5. See the proof
6. *(drawer contents, only when open)*
7. Code
8. Sources

Nothing else is focusable: the canvas is `aria-hidden="true"` and `tabindex="-1"`, and dragging the globe is decorative and needs no keyboard equivalent (2.5.7: the drag is not needed for any function).

- **Step dots:** `<ol aria-label="Shipment steps">`. Each `<li>` holds a `<button>`: 8 px visual dot, **24 x 24 hit area** (2.5.8), `aria-label="Step 3 of 7: the port hands the container to the ship. Both confirm."`, and `aria-current="step"` on the active one. Focus or Enter calls `scrollTo` with the section offset for that step (via `ScrollTrigger.labelToScroll` or a computed offset).
  - The hash link sits next to the caption with **visible text first in its accessible name**: `aria-label="2b3d51f0…, testnet transaction"`, or no `aria-label` plus `title`. This fixes Lighthouse `label-content-name-mismatch` (2.5.3).
- **Focus visible:** 2 px lime outline at 3 px offset on every control, including the dots. `scroll-padding-top: 72px` so the header never hides a focused element (2.4.11 Focus Not Obscured).
- **Screen-reader order = DOM order = story order:**
  1. header
  2. H1 + sub
  3. `<section aria-label="The problem">` with the three numbers as a `<ul>`
  4. scene 3 H2
  5. scene 4 H2, then the step list (the full sentence for each step lives in the dot's `aria-label`)
  6. scene 5 H2 + legend
  7. scene 6 H2, `#source`, Verify, result (`role="status"`), drawer
  8. scene 7, scene 8, footer.
- Each scene's visual gets one `<div role="img" aria-label="…">` sentence. These are attributes, so they **cost no visible words**. Example for scene 3: "Five companies wired to each other with ten tangled lines, which collapse into one ring with five links."
- **Live regions:** only `#result` (`role="status"`) and `#source`. The scroll caption in scene 4 is `aria-live="off"`, because announcing on every scroll is noise. The dots carry the story.
- **Reflow and zoom (1.4.10, 1.4.4):** at 320 px wide and at 200% text zoom, drop the sticky behaviour (`@media (max-width: 340px), (min-resolution: …)` is not reliable for zoom). Instead test that `.stage` content fits in `100svh`; if it overflows, switch to the static layout via `ResizeObserver`.

### 5. Performance budget (Lighthouse mobile ≥ 80, no long task over 200 ms)

| Item | Budget | Note |
|---|---|---|
| Initial JS (gzip) | ≤ 260 KB | three.module.min.js about 165 to 180 KB gzip [INFERENCE, Medium]; GSAP core + ScrollTrigger about 45 KB [INFERENCE, Medium]; scene code ≤ 25 KB; app.js 5 KB |
| stellar-sdk (177 KB gzip, measured) | **lazy** | `import()` on `requestIdleCallback` 2 s after load, or when scene 5 enters, whichever comes first. Verify stays in the loading state until it resolves. This is the biggest Lighthouse lever. |
| Earth texture | 1 packed RGB: 2048x1024 WebP q72 ≤ 300 KB on desktop (`pointer: fine`), 1024x512 ≤ 90 KB on mobile | decode with `createImageBitmap` (off the main thread), then `renderer.initTexture()` before the reveal |
| Sphere | 96x48 segments on desktop, 64x32 on mobile | |
| Draw calls per frame | **≤ 12** | Earth 1, route tube 1, corridors 1 (merged), stops 1 (instanced), container 1 (merged with vertex colours), ship 1 (< 500 triangles), coins 1 (instanced), socket 1, Rio ring 1 sprite |
| Triangles | ≤ 60 k | |
| Lights | none in the shaders (unlit with baked shading), or 1 directional | no shadows, no post-processing |
| Pixel ratio | `Math.min(devicePixelRatio, matchMedia("(pointer: coarse)").matches ? 1.5 : 2)` | `antialias: true`; `powerPreference: "high-performance"` |
| Shader compile | `await renderer.compileAsync(scene, camera)` before the first visible frame | avoids a 100 to 300 ms first-frame stall [INFERENCE, Medium] |
| Render loop | render only when the canvas is visible and either scroll or idle rotation changed something; stop on `visibilitychange`; skip rendering during scene 6 if the globe opacity is under 0.25 | |
| Scroll callbacks | only write numbers into a state object; no allocation, no DOM reads | DOM overlay positions are written in the same rAF as the render |
| LCP | the H1 is HTML text visible at first paint, preload 600 woff2, canvas fades in later | v2 LCP 6.6 s came from render delay [FACT], with the SDK parse likely the cause [INFERENCE, Medium] |
| Compression | Vercel serves brotli; the local `http.server` does not, so local Lighthouse runs on raw bytes | measure on the preview |
| Fallback | no WebGL2, context lost, or `Save-Data`: static mode, the same as reduced motion | |

**Static frames for reduced motion and fallback, without extra assets:** after load, at idle, render the final state of scenes 1, 4, 7 and 8 once each to `canvas.toBlob()`, then drop the blob URLs into `<img alt="">` in each section. That is one render per idle callback, so no long task. Without WebGL, use the CSS/SVG versions of scenes 2, 3, 5 and 6, which already exist because those scenes are SVG and DOM by design.

**Film mode for the video.** `?film=1` hides the cursor, fixes DPR at 2, turns off random flicker, and runs `gsap.to(window, { scrollTo: label, duration })` through the scenes at the second-counts above. Recordings come out identical and match the narration timings.

### 6. The 10 most important fixes vs v2, ranked

1. **Cut 796 words to 103 or fewer.** Every paragraph goes; the copy above is the whole page. Impact: Pedro's main complaint and an automated gate. [FACT, measured]
2. **Make the drawer really closed.** `max-height: 0` leaves 154 words in `innerText` and 9 links in the tab order. Use `hidden` or `<details>`, and move `#about` and the long result detail inside it. [FACT]
3. **Put the Earth in the first frame.** v2's first screen is text only at 1440 px, and on mobile the globe starts 3.7 screens down at 164 px wide. v3 uses a full-bleed Earth behind the H1. [FACT]
4. **Make the 3D carry meaning at 3:1 or more.** v2 land on sphere is 1.17, the route is 2.91, and unlit stops are invisible. v3: lime route 9.3 to 12.2, unlit stops in muted-fg 3.7 to 4.9, text never over the lit globe. [FACT]
5. **Lazy-load stellar-sdk (177 KB gzip) and keep the H1 visible at first paint.** v2 Lighthouse mobile is 76 with LCP 6.6 s. Combined with brotli on Vercel this is the path to 80 or more. [FACT for the numbers, INFERENCE for the cause]
6. **Show the offline snapshot as a warning, not success.** `.source.warn` uses lime today. Use warning `#F2930D` plus a `wifi-off` icon, and show MISMATCH in destructive with a `circle-x` icon. [FACT, from CSS line `.source.warn`]
7. **Never use colour alone for internal vs external.** v2 uses → vs ⇒ with lime. v3 uses dashed info vs solid lime, single vs double check, and a legend with line samples. [FACT, from chains.js]
8. **Fix label in name for the hash links** (Lighthouse failure, WCAG 2.5.3). The visible hash must come first in the accessible name. [FACT]
9. **Scrub the 3D, trigger the text.** v2's IntersectionObserver plus 900 ms tween is fine. In v3, never scrub text opacity. Text half faded when the visitor stops is the tell of a template. Remove `scroll-behavior: smooth`. [INFERENCE, High]
10. **One caption, not two.** v2 shows each step sentence twice, once in `#caption` and once in the step card (see `v2-390-globe.png`), at 12 to 16 words each. v3 has one caption of 3 words or fewer, with the full sentence only in the dot's `aria-label`. [FACT]

If time runs out, cut in this order: scene 7's coin flights become a static row. Scene 2's 3D camera follow becomes the SVG row of icons. Scene 8's corridors drop from 12 to 6. **Never cut**: scene 1 Earth, scene 4 arc + checks, scene 6 Verify, reduced motion.

## What would change the conclusion
- If Pedro's word counter counts `aria-label`s or canvas text, the accessibility plan has to move the step sentences into a `hidden` element referenced by `aria-describedby`, which is also not visible text.
- If three.js is not running by the 23:00 cut, the brief falls back to the d3 globe. Then only the graphite-grade rule, the scrub/trigger rule, the copy and fixes 1, 2, 4 to 10 apply.
- If a mid-range Android reaches only 30 fps with the 2048 texture, drop to 1024 for every device.
- If the cold testers do not retell the "both confirm" beat, scene 4's key icons are too small: raise them from 24 to 40 px.

## Never-skip checklist
- Library citations: done ([[radox-custody-rail-look-signal-adapted-d030]], [[claims-hackmeridian-material-may-and-may-3e4f]], [[product-framing-rio-miami-is-the-34f9]]).
- Measured contrast: done, section 3, Python WCAG formula, every pair used.
- Font licence and fallbacks: done. Inter OFL file present in `page/fonts/`; fallback stack with metric overrides. Lucide is ISC [INFERENCE]: add its licence file.
- Exact colour codes: done (hex for every token as rendered).
- States beyond the happy path: done for Verify (loading, ready, hover, active, focus, checking, MATCH, MISMATCH, error, offline), drawer (open and closed), WebGL fail, and reduced motion. Empty state: n/a (the data is always the two snapshot shipments).
- Visible focus, keyboard path, 24x24 targets: done (section 4). Dots are 24 px, buttons 44 to 56 px.
- Never colour alone: done (scenes 5 and 6, offline and mismatch icons).
- Semantic tokens: done. Use `--primary`, `--warning`, `--destructive`, `--info`; do not hard-code hex in JS (read with `getComputedStyle`, as v2 does).

## Not checked
- The v3 build itself (none pushed yet). Every v3 figure is a spec to re-measure.
- The exact gzip sizes of three.js and GSAP at the pinned versions.
- Lighthouse on the Vercel preview (compressed).
- Real iOS Safari behaviour of `svh` with sticky stages.
- The 17 Playwright cases: they are not in the repo, so I could not confirm which strings and ids they assert. Keep the ids `verify`, `result`, `source`, `status`, `state`, `history`, `about`, the `#switch button[data-s]` buttons and their strings.
- Real screen-reader runs (NVDA or VoiceOver).
- The localhost:8765 server switched to a different page during this review. All v2 measurements after that were taken on my own export of `origin/landing-v2` (port 8799).

## Open questions for the owner
1. How does the 120-word counter define "visible": `innerText`, or only on-screen and unclipped? This decides whether the skip link and the reduced-motion step list count.
2. Is "9 in 10 not electronic" acceptable to Pedro instead of the brief's "still paper"? The source does not support "paper".
3. In scene 4, may shipment 2 say "Own laptop keys" (the team signed on their own computers), or does Pedro want team names off the page?
4. Is the "Membership" wording fine for the subscription, or should it read "Subscription"? "Membership + per-shipment fee" saves one word.

## Library (cited, saved)
- Cited: [[radox-custody-rail-look-signal-adapted-d030]] (tokens, minimum sizes, Verify target 48 px), [[claims-hackmeridian-material-may-and-may-3e4f]] (no names, no logos, no traction), [[product-framing-rio-miami-is-the-34f9]] (Rio–Miami as the first corridor and the future in future tense).
- Proposed for saving (not written, read-only task): "Landing v3 rules: scrub 3D, trigger text; graphite-graded Earth; drawer via `hidden`; v2 baseline 796 words, Lighthouse 76".

## Versions
- **Chosen:** the graphite Earth as the single narrator in a fixed canvas, with SVG/DOM for the diagram scenes (3, 5, 6).
- **Considered and lost:** full photoreal Blue Marble with bloom and a WebGL particle "data flow" in every scene, the typical award-site look. It lost on three counts:
  - it breaks the one-lime Signal identity (blue oceans, warm city lights);
  - text over a bright planet fails contrast;
  - bloom plus particles costs about 2 to 4 draw passes and full-screen fill, which risks Lighthouse 80 and the 200 ms long-task gate on a phone.
  - Also, nothing in the diagram scenes would work in reduced motion without a second build.
