# Installation and portability

## Local installation now

From the repository root:

```sh
python3 tools/install.py --target /absolute/project/.claude/skills --skill creator-story
python3 tools/install.py --target /absolute/project/.agents/skills --skill creator-story
```

Use the directory supported by your actual client version. The installer copies one package, including references and UI metadata. It refuses existing destinations and unsafe source paths; it does not mutate shell startup, create hooks, run downloaded code, or change global settings. Install several skills with repeated `--skill` flags, or use `--all`. `--dry-run` prints the plan without writing.

Updates are intentionally manual in 0.1: compare the installed folder with the new version, preserve local edits, move the old folder aside, then install. No silent overwrite. Remove only the copied package directory to uninstall.

## Ecosystem installation after publishing

The Vercel Skills CLI supports repository and local-path sources. The intended public repository is `novincode/brainkit`; remote commands become usable after publication:

```sh
npx skills add novincode/brainkit --list
npx skills add novincode/brainkit --skill creator-story --agent claude-code
npx skills add novincode/brainkit --skill creator-story --agent codex
```

These are documented upstream command forms, not installation tests performed for this project. Review/pin an installer version in production. Prefer a reviewed tagged checkout for reproducibility; do not assume branch-head installs are immutable.

## Hosts without skill discovery

Supply `skills/creator-story/SKILL.md` and its requested reference files as ordinary context. The model can follow the procedure if it can read them; automatic triggering, slash commands, filesystem access, and tools are host capabilities and are not universally portable.

## Profiles and private data

Copy `profiles/default.json` into ignored `local/profiles/me.json`. Pass that path explicitly in a repository workflow, or supply its small relevant fields directly in another client. Profiles are not installed or auto-discovered by these packages. Do not add personal data to a globally shared skill entry.

## Compatibility status

| Surface | Status |
|---|---|
| Local copy, self-contained references | Covered by automated filesystem tests |
| SKILL.md name/description and project budgets | Covered by local checks; official validator also used during creation |
| Claude Code discovery and behavior | Manual client test pending |
| Codex discovery and behavior | Manual client test pending |
| Generic model with supplied text | Documented fallback; behavior not benchmarked |
| Third-party CLI remote installation | Pending published remote and live test |

## GitHub publishing

The project is prepared for a public GitHub repository, but no remote is assumed. Once `gh auth status` succeeds, from this folder:

```sh
gh repo create novincode/brainkit --public --source=. --remote=origin --push
```

Choose another name if that repository already exists. Review the exact staged contents before publication. Do not use forced pushes or send credentials to the repo. The creation command is documented for the user/next maintainer, not automatically run by installation.
