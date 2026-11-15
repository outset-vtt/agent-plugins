# Outset Creator 0.4.0

- Scene building gives every named NPC a persistent NPC sheet through the actor tools. Role NPCs such as merchants, guards and innkeepers start from the closest installed stat block with `draft.compendiumSource`. NPCs who act like adventurers get a character-type class build. An existing NPC without rules adopts a stat block in place with `update_actor` `patch.compendiumSource` and keeps its name, notes, inventory, owners and token. Unnamed crowds and combat-only creatures stay monster tokens.
- The first authoring task points at the Barrowdale Goblin Raider quickstart. The stale installation-blocker note is gone; the November 8, 2026 production rerun completed the quickstart through installation, monster creation, rolls and reload.
- Pin authoring skill references and installation examples to the matching 0.4.0 guide and skills tags. Guide 0.4.0 replaces the Emberwatch and Lantern Marsh examples with Barrowdale.

Packaging and validation checks passed for this release. Stat-block NPC guidance needs an Outset server with `compendiumSource`, live since November 15, 2026. Claude/Cowork uploads, plugin-host installation and fresh OAuth consent were not retested for this release.
