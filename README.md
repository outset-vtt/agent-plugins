# Create in Outset with your agent

Outset Creator gives your agent workflows for compendiums, monsters, scenes and reusable assets.

[Open Outset](https://app.outset-vtt.gg/) · [Install skills](guides/install-skills.md) · [Connect Outset MCP](guides/connect-outset.md) · [Guides and examples](https://github.com/outset-vtt/compendium-authoring-guide)

## Get started

1. **[Install the skills](guides/install-skills.md)** for Codex, Claude Code, or Claude/Cowork.
2. **[Connect your Outset account](guides/connect-outset.md)** for live operations. Use the read-only check before changing a campaign.
3. Choose a task below. If you only want local compendium files, start with the authoring skill and validate the rules in Outset before use.

| I want to… | Skill | What I need |
| --- | --- | --- |
| Author custom rules or a readable book | [Author compendiums](plugins/outset-creator/skills/author-outset-compendium/SKILL.md) | Local source files; Outset editor for authoritative rules validation |
| Create a monster with a persistent sheet | [Manage monsters](plugins/outset-creator/skills/manage-outset-monsters/SKILL.md) | Connected MCP and campaign DM access |
| Build an encounter from a map | [Build scenes](plugins/outset-creator/skills/build-outset-scenes/SKILL.md) | Connected MCP and campaign DM access |
| Generate reusable visuals or audio | [Generate assets](plugins/outset-creator/skills/generate-outset-assets/SKILL.md) | Connected MCP; approved credits for paid generation |

## Try a first task

For local authoring:

> Use author-outset-compendium and the public Reed Warden quickstart to help me create a monster with working Staff rolls. Explain what remains manual.

For an existing campaign, after connecting:

> List the campaigns and scenes my Outset account can access, including my role. Do not change anything or start generation.

Then choose the exact campaign and ask for the work you want. See the [connection check](guides/connect-outset.md#verify-the-connection) if the agent cannot list it.

The [public authoring guide](https://github.com/outset-vtt/compendium-authoring-guide) owns tutorials, source examples and validation guidance. Skills describe the agent workflow and link to that canonical reference.

## Downloads and compatibility

[Release 0.3.1](https://github.com/outset-vtt/agent-plugins/releases/tag/v0.3.1) includes `outset-creator.zip` for Codex plugin-capable hosts, four individual skill ZIPs for Claude/Cowork, and `SHA256SUMS`. Choose your download in [installation instructions](guides/install-skills.md). The authoring skill pins its guide references to **v0.3.1**; `main` may contain newer changes than a tagged release. See the [first-use verification record](https://github.com/outset-vtt/compendium-authoring-guide/blob/v0.3.1/guides/first-use-verification.md): Codex skill discovery and authenticated MCP reads passed, but production rules installation blocked the gameplay check.

This package contains skills, not an MCP connection. Live operations use the separately authorized Outset service. Tool names may retain `dm-harness`; discover the live schemas before calling tools. Compendium examples target D&D SRD 5.2.1.

## Checks and contributions

```sh
python3 scripts/validate.py
python3 scripts/test_packaging.py
python3 scripts/package_plugin.py
```

Validation checks the manifest, skill metadata and repository-relative links. Packaging creates five ZIPs and checksums under `dist/`; its artifact test checks skill contents, bundled references, exclusion of untracked files and repeatability. See [release verification](guides/releasing.md). These commands do not sign into Outset, exercise live tools, spend credits or install content.

Use original or appropriately attributed examples. Keep credentials, signed URLs, private campaign data and dependencies on unpublished repositories out of contributions. Code, skills and original examples are [MIT licensed](LICENSE).
