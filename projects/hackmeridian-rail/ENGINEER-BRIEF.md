# Engineer brief: 10 minutes with a Stellar engineer at the venue

## Para o Pedro (PT)

**O que o contrato faz, em uma frase:** registra quem está com a carga em cada trecho da viagem. Cada passagem de mão só vale se quem entrega e quem recebe assinarem a mesma transação Stellar. Se faltar uma das assinaturas, a chamada falha.

Como funciona, em quatro pontos:
- `open`: a Radox (operador) abre a remessa com a rota fixa. A chave da remessa é sha256(container | origem).
- `handover`: cada troca de custodiante exige a assinatura dos dois lados, e o próximo precisa ser a próxima parada da rota. O token continua com o dono; só a custódia muda.
- `deliver`: o último custodiante e o dono do token assinam a entrega. O resgate (burn) usa o `redeem` que a Radox já tem.
- Na abertura, em cada passagem e em cada atestado de sensor (`attest`), o contrato atualiza um hash de 32 bytes, o "head". O RPC guarda os eventos só por uns 7 dias, então o histórico é refeito a partir do Horizon e conferido contra esse head.

Os 7 passos rodaram na testnet, todos com chaves de teste. Contrato: `CCBJVXMJYWPHTDJHDFPRGKPGXGEP24JOPJAMUS5C3BMZJTRTWR2H4LII`.

**As 3 perguntas, nesta ordem:**
1. Autorização: é certo exigir as duas assinaturas dentro do contrato, ou empresas reais usariam contas-contrato com regras próprias (por exemplo, duas pessoas aprovando)?
2. Head vs eventos: guardar um hash no contrato e conferir o histórico pelo Horizon é o padrão certo, ou existe um jeito melhor de manter histórico por anos?
3. Padrão: isso vira um SEP? Por onde se começa, e quem deveria ler o rascunho primeiro?

**Regra:** nada que o engenheiro disser vai para o deck, o vídeo ou o README sem o OK dessa pessoa, nem o nome dela. Anote a resposta e a pessoa; depois a sessão do deck decide o que usar.

Você mostra o texto em inglês abaixo na tela do celular.

---

## For the engineer (EN, show this)

**What it is.** `custody_registry`, a Soroban contract that records who physically holds a tokenized good at each leg of a shipment. Testnet only, test keys. Contract `CCBJVXMJYWPHTDJHDFPRGKPGXGEP24JOPJAMUS5C3BMZJTRTWR2H4LII`. Code: github.com/pwsaragossy/rio-miami-rail.

**How it works.**
- `open`: the operator opens a shipment on a fixed route. The key is sha256(container | origin).
- `handover(from, to, evidence_hash, assurance)`: `from.require_auth()` and `to.require_auth()` run in the same call, and `to` must be the next stop on the route. Ownership of the token does not move; only custody does.
- `deliver`: needs the final custodian and the token holder. The burn uses an existing `redeem`.
- `open`, each `handover` and each `attest` (a signed event from an allow-listed source, such as a sensor) extend a 32-byte `head` kept in persistent storage: sha256 of the previous head plus that step's fields. RPC keeps events for about 7 days, so we replay each shipment's transactions from Horizon and check them against the stored head.
- Admin can `freeze` a shipment and `pause` the contract.

**Three questions.**
1. **Auth model.** Custodians are plain accounts today, and both sign one transaction. Would real logistics companies use contract accounts with their own policies (for example, two approvers) instead? Does anything in the design break if they do?
2. **Head chain vs events.** Is an on-chain head plus Horizon replay the right way to keep a verifiable history for years? Or would you index events into our own store, or use something else?
3. **A standard.** If several companies should integrate once, is a SEP the right vehicle, as opposed to a contract interface only? Where would you start, and who should review a first draft?

We will not quote you or use your name anywhere without your OK.

## Sources
- Multiple addresses in one call, using `require_auth` on each: developers.stellar.org/docs/learn/fundamentals/contract-development/authorization (read 2026-10-25 19:18 UTC); [[two-signers-in-one-soroban-call-1b93]].
- RPC `getEvents` keeps about 7 days: developers.stellar.org/docs/build/guides/events (read 2026-10-25); [[stellar-rpc-getevents-keeps-about-7-187e]].
- SEPs are open documents in the stellar-protocol GitHub repo, with a "lightweight approval process"; CAPs change the core protocol: developers.stellar.org/docs/learn/fundamentals/stellar-ecosystem-proposals (read 2026-10-25).
- No SEP for chain of custody was found (searched 2026-10-24): [[no-sep-and-no-stellar-project-aa39]].
- Contract behaviour: custody_registry lib.rs, open lines 242-286, handover 291-327, deliver 363-390.
