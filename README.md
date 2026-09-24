# Outset agent plugins

Public agent skills for creating content in [Outset VTT](https://github.com/outset-vtt).

## Outset Creator

| Skill | What it does | Requires |
| --- | --- | --- |
| [Author compendiums](plugins/outset-creator/skills/author-outset-compendium/SKILL.md) | Rules source, reviewed reading editions, books, and validation | Local files; Outset editor for authoritative rules validation |
| [Manage monsters](plugins/outset-creator/skills/manage-outset-monsters/SKILL.md) | Persistent monster sheets and isolated token instances | Connected Outset MCP and campaign DM access |
| [Build scenes](plugins/outset-creator/skills/build-outset-scenes/SKILL.md) | Maps, terrain, encounters, lighting, private notes, previews, and recovery | Connected Outset MCP and campaign DM access |
| [Generate assets](plugins/outset-creator/skills/generate-outset-assets/SKILL.md) | Reusable visuals and audio, estimates, model review, and installation | Connected Outset MCP; paid generation needs approved credits |

Try: “Use author-outset-compendium to turn these original rules into a linked reading edition.” Or: “Use build-outset-scenes to prepare an encounter from this map using my existing assets.”

## Use the skills

Clone this repository and give your agent the selected skill directory under `plugins/outset-creator/skills/`. Install those directories using your agent's skill installer. Each directory is a self-contained Agent Skill; preserve its supporting references.

### Codex

For Codex, ask its skill installer to install the desired directory from this repository. See the [official skill documentation](https://developers.openai.com/codex/skills/). The [plugin directory](plugins/outset-creator) also contains a `.codex-plugin/plugin.json` manifest for plugin-capable hosts. It can be packaged with `python3 scripts/package_plugin.py`; the resulting ZIP contains the manifest and skills at its root.

### Claude Code

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

### Claude and Cowork

Use [Claude's custom skill upload](https://support.claude.com/en/articles/12512180-use-skills-in-claude). Package each skill directory separately, retaining `SKILL.md` and its references. For example, from this repository's root:

```sh
mkdir -p dist
(cd plugins/outset-creator/skills && zip -r ../../../dist/author-outset-compendium.zip author-outset-compendium)
```

In **Customize > Skills**, choose **+ > Create skill > Upload a skill**, upload that ZIP, and enable it. Code execution and file creation must be enabled; organization settings may also control skill access. Repeat for the other skills you want, then ask Claude to use the selected skill by name. Cowork uses skills enabled for your Claude account; a local `~/.claude/skills/` installation alone does not make them available there.

The release's `outset-creator.zip` is the Codex plugin bundle. For Claude's skill upload, use the individual skill ZIPs described above. This repository does not currently provide a Claude plugin marketplace manifest.

### Connect Outset

This is a skills-only package. Connect and authorize your Outset MCP separately in the host you use. Installing instructions does not connect an account, grant DM access, or fund generation. Tool names may retain the historical `dm-harness` identifier; wire-format names are not renamed by these skills. Live tool schemas and advertised capabilities are authoritative.

## Guides and examples

[Compendium authoring guide](https://github.com/outset-vtt/compendium-authoring-guide) contains the canonical public tutorials, original mini-compendium, source review, and standalone reading-edition validator.

## Status and contributing

Current public release: **0.2.0**. Compendium authoring defaults to the built-in SRD 5.2.1 base. Skill structure and references are checked in CI. Live MCP workflows are adapted from Outset's authoring procedures; this repository's checks do not exercise a production account, spend credits, or install content.

Keep contributions useful to creators. Public tool names, schemas, permission scopes, coordinate conventions, and recovery semantics are welcome. Do not commit credentials, signed URLs, private account/campaign data, customer content, or instructions that require an unpublished repository. Use original or appropriately attributed examples. Run `python3 scripts/validate.py` before submitting a change.

Code, skills, and original examples are available under the [MIT license](LICENSE).
