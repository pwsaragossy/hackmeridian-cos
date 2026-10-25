---
id: elevenlabs-voice-cloning-needs-a-paid-fe7a
title: "ElevenLabs voice cloning needs a paid plan and this connector cannot clone"
type: finding
status: active
origin: hackmeridian-rail
provenance: agent
confidence: medium
sources: ["https://elevenlabs.io/pricing (read 2026-10-25)", "creative_get_flow_node_types on the attached ElevenLabs connector (2026-10-25)"]
created: 2026-10-25
updated: 2026-10-25
review_by: 2027-04-25
group:
aliases: []
tags: [elevenlabs, voice, video]
---
# ElevenLabs voice cloning needs a paid plan and this connector cannot clone

Checked 2026-10-25 without spending. The ElevenLabs pricing page lists Instant Voice Cloning from the Starter plan up; the Free plan has Text to Speech and Voice Design but no cloning. The page showed a first-month promo price for Starter, so read the price on the page at the time of purchase, not from this note.

The ElevenLabs connector attached to Claude Code (the "creative" voice tools) offers these node types: tts, sfx, llm, dubbing-audio, voice-changer, voice-isolator, voice-creation, audio-effects, speech-to-text. "voice-creation" designs a new voice from a text description (Text to Voice); none of them clones a voice from a sample. Cloning the owner's voice therefore needs a paid plan and either the full ElevenLabs connector (https://api.elevenlabs.io/v1/mcp) or the ElevenLabs web app.

A clean sample of the owner's voice exists locally: ~/Movies/FINAL youtube.mp4 (244 s, English, one speaker, an Agent Pay demo narration, speech about -20 dB with pauses near -83 dB). Not uploaded anywhere.

Compared: none similar
