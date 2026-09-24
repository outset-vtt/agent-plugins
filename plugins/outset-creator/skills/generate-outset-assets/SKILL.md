---
name: generate-outset-assets
description: Generate and recover reusable Outset monsters, characters, props, and audio through MCP, with cost estimates, model review, and optional campaign installation.
---

# Generate Outset Assets

Create reusable personal masters through the connected Outset MCP. No campaign is required for generation. Discover tools by final name; live schemas and limits take precedence over examples. If tools are absent, explain the missing Outset connection instead of inventing a request endpoint.

Tools: `list_asset_library`, `get_asset_library_item`, `estimate_asset_generation_batch`, `generate_assets`, `get_asset_generation_batch`, `preview_asset_model_front`, `approve_asset_model_front`, `retry_asset_generation_items`, `add_asset_to_campaign`, and `get_asset_installation`.

Library reads require `assets:read`; generation requires `assets:generate`; installation requires `assets:write`. Monster stat binding additionally requires `monsters:read`. Optional publication tools and their permissions must be discovered separately.

## Prepare a batch

- Inspect existing library items and active batches before creating replacements. Resume unfinished work when it matches the request.
- Choose only advertised asset kinds. Write a prompt for the reusable subject, readable silhouette or sound mix, materials, role, and style. Keep scene coordinates and map UVs out of reusable asset prompts.
- Use caller-stable item keys such as `monster.marsh-scout` or `sfx.wooden-gate`. Keep them through estimation, submission, polling, and retry.
- Resolve built-in monster stat IDs from tool results. Bind `monsterStatBlock.stableSrdId` only to an observed ID and verify the estimate's resolved monster label. Omit stats when the user wants a generic visual. Never use campaign-qualified references in campaign-free generation.
- Split at the live batch limit. For standalone scene generation, require the advertised inspectable preview and approval lifecycle; otherwise use scene authoring.

## Estimate and submit

Estimate the exact items. Show prompts, expected estimate, conservative reservation, available balance, sufficiency, and each batch's proposed ceiling. Obtain explicit approval for the exact batch and ceiling before paid submission. Native paid-action approval is sufficient after the matching estimate is visible. Changed prompts, kinds, bindings, options, or item sets require a new estimate.

Use a fresh UUIDv4 `submissionId` for deliberately new work. Reuse it only to retry the identical request. Set `maxEstimatedCreditMicros` to the approved ceiling; do not raise it silently. Insufficient credits require a smaller approved batch or deferral.

Record returned batch, item, job, library IDs, request hash, item keys, statuses, errors, and credit information. Inspect `structuredContent.result`. Do not treat `queued`, `running`, or item-level `generating` as success.

## Monitor and review

Poll with moderate backoff to `completed`, `completed_with_errors`, or `failed`; inspect individual items as well as aggregate status. An item in `reviewing` has completed paid generation and needs unpaid model-front review, not a paid retry.

For a reviewing character or monster:

1. Call `preview_asset_model_front` with the exact batch ID and item key; inspect the PNG and generation reference when supplied. Canonical front is `+Z`.
2. If default candidates do not face forward, request one through eight unique whole-degree offsets from 0 through 359.
3. Approve the exact artifact, ordered candidate array, and chosen member with `approve_asset_model_front`.
4. Poll again. A stale artifact or changed candidates requires another preview. Never install or publish a pending master through another surface.

Front approval saves a render offset on the master. It does not change tactical facing, actor data, existing campaign copies, or immutable releases.

## Recover and deliver

For partial failures, preserve ready siblings and report failed item keys and safe errors. Retry only selected failed keys after paid approval under the live tool's cost contract. Never create a replacement batch merely to retry failures. After an uncertain submission, replay its identical ID or poll its observed batch.

Install only when the user requested campaign use. Resolve the destination campaign and compatible personal version, call `add_asset_to_campaign`, and follow `get_asset_installation` to its advertised terminal state. Installation does not imply scene placement.

Use `generate_and_publish_assets` only for an explicit direct Marketplace-publication request after confirming distribution rights, discovering the live contract, and showing the exact paid estimate. Personal versions, immutable Marketplace releases, and installed campaign copies have separate lifecycles. Updating a master does not rewrite copies or releases; do not invent a publisher's rules version to describe an Outset interpretation change.

Report terminal batch statuses, ready library items, unresolved item keys, returned estimated or charged credits, and requested installation or publication outcomes. Do not expose signed upload URLs, tokens, provider credentials, or internal diagnostic dumps.
