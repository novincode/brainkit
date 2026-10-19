# Research findings and limits

Research date: 2026-10-19. This is a selective architecture review, not a complete ecosystem census or months-long commit audit. Current pages can change; pin exact revisions before importing code. No external skill implementation was copied into this repository.

## Skill projects worth studying

| Primary source | Inspected evidence | What to borrow conceptually | What to avoid assuming |
|---|---|---|---|
| [Agent Skills specification](https://agentskills.io/specification) | Format and resource guidance | Small entry points, explicit triggers, on-demand resources | A format guarantees behavior or all hosts work identically |
| [Anthropic skill-creator](https://raw.githubusercontent.com/anthropics/skills/main/skills/skill-creator/SKILL.md) | Current public instruction file | Iterate from concrete tasks; distinguish triggering from output evaluation | One generated rubric proves quality |
| [Superpowers](https://github.com/obra/superpowers) | README and dated release notes | Compose workflows; keep maintenance separate from execution | A software-development process should be imposed wholesale on creative work |
| [Vercel Skills](https://github.com/vercel-labs/skills) | README and releases | Use existing discovery/installation; respect updates and host directories | This project needs its own package manager |
| [Marketing Skills](https://github.com/coreyhaines31/marketingskills) | README taxonomy and cross-links | Separate research, copy, editing, and measurement by job | Marketing copy procedures automatically produce good personal stories |
| [Remotion Skills](https://github.com/remotion-dev/skills) | README skill list | Split creative direction from rendering and tool operation | Tool fluency supplies taste |

These are useful exemplars, not a ranked “best scripts” list. Popularity, stars, and skill count were not used as evidence of output quality.

## Evolution evidence actually available

Direct commit feeds and anonymous GitHub API access were unavailable in this environment. Instead, the review used dated release notes, visible short commit identifiers on release pages, and specific public PR descriptions. PR proposals are labeled as proposals; they are not treated as merged history.

| Date / artifact | Observed change or proposal | Architecture implication |
|---|---|---|
| Superpowers 5.0.1, March 2026 | Release notes describe moving resources into their skill package | Test installation outside the source repository |
| Superpowers 5.0.2, 2026-03-11 | Release notes describe eliminating bundled runtime dependencies | Prefer a small dependency surface until needed |
| Superpowers 5.0.6, 2026-03-24 | Maintainer reports replacing expensive review-agent loops with inline review after comparison | Measure review overhead; do not make agent teams ceremonial |
| Superpowers 6.1.0, 2026-06-30 | Release notes describe trimming session bootstrap/reference content | Minimize always-loaded guidance |
| Superpowers 6.4.2, 2026-09-25 | Release notes narrow plan writing to implementation decisions | Keep planning distinct from execution |
| Anthropic PR [#607](https://github.com/anthropics/skills/pull/607), 2026-03-12, proposed commit `799dda2` | Open proposal adds evaluation generation and a workflow menu | Provide concrete evaluation entry points; inspect current upstream before reuse |
| Anthropic PR [#1443](https://github.com/anthropics/skills/pull/1443), 2026-07-15, proposed commit `8a53333` | Open proposal reports inconsistent evaluation field names | Keep templates and checks aligned; avoid claiming upstream accepted the fix |
| Vercel [v1.7.2](https://github.com/vercel-labs/skills/releases), 2026-10-09, visible commit `671e8c3` | Release lists frontmatter parsing and locked-path fixes | Packaging and update edge cases deserve tests |

Source for the Superpowers entries: [release notes](https://github.com/obra/superpowers/blob/main/RELEASE-NOTES.md). These are maintainer reports, not independently reproduced benchmark results. Follow-up: inspect first/middle/latest commits and selected diffs once access works; save full SHAs, file paths, licenses, and exact retrieval dates.

## Existing private skill layout

The local AtomCut skill package was inspected only for structure: a canonical skill directory, topic references, design-system material, and a packaging script that copies resources into the tool distribution. The public design adopts the general separation between craft and distribution, but keeps rendering integration optional. No private source, prose, internal names, or design-system assets were copied here.

## Creator material inspected

Two modest seed studies are in `bank/studies/`:

1. Derek Sivers' creator-published text accompanying his short talk. Useful for narrative escalation and a final reframing.
2. 3Blue1Brown's official Fourier Transform lesson adaptation. Useful for showing a destination and constructing understanding through a visual mechanism.

Only the text was inspected. Neither record claims direct video/audio inspection, verified timing, current view counts, or causal retention evidence. These seeds establish a research method; thirty actual multimodal studies remain roadmap work.

## API and video decisions

- Start manually. YouTube metadata APIs become useful when repeated collection is the bottleneck.
- Official caption download requires permission to edit the video; an API key alone cannot retrieve every creator's transcript. See [Google's reference](https://developers.google.com/youtube/v3/docs/captions/download).
- Retention analysis needs owner-authorized analytics or supplied exports. Use [YouTube's guidance](https://support.google.com/youtube/answer/9314415) to interpret available curves; do not infer them from views.
- Reading a public URL is not equivalent to watching a video. Actual video analysis needs accessible footage/frames and, for delivery claims, audio inspection. Tool support varies by host.
- Third-party transcript services, scraping, or ASR are optional acquisition adapters. Decide on access, reliability, rights, cost, and source freshness before adopting one.

## Voice decisions

The current [ElevenLabs model page](https://elevenlabs.io/docs/overview/models) lists v4, v3, and Multilingual v2. Current [prompting guidance](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices) distinguishes model-specific performance syntax. The starter plan compares models and voices separately and begins with clean text. Actual generation, listening, voice selection, and a provider cost benchmark have not happened.

## What would make this project distinctive

This is a product hypothesis: evidence-linked craft plus a small, explicit taste profile may be more useful than another broad prompt collection. Validate it through same-brief comparisons. The differentiator should become repeatable creator preference and better finished work, not the number of files or claims of viral psychology.
