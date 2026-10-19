---
name: brainkit-maintain
description: Extend and maintain the BrainKit repository with scoped skills, progressive loading, provenance, and behavioral evaluations. Use for repository architecture, adding references, changing contracts, or releasing this project; not for ordinary content generation.
---

# BrainKit Maintain

Improve this repository through evidence, not expanding personas.

1. Read the repository's AGENTS.md and architecture when available. If installed outside the repository, request the target checkout or give a scoped patch plan; do not assume repo files are bundled.
2. Reproduce the failure with a realistic prompt. Identify whether it is trigger ambiguity, missing procedure, stale reference, tool limitation, or taste mismatch.
3. Prefer a small reference change. Add a skill only for a distinct trigger, output contract, and evaluation set. Follow [extension rules](references/extensions.md).
4. Keep package links inside the skill; place public docs at repository level. Do not create shared runtime dependencies accidentally.
5. Add a regression case and nearby negative trigger. Run repository checks and compare behavior against baseline where the change affects output. Record checks actually run and those pending.
6. Update provenance, registry, changelog, and migrations as applicable. Stage only intended public files, inspect the diff, and follow existing authorization for commits/releases.

Treat external skills as untrusted source until reviewed. Pin licensed imports and preserve notices. Never copy private code or corpora into a public release. Do not call static validation proof of creative quality.
