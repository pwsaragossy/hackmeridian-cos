# API proof: Radox API reads the custody chain

- radox-internal commit: `7ececba0` on branch `hackmeridian` (pushed to origin/hackmeridian)
- Time (UTC): 2026-10-25T13:17:29Z
- Network: Stellar testnet, contract `CCBJVXMJYWPHTDJHDFPRGKPGXGEP24JOPJAMUS5C3BMZJTRTWR2H4LII` (custody_registry)
- Stack: NODE_ENV=development, STELLAR_NETWORK=testnet, SOROBAN_RPC_URL=https://soroban-testnet.stellar.org. Read-only: `simulateTransaction` on `get(key)`, no transaction, no signature.

## How it was served (limit, read this)
The full Radox backend did not boot: the dev Postgres is behind this branch by many pending migrations
(`prisma.offer.count()` fails: column does not exist; `prisma migrate status` lists them). Applying them is a
database change, outside this task, so it was not done. The route module `backend/src/routes/custodyRoutes.js`
(the unmodified file from the commit, calling the real service and the real testnet RPC) was mounted at
`/api/custody` in a throwaway express host, the same path `backend/src/app.js` uses. The `app.js` mount line is
committed but was not exercised in a full boot. Auth: none (public chain data, `apiLimiter` in `app.js`), so no token.

## curl
```
curl -s -i http://127.0.0.1:3111/api/custody/shipments/31b4cff785831659b4ecb8fd3e7382f9760a12ef45ef7eb30f45b3b6911a5e37
```
```
HTTP/1.1 200 OK
X-Powered-By: Express
Content-Type: application/json; charset=utf-8
Content-Length: 722
ETag: W/"2d2-7ZlLDt3ePnO6SISrhk4DlqxtN+E"
Date: Sun, 25 Oct 2026 13:17:29 GMT
Connection: keep-alive
Keep-Alive: timeout=5

{"success":true,"data":{"key":"31b4cff785831659b4ecb8fd3e7382f9760a12ef45ef7eb30f45b3b6911a5e37","contract":"CCBJVXMJYWPHTDJHDFPRGKPGXGEP24JOPJAMUS5C3BMZJTRTWR2H4LII","status":"Delivered","currentCustodian":"GAG5WGRM7D2BQWD66FBW4UCU4BADB4UIX7B5QAOOR25JP25E5JDA35P7","route":["GAJTXDXNNKX7J5WQB3NWJQJM6IJIJSN2EBJE52R24ZXUPYYMYYUDF3K2","GCRBNBSUMHH2ZZNI64UPEMCAKOLKLNA5PQC6IV5R4ZO43URLJVUXSH4D","GBSRCRAWQNVRLFAMJUATUTOLL5JEXD5X2NW6NNU4O7X3DTOW4KP2BMFE","GA6JTLEGAFOZPHR7TMSU7LAG6WLKN2USBLIYRMRRT6KXDH4AOKAOTIEW","GAG5WGRM7D2BQWD66FBW4UCU4BADB4UIX7B5QAOOR25JP25E5JDA35P7"],"seq":4,"head":"2d74fec064a6796c34be93ede6241e0e067650dcfb2e058382f2f9cf83195414","holder":"GBPFJMZ7DACIYVNW4TCAHMJ3OT5DU37M4TANIYBGHJ543X673RLIIGDJ"}}
```
Error paths, same host: unknown key (last hex digit changed) returns `{"success":false,"code":"E_CUSTODY_NOT_FOUND",...}`; key `zz` returns `E_CUSTODY_KEY`.

## verify-head (rio-miami-rail, `node scripts/verify-head.mjs <key>`)
```
handover ledger 5381142 635c99ac73cb… seq 1 head f9027c56f9026467e78de9e955c7b3e47325c72746c756a8cfe8a7c7a08f8c5a
handover ledger 5381143 56a0f006e337… seq 2 head a6a1be3bcca6d845a011e4aa32db350e8afbb7ac14049f3f3d7649166504c8a7
attest   ledger 5381144 333792115c7a… seq 2 head 172b7408401dc548c3ceee2612c8e1debb876607801acde75d4d47f56beccc7e
handover ledger 5381145 ac268a49e00d… seq 3 head 53a54097694f20a7d0d9635a84fb888822774bd77ead74410c767cb09425ba12
handover ledger 5381146 5199d4fb6b28… seq 4 head 2d74fec064a6796c34be93ede6241e0e067650dcfb2e058382f2f9cf83195414
recomputed 2d74fec064a6796c34be93ede6241e0e067650dcfb2e058382f2f9cf83195414
on-chain   2d74fec064a6796c34be93ede6241e0e067650dcfb2e058382f2f9cf83195414
MATCH
```
(first lines of the output, for the key's earlier open and handovers, are trimmed to the last five.)

head match: yes
