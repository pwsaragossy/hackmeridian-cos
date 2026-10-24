# Pesquisa Raven: custódia (chain-of-custody) Soroban, Rio -> Miami

Consulta em 2026-10-25 via gateway Raven (stellarDocs, scout, lumenloop). asOf dos resultados: 2026-10-24/25.
Tudo abaixo vem de trechos retornados; o que não apareceu está marcado "não verifiquei".

## 1. Versões e mudanças de protocolo 23-29

- soroban-sdk: a release mais recente que apareceu foi **29.0.1** (2026-10-12; corrige o wasmi que o 29.0.0 trouxe por engano). A 29.0.0 saiu em 2026-10-07. A 28.0.0 saiu em 2026-09-18 (CAP-85, `Env::executable_refs()`). Não apareceu nenhuma 30.x do soroban-sdk: não verifiquei.
  Fonte: https://github.com/stellar/rs-soroban-sdk/releases/tag/v29.0.1 (asOf 2026-10-12); .../v29.0.0; .../v28.0.0
- Atenção ao Radox 25.3.0: existe advisory GHSA-x2hw-px52-wp4m (CVE-2026-32322), corrigido em 25.3.0 e 23.5.3. Detalhe do bug: não verifiquei.
  Fonte: https://github.com/stellar/rs-soroban-sdk/security/advisories/GHSA-x2hw-px52-wp4m
- stellar-cli: a mais recente que apareceu foi **28.1.0** (2026-09-26). Antes: 28.0.0 (2026-08-26), 27.1.0 (2026-07-31), 27.0.0 (2026-06-17, suporte a auth entries `AddressV2`). Não apareceu CLI 29.x: não verifiquei se existe.
  Fonte: https://github.com/stellar/stellar-cli/releases/tag/v28.1.0 ; .../v27.0.0
- Protocolo: stellar-core v29.0.0 saiu em 2026-10-05. **stellar-core v30.0.0 já saiu em 2026-10-16** (CAP-0084/0087) e o js-stellar-sdk 17.3.0 (2026-10-21) diz "Protocol 30". Se a testnet está no 29, a rede ainda não votou o 30; o estado da testnet não verifiquei. Use soroban-sdk 29.x para casar com o 29.
  Fonte: https://github.com/stellar/stellar-core/releases/tag/v29.0.0 ; .../v30.0.0 ; https://github.com/stellar/js-stellar-sdk/releases/tag/v17.3.0
- Mudanças que afetam multi-party auth:
  - CAP-71 (protocolo 27): delegação de autenticação e credenciais `SOROBAN_CREDENTIALS_ADDRESS_V2` (amarradas ao endereço). No js-stellar-sdk 17.0.0 (Protocolo 28) V2 virou o padrão dos dois lados do fluxo de auth.
    Fonte: https://github.com/stellar/stellar-protocol/blob/master/core/cap-0071.md ; https://github.com/stellar/js-stellar-sdk/releases/tag/v17.0.0
  - CAP-72: signatários "delegados" em G-accounts, usáveis só dentro do ambiente de contratos.
    Fonte: https://github.com/stellar/stellar-protocol/blob/master/core/cap-0072.md
  - Doc `delegate_auth`: uma conta custom encaminha o contexto do `__check_auth` a outro endereço.
    Fonte: https://developers.stellar.org/docs/build/smart-contracts/example-contracts/delegate-auth
  - Protocolo 28 = CAP-0083, 0085, 0086 (conteúdo de 83 e 86: não verifiquei). Fonte: https://github.com/stellar/stellar-core/releases/tag/v28.0.0
  - Conteúdo exato do protocolo 29 além de "melhor precisão no cruzamento de ofertas DEX": não verifiquei. Fonte: stellar-core v29.0.0.
- Eventos: sem mudança de protocolo encontrada; ver seção 4.
- TTL/arquivamento: stellar-core 25.1.0 reduziu o TTL máximo de entrada para ~4 semanas **na testnet**. Outras mudanças de TTL em 23-29: não verifiquei.
  Fonte: https://github.com/stellar/stellar-core/releases/tag/v25.1.0 (asOf 2026-01-23). Padrão de uso: https://developers.stellar.org/docs/build/guides/archival/test-ttl-extension

## 2. Exigir duas autorizações numa chamada

- Padrão: chamar `require_auth()` em cada um dos dois `Address` dentro da função. Cada `require_auth` vira uma entrada de autorização (`SorobanAuthorizationEntry`) na transação, com credenciais assinadas e árvore de invocação autorizada; o host confere cada uma.
  Fonte: https://developers.stellar.org/docs/learn/fundamentals/contract-development/authorization#require_auth-implementation-details
  Fonte: https://developers.stellar.org/docs/learn/fundamentals/contract-development/contract-interactions/stellar-transaction#authorization-data
- Para amarrar a assinatura aos argumentos (hash do documento, local, hora) usar `require_auth_for_args`; o trecho retornado cita a função, mas o uso exato com args: não verifiquei além disso. Mesma fonte da autorização acima.
- Cliente: o guia "signing Soroban invocations" mostra o cliente montando e assinando as auth entries (`tx.signAuthEntries({ address, signAuthEntry, expiration })`, e `NodeSigner.signAuthEntry`). Cada parte assina só a sua entrada; a transação é montada, simulada e reenviada com as assinaturas.
  Fonte: https://developers.stellar.org/docs/build/guides/transactions/signing-soroban-invocations#step-1-client-builds-and-signs-auth-entries
  Freighter assina auth entries: https://developers.stellar.org/docs/build/guides/freighter/sign-auth-entries
  `authorizeEntry()` no js-stellar-sdk 17.3.0 trata entradas com delegados: https://github.com/stellar/js-stellar-sdk/releases/tag/v17.3.0
- C-address (smart account) e G-account: ambos funcionam como `Address` em `require_auth`. Contas de contrato implementam `__check_auth`; o guestbook oficial usa smart account OpenZeppelin com passkey WebAuthn, que assina a auth entry e depois re-simula com a assinatura real.
  Fonte: https://developers.stellar.org/docs/build/apps/guestbook/frontend#sending-a-donation ; https://developers.stellar.org/docs/build/apps/guestbook/setup-passkeys#the-smart-account-client
- Cuidado de fluxo: o payload tem de passar de um custodiante ao outro (ou a um servidor) para juntar as duas assinaturas, pois cada um assina a sua própria entrada com o mesmo conjunto de argumentos. Isto é inferência do padrão acima, não vem de um trecho.

## 3. Representação do token

- (a) Ativo clássico via SAC: o SAC é a única forma de contratos tocarem ativos clássicos; `clawback` e `set_admin` exigem privilégio especial; quando um lado é o emissor, a transferência emite mint ou burn. Dá clawback/burn no emissor, mas é fungível (código+emissor) e exige trustline. Para uma conta C-address, trustline não se aplica ao saldo de contrato: não verifiquei detalhes.
  Fonte: https://developers.stellar.org/docs/tokens/stellar-asset-contract#authorization-semantics ; .../stellar-asset-contract#sending-to-a-muxed-address
- (b) Token de contrato: interface SEP-41 (inclui `burn`, `burn_from`).
  Fonte: https://developers.stellar.org/docs/tokens/token-interface
- OpenZeppelin Stellar Contracts: coleção de contratos auditados. Quatro crates: `stellar-macros`, `stellar-access` (access control), `stellar-contract-utils`, `stellar-tokens`. Módulos de fungível com extensões Burnable, Capped, Allowlist, Blocklist; existe exemplo de NFT (non-fungible) oficial, e o diretório lista tokens fungíveis, não fungíveis, RWA e vault. Números de versão dos crates: **não verifiquei** (confira em crates.io).
  Fonte: https://developers.stellar.org/docs/tools/sdks/contract-sdks#openzeppelin-contract-and-extension-crates ; https://developers.stellar.org/docs/tools/openzeppelin-contracts#audited-modules-available ; https://developers.stellar.org/docs/build/smart-contracts/example-contracts/non-fungible-token (2026-08-03)
  Se NFT tem extensão Burnable: não verifiquei no trecho (só a do fungível apareceu).
- Recomendação (julgamento meu, não da fonte): para um único ativo físico, um NFT OpenZeppelin (non-fungible) num contrato próprio casa melhor: o contrato de custódia pode ser o dono do estado e queimar o NFT na entrega final. O SAC serve melhor se o ativo for fracionado entre investidores.

## 4. Eventos

- Forma atual: macro `#[contractevent]` (ex.: `#[contractevent(topics = ["COUNTER","increment"], data_format = "single-value")]`). O exemplo oficial de testes compara eventos com a struct do macro e menciona o caso de contratos que não usam o macro; `env.events().publish` é portanto o caminho legado (inferência; deprecação formal: não verifiquei).
  Fonte: https://developers.stellar.org/docs/build/smart-contracts/example-contracts/events
- Leitura: `getEvents` do Stellar RPC, **janela de retenção de 7 dias**. Para histórico maior é preciso indexar (guia de replay de ledger close meta).
  Fonte: https://developers.stellar.org/docs/build/guides/events/publish ; https://developers.stellar.org/docs/build/guides/events/replay-ledger-close-meta
  Janela específica da testnet pública: não verifiquei; a doc diz 7 dias de modo geral.

## 5. Projetos do ecossistema e padrões de atestação

Candidatos do LumenLoop/Scout (similaridade semântica, não prova de equivalência; nenhum é custódia física com dupla assinatura):
- AgTrail (rastreabilidade alimentar, IoT e QR, Nigéria), tags Supply-Chain. Slug lumenloop: `agtrail`.
- Autify (gestão de cadeia de suprimentos, blockchain + IA). Slug: `autify`.
- Airswift (financiamento de cadeia de suprimentos, recebíveis tokenizados em Soroban; SCF #16). Slug: `airswift`.
- Pipeline, "Commodity Trade Finance Protocol" (SCF #43, Build, US$ 140 000). Slug: `pipeline`.
- BorderDollar (invoice finance cross-border, SCF #26). CashAbroad (pagamentos para logística, 4 h). 
- Trustless Work: escrow que segura fundos até verificação da entrega, caso "Trade & B2B". https://trustlesswork.com/escrow-times/use-case-traded-b2b (2026-01-01)
- ChainCred (dados financeiros verificáveis em Soroban), LumosCore Verification Layer: adjacentes a atestação.
Fonte: lumenloop.search_directory("supply chain"), find_similar_scf_submissions, search_content_semantic (asOf 2026-10-24).
- Padrão/SEP de atestação: nenhum SEP de "attestation" ou "chain of custody" apareceu. Os SEPs retornados são outros: SEP-10 (web auth), SEP-45 (web auth para contas de contrato, Draft), SEP-53 (assinar/verificar mensagens, Final), SEP-59 (External Account API), SEP-7. Conclusão: não encontrei padrão; hash+evento próprio é razoável. Fonte: scout.searchResearch source=sep (asOf 2026-10-24); https://github.com/stellar/stellar-protocol/blob/master/ecosystem/sep-0053.md

## 6. Âncoras/rampas Brasil <-> EUA e C-address

- Lumx: corredor BRL-USDC em produção na Stellar para liquidação institucional (2026-08-04); cuida de on/off-ramp e compliance. SEP-6/24/31: não verifiquei. https://lumx.io/blog-posts/lumx-launches-brl-usdc-corridor-on-stellar-for-institutional-payment-settlement-in-brazil
- PagFinance: BRLP, token de liquidação BRL regulado, emitido só após receber BRL. Slug `pagfinance`.
- TroqPay: lojistas brasileiros recebem Pix e USD. Slug `troqpay`. BWB (CVM, imóveis tokenizados BR). Slug `bwb`.
- Projetos SCF: "Instant payments on Pix with USDC", "Regulated BRL Settlement on Stellar", "Diameter Stellar: USD to USDC", "On-ramp thru US bank account" (Meru). Status operacional: não verifiquei.
- Mercado Bitcoin oferece USDC na Stellar (2022-05-31). https://www.prnewswire.com/news-releases/mercado-bitcoin-integrates-usdc-on-stellar-301557574.html
- Perna USD: Coinme (dinheiro vivo EUA), U.S. Bank USBDC (piloto na Stellar, 2026-09-09), USDT0 via Ramp Network (2026-09-02).
- Padrões: SEP-6 (programático), SEP-24 (hospedado, âncora faz KYC), SEP-31 (cross-border). Fonte: https://developers.stellar.org/docs/learn/fundamentals/anchors
- C-address: **SEP-45** (Draft) autentica contas de contrato (C...) com âncoras; o Anchor Platform tem guia SEP-45. A doc de "send and receive C accounts" cobre memo para C-address. Quais âncoras BR/EUA já implementam SEP-45: não verifiquei.
  Fonte: https://developers.stellar.org/docs/platforms/anchor-platform/sep-guide/sep45 ; https://developers.stellar.org/docs/build/guides/transactions/send-and-receive-c-accounts ; https://developers.stellar.org/docs/platforms/stellar-disbursement-platform/admin-guide/embedded-wallets
- SCF #41 "Latch: C-Address Onboarding" (slug `latch`) é candidato para onboarding de C-address.

## Lacunas (não verifiquei)
Versões dos crates OpenZeppelin; stellar-cli 29.x; soroban-sdk 30.x; protocolo ativo da testnet; conteúdo do protocolo 29; extensão Burnable do NFT OZ; deprecação formal de `events().publish`; suporte SEP-45 de âncoras BR/EUA.
