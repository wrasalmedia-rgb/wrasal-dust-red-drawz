# WRASAL DUST × GitHub

This repository exists to support the production architecture for WRASAL DUST in a structured, version-controlled way. It should be treated as the technical and production counterpart to the Notion archive, not as a replacement for it.

## Role of this repository

The Notion archive is the human-readable production bible: the place for creative discussion, visual exploration, and decision context. GitHub is the operational system for:

- versioned project records,
- structured registries,
- prompt templates,
- shot definitions,
- verification records,
- validation logic,
- and change history.

Together, these systems should support a shared asset vocabulary with consistent IDs and a clear distinction between what is proposed, generated, verified, and approved.

## Evidence, interpretation, and approvals

The repository explicitly distinguishes between these categories:

- proposed material: still in development or under review
- generated output: created by a tool or process
- verified asset: checked against acceptance or continuity criteria
- approved asset: validated by a human decision and accepted as a production asset

This distinction is critical. A generation workflow may produce an output that is valuable but not yet canon. A verification status does not imply approval. Human approval remains the gate for canonical adoption.

## Reference discipline

References should be treated intentionally:

- Use them to ground production decisions.
- Keep evidence separate from interpretation.
- Document assumptions clearly.
- Record which outputs were based on which references and which decisions were made by humans.

If a reference is ambiguous, that ambiguity should be recorded rather than hidden.

## File structure responsibilities

The repository folders are organized as follows:

- `canon/` holds durable creative records, world-building, and narrative decisions.
- `production/` holds structured production registries for characters, locations, props, wardrobe, shot data, and continuity.
- `prompts/` holds reusable generation templates.
- `shotlists/` contains structured shot identities and sequencing definitions.
- `verification/` contains the rules and record templates for evidence-driven validation.
- `schemas/` defines the schema contracts that structure the data.

## Canonical integrity

The repository must preserve canonical integrity by avoiding ambiguous status labeling. A proposed asset must not be mistaken for a canon asset. A verified output should not be mistaken for an approved production asset. A successful commit does not make an output canon.

## Shared asset IDs

All major asset entities should be identified by stable IDs so the GitHub and Notion records can align without drift. This includes:

- characters
- locations
- props
- wardrobe elements
- shots
- prompts
- verification artifacts

When the same asset exists in both systems, they should be connected by the same stable identifier rather than duplicate conflicting records.

## Standard production lifecycle

The repository encodes the following lifecycle:

1. DECLARE
2. SCOPE
3. BUILD
4. VERIFY
5. REVIEW
6. RELEASE
7. ARCHIVE

This sequence is intended to keep the pipeline auditable and maintain a clear frontier between proposal and approval.

## What this repository does not do

This repository does not:

- declare an asset approved or canonical without explicit, traceable review
- replace production judgment with automated output generation
- claim that a generated artifact is production-ready merely because it exists in a commit
- store secrets, credentials, generated media, or private reference content in unreviewed form

## Next recommended use

Populate the registries with the reviewed Notion records, align the IDs, and then add the first versioned shotlist and verification criteria. Once those records are stable, begin the first review workflow for proposed material before any release or approval decision.
