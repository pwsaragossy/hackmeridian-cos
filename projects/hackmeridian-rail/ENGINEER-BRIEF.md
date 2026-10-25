# Engineer brief: 10 minutes with a Stellar engineer at the venue

## Para o Pedro (PT)

**O que o contrato faz, em uma frase:** registra quem está com a carga em cada trecho da viagem. Cada passagem de mão só vale se quem entrega e quem recebe assinarem a mesma transação Stellar. Se faltar uma das assinaturas, a chamada falha.

Como funciona, em quatro pontos:
- `open`: a Radox (operador) abre a remessa com uma rota fixa. Nosso sistema calcula a chave como sha256(container | origem); o contrato só guarda essa chave.
- `handover`: cada troca de custodiante exige a assinatura dos dois lados, e quem recebe precisa ser a próxima parada da rota. O token continua com o dono; só a custódia muda.
- `deliver`: o último custodiante e quem recebe a carga assinam a entrega. Atenção: o contrato não confere se essa pessoa tem mesmo o token. O resgate (burn) é uma chamada separada, o `redeem` que a Radox já tem.
- Na abertura, em cada passagem e em cada atestado de sensor (`attest`), o contrato atualiza um hash de 32 bytes, o "head". O RPC guarda os eventos por cerca de 7 dias no padrão, então o histórico é refeito a partir do Horizon e conferido contra esse head.

Os 7 passos rodaram na testnet, todos com chaves de teste. Contrato: `CCBJVXMJYWPHTDJHDFPRGKPGXGEP24JOPJAMUS5C3BMZJTRTWR2H4LII`.

**As 3 perguntas, nesta ordem:**
1. Assinatura: o contrato já aceita contas-contrato. A dúvida real é como duas empresas assinam a mesma transação na prática.
2. Histórico: o Horizon público guarda só um ano e vai ser descontinuado, e é dele que hoje refazemos o histórico. Para guardar anos, qual é o caminho certo?
3. Padrão: isso vira um SEP ou basta uma interface de contrato? Por onde se começa, e quem deveria ler o rascunho primeiro?

**Regra:** nada que o engenheiro disser vai para o deck, o vídeo ou o README sem o OK da pessoa, e o nome dela também não. Anote a resposta e quem respondeu; depois a sessão do deck decide o que usar.

O texto em inglês abaixo é para mostrar na tela do celular.

---

## For the engineer (EN, show this)

**What it is.** `custody_registry`, a Soroban contract that records who physically holds a tokenized good at each leg of a shipment. Testnet only, test keys. Contract `CCBJVXMJYWPHTDJHDFPRGKPGXGEP24JOPJAMUS5C3BMZJTRTWR2H4LII`. Code: github.com/pwsaragossy/rio-miami-rail.

**How it works.**
- `open`: the operator opens a shipment on a fixed route. The key is sha256(container | origin), computed by our client; the contract treats it as an opaque 32-byte key.
- `handover(from, to, evidence_hash, assurance)`: `from.require_auth()` and `to.require_auth()` both run in one call, and `to` must be the next stop on the route. The token never moves; only custody does.
- `deliver(final_custodian, holder)`: both must sign, and every handover must be done. The contract does not check that `holder` owns the token. The burn is a separate `redeem` call.
- `open`, each `handover` and each `attest` extend a 32-byte `head` in persistent storage: sha256 of the previous head plus that step's fields. `attest` comes from an allow-listed source, such as a sensor, and still works on a delivered or frozen shipment.
- Admin can `freeze` a shipment and `pause` the contract.

**Three questions.**
1. **Co-signing in practice.** `require_auth` already works with contract accounts, so we expect the design to hold. Our concern is operations: two companies must co-sign one invocation. Is the normal pattern for each side to sign its auth entry separately and one party to submit? Or is there a better pattern?
2. **History over years.** Shipments live in persistent storage. Each write or read in a transaction extends the TTL to about 30 days once fewer than 7 days remain. Expired persistent entries are archived, not deleted, and are restored when a transaction touches them. The chain of handovers is also in events, and RPC keeps events for about 7 days by default. Horizon is documented as "soon to be deprecated", and SDF's public Horizon keeps one year of history. For years of history, would you rely on archival and restore, on our own indexer fed by Galexie, or on a third-party Horizon?
3. **A standard.** If several companies should integrate once, is a SEP the right vehicle, or only a contract interface (as SEP-41 is for tokens)? Where would you start, and who should review a first draft?

We will not quote you or use your name anywhere without your OK.

## Sources
- Many addresses can call `require_auth` in one invocation, and contract accounts can set their own policies: developers.stellar.org/docs/learn/fundamentals/contract-development/authorization (read 2026-10-25 19:18 UTC); [[two-signers-in-one-soroban-call-1b93]].
- Horizon "will soon be deprecated" (developers.stellar.org/docs/data/indexers, undated); SDF's public Horizon "had its historical data truncated to one year" (developers.stellar.org/docs/data/apis/horizon, note of 2024-08-01). Archived persistent entries are restored on access (developers.stellar.org/docs/learn/fundamentals/contract-development/storage/state-archival). All three were read by the engineer specialist on 2026-10-25: [[horizon-public-history-one-year-and-983a]].
- `getEvents` keeps a default of 120,960 ledgers, about 7 days, and the RPC operator can change it: developers.stellar.org/docs/data/apis/rpc/api-reference/methods/getEvents (read by the reviewer, 2026-10-25); [[stellar-rpc-getevents-keeps-about-7-187e]].
- A SEP is an open document in the stellar-protocol GitHub repository with a "lightweight approval process"; a CAP changes the core protocol: developers.stellar.org/docs/learn/fundamentals/stellar-ecosystem-proposals (read 2026-10-25); [[seps-are-open-github-documents-with-ee26]].
- No SEP for chain of custody was found (search of 2026-10-24): [[no-sep-and-no-stellar-project-aa39]].
- Contract behaviour: custody_registry lib.rs. TTL at lines 15-17. `open` is at 242-288, `handover` at 291-329, `attest` at 332-360 (no open check), `deliver` at 363-392. Reviewer verdict: approve with changes, all applied (2026-10-25).
