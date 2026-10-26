# Review v14 cover and cost slide (slides 1, 3)
Verdict: PASS with 2 must-fix wording items. check_deck exit 0 (slides=10, failures=0).

1. Title/tagline: slide 1 title + subtitle and tagline match FORM lines 8 and 14 and PITCH-FINAL word for word. OK.
2. Sources opened:
 - WTO tr_finance_e.htm: "Some 80 to 90 per cent of world trade relies on trade finance" (trade credit and insurance/guarantees). No date on the overview itself (page lists dated news items up to 16 Oct 2026). "undated page" is correct. README matches.
 - ADB survey page: "the estimated global trade finance gap remains at $2.5 trillion, as in 2023." Publication December 2025. Deck matches; no "requested/approved". Deck says "US$2.5T" where README says "about US$2.5 trillion": acceptable shorthand.
3. MUST-FIX A: "Finance runs blind." overstates (all finance, always) and sits over a R$900M robbery card that is not about finance. Replace with: "Cargo goes missing. No shared record." (6 words; matches README problem statement, framing = companies, no credit-fix claim). The "The gap:" line is already narrow and fine.
4. Hin Leong / HSBC: none in build_deck.py code or text. Only a source comment (line 196, "Hin Leong cut") and PITCH-FINAL.md line 27 "(market size; Hin Leong cut)". Not on slides; remove the PITCH-FINAL mention if that file is ever published.
5. MUST-FIX B: slide 1 "Pilot corridor: Rio–Miami" differs from README/FORM "First corridor: Rio–Miami" and "pilot" implies a running pilot, while FORM says the first live shipment with a financial institution is still next. Replace with: "First corridor: Rio–Miami".
6. Layout (s-01): "Pilot corridor" baseline ~y663, logos start ~y715; no overlap; nothing collides with the QR/route graphic. s-03: three cards fit, no clipping.

## Versions
v1 (as submitted): "Finance runs blind." / "Pilot corridor" -> README/FORM mismatch on corridor word, overclaim on finance.
v2 (this review): "No shared record." / "First corridor" -> matches README word for word, no claim beyond the rail; judge: README ec97106, FORM, WTO/ADB quotes above, check_deck exit 0.
v3 (optional): none needed; further change would exceed scope.
