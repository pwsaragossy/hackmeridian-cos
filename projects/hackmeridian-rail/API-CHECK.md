# API check

Evidence for the TRACK item `api`. Public testnet API in production at https://rio-miami-rail.vercel.app/docs, deployed 2026-10-26 after Pedro's yes, from rio-miami-rail branch public-api (36f3927, then 110e6a3 with the footer, llms.txt and sitemap lines).

- scripts/api-check.mjs: 18/18 against production, saved in rio-miami-rail proofs/api-check.json (commit 88bb31e). Examples: open 50e590db…f967, handover 8ecee4d6…545b, deliver 4d360579…98eb, refusal E_WRONG_CUSTODIAN.
- ?network=mainnet answers 503 E_MAINNET_NOT_DEPLOYED; nothing is sent to mainnet.
- Reviewer and security reviews applied (API session).

## check.py, 2026-10-26 05:46 UTC

```
PASS lifecycle: 7/7 SUCCESS
FAIL repo: PRIVATE
PASS site: HTTP 200
PASS api: HTTP 200, status Delivered
PASS docs: HTTP 200, parameters True, request access True
FAIL form: 2 placeholder(s) left: {{VIDEO URL: central sends it after Pedro's upload}}; {{UPLOAD: deck/yc/radox-custody-rail-yc.pdf}}
PASS deck: deck/yc/radox-custody-rail-yc.pdf 672645 bytes
5
```
