# Connect your agent to Outset

Skills provide instructions. MCP provides authorized access to your Outset account. Install the [skills](install-skills.md) separately, then connect the host you use.

## Before you connect

- Sign in to [Outset](https://app.outset-vtt.gg/) and confirm you can open the intended campaign.
- Use an account with DM access for scene building and monster management.
- Your host must support remote HTTP MCP and browser OAuth sign-in. Workspace administrators may control connector availability.

**Server URL:** `https://api.outset-vtt.gg/mcp`

Outset advertises browser OAuth with PKCE and automatic client registration. Use sign-in, not a pasted API key. Installing a skill or connecting MCP does not grant extra campaign permissions or generation credits.

## Codex

With the Codex CLI installed:

```sh
codex mcp add outset --url https://api.outset-vtt.gg/mcp
codex mcp login outset
codex mcp list
```

Follow the browser sign-in and consent flow with your Outset account. If the add command already completed sign-in, the login step may be unnecessary. Start a new session after configuring the server, then use the verification prompt below.

For a host-managed connection, use its custom MCP setup, enter the same URL and choose OAuth. Do not assume a CLI configuration also connects a separately managed host account. See [official Codex MCP guidance](https://developers.openai.com/codex/mcp) and [OpenAI's custom MCP setup](https://developers.openai.com/plugins/quickstart).

## Claude Code

In a terminal:

```sh
claude mcp add --transport http --scope user outset https://api.outset-vtt.gg/mcp
```

Open Claude Code, run `/mcp`, select Outset and complete browser authentication. Check the connection with `claude mcp get outset`, then use the verification prompt.

The user scope makes this connection available to your local Claude Code projects. It does not configure Claude/Cowork's remote connector. [Official Claude Code MCP instructions](https://code.claude.com/docs/en/mcp).

## Claude and Cowork

1. Open **Customize → Connectors**, then **Add custom connector**.
2. Name it **Outset** and enter `https://api.outset-vtt.gg/mcp`.
3. Choose browser sign-in/OAuth. If offered an OAuth client choice, use **Register automatically**, which matches Outset's advertised registration endpoint.
4. Complete setup and connect with your Outset account.
5. Enable the connector for the conversation, then use the verification prompt.

For organization-managed accounts, an owner may need to add the connector first; each member then connects their own account. See [Claude's remote connector instructions](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp) for current host labels and availability.

## Verify the connection

Ask your agent:

> Use Outset to list the campaigns and scenes my account can access, including my role. Do not create, edit, install, publish or generate anything.

The live `list_campaign_scenes` tool should return accessible campaign/scene summaries and your role. An authenticated empty list is possible when the account has no campaign memberships. A configured server or installed skill alone is not proof of successful access.

Confirm the campaign name and role before asking for changes. This check does not require paid generation or modifying a campaign.

## Troubleshooting

| Symptom | Next step |
| --- | --- |
| The skill is installed but no Outset tools appear | Add and enable the MCP connection in this host, then start a new session |
| Authentication is required or expired | Reconnect/sign in through the host; in Codex use `codex mcp login outset`, in Claude Code use `/mcp` |
| Client registration fails | Confirm the URL and use automatic registration if the host offers it; no client secret is required by the advertised public-client flow |
| Your campaign is absent | Confirm the signed-in Outset account and campaign membership; an empty list is not permission to create replacements |
| Reads work but a write is denied | Check current DM membership and the connection's granted scopes; reconnect if consent needs updating |
| Remote connection fails | Use the HTTPS API URL ending in `/mcp`, not the app URL; check host connector policy and service reachability |
| A tool referenced by a skill is missing | Discover the current tools; report the missing capability instead of inventing a request |

## Verification scope

The public [resource metadata](https://api.outset-vtt.gg/.well-known/oauth-protected-resource) and [authorization metadata](https://api.outset-vtt.gg/.well-known/oauth-authorization-server) were checked on November 7, 2026. Host commands follow the official references above. This guide is not a claim that every host/version has passed an end-to-end OAuth test; use the read-only check to verify your own connection.
