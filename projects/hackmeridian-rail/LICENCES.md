# LICENCES

repo HEAD: 179bb9cfc3b85bc37fe0af2ea8eeee4dfb29532f (github.com/pwsaragossy/rio-miami-rail, fresh clone, 6 commits)
time: 2026-10-25T11:47:05Z (UTC)

Repo licence: Apache-2.0. LICENSE file is the Apache License 2.0 text; root Cargo.toml line 6 `license = "Apache-2.0"`; contracts/custody_registry/Cargo.toml uses `license.workspace = true`. `git log --oneline -- LICENSE` returns one commit: `02f577a repo: Apache-2.0 licence, cargo workspace, AI usage log` (confirmed). A NOTICE file also exists.

Commands (run in the fresh clone):
```
git clone -q https://github.com/pwsaragossy/rio-miami-rail rmr-fresh && cd rmr-fresh
git rev-parse HEAD; date -u +%FT%TZ; git log --oneline -- LICENSE
grep -rn "^license" --include=Cargo.toml .
cargo metadata --format-version 1 --manifest-path Cargo.toml > meta.json
jq -r '.packages[]|"\(.name)	\(.version)	\(.license // "NONE")"' meta.json | sort
grep -c "^\[\[package\]\]" Cargo.lock    # 215, equals the package count above
find . -name package.json -o -name package-lock.json | grep -v "^./.git/"    # no output
```

## Cargo (Cargo.lock: 1 file, 215 packages, 0 with missing licence; includes workspace member custody_registry)

| name | version | licence |
|---|---|---|
| ahash | 0.8.12 | MIT OR Apache-2.0 |
| allocator-api2 | 0.2.21 | MIT OR Apache-2.0 |
| android_system_properties | 0.1.6 | MIT OR Apache-2.0 |
| arbitrary | 1.3.2 | MIT OR Apache-2.0 |
| ark-bls12-381 | 0.5.0 | MIT OR Apache-2.0 |
| ark-bn254 | 0.5.0 | MIT OR Apache-2.0 |
| ark-ec | 0.5.0 | MIT OR Apache-2.0 |
| ark-ff | 0.5.0 | MIT OR Apache-2.0 |
| ark-ff-asm | 0.5.0 | MIT OR Apache-2.0 |
| ark-ff-macros | 0.5.0 | MIT OR Apache-2.0 |
| ark-poly | 0.5.0 | MIT OR Apache-2.0 |
| ark-serialize | 0.5.0 | MIT OR Apache-2.0 |
| ark-serialize-derive | 0.5.0 | MIT OR Apache-2.0 |
| ark-std | 0.5.0 | MIT/Apache-2.0 |
| arrayvec | 0.7.8 | MIT OR Apache-2.0 |
| autocfg | 1.5.1 | Apache-2.0 OR MIT |
| base16ct | 0.2.0 | Apache-2.0 OR MIT |
| base64 | 0.22.1 | MIT OR Apache-2.0 |
| base64 | 0.23.1 | MIT OR Apache-2.0 |
| base64ct | 1.8.3 | Apache-2.0 OR MIT |
| bitflags | 1.3.2 | MIT/Apache-2.0 |
| block-buffer | 0.10.4 | MIT OR Apache-2.0 |
| block-buffer | 0.12.1 | MIT OR Apache-2.0 |
| bs58 | 0.5.1 | MIT/Apache-2.0 |
| bumpalo | 3.20.3 | MIT OR Apache-2.0 |
| byteorder | 1.5.0 | Unlicense OR MIT |
| bytes-lit | 0.0.6 | Apache-2.0 |
| cc | 1.10.0 | MIT OR Apache-2.0 |
| cfg-if | 1.0.5 | MIT OR Apache-2.0 |
| cfg_eval | 0.1.2 | Zlib OR MIT OR Apache-2.0 |
| chrono | 0.4.45 | MIT OR Apache-2.0 |
| const-oid | 0.9.6 | Apache-2.0 OR MIT |
| core-foundation-sys | 0.8.7 | MIT OR Apache-2.0 |
| cpufeatures | 0.2.17 | MIT OR Apache-2.0 |
| cpufeatures | 0.3.1 | MIT OR Apache-2.0 |
| crate-git-revision | 0.0.6 | Apache-2.0 |
| crate-git-revision | 0.0.9 | Apache-2.0 |
| crypto-bigint | 0.5.5 | Apache-2.0 OR MIT |
| crypto-common | 0.1.6 | MIT OR Apache-2.0 |
| crypto-common | 0.2.2 | MIT OR Apache-2.0 |
| ctor | 0.5.0 | Apache-2.0 OR MIT |
| ctor-proc-macro | 0.0.6 | Apache-2.0 OR MIT |
| curve25519-dalek | 4.1.3 | BSD-3-Clause |
| curve25519-dalek | 5.0.0 | BSD-3-Clause |
| curve25519-dalek-derive | 0.1.1 | MIT/Apache-2.0 |
| custody_registry | 0.1.0 | Apache-2.0 |
| darling | 0.20.11 | MIT |
| darling | 0.24.1 | MIT |
| darling_core | 0.20.11 | MIT |
| darling_core | 0.24.1 | MIT |
| darling_macro | 0.20.11 | MIT |
| darling_macro | 0.24.1 | MIT |
| data-encoding | 2.11.1 | MIT |
| defmt | 1.2.0 | MIT OR Apache-2.0 |
| defmt-macros | 1.2.0 | MIT OR Apache-2.0 |
| defmt-parser | 1.1.0 | MIT OR Apache-2.0 |
| der | 0.7.10 | Apache-2.0 OR MIT |
| deranged | 0.5.9 | MIT OR Apache-2.0 |
| derive_arbitrary | 1.3.2 | MIT/Apache-2.0 |
| digest | 0.10.7 | MIT OR Apache-2.0 |
| digest | 0.11.3 | MIT OR Apache-2.0 |
| downcast-rs | 1.2.1 | MIT/Apache-2.0 |
| dtor | 0.1.1 | Apache-2.0 OR MIT |
| dtor-proc-macro | 0.0.6 | Apache-2.0 OR MIT |
| dyn-clone | 1.0.20 | MIT OR Apache-2.0 |
| ecdsa | 0.16.9 | Apache-2.0 OR MIT |
| ed25519 | 2.2.3 | Apache-2.0 OR MIT |
| ed25519-dalek | 2.2.0 | BSD-3-Clause |
| educe | 0.6.0 | MIT |
| either | 1.19.0 | MIT OR Apache-2.0 |
| elliptic-curve | 0.13.8 | Apache-2.0 OR MIT |
| enum-ordinalize | 4.4.2 | MIT |
| enum-ordinalize-derive | 4.4.2 | MIT |
| equivalent | 1.0.3 | Apache-2.0 OR MIT |
| escape-bytes | 0.1.1 | Apache-2.0 |
| ethnum | 1.5.3 | MIT OR Apache-2.0 |
| ff | 0.13.1 | MIT/Apache-2.0 |
| fiat-crypto | 0.2.9 | MIT OR Apache-2.0 OR BSD-1-Clause |
| fiat-crypto | 0.3.0 | MIT OR Apache-2.0 OR BSD-1-Clause |
| find-msvc-tools | 0.1.15 | MIT OR Apache-2.0 |
| fnv | 1.0.7 | Apache-2.0 / MIT |
| futures-core | 0.3.34 | MIT OR Apache-2.0 |
| futures-task | 0.3.34 | MIT OR Apache-2.0 |
| futures-util | 0.3.34 | MIT OR Apache-2.0 |
| generic-array | 0.14.9 | MIT |
| getrandom | 0.2.17 | MIT OR Apache-2.0 |
| group | 0.13.0 | MIT/Apache-2.0 |
| hash32 | 0.3.1 | MIT OR Apache-2.0 |
| hashbrown | 0.12.3 | MIT OR Apache-2.0 |
| hashbrown | 0.15.5 | MIT OR Apache-2.0 |
| hashbrown | 0.17.1 | MIT OR Apache-2.0 |
| heapless | 0.8.0 | MIT OR Apache-2.0 |
| heck | 0.5.0 | MIT OR Apache-2.0 |
| hex | 0.4.3 | MIT OR Apache-2.0 |
| hex-literal | 0.4.1 | MIT OR Apache-2.0 |
| hmac | 0.12.1 | MIT OR Apache-2.0 |
| hybrid-array | 0.4.15 | MIT OR Apache-2.0 |
| iana-time-zone | 0.1.65 | MIT OR Apache-2.0 |
| iana-time-zone-haiku | 0.1.2 | MIT OR Apache-2.0 |
| ident_case | 1.0.1 | MIT/Apache-2.0 |
| indexmap | 1.9.3 | Apache-2.0 OR MIT |
| indexmap | 2.14.2 | Apache-2.0 OR MIT |
| indexmap-nostd | 0.4.0 | Apache-2.0 |
| itertools | 0.13.0 | MIT OR Apache-2.0 |
| itoa | 1.0.18 | MIT OR Apache-2.0 |
| jiff | 0.2.38 | Unlicense OR MIT |
| jiff-core | 0.1.1 | Unlicense OR MIT |
| jiff-static | 0.2.38 | Unlicense OR MIT |
| jiff-tzdb | 0.1.9 | Unlicense OR MIT |
| jiff-tzdb-platform | 0.1.3 | Unlicense OR MIT |
| js-sys | 0.3.106 | MIT OR Apache-2.0 |
| k256 | 0.13.4 | Apache-2.0 OR MIT |
| keccak | 0.1.6 | Apache-2.0 OR MIT |
| libc | 0.2.191 | MIT OR Apache-2.0 |
| libm | 0.2.16 | MIT |
| log | 0.4.34 | MIT OR Apache-2.0 |
| macro-string | 0.1.4 | MIT OR Apache-2.0 |
| memchr | 2.8.3 | Unlicense OR MIT |
| num-bigint | 0.4.8 | MIT OR Apache-2.0 |
| num-conv | 0.2.2 | MIT OR Apache-2.0 |
| num-derive | 0.4.2 | MIT OR Apache-2.0 |
| num-integer | 0.1.47 | MIT OR Apache-2.0 |
| num-traits | 0.2.19 | MIT OR Apache-2.0 |
| once_cell | 1.21.4 | MIT OR Apache-2.0 |
| p256 | 0.13.2 | Apache-2.0 OR MIT |
| paste | 1.0.15 | MIT OR Apache-2.0 |
| pin-project-lite | 0.2.17 | Apache-2.0 OR MIT |
| pkcs8 | 0.10.2 | Apache-2.0 OR MIT |
| portable-atomic | 1.15.0 | Apache-2.0 OR MIT |
| portable-atomic-util | 0.2.8 | Apache-2.0 OR MIT |
| powerfmt | 0.2.1 | MIT OR Apache-2.0 |
| ppv-lite86 | 0.2.21 | MIT OR Apache-2.0 |
| prettyplease | 0.2.37 | MIT OR Apache-2.0 |
| primeorder | 0.13.6 | Apache-2.0 OR MIT |
| proc-macro2 | 1.0.107 | MIT OR Apache-2.0 |
| quote | 1.0.47 | MIT OR Apache-2.0 |
| rand | 0.8.8 | MIT OR Apache-2.0 |
| rand_chacha | 0.3.1 | MIT OR Apache-2.0 |
| rand_core | 0.6.4 | MIT OR Apache-2.0 |
| ref-cast | 1.0.27 | MIT OR Apache-2.0 |
| ref-cast-impl | 1.0.27 | MIT OR Apache-2.0 |
| rfc6979 | 0.4.0 | Apache-2.0 OR MIT |
| rustc_version | 0.4.1 | MIT OR Apache-2.0 |
| rustversion | 1.0.23 | MIT OR Apache-2.0 |
| schemars | 0.8.22 | MIT |
| schemars | 0.9.0 | MIT |
| schemars | 1.2.3 | MIT |
| sec1 | 0.7.3 | Apache-2.0 OR MIT |
| semver | 1.0.28 | MIT OR Apache-2.0 |
| serde | 1.0.229 | MIT OR Apache-2.0 |
| serde_core | 1.0.229 | MIT OR Apache-2.0 |
| serde_derive | 1.0.229 | MIT OR Apache-2.0 |
| serde_json | 1.0.154 | MIT OR Apache-2.0 |
| serde_with | 3.24.0 | MIT OR Apache-2.0 |
| serde_with_macros | 3.24.0 | MIT OR Apache-2.0 |
| sha2 | 0.10.9 | MIT OR Apache-2.0 |
| sha3 | 0.10.9 | MIT OR Apache-2.0 |
| shlex | 2.0.1 | MIT OR Apache-2.0 |
| signature | 2.2.0 | Apache-2.0 OR MIT |
| slab | 0.4.12 | MIT |
| smallvec | 1.16.4 | MIT OR Apache-2.0 |
| soroban-builtin-sdk-macros | 29.0.1 | Apache-2.0 |
| soroban-env-common | 29.0.1 | Apache-2.0 |
| soroban-env-guest | 29.0.1 | Apache-2.0 |
| soroban-env-host | 29.0.1 | Apache-2.0 |
| soroban-env-macros | 29.0.1 | Apache-2.0 |
| soroban-ledger-snapshot | 29.0.1 | Apache-2.0 |
| soroban-sdk | 29.0.1 | Apache-2.0 |
| soroban-sdk-macros | 29.0.1 | Apache-2.0 |
| soroban-spec | 29.0.1 | Apache-2.0 |
| soroban-spec-rust | 29.0.1 | Apache-2.0 |
| soroban-wasmi | 0.31.1-soroban.29.0.0 | MIT/Apache-2.0 |
| spin | 0.9.9 | MIT |
| spki | 0.7.3 | Apache-2.0 OR MIT |
| stable_deref_trait | 1.2.1 | MIT OR Apache-2.0 |
| static_assertions | 1.1.0 | MIT OR Apache-2.0 |
| stellar-strkey | 0.0.13 | Apache-2.0 |
| stellar-strkey | 0.0.16 | Apache-2.0 |
| stellar-xdr | 28.0.0 | Apache-2.0 |
| strsim | 0.11.1 | MIT |
| subtle | 2.6.1 | BSD-3-Clause |
| syn | 2.0.119 | MIT OR Apache-2.0 |
| syn | 3.0.9 | MIT OR Apache-2.0 |
| thiserror | 1.0.69 | MIT OR Apache-2.0 |
| thiserror | 2.0.21 | MIT OR Apache-2.0 |
| thiserror-impl | 1.0.69 | MIT OR Apache-2.0 |
| thiserror-impl | 2.0.21 | MIT OR Apache-2.0 |
| time | 0.3.55 | MIT OR Apache-2.0 |
| time-core | 0.1.9 | MIT OR Apache-2.0 |
| time-macros | 0.2.32 | MIT OR Apache-2.0 |
| tinyvec | 1.13.3 | Zlib OR Apache-2.0 OR MIT |
| typenum | 1.20.1 | MIT OR Apache-2.0 |
| unicode-ident | 1.0.27 | (MIT OR Apache-2.0) AND Unicode-3.0 |
| version_check | 0.9.5 | MIT/Apache-2.0 |
| visibility | 0.1.1 | Zlib OR MIT OR Apache-2.0 |
| wasi | 0.11.1+wasi-snapshot-preview1 | Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT |
| wasm-bindgen | 0.2.129 | MIT OR Apache-2.0 |
| wasm-bindgen-macro | 0.2.129 | MIT OR Apache-2.0 |
| wasm-bindgen-macro-support | 0.2.129 | MIT OR Apache-2.0 |
| wasm-bindgen-shared | 0.2.129 | MIT OR Apache-2.0 |
| wasmi_arena | 0.4.1 | MIT/Apache-2.0 |
| wasmi_core | 0.13.0 | MIT/Apache-2.0 |
| wasmparser | 0.116.1 | Apache-2.0 WITH LLVM-exception |
| wasmparser-nostd | 0.100.2 | Apache-2.0 WITH LLVM-exception |
| windows-core | 0.62.2 | MIT OR Apache-2.0 |
| windows-implement | 0.60.2 | MIT OR Apache-2.0 |
| windows-interface | 0.59.3 | MIT OR Apache-2.0 |
| windows-link | 0.2.1 | MIT OR Apache-2.0 |
| windows-result | 0.4.1 | MIT OR Apache-2.0 |
| windows-strings | 0.5.1 | MIT OR Apache-2.0 |
| zerocopy | 0.8.63 | BSD-2-Clause OR Apache-2.0 OR MIT |
| zerocopy-derive | 0.8.63 | BSD-2-Clause OR Apache-2.0 OR MIT |
| zeroize | 1.9.1 | Apache-2.0 OR MIT |
| zeroize_derive | 1.5.0 | Apache-2.0 OR MIT |
| zmij | 1.0.23 | MIT |

## npm

none in the repo at 179bb9cfc3b85bc37fe0af2ea8eeee4dfb29532f (no package.json or package-lock.json; the page/ folder has none)

## Distinct licence strings (counts)

Distinct: MIT OR Apache-2.0 x111; Apache-2.0 OR MIT x30; MIT x19; Apache-2.0 x19; MIT/Apache-2.0 x13; Unlicense OR MIT x7; BSD-3-Clause x4; Zlib OR MIT OR Apache-2.0 x2; MIT OR Apache-2.0 OR BSD-1-Clause x2; BSD-2-Clause OR Apache-2.0 OR MIT x2; Apache-2.0 WITH LLVM-exception x2; Zlib OR Apache-2.0 OR MIT x1; Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT x1; Apache-2.0 / MIT x1; (MIT OR Apache-2.0) AND Unicode-3.0 x1
