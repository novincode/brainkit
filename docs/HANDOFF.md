# Handoff to the next maintainer / Claude

## Goal

Build an open-source creator craft system for strong original stories, recognizable voice, intentional visuals, and evidence-based iteration. The user prefers easy words, impact, concrete events, little repetition, and natural direct language. Those preferences should inform a private profile, not hard-code one personality into the public project.

## Start

Read `AGENTS.md`, `docs/ARCHITECTURE.md`, `registry.json`, and `docs/ROADMAP.md`. Do not load the whole bank or every skill. Use `creator-maintain` for repo work and a selected craft skill for content.

## Implemented

- Eight standalone SKILL.md packages and on-demand references.
- Registry, neutral profile, artifact templates, six original fictional calibration scripts.
- Source policy, two text-only creator studies, an original pattern hypothesis, architecture research with dated evolution examples.
- Non-overwriting local installer, structural validation, unit tests and CI.
- Roadmap, release gates, installation and contribution documentation.

## First user-facing next step

Run the six-script calibration and ask for exact liked/disliked lines. Capture scoped preferences rather than rewriting a big persona prompt. Then test a different subject. Do not invent the creator's experiences.

## Outstanding work

- Deep multimodal video analysis: not done. Seed studies read creator-published text only.
- Full commit/diff archaeology: not done. Public release notes and two proposed PR commits were reviewed; commit feeds/API access failed.
- Voice generation/listening: not done. No paid API calls, voice winner, or audio quality claim.
- Behavioral benchmark and live client discovery: not done. See validation log for any bounded smoke test.
- GitHub publication: requires working authentication/network. The local `gh` session reported invalid authentication during creation. Do not claim a public URL before creation/push succeeds.

## Continue in order

1. Run `python3 tools/validate.py` and `python3 -m unittest discover -s tests`.
2. Check `docs/VALIDATION.md` and Git state for current test/commit status.
3. Use already-authorized GitHub publishing once authentication works; documented command is in installation instructions.
4. Calibrate taste; run real held-out script comparisons; preserve raw results privately.
5. Inspect a small matched video sample; scale the bank only after annotations are useful.
6. Run a budgeted ElevenLabs audition with available authenticated voices/models.

## Do not overbuild

No separate npm package, vector database, custom MCP server, automated scraping pipeline, or role swarm is needed to prove the first useful loop. Add infrastructure when measured work shows a bottleneck. “Human” comes from truthful material, specificity, judgment, and delivery; profanity alone is not the product.
