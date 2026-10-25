# Look: Radox Custody Rail (page + deck)

Decided 2026-10-25 by the owner ("Usar Signal (Recomendado)"). The look reuses Radox's own identity "Signal" (radox-internal `DESIGN.md`): dark graphite, monochrome, one lime accent. It is adapted for a projector. Source and contrast numbers: [[radox-custody-rail-look-signal-adapted-d030]]. Effect: "sóbrio, tipo terminal de porto: grafite com uma só linha lime marcando o corredor Rio-Miami, legível do fundo da sala."

## Colours

| Role | Page and dark deck slides | Cream deck slides (template) |
|---|---|---|
| Background | `#0E0F11` | `#F7F6F2` (keep the template's) |
| Card / panel | `#131517` | `#FFFFFF`, 1px border `#DFDDD6` |
| Hairline | `#1F2329` | `#DFDDD6` |
| Text | `#E7E8EA` (15.6:1) | `#0E0F11` (17.7:1) |
| Secondary text | `#A3A8B0` (8.0:1) | `#4D5560` (7.0:1) |
| Accent | lime `#C6F24E`, text on lime always `#0E0F11` (14.8:1) | dark lime `#556F00` for text and lines (5.3:1); a pill or button is lime `#C6F24E` fill with `#0E0F11` text |
| Passive status, links | `#9FB2CC` (8.9:1) | `#3F5675` (6.9:1) |

The template's yellow `#FDDA24` is replaced by lime on dark slides and never used for text on cream (1.28:1). Lime, Signal muted `#8A8F98` and slate `#9FB2CC` all fail on cream, so never put them on it as text. Do not use Signal's faint `#7B808A` for text on a projector.

## Deck (DECK-TEMPLATE.pptx)

- Slides: the cover and the proof/demo slides are dark (`#0E0F11`); text slides keep the template's cream.
- Fonts: keep the template's (Inter Tight titles, Instrument Sans body, JetBrains Mono labels). Install nothing new.
- Sizes: titles 40 pt or more; body 24 pt; nothing that must be read under 18 pt. The template's 12 pt footer stays decorative.
- Keep the template's fixed parts: HackMeridian logo, footer, "PITCH STEP 0X/04" labels. On dark slides, check that the logo has a variant that reads on dark.
- Signature device: the Rio de Janeiro → Miami corridor as one hairline with lime endpoints or dots, `#556F00` on cream.
- Bans (from Signal): no gradients, shadows, glass or blur, and no card grids. No coloured side stripes.
- Check: render each slide at 1280x720 and read it at arm's length before export.

## Page

Already applied at https://rio-miami-rail.vercel.app (rio-miami-rail `page/index.html`, CSS variables in `:root`). Inter, body 18 px, labels 14 px minimum, focus ring 2px lime, and a 48 px target for the "Verify head" button. The fixed label "Testnet - test keys - not real custodians" stays at 16 px with a lime border.
