# Landing page v2: brief for Leo's agent

Owner: Leo's agent. Asked by Pedro, Sun 25 Oct 20:40 UTC ("manda o agente do leo fazer").

## Why
Pedro scored the current page and the globe v1 preview 3/10 on Design and UX: "ninguém entendeu nada e não motivou ninguém". Proof without a story does not convince. A layperson must understand the product and want it.

Ambition: a first-time visitor with no blockchain knowledge, cold, in 30 seconds on a phone, says back: goods move from Rio to Miami through several companies; each company hands custody to the next and both confirm; one shared record follows the goods across every company, like SWIFT for cargo; anyone can check it. And says why it matters.
Judge (set by Pedro's session, not by you): (1) real people, cold, 30 s, answers written verbatim on your card: Vhendala (she has not seen v2) and one person Pedro picks; (2) the existing Playwright cases on the preview (both shipments, live and offline snapshot, 375 and 1280 px, Verify head MATCH); (3) every colour and font in the page CSS is from the token list below.

## Where
- Repo `pwsaragossy/rio-miami-rail`, new branch `landing-v2` from `origin/main`, folder `page/`. Keep `app.js` verification logic, `snapshot.json` and the offline mode working.
- Do not touch `main` or production. Push the branch; Pedro's session deploys a Vercel preview from it (the Vercel account is Pedro's) and sends the URL to the testers.
- Data you can use: `proofs/lifecycle.json` (7 tx, 5 parties), `proofs/three-machine.json` (Leo and Vhendala signed on their own computers), `proofs/multi-chain.json` (two companies' chains on one registry, sharing a terminal and a vessel). Sourced numbers: `projects/hackmeridian-rail/PROBLEM-NUMBERS.md` and `MARKET-NUMBERS.md` in the workspace.

## The story, one idea per screen, plain English, no hashes or jargon above the proof section
1. The stakes. A container leaves Rio. Five companies touch it: warehouse, port, carrier, customs, recipient. Each keeps its own paper or legacy system. Nobody can say who holds it right now. Numbers: about 45 million bills of lading a year, about 11% electronic (DCSA); 22% of cargo thefts involve insiders (TT Club & BSI, Apr 2026).
2. The idea. One shared record that travels with the goods across every company, like SWIFT did for bank messages. Each company integrates once and reaches everyone.
3. Watch it happen. A 3D globe (orthographic, drag to rotate, settles on the Atlantic), the Rio–Miami arc, a container moving along it, each stop lighting up in lime as the two companies confirm the handover, one caption per step a 12-year-old understands ("The port hands the container to the ship. Both confirm."). Each lit stop is backed by its real testnet transaction.
4. Many supply chains, one rail. The multi-chain run: two companies' routes drawn on the same globe, sharing the terminal and the vessel, internal handovers inside a company and external handovers between companies.
5. Why you can trust it. One button: Verify. MATCH. Anyone can check, no login. Proof details (hashes, ledgers, contract IDs) collapsed below.
6. What comes next. Rio–Miami is the pilot corridor; Radox is part of the Rio–Miami trade-corridor initiative and its technology rail; any tokenized asset on Stellar that follows the standard will use the rail through one API.

## Voice (Pedro's rule: sell only the strong part)
Confident founder voice. No hedges ("not yet", "none confirmed", "only a demo"). Never say anything false: no partner, port, airport or chamber named, no signed deal, no users or revenue. Keep the small label "Stellar testnet · test keys".

## Design: Radox Signal tokens (copy these values, nothing else)
Font: Inter (self-host the woff2 in `page/`, no CDN). Radius 0.625rem. Dark theme:
- background #0E0F11 (220 10% 6%), foreground #E7E8EA (220 7% 91%)
- card #131517 (210 10% 8%), popover/secondary/muted #16181B (216 10% 10%)
- primary/accent/ring lime #C6F24E (76 86% 63%), text on lime #0E0F11
- muted-foreground #8A8F98, soft #C8CBD0, faint #7F848E
- border #1F2329, border-hover #303740
- success hsl(160 60% 40%), warning hsl(35 90% 50%), info #9FB2CC, destructive-text hsl(0 84% 68%)
One lime signal on dark graphite. No other colours.

## Motion and budget
d3-geo + world-110m TopoJSON, vendored in `page/` (no runtime CDN). Scroll-driven reveal, container animation, stops lighting up. `prefers-reduced-motion`: a static, complete version. Added JS + data at most 200 KB gzip. Works at 375 px.

## Gates
- 22:30 UTC: branch pushed, Playwright cases pass, token check passes; one line on your card with the commit.
- Pedro's session deploys the preview and runs the cold test with Vhendala and Pedro's tester.
- Production only if the cold test passes. If it does not close by Mon 02:00, production stays as it is.
