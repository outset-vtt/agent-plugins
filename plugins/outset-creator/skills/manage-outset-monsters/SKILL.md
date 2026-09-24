---
name: manage-outset-monsters
description: Manage rules-aware monster sheets through the Outset MCP. Use for persistent monsters, token instances, compendium creation, revision conflicts, and link cleanup.
---

# Manage Outset Monsters

Manage monster sheets through the hosted Outset MCP while preserving campaign rules, isolated combat state, token presentation, and current DM authorization.

## Discover Authoritative State

Find tools by their final names even when the host prefixes them. Required tools are:

`get_authoring_payload_schema`, `list_monster_campaigns`, `get_monster_authoring_context`, `list_monster_compendium_entries`, `get_monster_compendium_entry`, `list_campaign_monsters`, `get_monster`, `create_monster`, `update_monster`, `delete_monster`, `create_monster_for_token`, `link_monster_to_token`, `unlink_monster_from_token`, and `get_monster_operation`.

If they are unavailable, ask the user to connect or reauthorize Outset. Reads require `monsters:read`; mutations require both `monsters:read` and `monsters:write`. Every call also requires current DM membership.

Start with `list_monster_campaigns`, then call `get_monster_authoring_context`. Before create or create-for-token, load the deferred `monsterCreateSource` contract with `get_authoring_payload_schema`; before update, load `monsterPatch`. Treat those strict payload schemas plus the context's enums, valid owners, actor profiles, installed conditions, writable and derived rows, pack summaries, diagnostics, and `creationRevision` as authoritative for creation. Existing monsters retain their adopted rules; unrelated catalog diagnostics do not block ordinary edits. If adoption is unavailable, preserve saved content and use manual metadata edits.

## Choose The Correct Lifecycle

- Use `create_monster` for a reusable persistent sheet.
- Use `create_monster_for_token` to create a dedicated `entityInstance` for an existing unlinked monster token.
- Use `link_monster_to_token` to clone a persistent sheet into a fresh instance. The clone refills resources and charges and clears temporary resources and active conditions.
- Link an orphan `entityInstance` directly only when the server reports no token references.
- Never share a persistent sheet as mutable token combat state. Later persistent edits do not propagate to existing instances.
- Never create, place, or relocate tokens, characters, assets, or Collection items through this workflow. Route token placement to the scene or adventure authoring workflow, which owns `world-v1` positions and map/grid projection.

## Author Rules-Aware Content

For custom creation, use only the semantic draft fields returned by the deferred strict payload schema. The mutation tool intentionally advertises an open placeholder to keep the default MCP catalog compact, but the server validates the submitted object against the complete loaded schema. Supply caller-stable keys for new nested rows; never invent persisted row IDs, lifecycle, kind, timestamps, attribution, provenance, or formula-derived values. Send `fieldType` for draft and patch field rows; returned canonical actor-sheet rows use `type`.

For compendium creation, first resolve an installed `packId` and `entryId`. Preserve the pack-qualified selection and let the server derive the seed and provenance. Never copy opaque entry data into a custom draft to imitate compendium provenance.

Use only:

- actor types whose sheet kind is `monster`;
- writable, non-formula attributes;
- advertised resources and installed conditions;
- current campaign member IDs as owners;
- strict Rules Action v2 pipelines that compile against the selected actor profile.

Use `update_monster` as a merge. Omitted fields remain unchanged. Express removals only through explicit `removeIds`. Do not try to change the rules system, actor type, lifecycle, or sheet kind.

## Preserve Optimistic Preconditions

Generate a new UUIDv4 `operationId` for each new mutation. Reuse it only to retry the identical request.

- Echo the latest `creationRevision` for create and create-for-token. Updates validate against the monster's adoption, not the newest catalog.
- Echo the current `monsterRevision` for update, delete, and link.
- Echo the token's exact current `actorSheetId` as `expectedActorSheetId`; use `null` only when the token is currently unlinked.
- On a stale revision or changed link, reload the context, monster, and token state. Never overwrite the conflict silently.

Create, link, and unlink token work is durable. Poll `get_monster_operation` until `succeeded`, `failed`, or `conflicted`. Do not report success from `queued` or `running`.

## Handle Destructive Work Deliberately

Treat update requests containing removals, `delete_monster`, and `unlink_monster_from_token` as destructive.

- Before deletion, inspect every returned token reference, including archived scenes.
- If deletion returns `deleted: false`, report every blocking scene and token. Unlink explicitly before retrying.
- Unlinking an instance clears the token first, then removes the instance only when no other token references it.
- Unlinking a persistent sheet never deletes that persistent sheet.
- Deletion and unlink never remove tokens, assets, Collection items, or compendium content.

These operations perform no AI generation, require no preview, and spend no credits.

## Completion Standard

Report the campaign, monster ID and lifecycle, current monster revision, token scene and entity when applicable, durable operation status, and any blocking diagnostics or references. State explicitly whether a persistent source or isolated instance changed.
