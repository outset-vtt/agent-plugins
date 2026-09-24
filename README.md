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

For Codex, ask its skill installer to install the desired directory from this repository. See the [official skill documentation](https://developers.openai.com/codex/skills/). The [plugin directory](plugins/outset-creator) also contains a `.codex-plugin/plugin.json` manifest for plugin-capable hosts. It can be packaged with `python3 scripts/package_plugin.py`; the resulting ZIP contains the manifest and skills at its root.

This is a skills-only package. Connect and authorize your Outset MCP separately in the host you use. Installing instructions does not connect an account, grant DM access, or fund generation. Tool names may retain the historical `dm-harness` identifier; wire-format names are not renamed by these skills. Live tool schemas and advertised capabilities are authoritative.

## Guides and examples

[Compendium authoring guide](https://github.com/outset-vtt/compendium-authoring-guide) contains the canonical public tutorials, original mini-compendium, source review, and standalone reading-edition validator.

## Status and contributing

Current public release: **0.2.0**. Compendium authoring defaults to the built-in SRD 5.2.1 base. Skill structure and references are checked in CI. Live MCP workflows are adapted from Outset's authoring procedures; this repository's checks do not exercise a production account, spend credits, or install content.

Keep contributions useful to creators. Public tool names, schemas, permission scopes, coordinate conventions, and recovery semantics are welcome. Do not commit credentials, signed URLs, private account/campaign data, customer content, or instructions that require an unpublished repository. Use original or appropriately attributed examples. Run `python3 scripts/validate.py` before submitting a change.

Code, skills, and original examples are available under the [MIT license](LICENSE).
