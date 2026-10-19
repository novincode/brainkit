# BrainKit launch package

Public name: **BrainKit**. Intended repository: `novincode/brainkit`. Edition: Codex-built. The local checkout folder retains its original name to preserve existing links. Claude's separately developed version is not part of this repository.

## GitHub About and topics

Open-source AI creator skills for Claude Code, Codex, and other agents. Storytelling, image/video generation, voiceover, motion, music, sound, and creator taste.

Suggested topics: `agent-skills`, `claude-code`, `codex`, `content-creation`, `storytelling`, `video-production`, `image-generation`, `voiceover`, `motion-design`, `text-to-speech`, `music-generation`, `prompt-engineering`.

## Publish from the checkout

```sh
python3 tools/validate.py
python3 -m unittest discover -s tests -v
gh auth status
gh repo create novincode/brainkit --public --source=. --remote=origin --push --description 'Open-source AI creator skills for Claude Code, Codex, and other agents. Storytelling, image/video generation, voiceover, motion, music, sound, and creator taste.'
gh repo edit novincode/brainkit --add-topic agent-skills --add-topic claude-code --add-topic codex --add-topic content-creation --add-topic storytelling --add-topic video-production --add-topic image-generation --add-topic voiceover --add-topic motion-design --add-topic text-to-speech --add-topic music-generation --add-topic prompt-engineering
```

If the repo already exists, inspect it before selecting a remote. Do not overwrite unrelated repositories or force-push. Authentication and network connectivity are prerequisites; preparation is not publication.

## Cover and social preview

The README references `assets/brainkit-cover.png`. `assets/cover-candidates.png` preserves the three-direction comparison sheet. The launch direction is orange paper-brain, heavy type, warm paper. The assistant selected A as the default after the user confirmed BrainKit and editorial punch.

For GitHub's separate social preview, open repository Settings → Social preview and upload the banner using the required crop. This setting is separate from the README image. Verify GitHub's current size/crop requirements before uploading; do not claim it was uploaded because the asset is committed.

## Launch with evidence

Show one real brief, its output, and one revision based on feedback. Invite same-brief comparisons with and without a skill. Useful issues include the prompt, loaded files, output, failure, and desired change. Separate benchmark claims from taste and popularity.

GitHub Sponsors and Buy Me a Coffee are configured for `novincode`. Stars are welcome; stars and search ranking are never guaranteed.

## Artwork provenance

Original art direction followed by three generated editorial concepts and a single banner refined from concept A. No third-party logo, character, or photo asset was supplied. Image generation was used for the cover, not for exact diagrams or measured data.
