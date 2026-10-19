# Creator Skills

Portable craft skills for making videos people choose to watch—and finish.

Start with a real idea. Write a story worth telling. Direct its voice and visuals. Test what worked. Keep the creator's taste across projects.

**Status: 0.1.0 foundation.** Eight usable instruction skills, a local installer, evidence templates, calibration scripts, and evaluation cases. No trained model, proven retention uplift, automatic video analysis, or audio generation is claimed. Viral reach is an outcome to investigate, never a guarantee.

## Start here

Requires Python 3.10+ for tooling; using the Markdown instructions needs no runtime or API key.

```sh
python3 tools/validate.py
python3 tools/install.py --target /path/to/your/project/.claude/skills --skill creator-story
```

For Codex, use your client's supported skill directory, commonly `.agents/skills`. Restart or refresh discovery as your client requires. Each installed skill includes its own references; it does not depend on the repo remaining beside it.

Try: “Use creator-story. Write three 30-second scripts about postponing a creative project. Plain words. One dry, one warm, one blunt. Label invented events as fiction.”

For the full workflow, install `creator-director` and the craft skills you want. The director can also work alone using its compact fallback. See [installation](docs/INSTALLATION.md).

## Choose a skill

| Skill | Owns | Does not own |
|---|---|---|
| `creator-director` | Brief, routing, handoff, consistency | Loading everything by default |
| `creator-story` | Hooks, scenes, turns, payoffs, spoken scripts | Inventing the creator's life |
| `creator-research` | Source inspection, annotations, mechanism hypotheses | Pretending metadata is footage |
| `creator-voice` | Performance direction, model/voice audition design | Declaring a best voice without listening |
| `creator-visual` | Art direction, color, motion, readable storyboards | Tool-specific rendering APIs |
| `creator-review` | Useful edits and explicit taste feedback | Automatic model training |
| `creator-measure` | Experiments, outcome interpretation | Promising virality |
| `creator-maintain` | Adding and improving skills in this repository | Editing user preferences silently |

## Architecture

Canonical installable packages live in `skills/`. Human documentation lives in `docs/`. A small registry describes routing; references are loaded only when needed. `bank/` contains source-linked observations and reusable patterns. `evals/` separates behavioral tests from structural validation. `profiles/` provides public templates; personal profiles and raw media belong in ignored `local/`.

Read [architecture and decisions](docs/ARCHITECTURE.md), [roadmap](docs/ROADMAP.md), [research findings](docs/RESEARCH.md), and [Claude handoff](docs/HANDOFF.md).

## Calibrate before adding more prompts

Read [six original short scripts](examples/calibration/short-scripts.md). Choose the lines that sound like you and the ones you would never say. Record exact feedback with [this form](templates/feedback.json). This updates explicit preferences and examples; it does not train model weights.

## Contribute

Bring one reproducible failure, one small fix, and a test that could catch it again. See [CONTRIBUTING.md](CONTRIBUTING.md). New references need provenance. Third-party text is not automatically covered by this project's MIT license; see [THIRD_PARTY.md](THIRD_PARTY.md).

No telemetry. No install hooks. No default paid calls. No required connection to AtomCut, ElevenLabs, or a particular model provider.
