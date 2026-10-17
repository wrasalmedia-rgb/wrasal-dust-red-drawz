# WRASAL DUST × Red Drawz

This repository is the GitHub counterpart to the WRASAL DUST production archive. It is intentionally structured as a versioned, auditable production system for a creative project rather than as a public-facing creative encyclopedia.

## Purpose

The repository preserves the distinction between:

- Canon and proposed material.
- Asset specifications and generated outputs.
- Generated outputs and verified assets.
- Verified assets and human-approved production assets.
- Evidence and interpretation.
- AI recommendations and human-authorized decisions.

The repository exists to hold the authoritative project architecture, structured registries, prompt templates, shot definitions, and verification records. It is designed to support consistent production work while keeping a clean chain between recommendation, review, verification, approval, and release.

## Scope and governance

This project is not a statement that any asset is approved canon. A successful commit is not equivalent to authorial approval. The repository must be treated as a controlled production environment in which:

- Proposed records are explicit and clearly labeled as such.
- Canonical records are reviewed, approved, and traceable to a decision.
- Generated outputs remain separate from approved production assets.
- Verification records show evidence that a result satisfies the required criteria.
- Human signoff determines which artifacts become approved production assets.

## Build mode

Build-to-deploy. Each phase in the production lifecycle is tracked intentionally:

1. DECLARE
2. SCOPE
3. BUILD
4. VERIFY
5. REVIEW
6. RELEASE
7. ARCHIVE

## Repository design

The repository is organized so the production architecture and the creative bible remain separate but connected:

- `canon/` contains project-level records that describe durable creative decisions.
- `production/` contains registries of asset classes and production records.
- `prompts/` contains reusable prompt templates, prompt families, and repair workflows.
- `shotlists/` contains shot definitions and structured sequencing work.
- `references/` contains reference documentation and evidence standards.
- `verification/` contains acceptance criteria, continuity checks, and evidence capture templates.
- `schemas/` defines the JSON contract for structured records.

## Canon vs proposed material

The repository must preserve the distinction between concepts that are proposed and concepts that are canon. Proposed ideas may be useful, executable, and even artistically strong, but they are not canon unless explicitly approved.

This distinction should be reflected in both the file contents and the structured IDs used throughout the repository.

## Stable IDs

Use stable IDs for all core categories:

- Characters
- Locations
- Props
- Wardrobe
- Shots
- Prompts
- Verification records

Stable IDs are required so the GitHub system and the Notion archive can reference the same assets without creating contradictory sources of truth.

## Notion and GitHub relationship

Notion remains the human-readable creative bible, working docs, and discussion space. GitHub is the version-controlled production system containing structured registries, templates, schemas, and change history. The two systems should reference the same asset IDs by design rather than duplicate the same information in contradictory forms.

## Repo status

This repository represents the initial architecture and production scaffolding for WRASAL DUST. It is not a claim of completed canon, approved design, or final release assets.

## Safety and handling

The repository intentionally excludes or prohibits:

- Generated media artifacts unless explicitly approved and placed in a designated outputs area.
- Credentials, API keys, secrets, tokens, or private environment files.
- Unlicensed third-party reference materials.
- Personal, confidential, or non-project-specific private reference assets.

## Immediate next steps

The next work items are:

1. Populate the canonical records with approved creative decisions.
2. Align asset IDs across the production registries and Notion registers.
3. Draft the first approved shotlist and verification criteria.
4. Create the first staged production review and approval flow.
5. Add any generated outputs only after verification and human signoff.

## Contributing

This repository is intended for controlled project operations and review. Proposed entries should be structured, clearly labelled, and easy to verify. Contributions should preserve the project’s separation between idea, output, verification, and approval.

## Related documentation

- `references/README.md`
- `verification/acceptance-criteria.md`
- `schemas/asset.schema.json`
- `schemas/shot.schema.json`
- `schemas/verification.schema.json`

## Project status

Status: INITIAL ARCHITECTURE

This repository has been initialized with the recommended directory layout and the first structured registries required to support production control, record integrity, and verification tracking.
