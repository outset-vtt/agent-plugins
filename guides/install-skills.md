# Install Outset Creator skills

Clone this repository and give your agent the selected skill directory under `plugins/outset-creator/skills/`. Install those directories using your agent's skill installer. Each directory is a self-contained Agent Skill; preserve its supporting references.

## Codex

For Codex, ask its skill installer:

> Install the author-outset-compendium skill from https://github.com/outset-vtt/agent-plugins/tree/main/plugins/outset-creator/skills/author-outset-compendium

Repeat with the desired skill directory for monsters, scenes or assets. See the [official skill documentation](https://developers.openai.com/codex/skills/). The [plugin directory](../plugins/outset-creator) also contains a `.codex-plugin/plugin.json` manifest for plugin-capable hosts. It can be packaged with `python3 scripts/package_plugin.py`; the resulting ZIP contains the manifest and skills at its root.

## Claude Code

Install the individual skills using [Claude Code's skill directories](https://code.claude.com/docs/en/skills). From a terminal on macOS or Linux:

```sh
git clone https://github.com/outset-vtt/agent-plugins.git
cd agent-plugins
mkdir -p ~/.claude/skills
cp -R plugins/outset-creator/skills/* ~/.claude/skills/
```

This installs all four skills for your local projects, including their references. To install just one, copy its directory instead of `*`. For project-only use, copy the directories into your project's `.claude/skills/` instead. Review any existing same-named skill before copying over it.

Start Claude Code in your project and invoke a skill directly:

```text
/author-outset-compendium Add an original monster to my SRD 5.2.1 compendium.
```

You can also ask Claude to use a skill by name. To update a copied installation, pull this repository's latest changes and copy the selected directories again.

## Claude and Cowork

Use [Claude's custom skill upload](https://support.claude.com/en/articles/12512180-use-skills-in-claude). Package each skill directory separately, retaining `SKILL.md` and its references. For example, from this repository's root:

```sh
mkdir -p dist
(cd plugins/outset-creator/skills && zip -r ../../../dist/author-outset-compendium.zip author-outset-compendium)
```

In **Customize > Skills**, choose **+ > Create skill > Upload a skill**, upload that ZIP, and enable it. Code execution and file creation must be enabled; organization settings may also control skill access. Repeat for the other skills you want, then ask Claude to use the selected skill by name. Cowork uses skills enabled for your Claude account; a local `~/.claude/skills/` installation alone does not make them available there.

The release's `outset-creator.zip` is the Codex plugin bundle. For Claude's skill upload, use the individual skill ZIPs described above. This repository does not currently provide a Claude plugin marketplace manifest.

## Next: connect and verify

For live campaign operations, [connect Outset MCP](connect-outset.md), then run the read-only verification prompt. Installing a skill alone does not connect your account.
