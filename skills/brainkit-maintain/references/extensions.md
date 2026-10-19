# Extension rules

Prefer `references/documentary.md` over a new `documentary-master` skill unless documentary work has a genuinely independent trigger and deliverable. New skills must work when installed alone.

Before adding a provider adapter, isolate capabilities, authentication, costs, request/response mapping, and failure modes. Maintain dated compatibility notes and do not embed credentials. Keep the neutral artifact usable when the provider is disconnected.

For a new skill: initialize required name/description metadata; write a concise procedure; directly link relevant references; add UI metadata if supported; add to registry; include positive, negative, adversarial, and held-out tasks; run installed-package tests.

For contract changes: add optional fields compatibly; major-version renamed/removed required fields and changed semantics; supply migration instructions. For behavior: record old/new examples and token/cost impact. Do not promote a model's self-score into a validated benchmark.
