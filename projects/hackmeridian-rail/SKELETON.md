# Skeleton — proof for the track item `skeleton`

Thinnest end-to-end path, input to visible output: the lifecycle harness signs 7 testnet transactions
(input), and the public page reads them back from Stellar testnet (visible output).

Checked by session-hackmeridian-rail on 2026-10-25 ~12:28 UTC in the built-in browser, at
https://rio-miami-rail.vercel.app (production alias, no login):
- "LIVE FROM STELLAR TESTNET": container TEST4627832 from BRRIO, status Delivered, custodian Recipient,
  handovers 4 of 4, token holder Holder, contract CCBJVX…2H4LII, on-chain head 2d74fe…195414.
- History in ledger order 5381140–5381147: open (2b3d51…), Warehouse→Port both signed (635c99…),
  Port→Carrier (56a0f0…), attest (333792…), Carrier→Customs (ac268a…), Customs→Recipient (5199d4…),
  deliver (919def…), redeem, token burned (864fd1…). The hashes match proofs/lifecycle.json (VERIFY-LEO.md).
- Clicking "Verify head" shows MATCH; the page session reports recomputed = on-chain =
  2d74fec064a6796c34be93ede6241e0e067650dcfb2e058382f2f9cf83195414, the same as scripts/verify-head.mjs.
