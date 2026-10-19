# Evaluation protocol

## Three distinct checks

1. **Structural:** valid metadata, package links, registry coverage, context budget, installer boundaries. Deterministic checks can establish these.
2. **Behavioral:** does the skill trigger appropriately and handle realistic constraints? Use `evals/cases.json`, including negatives and adversarial source content. Static checks do not run these cases.
3. **Creative outcome:** do people prefer the finished artifact, understand it, and choose to continue? Use blind comparisons and, later, real publication outcomes. A model judging its own work is insufficient.

## Baseline experiment

Use the same brief and base model/settings with no skill versus the selected skill. Keep creator profile access equal in both conditions when testing the skill itself. Separately test the benefit of the profile. Randomize displayed versions; include ties and “both bad.” Capture exact reasons.

Record model/version, date, prompt, loaded files, output, input/output token counts if available, elapsed time, cost, and evaluator identity/role. Run multiple samples for variable outputs. Hold out topics and some creators; keep private test prompts out of the public example bank.

## Rubric

| Dimension | Weak | Strong |
|---|---|---|
| Integrity | Invented experience, claims, or inspection | Claims match sources; fiction is labeled |
| Clarity | Vague stakes and unexplained context | Viewer can state the question and answer |
| Progression | Rephrases the point | Each beat changes understanding |
| Voice | Generic slogans or forced edginess | Speakable and appropriate to the creator |
| Payoff | Promise abandoned or cheaply repeated | Opening is repaid with a meaningful change |
| Production usefulness | Mixed speech and instructions | Artifacts separate and actionable |
| Restraint | Excessive intake, references, variants | Smallest complete useful response |

Use explicit pass/fail for integrity constraints. Pairwise preference is better than inventing a universal viral score. Report disagreement and failed cases rather than hiding them in an average.

## Initial release gate

Require no critical integrity failures in the selected release cases and a documented creative comparison before claiming an improvement. Report uncertainty on small samples. Twenty held-out tasks is a starting pilot, not statistical proof of universal performance.

The foundation includes cases, not completed benchmark results. Any one-off smoke test must be labeled with its exact scope. Live voice, footage, client discovery, retention uplift, and cross-model behavior remain unverified until actually tested.
