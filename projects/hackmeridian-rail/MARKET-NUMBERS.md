# Market numbers: pilot corridor and global layer

Verified 2026-10-25, 19:11–19:25 UTC. Three researcher subagents opened the sources. An independent reviewer subagent then re-opened every URL, read the UNCTAD and WTO PDFs as text, and compared each quote word for word.

Claims guard: these are market figures, not ours. They size the trade our registry is built for. They are not our traction and not our revenue, and no sentence may say that we serve, process or capture any share of them. There is no price in this file: pricing is Pedro's decision.

## 1. Pilot corridor (Brazil–US, Miami)

| # | Number | Exact claim (use this wording) | Source (verbatim on page) | Date | Reviewer |
|---|---|---|---|---|---|
| C1 | US$94.2B | US–Brazil goods trade (exports plus imports) was about US$94.2 billion in 2025. | US Census Bureau, "Trade in Goods with Brazil", annual 2025: exports 54,329.2, imports 39,881.5 (US$ millions, nominal) [1]. The sum is ours. | 2025 data | KEEP-WITH-FIX |
| C2 | US$6.1B, #1 | Brazil was Florida's largest goods export market in 2025: US$6.1 billion, 8% of the state's goods exports. | USTR: "The state's largest market was Brazil." / "Florida exported $6.1 billion in goods to Brazil in 2025, representing 8 percent of the state's total goods exports." [2] | 2025 data | KEEP |
| C3 | ~0.87M TEU | A commercial booking-data vendor counts about 525,000 TEU Brazil-to-US and 343,000 TEU US-to-Brazil in 2024, about 0.87 million TEU in all. | Vizion (vendor blog): "In 2024, Brazil exported 525,054 TEU to the United States" / "U.S. exports to Brazil totaled just 342,588 TEU" [3] | 17 Jul 2025 | KEEP-WITH-FIX (vendor estimate) |
| C4 | 1,115,058 TEU | PortMiami handled 1,115,058 TEU in fiscal year 2025 (Oct 2024 to Sep 2025). | Miami-Dade County release [4] | 2 Dec 2025 | KEEP-WITH-FIX |

Corridor cautions (reviewer):
- C3 is a vendor estimate built from booking data. A second vendor (Datamar) is about 5% lower on the US-to-Brazil leg. No primary TEU count for this lane was found (BTS, MARAD, ANTAQ and Comex Stat were searched). Say "about 0.87 million TEU (Vizion, vendor estimate)".
- C4 is PortMiami's total, all trades. No source says how much of it is Brazil cargo. Never put C3 and C4 together in a way that implies PortMiami carries the Brazil volume.

## 2. Global layer

| # | Number | Exact claim (use this wording) | Source (verbatim on page) | Date | Reviewer |
|---|---|---|---|---|---|
| G1 | US$26.26T | World merchandise exports were worth US$26.26 trillion in 2025. | WTO: "The current US dollar value of world merchandise trade as measured by exports was US$ 26.26 trillion in 2025, up 7% compared to 2024." [5] | Mar 2026 | KEEP-WITH-FIX (wto.org URL) |
| G2 | ~80% | Around 80% of international goods trade by volume is carried by sea. | UNCTAD: "Around 80% of the volume of international trade in goods is carried by sea" [6] | page undated | KEEP-WITH-FIX |
| G3 | 12,720 Mt | Seaborne trade reached 12.72 billion tonnes in 2024. | UNCTAD Review of Maritime Transport 2025, ch. I: "Maritime trade volumes reached 12,720 million tons in 2024, growing by 2.2 per cent (Clarksons Research, 2025a, July)" [7] | Sep 2025 | KEEP |
| G4 | 920M TEU | Ports worldwide handled 920 million TEU in 2024. | UNCTADstat: "In 2024, 920 million twenty-foot equivalent units (TEUs) of containers were handled in ports worldwide." [8] | data updated 15 Apr 2026 | KEEP |
| G5 | 45M | Ocean carriers issue around 45 million bills of lading a year. | DCSA: "Ocean carriers issue around 45 million bills of lading a year." [9] (already verified in PROBLEM-NUMBERS.md) | 15 Feb 2023 | KEEP |
| G6 | 80–90% | The WTO says 80 to 90% of world trade relies on trade finance. | WTO: "Some 80 to 90 per cent of world trade relies on trade finance (trade credit and insurance/guarantees), mostly of a short-term nature." [10] | page undated | KEEP-WITH-FIX (context, not a market size) |
| G7 | US$350B | MIGA puts the trade finance gap in Latin America and the Caribbean at US$350 billion, of a US$1.5 trillion global gap. | MIGA: "the worldwide trade finance gap currently stands at $1.5 trillion" / "Latin America and the Caribbean accounting for $350 billion of this shortfall." [11] | 5 May 2025 | KEEP-WITH-FIX |
| G8 | 13 | UNCITRAL's MLETR status page lists 13 jurisdictions with laws based on the model law for electronic transferable records; neither the US nor Brazil is among them. | UNCITRAL status table, counted by the reviewer [12] | page undated, checked 25 Oct 2026 | KEEP |

Global cautions (reviewer):
- G4 counts every lift at every port, so one container journey is counted several times. Never say "920 million containers shipped".
- G3 is UNCTAD citing Clarksons Research, a commercial provider.
- G7 conflicts with ADB's US$2.5 trillion global gap (Dec 2025), which is already on the deck. Show one global gap and name its source. Use G7 only for the regional US$350B, and say the global figure differs by source.
- G8 does not mean the US has no law for electronic bills of lading: some US state laws sit outside this model-law list.

## 3. Bottom-up line (no price)

Survives (B1, illustration, not a forecast and not TAM): "Illustratively, if each of the roughly 45 million ocean bills of lading issued a year (DCSA, 2023) passed through the 4 dual-signed handovers in our testnet demo, that would be about 180 million custody handovers a year. The 4 is our design assumption, not a market statistic."

Dropped (B2, corridor): about 0.87M TEU × 4 handovers ≈ 3.5M. A TEU is not a shipment, and one bill of lading usually covers several containers. The TEU figure is a vendor estimate, and no Brazil–US count of bills of lading or shipments was found. For the corridor, say only C1–C3 and do not multiply them.

Also dropped: the World Shipping Council's "about 250 million containers a year" (secondary, source page 404); ICC DSI "US$30–40B trade growth from eBL" (no method on the page); ICC "US$9T to G7 trade" (2021, secondary, modelled).

## 4. Ready sentences (market figures, not ours)

- Deck (market slide): "Pilot corridor: US–Brazil goods trade was about US$94 billion in 2025¹, and Brazil was Florida's largest export market². Global layer: US$26.3 trillion of merchandise exports³, around 80% of it by volume moving by sea⁴, documented by around 45 million ocean bills of lading a year⁵." Footnotes: ¹ US Census Bureau, 2025. ² USTR, 2025. ³ WTO, Mar 2026. ⁴ UNCTAD. ⁵ DCSA, 2023. Small print: "Market figures, not Radox volumes."
- Deck (optional bottom-up line, small print, labelled "illustration"): the B1 sentence above, word for word.
- README (Market section): "The pilot corridor carries about US$94 billion a year in US–Brazil goods trade (US Census Bureau, 2025), and Brazil is Florida's largest goods export market at US$6.1 billion (USTR, 2025). Worldwide, merchandise exports reached US$26.26 trillion in 2025 (WTO), and ocean carriers issue around 45 million bills of lading a year (DCSA, 2023). These are market figures, not our volumes."
- Form (Market / ecosystem potential field): "We start on a corridor of about US$94 billion a year in US–Brazil goods trade (US Census, 2025), where Brazil is Florida's top export market (USTR). The same custody standard applies to the around 45 million ocean bills of lading issued worldwide each year (DCSA). Market figures, not our traction."

## Sources

[1] US Census Bureau, "Trade in Goods with Brazil": https://www.census.gov/foreign-trade/balance/c3510.html (opened 2026-10-25)
[2] USTR, "Florida" trade data page: https://ustr.gov/countries-regions/united-states-trade-data/florida (opened 2026-10-25)
[3] Vizion, "The 50% tariff threat: what Brazil–U.S. booking data reveals", 17 Jul 2025: https://www.vizionapi.com/blog/the-50-tariff-threat-what-brazil-u-s-booking-data-reveals (opened 2026-10-25; commercial vendor)
[4] Miami-Dade County news release, 2 Dec 2025: https://www.miamidade.gov/global/release.page?Mduid_release=rel1764622080449470 (opened 2026-10-25)
[5] WTO, Global Trade Outlook and Statistics, March 2026: https://www.wto.org/english/res_e/booksp_e/gtos0326_e.pdf (opened 2026-10-25)
[6] UNCTAD, Review of Maritime Transport topic page: https://unctad.org/topic/transport-and-trade-logistics/review-of-maritime-transport (opened 2026-10-25)
[7] UNCTAD, Review of Maritime Transport 2025, chapter I: https://unctad.org/system/files/official-document/rmt2025ch1_en.pdf (opened 2026-10-25)
[8] UNCTADstat, container port throughput: https://unctadstat.unctad.org/insights/theme/109 (opened 2026-10-25)
[9] DCSA, 15 Feb 2023: https://dcsa.org/newsroom/dcsas-member-carriers-commit-to-a-fully-standardised-electronic-bill-of-lading-by-2030 (opened 2026-10-25)
[10] WTO, trade finance page: https://www.wto.org/english/thewto_e/coher_e/tr_finance_e.htm (opened 2026-10-25)
[11] MIGA press release, 5 May 2025: https://miga.org/press-release/miga-and-idb-invest-sign-first-ever-trade-finance-guarantee-framework (opened 2026-10-25)
[12] UNCITRAL, MLETR status: https://uncitral.un.org/en/texts/ecommerce/modellaw/electronic_transferable_records/status (opened 2026-10-25)

Library: [[brazil-to-us-corridor-sizes-census-cc8c]], [[unctad-920-million-teu-port-throughput-3e8e]], [[wto-80-to-90-percent-of-98f6]], [[dcsa-45-million-bills-of-lading-1af2]], [[adb-trade-finance-gap-survey-dec-d033]], [[market-numbers-reviewer-pass-corridor-teu-2a95]].
