---
name: build-outset-scenes
description: Build and revise playable Outset scenes through MCP. Use for maps, grid calibration, terrain, encounters, props, lighting, private GM notes, and coordinated adventures.
---

# Build Outset Scenes

Build through the connected Outset MCP. Live descriptions, schemas, permissions, and limits are authoritative. Discover tools by final name even if the host adds a prefix. If unavailable, explain the missing connection and continue with a clearly labeled offline brief where useful.

## Discover and scope

The core tools are `list_campaign_scenes`, `get_scene`, `update_scene_settings`, `inspect_scene`, `project_scene_coordinate`, `list_scene_build_inputs`, `preview_scene_build`, `get_scene_build_preview_artifact`, `approve_and_apply_scene_build_preview`, `get_scene_build_summary`, `get_scene_build`, `refresh_scene_build_preview`, `retry_scene_build_items`, and `revert_scene_build`.

Reads require `scenes:read`; changes require `scenes:write` and current DM membership. Generated inputs need `assets:generate`; spatial notes require their advertised scopes. Copy campaign, scene, asset, entity, revision, build, and artifact IDs from results.

Resolve the campaign, new or existing scene, tactical purpose, footprint, terrain, encounter groups, and available assets. Make low-risk creative choices within the brief. Ask only when missing information affects campaign selection, cost, destructive changes, or expected encounter balance. Without party and rules context, describe an encounter as tactically arranged and balance-unverified.

## Inspect and compose

1. Read the existing scene and revision, including protected characters and portals. Existing-scene builds merge: omitted content remains; only explicit removal lists delete it.
2. Read [coordinates and maps](references/coordinates-and-maps.md) for spatial work. Persist `world-v1`; project pixels and map UVs with the live projection tool. A map's center differs from its image's top-left. Resolve topology, physical scale, spacing, and origin separately.
3. Page through targeted `list_scene_build_inputs` results. Reuse ready assets when their role, style, geometry, and rules defaults fit. Require exact kit/version identity for modular terrain.
4. Load the live `SceneBuildBlueprintV2` schema. Use stable semantic keys, reference every asset alias, and generate only missing inputs. For compatible rectangular layouts, discover `draft_modular_dungeon_blueprint`. For coordinated scenes, load the advertised `AdventurePackage.v2` schema and use the unified adventure lifecycle rather than applying child previews independently.
5. Preserve recognizable topology, entrances, landmarks, cover, movement lanes, and rally placement. Fit props using measured bounds. Irregular caves need appropriate geometry, not an unexplained rectangular substitute. Place every light at a visible source and preserve its intended enabled state.
6. Keep `target.dmNotes` a synopsis; put keyed adventure content in private spatial GM notes. Creating a note never reveals it. Reveal or revoke only on an explicit request identifying the audience and content.

Do not author persistent characters, ownership, raw document identities, actor IDs, fog exploration, live encounters, chat, dice, or live audio through a blueprint. Do not update or remove existing characters or portals. For persistent monster sheets and existing token links, use the monster tools; scene builds own the isolated sheets for tokens they create.

## Preview, apply, and recover

Read [approval and recovery](references/approval-and-recovery.md). Preview does not change scene content or spend generation credits. Render the exact artifact and show the diff, removals, warnings, generation prompts, estimate, and proposed ceiling before apply. A changed blueprint or stale preview needs a fresh visible artifact and matching approval.

Inspect assembled textured previews when ready inputs permit it. Apply only the approved artifact IDs, then follow the durable build to a terminal state. Partial success is not completion. Retry selected failed items without replacing ready siblings; do not replay uncertain work under a new submission ID.

## Verify and deliver

Re-read the saved scene and inspect its exact revision from top, overview, and gameplay views. A partial render is not complete visual evidence. Check map scale and origin, rally position, seams, lighting, prop fit, and traversable connections. Use `inspect_scene_navigation` when available to verify important routes with an existing creature. For adventures, run `validate_adventure_scene` when available and resolve dangling references.

Report complete, partial, conflicted, failed, or reverted status; scene/build IDs; final revision; returned credit usage; and any unresolved warnings. Distinguish private notes from explicitly revealed notes. Revert only when requested; generated assets and charges survive a revert.
