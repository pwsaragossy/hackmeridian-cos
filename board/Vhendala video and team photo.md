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
- 16:10 UTC (session-hackmeridian-rail): THREE-MACHINE SHIPMENT DONE, thank you. Leo's and Vhendala's responses checked independently (invocation bytes, nonces, ed25519 signatures under their own keys), then submitted from Pedro's Mac: handover 1 Warehouse->Leo 861544e4…, handover 2 Leo->Vhendala 9214980e…, handover 3 Vhendala->Recipient 850da342…, deliver 849c268d…, all successful on Horizon (ledgers 5384199-5384202). verify-head MATCH (head d9cf3a5f…614d); handover-signers shows Leo GDWN…TPPW and Vhendala GAUK…CEFR in the auth entries. Proof: rio-miami-rail branch three-machine d02424d, proofs/three-machine.json + proofs/tx/ (pushed). Frozen 7 untouched, check.py 7.
- 16:00 UTC (session-hackmeridian-rail): Vhendala's response CHECKED and valid (response-vhendala.json, commit 1ad0d6f): entries h2-to and h3-from, registry CD7BUCY3…NH3F, invocation bytes and nonces identical to the request, ed25519 signatures valid under GAUKDWMR…CEFR (CAP-71 address-bound payload), expiry ledger 5405258. Nothing more to do on her side; submit runs after Leo's response.
- 15:50 UTC (vhendala-agent): signed (`projects/hackmeridian-rail/three-machine/response-vhendala.json` written and pushed; h2-to from Leo to Vhendala and h3-from from Vhendala to Recipient verified against registry CD7BUCY3…NH3F).
- 15:25 UTC (session-hackmeridian-rail): REQUEST READY for Vhendala. Shipment opened on testnet at 15:24 (registry CD7BUCY3…NH3F, open tx 34860ed8…, both SUCCESS). Valid about 30 h. The request file is in the shared workspace (no gist). Paste in order, from your rio-miami-rail clone on branch three-machine:
  1. `git -C ~/hackmeridian pull`
  2. `KEY=vhendala` (check: `stellar keys address $KEY` prints GAUKDWMR…CEFR)
  3. Look (signs nothing): `node scripts/remote-auth.mjs sign --request ~/hackmeridian/projects/hackmeridian-rail/three-machine/request-vhendala.json --key $KEY --registry CD7BUCY3DC7GTHRWFRBHNOFPMGVCHFDL4LHKXZNGEJISSGHI24KSNH3F --known Warehouse=GAVDGEJFRQ4O2XQD7RTDJ5UJWDQ252ZFP6FIBFOV4PE3CM4GBYPH5UTZ --known Leo=GDWNU6TTJCZOQ3ZQI5NYALATL7IVMHR4PWEP5E3TXEK7EKOJNDORTPPW --known Vhendala=GAUKDWMR5EZWVG46O7OREZQ7ZY37NSHTFMT3US3RYICYT3HOJL4UCEFR --known Recipient=GD54SSZGLU6QXILEBQMJZ5F5IW35UELJN3FEKC77ZE23BXK5BHPV2CO4`
  4. Sign only if the printed lines say h2 "from Leo to YOU" and h3 "from YOU to Recipient", show the registry CD7BUCY3…NH3F and no UNKNOWN or REFUSED: `node scripts/remote-auth.mjs sign --request ~/hackmeridian/projects/hackmeridian-rail/three-machine/request-vhendala.json --key $KEY --registry CD7BUCY3DC7GTHRWFRBHNOFPMGVCHFDL4LHKXZNGEJISSGHI24KSNH3F --known Warehouse=GAVDGEJFRQ4O2XQD7RTDJ5UJWDQ252ZFP6FIBFOV4PE3CM4GBYPH5UTZ --known Leo=GDWNU6TTJCZOQ3ZQI5NYALATL7IVMHR4PWEP5E3TXEK7EKOJNDORTPPW --known Vhendala=GAUKDWMR5EZWVG46O7OREZQ7ZY37NSHTFMT3US3RYICYT3HOJL4UCEFR --known Recipient=GD54SSZGLU6QXILEBQMJZ5F5IW35UELJN3FEKC77ZE23BXK5BHPV2CO4 --yes --out ~/hackmeridian/projects/hackmeridian-rail/three-machine/response-vhendala.json`
  5. Send it back (the file holds only signatures): `cd ~/hackmeridian && git add projects/hackmeridian-rail/three-machine/response-vhendala.json && git commit -m "three-machine: response from vhendala" && git push`
  Then one line here: "signed". Pedro's machine submits all 4 transactions after both responses arrive.
- 15:16 UTC (vhendala-agent): steps 1-3 DONE (three-machine checked out, npm ci clean, testnet account funded). Vhendala public key: GAUKDWMR5EZWVG46O7OREZQ7ZY37NSHTFMT3US3RYICYT3HOJL4UCEFR — waiting for REQUEST READY on this card.
- 15:16 UTC (vhendala-agent): 14:00/15:00 check DONE — https://rio-miami-rail.vercel.app returns 200 OK logged out and check.py result on the cards is 7/7 PASS.
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
- 14:46 UTC (leo-agent): for your three-machine handover: steps in projects/hackmeridian-rail/THREE-MACHINES.md. First step: on your computer `stellar keys generate <alias> --network testnet --fund`, then post `stellar keys address <alias>` (public key only) here.
- Vhendala: first, steps 1–3 of the 14:37 line and post ONLY your public key (output of `stellar keys address vhendala`) on this card; the shipment cannot be prepared without it, by Sun 18:00
- Vhendala: then sign your handover when the REQUEST READY line appears on this card, by Sun 23:30
- Vhendala: run the README on your own computer from a clean clone, as a judge would, and write each step that fails on this card (fresh-run), Mon 00:00
- Vhendala: pick the YouTube or Vimeo account, upload a 10-second unlisted test clip, link on this card, by Sun 18:00
- Vhendala: team photo of Pedro, Leo and Vhendala for the team slide, by Sun 18:00
- Vhendala: open https://rio-miami-rail.vercel.app logged out and read the check.py result on the cards; anything red becomes a card line, at Sun 14:00 and 18:00
- Vhendala: read the finished demo script, deck draft and README as a judge, notes on this card, by Mon 01:00
- Vhendala: upload the final video (unlisted), link on this card, play it once against the scrub list, by Mon 08:00

## Decided
- 2026-10-25 16:12 UTC (Vhendala): Não será criada conta nova no YouTube; será usado o canal do YouTube do Pedro que já está pronto para subir o vídeo (teste e final).
- 2026-10-25 12:36 UTC (vhendala-agent): Oi Pedro e Leo! Painel oficial conectado com auto-sync e acompanhando em tempo real (vimos os 11/22 entregáveis e os 7/7 hashes na testnet).
- 2026-10-25 ~11:30 UTC: setup done, both GitHub invites accepted (gh api collaborators shows vhendala on both repos).
- 2026-10-25: the owner's earlier assignment had Vhendala narrate; replaced by her Voicebox decision below.
- 2026-10-25: Vhendala (GitHub vhendala) abre o painel e supervisiona o projeto; convites aceitos.
- 2026-10-25: Vhendala comunicou formalmente que a narração NÃO será feita por sua voz; o vídeo deve usar Voicebox para sintetizar o áudio da demonstração a partir do roteiro. Vhendala mantém o apoio na conta de vídeo, teste, foto do time e na revisão de produto.
