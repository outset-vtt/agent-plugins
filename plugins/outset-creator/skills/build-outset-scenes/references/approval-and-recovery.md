# Approval, Evidence, And Recovery

Read this reference when previewing, requesting paid or destructive approval,
monitoring a build, refreshing stale work, retrying failures, or reverting.

## Preview Ledger

Generate a fresh UUIDv4 `submissionId` for a new preview. Reuse it only to replay
the identical request. Record from `structuredContent.result`:

- campaign and scene IDs;
- base revision;
- build ID and preview hash;
- normalized blueprint and dependencies;
- exact diff, warnings, and explicit removals;
- expected and conservative credit estimates;
- proposed credit ceiling.

When available, render `get_scene_build_preview_artifact`. Verify that it is
approvable and not stale, and that its metadata matches the full preview. The PNG
is evidence; structured metadata remains the approval contract.

## Rendered Inspection

Use `inspect_scene` for assembled textured evidence before apply and after each
visual correction. Copy the preview hash or saved scene revision from its current
read. Keep overview and top views for composition, then focus a seam, prop group,
entrance or light source at a low angle. Reuse returned camera recipes for fair
before/after comparisons. Labels map numbered pixels to exact entity IDs.

`complete: false` means missing visuals or pending generated inputs. A partial
image cannot establish scene-wide visual quality. Isolation removes neighboring
geometry and lights; use it for diagnosis, then recheck in context. Inspect the
static-render warnings and use the app for unsupported visuals or gameplay UI.
Inspection does not approve a build or replace the apply artifact.

## Compact Approval Packet

```text
Target: <scene and campaign>
Build / revision: <buildId> / <baseRevision>
Creates: <counts and important identities>
Updates: <fields and records>
Removes: <every deletion, or none>
Generation: <each asset key and prompt>
Warnings: <all warnings, or none>
Credits: expected <x>; reservation and proposed ceiling <y>
Partial success: failed dependencies are skipped; independent ready work may apply
Persistence: generated assets, usage, and charges survive failure and revert
```

If the user changes any item, preview again. Apply only after the matching
artifact is visible and the exact diff and ceiling are approved.

## Apply And Monitor

Call `approve_and_apply_scene_build_preview` with the exact visible `buildId` and
`artifactId`. The artifact binds renderer version, preview hash, revision, and
ceiling. Do not use the retired text-echo apply payload.

The server re-estimates before spending. If cost exceeds the ceiling, reduce
inputs or obtain approval for a newly previewed estimate.

Poll `get_scene_build_summary`, falling back to `get_scene_build`, through
`queued`, `generating`, and `applying`. Terminal states are `completed`,
`completed_with_errors`, `conflict`, `failed`, and `reverted`. Load the full build
for recovery and the final audit.

## Recovery

- `completed_with_errors`: identify playable content and missing asset keys.
  Retry only selected failed keys, against the current post-apply revision, after
  renewed ceiling approval. Preserve ready siblings.
- `conflict` or stale preview: call `refresh_scene_build_preview` and present its
  new revision, diff, warnings, estimate, and artifact. Never auto-apply it.
- authorization error: request the missing scope or current DM membership.
- invalid cursor: restart listing without the old cursor.
- insufficient credits: reduce generation or use ready Collection items, then
  create a new preview.
- terminal failure: report the safe error and preserve the ledger. Use only an
  advertised recovery tool.

## Revert

Revert only after an explicit user request. Explain that the scene must still be
at the build's exact post-apply revision. Existing scenes restore before-values;
new scenes are archived. Generated assets, Collection items, usage, and charges
remain.
