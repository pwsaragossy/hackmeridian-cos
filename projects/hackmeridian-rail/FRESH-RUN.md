# Fresh run: README on a clean machine by someone who did not build it

Track item `fresh-run`. Run by Vhendala (QA; she wrote no code in rio-miami-rail), on her own Windows computer, from a clean clone, following README.md as written. Source: her agent's lines on `board/Vhendala video and team photo.md`, 17:26 and 17:54 UTC, 2026-10-25.

| Step (README) | Result |
|---|---|
| `npm ci` | PASS, 41 packages, 0 vulnerabilities (main 5e91bae) |
| `node scripts/verify-head.mjs --selftest` | PASS, all 3 vectors |
| `node scripts/verify-head.mjs 31b4cff7…5e37` | MATCH `2d74fec0…5414` |
| `PROOF_FILE=proofs/three-machine.json node scripts/verify-head.mjs 8f32b176…3aae` | MATCH `d9cf3a5f…614d` |
| `cargo test` | PASS, 24/24 |
| `node scripts/handover-signers.mjs` | first run crashed on Windows (path `C:\C:\…`); fixed in 306be64 (`fileURLToPath`); re-run on 66ebe7c: exit 0, "both custodians signed" |
| `PROOF_FILE=proofs/three-machine.json node scripts/handover-signers.mjs` | exit 0 on 66ebe7c |
| Live page and `/snapshot.json`, logged out | 200 OK, both shipments present |

Verdict: 100% PASS on main 66ebe7c (17:54 UTC). The one failure found (Windows path) was fixed and re-run. A second clean-clone check by an independent agent stays planned for Mon 00:00 as a re-check, not as the proof.
