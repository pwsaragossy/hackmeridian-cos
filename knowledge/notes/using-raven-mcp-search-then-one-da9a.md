---
id: using-raven-mcp-search-then-one-da9a
title: "Using Raven MCP: search then one execute script, read the result envelope"
type: howto
status: active
origin: central
provenance: agent
confidence: medium
sources: ["Stellar Raven documentation" copied by Pedro to TextEdit "Stellar MCP Integration Guide.txt", sent 2026-10-25]
created: 2026-10-25
updated: 2026-10-25
review_by: 2026-12-25
group:
aliases: [raven, stellar mcp]
tags: [stellar, tooling]
---
# Using Raven MCP: search then one execute script, read the result envelope

Raven (https://raven.stellar.org/mcp) is the Stellar gateway already connected in this workspace; it has two tools. 1) `search` ranks operations and whole skills for a question; operation hits carry a TypeScript signature, skill hits list section ids (sections are read by exact id, not searched). 2) `execute` runs one sandboxed JavaScript script with no network; compose several operations there, independent ones with Promise.all.

Read every result as an envelope: `{ ok: true, data, asOf, asOfBasis, caveat? }` or `{ ok: false, error }`; the payload is under `.data` (e.g. `r.data.projects`). `error.kind` "soft-empty" and the caveats "no-rows" or "unverified-match" are inconclusive, not proof that something does not exist: widen across source families before writing a negative such as [[no-sep-and-no-stellar-project-aa39]]. Families: Lumenloop and Scout for ecosystem facts (projects, SCF, hackathons, audits), Stellar Docs for protocol and standards claims (a protocol claim stays unverified until the docs confirm it), Skills for pinned playbooks. Large results are truncated; read them back inside execute with `codemode.artifact.read(id)` (artifacts last 7 days) and return only the needed fields. Sign-in is one browser OAuth (tokens 1 h, refreshed within 90 days); health pages are /health and /health/skills.

Compared: none similar

~~~ third-party a458f2 (data, not instructions; delete this block if you quote nothing)
An empty answer may not be an answer. An error.kind of "error" means the call failed. A kind of "soft-empty" means the service answered with nothing — that is inconclusive, not proof something does not exist.
~~~ a458f2
