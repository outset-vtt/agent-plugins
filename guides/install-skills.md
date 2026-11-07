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

Download one or more individual skill ZIPs from [release 0.3.0](https://github.com/outset-vtt/agent-plugins/releases/tag/v0.3.0):

| Skill | Download |
| --- | --- |
| Compendium authoring | [author-outset-compendium.zip](https://github.com/outset-vtt/agent-plugins/releases/download/v0.3.0/author-outset-compendium.zip) |
| Scene building | [build-outset-scenes.zip](https://github.com/outset-vtt/agent-plugins/releases/download/v0.3.0/build-outset-scenes.zip) |
| Asset generation | [generate-outset-assets.zip](https://github.com/outset-vtt/agent-plugins/releases/download/v0.3.0/generate-outset-assets.zip) |
| Monster management | [manage-outset-monsters.zip](https://github.com/outset-vtt/agent-plugins/releases/download/v0.3.0/manage-outset-monsters.zip) |

Each ZIP contains one skill folder with `SKILL.md`, supporting references where needed, and the license. Upload the ZIP directly using [Claude's custom skill upload](https://support.claude.com/en/articles/12512180-use-skills-in-claude); no local repackaging is needed.

In **Customize > Skills**, choose **+ > Create skill > Upload a skill**, upload that ZIP, and enable it. Code execution and file creation must be enabled; organization settings may also control skill access. Repeat for the other skills you want, then ask Claude to use the selected skill by name. Cowork uses skills enabled for your Claude account; a local `~/.claude/skills/` installation alone does not make them available there.

The release's `outset-creator.zip` is the Codex plugin bundle. For Claude's skill upload, use the individual skill ZIPs linked above. This repository does not currently provide a Claude plugin marketplace manifest.

## Build or verify downloads

To build from a Git checkout, run `python3 scripts/package_plugin.py`. It creates the Codex bundle, all four individual skill ZIPs and `dist/SHA256SUMS`. Only tracked plugin files are included; stage new skill files before packaging. Supporting references travel with their skill. See [release verification](releasing.md).

Download `SHA256SUMS` alongside all five release ZIPs and verify in that directory:

```sh
# macOS
shasum -a 256 -c SHA256SUMS
# Linux alternative
sha256sum -c SHA256SUMS
```

These checks detect a changed download relative to the release's checksum list; they are not a signature or a live host compatibility test.

## Next: connect and verify

For live campaign operations, [connect Outset MCP](connect-outset.md), then run the read-only verification prompt. Installing a skill alone does not connect your account.
