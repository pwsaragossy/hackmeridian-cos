# Demo video plan (v2, built on landing v3)

Status: APPROVED 05:40 UTC. Pedro: "VIDEO GO. Narração com minha voz clonada no Voicebox, por um agente no meu Mac." Production started.
Written Mon 2026-10-26 05:05 UTC. Marketing specialist draft, independent reviewer verdict "approve with changes", every must-fix applied below. Page: https://rio-miami-rail.vercel.app = rio-miami-rail landing-v3 0c7dd19.

## Story in one line
A container of coffee crosses from Rio to Miami through five companies that cannot see each other's records. Radox Custody Rail is SWIFT for goods: both companies sign every handover. You watch it happen through our API on Stellar testnet, and the real record matches its fingerprint.

## Why this fixes the rejected 20:47 cut
- Landing v3 is the spine: about 120 of the 181 s are page scenes. The old cut was mostly terminal and showed the page for 30 s at the end.
- No replayed terminal is left. The only terminal shown is a live recording of the public API in use (B7), if that API is ready. Otherwise B7 falls back, see below.
- "SWIFT for goods" is spoken at 0:10. The climax is MATCH, held on screen for 8 s with no speech.
- Pedro sees a storyboard (13 stills and the narration text) about 45 min after GO, and a rough cut before the final. He does not have to wait for a finished cut to give feedback.

## Beats (181 s = 3:01, about 396 words, 134 s of speech at 177 wpm, at least 1.5 s margin in every beat)
A 64 px strip runs along the bottom of every frame with "Stellar testnet · test keys". The lower third "Narration: AI voice generated from Pedro's voice" shows from 0:00 to 0:08.

| Beat | Time | On screen | Narration (English) |
|---|---|---|---|
| B1 | 0:00–0:19 | Scene 0 "Goods cross borders blind.": the globe and the coffee container from Rio to Miami, with five stops | A container of coffee leaves Brazil for Miami. Five companies hold it on the way, and each keeps its own records. Radox Custody Rail is SWIFT for goods: one shared record that every company on the route signs into. |
| B2 | 0:19–0:31 | Scene 1 "Who has it right now?". Caption: "Source: WTO, trade finance" | When cargo goes missing, every company says it handed over fine. And money rides on those records: the WTO says eighty to ninety percent of world trade relies on trade finance. |
| B3 | 0:31–0:43 | Scene 2 "Both hands sign." | At every handover, the company giving the cargo and the company receiving it both sign. The record is saved where no one can edit it. |
| B4 | 0:43–0:56 | Scene 3 "A token proves who owns the goods. Not who holds them." | A token on Stellar says who owns a container, not who is holding it. On the rail, each shipment gets a custody record: every handover signed by both companies, readable by anyone. |
| B5 | 0:56–1:06 | Scene 4 "Plug in once." | A port or an airport keeps its own software. One adapter connects it to everyone on the rail. |
| B6 | 1:06–1:20 | Scene 5 "Try it. Pass the coffee.", label "Practice run" in view. Slow taps; the shot cuts before the simulated GET COFFEE-0042 card appears | Try it yourself. Each company has a wallet, and a handover only happens when both tap sign. This is a practice run in the browser: nothing is sent. |
| B7 | 1:20–1:46 | The "Try the API" card on rio-miami-rail.vercel.app/docs, recorded live on a fresh shipment opened just before the take (its key is not shown earlier): Open a shipment (wait cut out, the "See it on the explorer" link appears, 2 s on that tx on stellar.expert testnet) → Next handover (route dot moves) → Wrong company → 409 E_WRONG_CUSTODIAN "Refused by the contract. No transaction was sent." → three more Next handover, jump-cut → Deliver. The Request pane (method, path, curl) and the Response pane (live JSON) stay in frame. Verify is left for B9 | Now the real thing: the open rail API on Stellar testnet. Open a shipment, and here is its transaction on the public explorer. Next handover: both companies sign. Send the wrong company, and the contract refuses it. Then the handovers to the buyer, and deliver. |
| B8 | 1:46–1:56 | stellar.expert https://stellar.expert/explorer/testnet/tx/9214980ea8f3923ca0e036a803517dba2b3d1c1a12d8e5cbb481f31625eb7c0c, Successful, `handover(…, GDWN…TPPW, GAUK…CEFR, …)` outlined | On another shipment, two teammates authorised a handover with their own keys. The contract refuses any handover that both companies have not signed. |
| B9a | 1:56–2:19 | Scene 6 "Check it yourself.", read live (card "Live from Stellar testnet"): Delivered, handovers 4 of 4, the "Signed by Warehouse and Port · 635c99…" list, cursor to "Check the fingerprint" | Don't trust us. Check it. This page reads the real record of a test shipment live from Stellar testnet. Where is the coffee? Delivered, four of four handovers. Who signed? Both companies' keys, on every handover, each one linked to its transaction. Has anyone changed it? Your browser rebuilds the fingerprint from every step and compares it with the one on Stellar. |
| B9b | 2:19–2:32 | Click; MATCH from 2:20, held | (from 2:20) Match. No account, no login: anyone can run this check. |
| B10 | 2:32–2:48 | Scene 7: the headline "Rio–Miami first. Every lane next." and the "Subscription + Fee per shipment" chips. The paragraph naming ZIS, Cisbra and Camacol is hidden by a CSS rule injected only for the recording (it sits between the headline and the chips, index.html lines 292–293, so cropping cannot remove it) | We start with Rio to Miami. Every lane is next. Each company pays a subscription plus a fee per shipment, the way banks pay for SWIFT. We are building the rail that ports, airports and chambers of commerce can plug into. |
| B11 | 2:48–3:01 | End card, graphite #0E0F11 with lime: "Built at HackMeridian: custody_registry contract, 26 tests, verification scripts, this page" / "Prior work: Radox platform, transfer_agent contract" / "Open source, Apache-2.0 · github.com/pwsaragossy/rio-miami-rail · rio-miami-rail.vercel.app" / last 2 s silent | Built this weekend: the custody contract with its tests, the verification scripts and this page. Prior work, disclosed: the Radox platform and its transfer agent contract. The code is open source. |

Rubric coverage: User Value 20 (B1, B2) · Ecosystem Alignment 20 (B4, B7, B8) · Technical Execution 15 (B7, B9) · Innovation 15 (B3, B8) · Hackathon Progress 10 (B11) · Product Design 10 (B6, B9) · Market 10 (B5, B10).

### B7 depends on the public API going live
The API session (local_119461cd) answered at about 05:15 UTC. The /docs page and the "Try the API" card are built as a preview, waiting for Pedro's yes, and are not in production yet. Wording it asked for: "open rail API on Stellar testnet", not "Radox API". Its limits: 5 opens per 10 min per IP and 20 per hour for everyone, so take 1 and take 2 must sit inside one 10-minute window, and nothing else may open shipments meanwhile.
- Facts confirmed by the API session (05:20 UTC):
  - It is the open Custody Rail API of rio-miami-rail (Vercel functions next to the page), not the closed Radox platform API. Once it is in production it is publicly hosted, so "open rail API on Stellar testnet" is true.
  - Endpoints: POST /api/sandbox/shipments (open, about 9–15 s, two confirmed transactions), POST /api/sandbox/shipments/{key}/handover (about 5 s, both the giving and the receiving company sign: 2 signers in tx.signers, throwaway test keys held by the server), POST /api/sandbox/shipments/{key}/deliver, and GET /api/shipments/{key}.
  - Production needs Pedro's yes plus the sandbox key in Vercel.
- 05:26 UTC: /docs is in production (HTTP 200, the "Try the API" panel with Open a shipment, Wrong company and Verify the record buttons). The API session verified 18/18 on production. B7 can be recorded right after VIDEO GO, so the fallback below is no longer expected. Do at most 2–3 rehearsal opens before the take, because of the caps.
- If /docs is not in production by 08:30 UTC, the fallback B7 is: the explorer clip 03 for tx 635c99ac73cb13416e6b52f29ac9a067fbc615e01b8de962eb36245db3f0bd38 (captioned "recorded 2026-10-25"), then the clip 08b (captioned "Radox API, local test run on testnet · recorded response"). The narration becomes: "Now the real thing: a handover on Stellar testnet, one call to our contract, naming both companies. And a recorded response from the Radox API, in a local test run on testnet: delivered, four handovers." Nothing in this fallback says the Radox API is publicly hosted.

## Hard limits (every frame and every line was checked against these)
- Testnet only. Mainnet is left out of the video.
- The Radox backend is never called public. The public piece is "the open rail API on Stellar testnet" (/docs).
- No partner, chamber, port, initiative or person outside the team is named. ZIS, Cisbra and Camacol are hidden in B10.
- No users, pilots or revenue are claimed.
- The WTO figure appears only as the size of the problem, with its source on screen.
- "SWIFT for goods" stays. No caveats.
- The practice run is labelled, and its simulated API card is cut before it appears.
- "Signed" is said only where the chain proves it: a handover transaction succeeds only if both custodians' require_auth passes. B8 says "their own keys", not "their own computers".

## Production (who, minutes, clock from GO at about 05:45 UTC)
| Clock (UTC) | Step | Who |
|---|---|---|
| 05:45–06:15 | Narration for B1–B6 and B8–B11 with the Voicebox profile "Pedro (cloned, rail video)" on Pedro's Mac, then a whisper readback of every line. B7 waits for the API facts | Agent A |
| 05:45–06:30 | Playwright capture, 1920x1080: scenes 0–7 with their own timing (not `?play`, because it never shows MATCH at 1080p), the swiftshader WebGL flags so the globe renders, the CSS rule that hides the scene-7 paragraph, a live read of scene 6, and the 9214980e explorer page | Agent B |
| 06:30 | Storyboard to Pedro: 13 stills and the narration text. His notes go into the cut | Agent A |
| 07:00 | Rough cut without B7 (B7 shown as a placeholder card) | Agent A |
| when /docs is live (target ~08:00, last 08:30) | Record B7 live on a fresh shipment (2 takes inside one 10-min window), then place the B7 narration, which is generated earlier with the rest | Agent B, then A |
| 08:30–08:50 | Final assembly (ffmpeg): the bottom strip, the lower third, the WTO caption, the end card | Agent A |
| 08:50–09:10 | Independent review of the cut: contact sheet every 2 s, a transcript of the audio, a search for the forbidden words, the MATCH frame, every caption | Reviewer (not A or B) |
| 09:10–09:25 | Pedro watches and says OK | Pedro |
| 09:25–09:45 | Unlisted upload to Pedro's YouTube. The description carries the AI-voice line and the repo and page links | Pedro |
| 09:45–09:55 | One play while logged out (sound, names, numbers, cuts), notes on her card | Vhendala |
| 09:55–10:00 | Link into README and the form's "Video link" field | Rail session |

Gates: 08:30, no API → fallback B7. 10:30, ship the best reviewed cut. 11:00, last upload start. 11:30, last link paste (the portal accepts edits until 12:00). STATE.md's older "video by 08:00" is replaced by this clock.
Other fallbacks:
- Testnet unreachable: scene 6 in snapshot mode, and B9a then says "a saved snapshot of the real record", never "live".
- Voicebox fails: a new seed, then a server restart, then a stock voice with the disclosure changed to "Narration: AI voice".
- stellar.expert down: the clips from 2026-10-25.

## Pedro decides
1. Approve this plan and give VIDEO GO (recommended), or ask for changes first.
2. DECIDED 05:35 UTC (Pedro, via the chief-of-staff session): "Manter". The paragraph stays on the live page, and the option he picked says Paulo authorised the names. The video still hides it in B10, under the video brief's no-partner-name rule.
2b. Still open:
3. Narration: (a) an agent on Pedro's Mac with the cloned profile, which is fastest and keeps Vhendala's rule (synthetic voice) (recommended); (b) Vhendala on her machine with a stock voice, about 30 min more.

## Sources
Draft: marketing specialist. Review: reviewer card, verdict approve with changes; all 5 must-fixes applied, plus the minor fixes (WTO caption, 8 s MATCH hold, strip on every frame, no mainnet line, slow taps in B6).
Library: [[recording-the-landing-v3-page-play-45f2]] [[stellar-expert-shows-both-teammate-keys-2899]] [[founder-voice-in-public-text-sell-d820]] [[claims-hackmeridian-material-may-and-may-3e4f]] [[wording-the-rio-miami-deck-readme-ef38]] [[hackmeridian-rubric-7-criteria-weights-scored-50e2]] [[deck-and-video-rules-for-async-8b70]].
Not checked: how Voicebox reads this text, the GPU globe in a headed browser, the /docs page itself (preview not seen by this session), Paulo's OK, and team availability at 06:30, 09:10 and 09:25.
