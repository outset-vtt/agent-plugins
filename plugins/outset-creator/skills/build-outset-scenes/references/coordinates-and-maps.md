# Coordinates And Maps

Read this reference for any spatial authoring, raster-map import, map-linked
content, grid calibration, or multi-level terrain work.

## Contents

1. [Canonical Contract](#canonical-contract)
2. [Raster Grid Calibration](#raster-grid-calibration)
3. [Projection Shapes](#projection-shapes)
4. [Map-Linked Content](#map-linked-content)
5. [Raster Import](#raster-import)

## Canonical Contract

- Persist only `coordinateSpace: "world-v1"`.
- Scene `[0,0,0]` is world origin. `+X` is right, `+Y` is up, and `+Z` is down on
  the tactical map.
- Entity transforms use world `[x,y,z]`; horizontal points and segments use world
  `[x,z]`.
- A map's persisted position is its world center. Raster pixels and normalized
  `mapUv` begin at the image's top-left, so raster `[0,0]` is not world `[0,0]`.
- `gridOrigin` is a world `[x,z]` point and `gridLineSpacing` is a world distance.
  The grid is calibration and interaction state, not a content transform.
- Physical distance is
  `worldDistance / gridLineSpacing * feetPerGridUnit`.
- `elevationStepWorld` is independent of grid spacing.
- Grid coordinates are transient. Project them back to world before persistence.
- Local coordinates require an explicit owner and follow that owner exactly once.
  They never follow grid recalibration.
- `placementUnits: grid` snapshots current spacing into `spatialScale`;
  `placementUnits: absolute` uses scale `1`. Later grid edits resize neither.

Use `get_scene` for axes, calibration, elevation, map transforms, rotation-aware
bounds, and resolved map-linked geometry. Reject a coordinate declaration that
does not match `world-v1`; do not silently normalize it.

Use `project_scene_coordinate` for every pixel, `mapUv`, world-to-map, or
world-to-grid conversion. Never reproduce projection arithmetic in a prompt.

## Raster Grid Calibration

Treat geometric and physical calibration separately:

- `gridTopology` selects square, pointy hex, or flat hex geometry.
- `gridLineSpacing` is the world-space distance between adjacent cell centers;
  for hexes it is not the radius, diameter, or edge length.
- `feetPerGridUnit` is the physical distance of one adjacent-cell step.
- `gridOrigin` controls lattice phase and alignment, not scale.
- `distanceDisplayUnit` changes presentation only.

Before previewing a calibration patch, collect the natural raster dimensions,
map entity and transform, source prose, printed grid or labeled scale bar, and
start or rally landmark. Existing environment values are claims to verify, not
source authority. Measure the longest unambiguous tick-to-tick span on the
original raster; do not measure a resized screenshot or decorative endcaps.

Classify the available evidence:

- For a printed grid, project multiple centers or corners and derive spacing and
  origin from that lattice. Use explicit prose or a scale bar to derive or verify
  the physical distance.
- For an ungridded map with an explicit distance per cell, preserve that value as
  `feetPerGridUnit` and derive visual spacing from a labeled scale bar.
- A scale bar without a printed grid or chosen distance per cell is
  underdetermined. Preserve an intentional existing density or ask for the
  desired travel unit rather than claiming exact calibration.
- Without labeled scale evidence, disclose that geographic scale is approximate.

For an existing map entity, project both scale-bar endpoints with
`project_scene_coordinate`. Let their Euclidean world distance be `Lworld`, the
labeled physical distance be `Dfeet`, and the authoritative physical distance
per cell be `F`. Set `gridLineSpacing = Lworld * F / Dfeet`. If printed cell
spacing `S` is authoritative instead, set
`feetPerGridUnit = Dfeet * S / Lworld`. Never change an explicitly stated `F`
merely to make an oversized overlay look smaller.

Choose topology from the source. When an ungridded map is silent, preserve the
existing pointy or flat orientation and disclose any new choice. Anchor a printed
square map to a real lattice corner and a printed hex map to a real hex center.
For an ungridded travel map, prefer the icon or landmark center over displaced
label text, disclose the chosen source pixel, and use its projected point as a
grid center. Ask only when multiple anchors remain plausible. When moving an
observed rally, preserve its vertical position, elevation, and every non-position
field. Recalibration changes snapping and measurement but does not move or resize
other world-positioned content.

Preview an environment-only merge when no other change is needed. Numerically
confirm `Lworld / gridLineSpacing = Dfeet / feetPerGridUnit`; do not count hex
polygons crossed by a scale bar that may not follow a lattice axis. Sanity-check
the implied whole-map physical extent, ruler distance between the projected
endpoints, rally alignment, and content bounds. Inspect top-down with grid lines
visible at full-map and start-area scales, then repeat the ruler and visual checks
after apply. Keep narrative travel times independent when the source says
landmark spacing is approximate.

Include `Dfeet`, `F`, projected `Lworld`, the derived spacing, topology choice,
origin anchor, and implied extent in the approval packet. These values are the
calibration provenance behind the raw environment diff.

`project_scene_coordinate` requires an applied map entity. For a net-new prepared
map, first preview placement using the exact natural aspect ratio and an observed
or explicitly disclosed world footprint. State that applying this staging pass
leaves the live scene partially calibrated and requires a second approved pass.
After apply, load the resulting scene, project the original-raster evidence, and
preview the environment-only calibration. Do not call a planned transform exact
unless the live MCP adds a prepared-map projection operation.

## Projection Shapes

Project a source pixel through its owning map:

```json
{
  "campaignId": "observed-campaign-id",
  "sceneId": "observed-scene-id",
  "projection": {
    "kind": "pixelToWorld",
    "mapEntityId": "observed-map-id",
    "pixel": [1600, 900],
    "imageSize": { "width": 3200, "height": 1800 }
  }
}
```

Other supported directions use the same observed owner:

```json
{ "projection": { "kind": "mapUvToWorld", "mapEntityId": "observed-map-id", "mapUv": [0.25, 0.75] } }
```

```json
{ "projection": { "kind": "worldToMapUv", "mapEntityId": "observed-map-id", "worldPoint": [-6.5, 3.25] } }
```

```json
{ "projection": { "kind": "worldToGrid", "worldPoint": [-6.5, 3.25] } }
```

Copy returned values. A `worldToMapUv` result outside `[0,1]` is outside the
raster. A `worldToGrid` result must not be persisted as a world point.

## Map-Linked Content

- A `mapUv` field is normalized top-left `[u,v]` and must have an explicit map
  owner.
- Raster-door world endpoints must be projected through their source map. The
  service may persist normalized anchors so a later map transform moves the door
  once.
- Map-linked blockers and notes retain their owner. Never attach a point projected
  for one map to another map.
- Actor, monster, portal, entity, and roaming placements use advertised
  world-prefixed fields.
- Trap triggers use `worldRegion`; relative movement uses `worldOffset`.
- Entity-local note anchors use `localPoint` or `localRegion` only with an
  explicit `entityId` owner.

## Raster Import

Keep binary data out of blueprints and normal MCP JSON:

1. Compute exact byte length and SHA-256.
2. Call `begin_map_upload`.
3. Transfer raw bytes to the expiring signed `PUT` URL.
4. Call `complete_map_upload`, then `finalize_map_import`.

Treat the signed URL as a bearer capability. Do not quote or persist it. For an
existing personal map, call `resolve_prepared_map` and use its observed
`libraryItemId`.

Rediscover the live finalization schema. If it cannot accept physical scale,
carry the source's `feetPerGridUnit` and display unit in the destination scene or
adventure environment patch; prepared-map geometry does not imply that physical
distance was persisted.

## Movement validation

After dressing a scene, use `inspect_scene_navigation` with an existing creature,
a fresh scene revision and world-space destinations to check the entrance and
key connections. Inspect the route, clearance and blocking prop IDs. A visually
clear aisle is not proof of reachability. Keep small decorative props nonblocking
unless their tactical purpose requires collision.
