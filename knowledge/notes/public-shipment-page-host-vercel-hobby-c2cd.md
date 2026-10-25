---
id: public-shipment-page-host-vercel-hobby-c2cd
title: "Public shipment page host: Vercel Hobby, static files via the API, production alias only"
type: decision
status: active
origin: hackmeridian-rail
provenance: agent
confidence: medium
sources: [https://vercel.com/docs/deployment-protection, https://vercel.com/docs/limits/fair-use-guidelines#commercial-usage]
created: 2026-10-25
updated: 2026-10-25
review_by: 2026-10-26
group:
aliases: []
tags: [hackmeridian-rail, hosting, vercel]
---
# Public shipment page host: Vercel Hobby, static files via the API, production alias only

Decided 2026-10-25 08:50 Lisbon (session-hackmeridian-rail, engineer subagent approved). The public read-only shipment page is hosted on Vercel, on Pedro's personal Hobby account (free, no team), which is already authenticated in the sessions' Vercel connector. Deploys send the static files inline through the API (`create_deployment`, framework null, target production). They do not use the Git integration, because the code repo is private and the Vercel account is linked to a different GitHub account. GitHub Pages was rejected (a private repo needs a paid plan). Cloudflare Pages and Netlify were rejected (each needs a new login).

Evidence: Vercel Standard Protection covers every domain except production domains, on all plans, so only the production alias (`https://rio-miami-rail.vercel.app`, live 2026-10-25 09:06 UTC, 200 with no cookies) goes to judges; the project alias `rio-miami-rail-treblelegacys-projects.vercel.app` redirects to a Vercel login. Per-deployment URLs require a Vercel login. Hobby is for non-commercial personal use. A free testnet demo for a two-day hackathon is a grey area with low risk, and moving off costs almost nothing because the page is static files. On 2026-10-25, curl with that Origin header showed soroban-testnet.stellar.org echoing ACAO (200 on getHealth, 204 on preflight), and horizon-testnet echoed ACAO too. Exact steps: KICKOFF.md §6 of hackmeridian-rail. Fallback: GitHub Pages from a public repo that holds only the page.

Compared: [[executability-audit-2026-10-25-02-04f7]] coexists (the audit raised the missing page host and this note answers it) ; [[review-of-executability-audit-2026-10-6701]] coexists (the review confirmed the same gap that this note answers) ; [[stellar-and-solana-hackathon-winners-no-31ca]] coexists (different subject, no overlap in what it states)
