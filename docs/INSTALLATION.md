# Installation and portability

## Local installation now

From the repository root:

```sh
python3 tools/install.py --target /absolute/project/.claude/skills --skill brainkit-story
python3 tools/install.py --target /absolute/project/.agents/skills --skill brainkit-story
```

Use the directory supported by your actual client version. The installer copies one package, including references and UI metadata. It refuses existing destinations and unsafe source paths; it does not mutate shell startup, create hooks, run downloaded code, or change global settings. Install several skills with repeated `--skill` flags, or use `--all`. `--dry-run` prints the plan without writing.

For updates, compare the installed folder with the new version, preserve local edits, move the old folder aside, then install. Remove only the copied package directory to uninstall. When upgrading from an earlier namespace, remove those old package copies after preserving edits, then install the current `brainkit-*` packages. Update saved prompts to use the new names.

## Ecosystem installation

The Vercel Skills CLI supports repository and local-path sources. Install from `novincode/brainkit`:

```sh
npx skills add novincode/brainkit --list
npx skills add novincode/brainkit --skill brainkit-story --agent claude-code
npx skills add novincode/brainkit --skill brainkit-story --agent codex
```

For reproducible production setups, pin a reviewed installer version and repository revision.

## Hosts without skill discovery

Supply `skills/brainkit-story/SKILL.md` and its requested reference files as ordinary context. The model can follow the procedure if it can read them; automatic triggering, slash commands, filesystem access, and tools are host capabilities and are not universally portable.

## Profiles and private data

Copy `profiles/default.json` into ignored `local/profiles/me.json`. Pass that path explicitly in a repository workflow, or supply its small relevant fields directly in another client. Profiles are not installed or auto-discovered by these packages. Do not add personal data to a globally shared skill entry.

## Client setup

| Client | Setup |
|---|---|
| Claude Code | Install into the project's `.claude/skills`, then refresh discovery |
| Codex | Install into the project's `.agents/skills`, then refresh discovery |
| Other skill-compatible agents | Use the client's supported skill directory |
| A model without file access | Supply the selected instruction and reference text as context |

## Updating the GitHub repository

The repository is published at `novincode/brainkit`. After reviewing and committing changes, push from the checkout:

```sh
git push origin main
```

Review staged contents before committing. Preserve the existing remote and avoid force-pushing shared history.
