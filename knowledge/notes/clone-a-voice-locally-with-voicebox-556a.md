---
id: clone-a-voice-locally-with-voicebox-556a
title: "Clone a voice locally with Voicebox through its API, with an explicit data dir"
type: howto
status: active
origin: hackmeridian-rail
provenance: agent
confidence: medium
sources: ["local run 2026-10-25, Voicebox 0.5.0 /openapi.json and /models/status"]
created: 2026-10-25
updated: 2026-10-25
review_by: 2027-04-25
group:
aliases: []
tags: [voice, voicebox, video, tts]
---
# Clone a voice locally with Voicebox through its API, with an explicit data dir

Done 2026-10-25 on Pedro's Mac, Voicebox 0.5.0, no upload and no cost. Licences are in projects/hackmeridian-rail/LICENCES.md (Voicebox MIT, Qwen3-TTS Apache-2.0, mlx-audio MIT). It replaces the ElevenLabs route of [[elevenlabs-voice-cloning-needs-a-paid-fe7a]].

1. Start the bundled server with an explicit data folder outside any synced workspace: `/Applications/Voicebox.app/Contents/MacOS/voicebox-server --host 127.0.0.1 --port 17493 --data-dir <folder>`. Without `--data-dir` it writes `./data` in the shell's current folder; started inside ~/hackmeridian, that put a voice sample into the team repo (see [[the-workspace-turn-end-sync-pushes-7635]]).
2. `POST /profiles` with `{"name", "language": "en", "voice_type": "cloned", "default_engine": "qwen"}`.
3. `POST /profiles/{id}/samples` as multipart: `file` = a clean mono WAV of 15-20 s (24 kHz is fine), `reference_text` = its exact transcript (a local parakeet-mlx transcription with SRT timestamps gives both the cut points and the text).
4. `POST /generate` with `profile_id`, `text`, `engine: "qwen"`, `model_size: "1.7B"`, optional `seed`. It returns at once with status `generating`; read the row in `<data-dir>/voicebox.db` table `generations` until `status = completed`, then the WAV is `<data-dir>/<audio_path>`. On Apple silicon it loads mlx-community/Qwen3-TTS-12Hz-1.7B-Base-bf16 from the Hugging Face cache and ran at about 5 tokens/s; 37 words took under a minute and came out as 12.6 s.
5. Check the output by transcribing it locally and comparing the words. Whether it sounds like the person is for that person to judge.
6. In zsh do not name a shell variable GID (read-only special parameter).

Compared: [[elevenlabs-voice-cloning-needs-a-paid-fe7a]] coexists (that note is the paid cloud route, this one the free local route used instead)

