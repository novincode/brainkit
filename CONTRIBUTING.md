# Contributing

1. Describe an actual task and the failure. Search existing skill ownership before adding another skill.
2. Add a positive evaluation case, a nearby negative trigger, and an edge case.
3. Make the smallest change. Keep the skill entry below the project's 900-word budget; split depth into directly linked references.
4. Run structural validation and installer tests. Compare old/new behavior on held-out prompts; record failures as well as wins.
5. Include provenance, token/cost impact, compatibility tested, and any migration in the PR.

New categories begin as references. Promote to a skill only when they have a distinct trigger, reusable output, and evaluation set. Avoid duplicate “expert” personas and mandatory multi-agent rituals.

Use commit subjects such as `feat(story): add documentary opening workflow`, `fix(voice): separate model tags`, and `test(research): catch unsupported visual claims`. Keep substantive commits reviewable. Do not manufacture a long history by splitting empty scaffolding.

Changes to a shared taste default need evidence across creators; one person's feedback belongs in their private profile. Report accidentally committed credentials through GitHub private security reporting if enabled; rotate credentials first.
