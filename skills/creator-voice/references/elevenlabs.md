# ElevenLabs provider notes

Checked against official documentation on 2026-10-19. This is a dated integration note; recheck before generation.

The current model page lists `eleven_v4`, `eleven_v3`, and `eleven_multilingual_v2` among speech options. Start a quality audition with an available expressive model and a consistent narration alternative. No model or voice is a universal winner.

The best-practices guide says v4/v3 use audio tags, punctuation, and text structure for pause/performance control and do not support SSML break tags. Avoid carrying tags or settings from one model into another without checking compatibility. Support for a tag does not guarantee the intended take.

Example audition input, to test rather than treat as a proven recipe:

Clean: “The draft was ready. Then the font needed fixing. Somehow that took the whole evening.”

Expressive-model candidate: “[whispering] The draft was ready. Then the font needed fixing. Somehow that took the whole evening.”

This exaggerated candidate is a controlled test of delivery, not a default recommendation. Start with clean text; a voice that already fits may need no tags. Keep editorial instructions outside spoken text unless the endpoint supports them.

Discover available voices/models in the authenticated account or UI. Record IDs and sample dates. Do not invent access, pricing, licensing, or subjective rankings from voice names.

Sources:

- https://elevenlabs.io/docs/overview/models
- https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices
