---
tags:
  - board
status: in-progress
project: hackmeridian-rail
owner: session-hackmeridian-rail
member: vhendala
due: 2026-10-25
since: 2026-10-25
updated: 2026-10-25
asked: 
---

# Vhendala: video and team photo

State in [STATE.md](../projects/hackmeridian-rail/STATE.md). Owner's words (2026-10-25): "esse é o tipo de pedido que a vhendala deve cuidar, coloca logo isso no panel como pendencia que pode ser resolvida agora."

## Can be done now (before Sun 18:00)
- Video account: create or pick the YouTube or Vimeo account the team uploads to; upload a 10-second test clip as unlisted; open its link in a logged-out browser and confirm it plays. Rules: 2–4 min video on YouTube or Vimeo ([[hackmeridian-2026-rules-and-submission-requirement-5868]]).
- Team photo: one small photo of Pedro, Leo and Vhendala at check-in (Sun 09:00, Warehouse ONE16) for the team slide; the template asks for a small team picture and at most 3 lines per member ([[hackmeridian-2026-official-pitch-deck-template-d5c7]]).
- Narration / Audio: Vhendala definiu que a locução NÃO será feita por voz humana direta; deve-se usar Voicebox para gerar o áudio e a narração sintética do vídeo a partir do script da demo (Mon 00:00–03:00).

## Sunday
- 14:41 UTC (session-hackmeridian-rail): branch `three-machine` is now pushed to github.com/pwsaragossy/rio-miami-rail (de412a5), approved by Pedro. The signing steps above can start now; finish by 23:30 UTC.
- 14:37 UTC (session-hackmeridian-rail): three-machine steps for Vhendala's agent (task: sign one handover of the extra shipment from her own computer, by Sun 23:30 UTC). Route Warehouse -> Leo -> Vhendala -> Recipient; she signs two entries in one file (handover 2 as incoming custodian, handover 3 as outgoing); the rail session submits. The branch `three-machine` of rio-miami-rail is NOT pushed yet; the parent session pushes it after review, so step 1 works only after that. No secret leaves her computer: she shares one public key and one response file of signatures.
  1. Once pushed: `git clone https://github.com/pwsaragossy/rio-miami-rail.git && cd rio-miami-rail && git checkout three-machine && npm ci` (if already cloned: `git fetch origin three-machine && git checkout three-machine && npm ci`)
  2. Make her own testnet key (funded by the test faucet, no real money): `stellar keys generate vhendala --network testnet --fund`
  3. Print the public key: `stellar keys address vhendala` and write ONLY that G... line on this card. Never paste the output of `stellar keys secret`.
  4. Wait for Pedro's card line "request ready" (a gist link, the `--registry` value and the `--known` list). Those values come from the card, never from the request file.
  5. Fetch the request: `gh gist view <gist id> --filename request-vhendala.json > request-vhendala.json`
  6. Look first, nothing is signed without `--yes`: `node scripts/remote-auth.mjs sign --request request-vhendala.json --registry <C... from the card> --key vhendala <the --known flags from the card>`
  7. Show her the printed lines. She says yes only if: h2-to reads "from Leo to YOU", h3-from reads "from YOU to Recipient", the registry is the one on the card, no line says UNKNOWN. A "REFUSED" message means stop and write it here.
  8. After her yes, same command plus `--yes --out response-vhendala.json`
  9. Send it back: `gh gist create response-vhendala.json` and write the gist link on this card (the file holds only signatures).

## Later (per KICKOFF timeline)
- Mon 00:00–03:00: gerar áudio via Voicebox sobre a gravação de tela; manter cópia offline.
- Mon 06:00: upload do vídeo final (não-listado), colar o link no card do projeto, confirmar execução deslogado.

## For the owner to decide (central asks, all at once)

## Tasks
- Vhendala: first, steps 1–3 of the 14:37 line and post ONLY your public key (output of `stellar keys address vhendala`) on this card; the shipment cannot be prepared without it, by Sun 18:00
- Vhendala: then sign your handover when the REQUEST READY line appears on this card, by Sun 23:30
- Vhendala: run the README on your own computer from a clean clone, as a judge would, and write each step that fails on this card (fresh-run), Mon 00:00
- Vhendala: pick the YouTube or Vimeo account, upload a 10-second unlisted test clip, link on this card, by Sun 18:00
- Vhendala: team photo of Pedro, Leo and Vhendala for the team slide, by Sun 18:00
- Vhendala: open https://rio-miami-rail.vercel.app logged out and read the check.py result on the cards; anything red becomes a card line, at Sun 14:00 and 18:00
- Vhendala: read the finished demo script, deck draft and README as a judge, notes on this card, by Mon 01:00
- Vhendala: upload the final video (unlisted), link on this card, play it once against the scrub list, by Mon 08:00

## Decided
- 2026-10-25 12:36 UTC (vhendala-agent): Oi Pedro e Leo! Painel oficial conectado com auto-sync e acompanhando em tempo real (vimos os 11/22 entregáveis e os 7/7 hashes na testnet).
- 2026-10-25 ~11:30 UTC: setup done, both GitHub invites accepted (gh api collaborators shows vhendala on both repos).
- 2026-10-25: the owner's earlier assignment had Vhendala narrate; replaced by her Voicebox decision below.
- 2026-10-25: Vhendala (GitHub vhendala) abre o painel e supervisiona o projeto; convites aceitos.
- 2026-10-25: Vhendala comunicou formalmente que a narração NÃO será feita por sua voz; o vídeo deve usar Voicebox para sintetizar o áudio da demonstração a partir do roteiro. Vhendala mantém o apoio na conta de vídeo, teste, foto do time e na revisão de produto.
