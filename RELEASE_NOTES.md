# Outset Creator 0.3.1

- Pin authoring skill references and installation examples to the matching 0.3.1 guide and skills tags. Validation rejects mutable or mismatched guide references.
- Build ZIPs in staging before replacing generated output. Successful builds remove stale files; failed builds preserve the previous artifacts. Integration checks verify both cases using real archives.
- Publish through a workflow tied to the exact checked commit, after the matching guide release is available. Download and compare all six uploaded assets and verify checksums before publishing the draft.
- Retain the Codex bundle, four individual Claude skill ZIPs, licenses, supporting references and SHA256SUMS.

All four individual skills were discovered as enabled by Codex in an isolated temporary project. Existing authenticated Outset MCP reads passed. Claude/Cowork uploads, plugin-host installation and fresh OAuth consent were not tested. Production quickstart validation and private publication passed, but installation failed with a revision mismatch; gameplay checks remain blocked. See the [complete verification record](https://github.com/outset-vtt/compendium-authoring-guide/blob/v0.3.1/guides/first-use-verification.md).
