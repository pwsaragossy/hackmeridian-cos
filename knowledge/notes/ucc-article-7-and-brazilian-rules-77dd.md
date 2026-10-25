---
id: ucc-article-7-and-brazilian-rules-77dd
title: "UCC Article 7 and Brazilian rules opened 2026-10-25: a Stellar token is a registry entry, not a title to cargo"
type: finding
status: active
origin: hackmeridian-rail
provenance: agent
confidence: medium
sources: ["law.cornell.edu/ucc/7 (7-102, 7-104, 7-105, 7-106, 7-501)", "uncitral.un.org MLETR status page", "planalto.gov.br Codigo Civil, Lei 11.076/2004"]
created: 2026-10-25
updated: 2026-10-25
review_by: 2027-04-25
group:
aliases: [title wording, document of title, electronic bill of lading, MLETR]
tags: [legal, tokenized-cargo, claims, hackmeridian]
---
# UCC Article 7 and Brazilian rules opened 2026-10-25: a Stellar token is a registry entry, not a title to cargo

All texts below were opened on 2026-10-25 (page text, not recalled). Jurisdiction: the cargo moves Brazil to the US, so both systems matter; the UCC is state law and the state version was not opened (destination state Florida not checked). This is a working note for the rail team, not legal advice; Radox's counsel confirms it.

**US, UCC Article 7 (Cornell LII text)**
- [FACT] 7-102(a)(1): a bailee is a person that, by a warehouse receipt, bill of lading or other document of title, acknowledges possession of goods and contracts to deliver them. With 1-201(b)(16) ([[ucc-1-201-b-16-a-ce13]]), a document of title must purport to be issued by or addressed to a bailee. An exporter-issued or platform-issued token has no bailee behind it, so it does not meet the test on its face. [INFERENCE] confidence medium.
- [FACT] 7-104(a): a document is negotiable only if its terms say goods go to bearer or to the order of a named person. 7-501 gives "due negotiation" only to negotiable documents. [INFERENCE] a financier who buys the bare token gets none of those protections, which is the commercial reason the deck must not sell it as title.
- [FACT] 7-105: only the issuer of a document may reissue it in the other medium (tangible to electronic and back), after the holder surrenders the old one, and the new one must say it is issued in substitution. [INFERENCE] the lawful route to a tokenized bill of lading is the carrier's or warehouse's own act; the rail's registry can index it, not create it.
- [FACT] 7-106 as shown on Cornell: control of an electronic document comes from a system that reliably establishes the person it was issued or transferred to; the safe harbor in (b) includes (b)(4), changes of the assignee only with the consent of the person in control. [INFERENCE] a token whose issuer or admin keeps clawback (the harness sets the clawback flag so the burn works) can change the holder without the holder's consent, so it does not fit that safe harbor. The page does not state its version and appears to be the text before the 2022 amendments (a search found the 2022 restatement of 7-106 enacted in some states, for example Ohio effective 2026-10-06, not read in full). Version and state both matter.

**International**
- [FACT] UNCITRAL status page (undated, "updated whenever the Secretariat is informed"): the MLETR has been adopted in 13 States; Brazil and the US are not listed. So do not say the registry or token is a legally recognised electronic transferable record.

**Brazil (Planalto texts)**
- [FACT] Código Civil art. 744: the carrier issues a "conhecimento" identifying the goods, as special law provides. Art. 887: a título de crédito produces effects only if it meets the legal requirements. Art. 889 §3: such a title may be issued from computer-created characters that appear in the issuer's own bookkeeping.
- [FACT] Lei 11.076/2004 arts. 1, 3 and 15: the agricultural deposit certificate and warrant (CDA/WA) are issued by the depositary, are electronic only while registered in a registry or settlement system, and must be deposited in a central depositary authorised by the Central Bank. [INFERENCE] a Stellar token is none of these; Brazil has statutory electronic titles, and the token is not one of them.
- Not opened: the bill-of-lading statute (Decreto 19.473/1930), maritime transport law, the crypto-asset law (Lei 14.478/2022), customs rules.

**Wording that follows**
- Say: "a custody record for the shipment, keyed to the container or AWB number; in production it would sit beside the carrier's bill of lading (not integrated in this build)"; "records who held the cargo and who signed for each handover"; "the token stays with its holder during transit"; "after the registry shows Delivered, the operator burns the token (operator policy, not enforced on-chain by the registry)".
- Do not say: title, document of title, digital bill of lading, replaces the bill of lading, proof of ownership, legally binding or recognised, UCC- or MLETR-compliant. Keep the intake sentences ("ownership stays with the token holder", "final delivery burns the token") only as a quote of what was submitted, marked as such ([[hackmeridian-scale-intake-as-submitted-the-7fb5]]).
- Counter-argument: the dual-signed handovers are signed by real bailees in production (warehouse, carrier). A court or a custodian's lawyer could ask whether that signature is an acknowledgment of possession that creates duties; 7-102(a)(1) also requires a contract to deliver, which the signature alone does not show. Open question for counsel; the demo uses test keys and says so.

Compared: [[ucc-1-201-b-16-a-ce13]] coexists (that note covers only 1-201(b)(16) and lists the Article 7 and Brazil points as not checked, this one covers them) ; [[no-sep-and-no-stellar-project-aa39]] coexists (ecosystem prior art, not law) ; [[brl-and-usd-ramps-on-stellar-1e41]] coexists (fiat ramps, not title law) ; [[hackmeridian-2026-rules-and-submission-requirement-5868]] coexists (event rules, not title law) ; [[hackmeridian-rubric-7-criteria-weights-scored-50e2]] coexists (rubric, not law) ; [[soroban-versions-on-2026-10-25-9619]] coexists (tool versions, not law) ; [[stellar-rpc-getevents-keeps-about-7-187e]] coexists (RPC retention, not law)
