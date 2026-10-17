# Changelog

## 0.2.0 - 2026-10-17

- Completed Stage A cross-system discovery across GitHub (`wrasal-dust-red-drawz`, `wrasal-control`, `image-prompt-presets`, `Welcome`), Notion, Linear, and Google Drive; explicitly documented access boundaries for the 12 unshared Notion DUST pages (`object_not_found:not_shared_with_connection`).
- Completed Stage B reconciliation and Canon/Continuity Risk Register in `verification/stage-a-g-production-discovery-report.md`, identifying `CONFLICT-001` through `CONFLICT-004`.
- Populated `canon/project-lock.md`, `canon/canon-decisions.md` (`decision-001` to `decision-007`), `canon/characters.md`, `canon/locations.md`, and `canon/story-timeline.md` with strict separation between established `CANON` locks from the brief and `PROPOSED` / `REFERENCE NEEDED` records.
- Completed Stage C Asset Dependency Map across all 10 required categories in `production/asset-registry.yaml`, `production/character-register.yaml`, `production/location-register.yaml`, `production/props-register.yaml`, `production/wardrobe-register.yaml`, and `production/continuity-register.yaml`, validated against updated `schemas/asset.schema.json`.
- Completed Stage D 7-tier Visual Reference Hierarchy and Readiness Report in `verification/visual-reference-hierarchy.md`.
- Completed Stage E Provisional Opening Sequence Shot Plan (`shot-open-001` through `shot-open-006`) with all 16 required columns in `shotlists/case-001.yaml` and updated `schemas/shot.schema.json`.
- Completed Stage F 14-section Master Cinematic Prompt Template in `prompts/master-shot-template.md` plus concrete shot prompts in `prompts/location-prompts/prompt-img-open-001.md`, `prompts/prop-prompts/prompt-img-open-003.md`, `prompts/prop-prompts/prompt-img-open-004.md`, and `prompts/character-prompts/prompt-img-open-005.md`.
- Completed Stage G First Production Test specification (`TEST-DUST-C001-001`) in `verification/first-production-test.md`, `verification/acceptance-criteria.md`, and `verification/continuity-checklist.md`.

### `TEST-DUST-C001-001` — Phase 1 Execution (authorised `2026-10-17`)

- Executed `run-01` of `TEST-DUST-C001-001` (Frames A, B, C) and archived the full trace in `verification/tests/TEST-DUST-C001-001/` (`execution-report-001.md`, `color-measurements.json`, `verification-records.json`). Frame A passed Gates A, C, D, E, F; Frames B and C failed Gate E and were retained as calibration evidence.
- Added `decision-008` (`H-05` garment specification lock): `prop-red-drawz-001` is locked for Case 001 as an **unbranded, plain matte crimson/oxblood heavyweight cotton undergarment** — zero logos, zero wordmarks, zero printed graphics, zero brand tags; matte finish; remains unlinked from the Linear commercial project `RED DRAWZ — Pre-production v2.2 (STYLE 001 — Oxblood Trunk)`. Mirrored into `production/props-register.yaml`, `production/asset-registry.yaml`, `production/continuity-register.yaml` (new rule `continuity-garment-spec-001`) and `production/wardrobe-register.yaml`.
- Added `decision-009`: promoted Frame A (`run-01`) and its deterministic `1.85:1` widescreen crop to **`APPROVED ASSET`** for `loc-harlem-ext-001` / `shot-open-001` — the first `APPROVED ASSET` in the repository.
- Added `decision-010` (Gate B heuristic calibration): the absolute `R/G <= 1.35` ceiling now applies **only to neutral achromatic reference surfaces**, while dark wood is evaluated by an **occluded wood control delta** of `|Δ(R/G)| <= 0.15`. Applied in `verification/acceptance-criteria.md` §2, `verification/first-production-test.md` §3 Criterion 2, `production/continuity-register.yaml`, `production/asset-registry.yaml`, and `prompts/prop-prompts/prompt-img-open-00{3,4}.md`.
- Executed controlled `run-02` for Frame B (`shot-open-003`) and a reference-conditioned `run-02` for Frame C (`shot-open-004`). Both clear the calibrated two-track Gate B (Track 1 `R/G = 1.159` / `1.123`; Track 2 max `|Δ(R/G)| = 0.112` / `0.127`) and the garment floors (`R/G >= 2.2`, `R/B >= 2.5`). Both are held at **`TESTED — AWAITING HUMAN REVIEW`**.
- Extended `schemas/asset.schema.json` with optional `approved_date`, `approved_by`, `approved_media`, `candidate_media`, `garment_spec_lock`, `calibrated_heuristic`, and `test_references` so promoted media can be registered with authoritative SHA-256 identity anchors. **Schema change requires Human Creative Authority ratification.**
- Documented open items in `execution-report-001.md` §Stage 11: `OI-01` (human visual confirmation of `run-02`), `OI-02` (**generated PNG media does not persist across sessions** because `.gitignore` excludes `*.png`), `OI-03` (no agent vision capability in this environment — all judgements are pixel-statistical), `OI-04` (governance state), `OI-05` (scope exclusions), `OI-06` (no commit/push performed).

## 0.1.0 - 2026-10-17

- Initialized the WRASAL DUST production architecture repository.
- Added canon ledger templates for project lock, canon decisions, characters, locations, and story timeline.
- Added YAML production registries for assets, characters, locations, props, wardrobe, and continuity rules.
- Added prompt architecture directories and master shot prompt template.
- Added shotlists for Teaser 001 and Case 001.
- Added JSON schemas and verification templates.

### Media preservation, authorisation reconciliation, and schema review (`2026-10-17`)

Responding to the Human Creative Authority's disposition of `ARENA EXECUTION REPORT 001`. **No media was regenerated.**

**Media preservation — production blocker**
- **Git LFS tested, not assumed, and FAILED verification**: `git lfs` client absent and not installable (no root), no `.gitattributes`, and LFS object-storage hosts (`media`/`cloud`/`objects.githubusercontent.com`) return `HTTP 000` while `api.github.com` returns `HTTP 200`. Full test matrix in `production/media-preservation-policy.md` §3.2.
- Adopted **`production/media-preservation-policy.md`**: retention table by media status (candidate / tested-awaiting-review / approved / superseded), the nine required metadata fields, and the five-step recovery procedure including the prohibition on regenerating a replacement and calling it the original.
- Designated the fallback durable store — `production/media/**` (approved assets) and `verification/tests/**` (test-bench media) — with `.gitignore` negations, verified by `git check-ignore -v` plus a negative control (`scratch/throwaway.png` still ignored by `.gitignore:4:*.png`).
- Created **`production/media-preservation-register.yaml`** recording all six `TEST-DUST-C001-001` media with stable asset ID, path/promotion path, SHA-256, byte length, dimensions, format, prompt version, run metadata, source media IDs, verification record, human decision, and derivative relationships — plus `storage_status` (`preserved-retrievable` / `recorded-only` / `preservation-incident`) so that **an approval record never implies availability**.
- Created **`production/media/README.md`** documenting store layout and deposit rules.
- Opened **`INC-2026-10-17-001`** (`verification/tests/TEST-DUST-C001-001/preservation-incident-001.md`): Frame A master and crop plus both `run-01` frames are **unrecoverable** — exhaustive filesystem search returned zero copies. Approval status is unaffected; media state is recorded as `preservation-incident`. No replacement generated.
- Re-verified SHA-256 of both surviving `run-02` frames against their generation-time values — **both match**.

**Authorisation-token reconciliation**
- Restored the superseded tokens (`retain_run_01_only`, `keep_heuristic_unchanged`) as structured `superseded.original_*_verbatim` blocks rather than prose quotation only.
- Added `authorisation_reference` and an explicit **authorised / executed / verified** fact-separation model to every affected record, so execution does not imply verification and approval does not imply preservation.
- Corrected two remaining stale hit sites: the Stage 6 candidate-comparison table (now struck through and labelled SUPERSEDED) and the run-01 `notes` instructing "Do not execute run-02 until instructed".
- Added record `verif-reconciliation-001` documenting all five required conditions. **Four PASS, one PASS WITH CAVEAT** (condition 1 — the originals were overwritten in place and are recovered by structured restoration, not from a committed revision, because the file was never committed). Full-text sweep: 17 hits, all in supersession or audit context.

**Schema review — ratification deferred**
- Hardened `schemas/asset.schema.json` to `0.3.0-draft`: media references now require `id`, `delivery_status`, `storage_status`, and a 64-hex `sha256`; `APPROVED ASSET` conditionally requires `approved_by` (const `human-creative-authority`), `approved_date`, and `decision_id`; non-approved media may not carry `approved_by`; `path: null` requires `durable_uri`; preservation states must be internally coherent; `additionalProperties: false` inside media items.
- Separated `garment_spec_lock` (`authority_type: design-constraint`) from `calibrated_heuristic` (`authority_type: verification-rule`) by const discriminator, so neither can silently acquire the other's authority.
- Added `derivative_of` / `transformation` (provenance), `sha256_history` / `superseded_by` (visible replacement), `durable_uri`, `present`, `byte_length`, plus `schema_version` and `version_history`.
- Added conformance suite **`schemas/tests/test-asset-schema.py`**: 21 checks, **0 failed** — 1 backward-compatibility check over all 51 registry entries, 14 negative tests, 6 positive tests, and 2 documented residual-risk probes.
- Wrote **`schemas/SCHEMA-REVIEW-001-asset-schema.md`** mapping the seven review requirements (5 PASS, 2 PARTIAL, 0 FAIL) and six open items (`R-1`…`R-6`). **Ratification deferred** pending `R-1` (mandatory provenance for derivatives) and `R-6` (schema versioning policy).

### Authority Review 003 implementation (`2026-10-17`)

**No media regenerated. No commit, no push.**

**Fresh-session retrieval test — PASSED**
- Executed as the first action of a **new** session: `verification/tests/TEST-DUST-C001-001/retrieval-test-001.md`.
- All five required assertions pass for the two media the store holds — files exist at declared paths, checksums match (`ca0ac612…`, `e8bee9b5…`), open with verified dimensions (`1402x1122`, `1152x922`), retrieved with no reliance on the prior workspace state, and all four declared-absent media are genuinely absent.
- **The `.gitignore` negations work**: media inside `verification/tests/**` survived a session boundary; the four `run-01` frames created before the negations existed did not.
- **Narrow pass, stated as such**: 2 of 6 media, one boundary. `production/media/**` is empty, so the approved-asset half of the store is **untested**; the `durable_uri` external-storage branch is **untested**; Git LFS remains **not verified**.

**Frame A disposition — loss accepted, shot reopened**
- `verification/tests/TEST-DUST-C001-001/disposition-record-001.md`: accepts the loss and reopens `shot-open-001` for controlled re-production. `decision-009` is **retained as historical evidence**, not rewritten or revoked; the recorded SHA-256 values are retained as identity references for any future recovery; the previous approval **does not transfer** to a replacement.
- `verification/tests/TEST-DUST-C001-001/reproduction-spec-open-001.md`: fixes the replacement's inputs in advance (recorded `run-01` prompt, new asset IDs, mandatory sequence, standing prohibitions). Carries forward the one known `run-01` defect (a ~2–3° optical tilt) as a **proposed** prompt amendment requiring approval.
- `shotlists/case-001.yaml`: `shot-open-001` set to `reopened-for-reproduction`. `production/asset-registry.yaml` gains a `media_disposition` block. **`INC-2026-10-17-001` stays open.** Re-generation is **not** authorised by the disposition.
- Permanent rule adopted: **an approved asset cannot be considered production-ready solely because its metadata survives; its actual media must remain retrievable.**

**Schema — `R-1` and `R-6` resolved, ratification recommended**
- **`R-1` mandatory derivative provenance**: new required `lineage` discriminator (`original` | `derivative`). A derivative must name a non-empty `derivative_of` **and** `transformation`; an original declares no parentage rather than a derivative with missing lineage. Applied to all four registry media entries and all six preservation-register entries.
- **`R-6` schema versioning policy**: explicit semantic versioning (patch / minor / major) recorded in the schema itself, with three supporting rules — compatibility assessed against the last *ratified* version; schema versioning distinct from asset versioning; every change records version, date, rationale, compatibility assessment and tests. `version_history` now **enforces** all five keys.
- Bumped to **`0.3.0-rc1`** with a `ratification_status` block. Ratification is **not** self-granted.
- Conformance suite extended to **35 checks, 0 failed** (backward compat over 51 entries, 20 negative, 9 positive, 2 residual-risk probes, 6 versioning-policy). One negative case caught a real defect mid-run: test `C4` supplied `derivative_of` without `lineage: derivative` — the new rule correctly rejected it, and the test was corrected rather than the rule.
- `schemas/SCHEMA-REVIEW-001-asset-schema.md` updated: requirements now **6 PASS · 1 PARTIAL · 0 FAIL**; `R-2` and `R-3` accepted as **process/review controls**, not schema constraints, adopting the Authority's position that JSON Schema cannot enforce transitions.

### Authority Review 004 implementation (`2026-10-17`)

**No generation run. No commit, no push.**

**Review copies created for the visual gate**
- `frame-{b,c}-*-run-02-review-1024.jpg` — downscaled JPEG surrogates (1024 px, 105 KB / 165 KB) created because the full-resolution PNG masters (2.4–2.6 MB) were not reaching the reviewing authority as inspectable images.
- Registered in the preservation register as `lineage: derivative` with explicit `derivative_of` and `transformation`, checksums and dimensions recorded (R-1 compliance applies to surrogates too).
- **The PNG masters remain the objects of record** for all measurement and any future approval; the surrogates are explicitly noted as not deliverables.

**Schema — pre-ratification conditions reviewed**
- **Condition 1 (diff reviewed) — CONFIRMED, with a material finding.** Full property-level diff against the last committed revision: 22 properties added, 8 removed, 2 modified; `$id` removed; `required` rewritten; `status` enum changed.
- **Condition 2 (checks reproducible) — CONFIRMED.** 35 checks, 0 failed, re-run after the schema was finalised.
- **Condition 3 (backward compatibility against the last ratified version) — NOT CONFIRMED AS STATED.** No schema version in this repository carries a recorded ratification. The `0.2.0` baseline asserted in `SCHEMA-REVIEW-001` §1 was **wrong**: it was written during the Stage A–G build, never ratified, and exists only uncommitted. The last *committed* schema is the original `0.1.0`-era template, against which **0 of 51** registry entries validate. Two readings offered to the authority — ratify as `0.3.0` declaring the committed template abandoned (recommended, since no record ever conformed to it), or as `1.0.0`. §1 and §6 corrected to remove the false "last ratified" claim.
- **Condition 4 (R-2 / R-3 process controls) — CONFIRMED.** New `schemas/PROCESS-CONTROLS-001.md` names nine controls `C-1`…`C-9`, each with procedure, evidence produced, **performing authority** (`production-architect`) and **ratifying authority** (`human-creative-authority`). No control permits self-ratification. Three are exercised (`C-5`, `C-7`, `C-9`); six are established but not yet exercised, and that is stated rather than implied.
- **Condition 5 (version + checksum) — CONFIRMED.** SHA-256 `cd6b0a462eb0211afeab955616901ebc3cc26a6f065a2ededd6def5ce74a2c96` recorded in `schemas/asset.schema.sha256` (sidecar manifest — a file cannot contain its own hash), verified with `sha256sum -c`, and cited in the ratification record.
- **Ratification remains with the Human Creative Authority and is not self-granted.** `0.3.0-rc1` keeps its suffix; `ratification_status.state` reads `release-candidate`.

**Frame A reproduction — open decision recorded**
- `reproduction-spec-open-001.md` §3 now poses the explicit choice: **(A) faithful reproduction** (reuse the `run-01` prompt verbatim, preserving the ~2–3° optical tilt as deliberate) vs. **(B) controlled revision** (adopt the level-horizon / zero-convergence correction, with the prompt delta documented as a revision).
- The correction must **not** be silently folded into a run described as matching the original prompt. **Status: OPEN. Reproduction not authorised under either option.**
- Recorded as `verif-open-decision-001-reproduction-mode`. Under either option the output stays a new candidate with a new checksum requiring its own verification and approval.

### Authority Review 005 — ratification gate held open (`2026-10-17`)

**No generation run. No commit, no push. Schema still unratified.**

**New delivery channel for the visual gate**
- Started a static server on `0.0.0.0:8000` serving `verification/tests/TEST-DUST-C001-001/`, with `visual-review/index.html` presenting Frame B and Frame C **PNG masters at full resolution** (1402×1122, 1152×922) alongside the JPEG surrogates, plus the six outstanding visual gates.
- Verified serving: gallery `HTTP 200`, both masters and the surrogate delivered at full size. Masters remain the objects of record; surrogates are labelled `lineage: derivative` and not deliverables.

**Baseline classification — blocking prerequisite recorded**
- New `schemas/BASELINE-CLASSIFICATION-001.md`: states the evidence (committed `6d223bc` template; **0/51** records valid; no ratification record exists for any schema version; working-tree `0.2.0` also unratified and uncommitted) and the two branches with consequences — **Branch A** ratify `0.3.0` with an *explicit* abandonment exception (recommended), **Branch B** ratify `1.0.0` as a major change against a published baseline.
- Records explicitly that the **0/51 statistic does not by itself settle the version** — whether committed means published is a policy decision about the project's own history, not a measurement. The Production Architect has **no standing to declare a baseline abandoned**; the decision field is left blank.
- `SCHEMA-REVIEW-001` §1 and §6 corrected again to remove any remaining implication that `0.2.0` was ratified.

**Ratification instrument prepared, not signed**
- New `schemas/SCHEMA-RATIFICATION-001.md`: pins the decision to SHA-256 `cd6b0a462eb0211afeab955616901ebc3cc26a6f065a2ededd6def5ce74a2c96`; both version branches pre-filled with checkboxes; decision-maker, date, rationale and accepted exceptions left **blank**; states that any schema edit invalidates the record.

**Control boundary made explicit**
- `schemas/PROCESS-CONTROLS-001.md` gains **§0a Control Boundary**: 3 controls exercised (`C-5`, `C-7`, `C-9`), **6 not exercised** (`C-1`–`C-4`, `C-6`, `C-8`). States that existence is not evidence of function, that `R-2` and `R-3` remain **open risks** until first execution, and that the boundary statement must be reproduced rather than paraphrased wherever the controls are cited as governance readiness.
- `SCHEMA-REVIEW-001` §10 rewritten: the gate now rests on three documents; Conditions 1, 2, 5 confirmed; **Condition 3 not confirmed**; **Condition 4 confirmed as designed only**.

### Notion metadata mirror + new visual-review channel (`2026-10-17`)

**No generation run. No commit, no push. No schema change.**

**Notion capability assessment (asked and answered)**
- The Notion connector **cannot upload image binaries**. Three independent blockers: (1) no file-upload tool, so no `file_upload` id can be minted; (2) `append_block_children` and `create_page` accept paragraph/heading/callout/to_do/toggle/quote/code/table/divider/list types only — `image` is not among them; (3) only `update_block` knows the `image` type, and using it would mean repointing an existing image block in the user's workspace, which was not done.
- The external-URL fallback was assessed and **not attempted**: it needs the connector to pass an undocumented `image` type, needs Notion's servers to reach a sandbox preview URL, and needs the fetch to land before the ephemeral sandbox dies. None verifiable.
- Human Creative Authority chose **metadata mirror only**.

**Metadata mirror created**
- New Notion database `DUST C001 - Media Preservation Register` (`f34ab684-c11d-417d-81b7-20cee1e8a24b`), child of *WRASAL / WRAYvolution — Cinematic Portfolio Production Blueprint v0.2*. 16 properties: Asset ID, Shot, Run, Asset Ref, Lineage, Derivative Of, Transformation, Delivery Status, Storage Status, SHA-256, Dimensions, Format, Byte Length, Canonical Path, Decision ID, Verification Record, Incident.
- **10 register entries mirrored** and verified by query: all 8 pre-existing entries plus the 2 new review JPEGs below.
- Description states the boundary: metadata only, no binaries; the repo YAML is the system of record and wins on conflict; four entries are `preservation-incident`; nothing here is approved.
- The mirror is a **read-only copy and not authoritative**. It changes no media status.

**New full-resolution review surrogates**
- `visual-review/frame-b-full.jpg` (1402x1122, 127,796 B, sha256 `9c1c6429…ea026`) and `visual-review/frame-c-full.jpg` (1152x922, 147,341 B, sha256 `904a33e6…48e6f`) — same pixel dimensions as the masters, lossy re-encode only.
- Registered as `lineage: derivative` (entries 9 and 10) with explicit `derivative_of` and transformation. **Masters remain the objects of record.**

**New delivery channel for the visual gate**
- `visual-review/frames-embedded.html` (376 KB): **self-contained** — both frames base64-embedded, no external file resolution needed. Includes full acceptance criteria, continuity checks, result summaries, and a table of the six assessments only a human can make. Presented to the reviewing authority.
- Earlier `visual-review/index.html` uses relative paths; the preview URL `https://8000-i1mdw5gju7hnrgc6ckuag.e2b.app/visual-review/` was reported as not reaching the reviewer, so the embedded variant is the primary attempt.

### Delivery-boundary diagnostic (`2026-10-17`)

**No generation run. No commit, no push. No schema change.**

**Question asked by the reviewing authority:** is `frames-embedded.html` actually available in the conversation, or only reported as created?

**Finding — it is not visible to the agent either.** `read_file` on any image returns
`[An image was provided here, but you do not have vision capabilities.]`. The agent has never seen
Frame B or Frame C. The only evidence available is a `present_file` tool acknowledgment
(`{"status": "success"}`), which reports that a handoff was **attempted**, not that anything **arrived**.
This is therefore not a case of "visible to the agent, invisible to the authority" — neither party can
confirm receipt. The distinction created / received / verified / approved holds.

**Artifact integrity proven (separate from delivery).** `frames-embedded.html` verified:
- 376,210 bytes; **zero external references** — no `src` or `href` other than `data:` URIs, so it is genuinely self-contained.
- Both embedded payloads decoded and hashed: payload 0 = 127,796 bytes `1402x1122` sha256 `9c1c6429…ea026`; payload 1 = 147,341 bytes `1152x922` sha256 `904a33e6…48e6f`.
- Both match the registered derivatives byte-for-byte. **The artifact is intact; the failure is in delivery, not in the file.**

**Probe built to bracket the boundary** (`visual-review/probe.html`, 11,788 bytes; embedded image 420x336, 8,198 bytes). The probe asks the authority to distinguish three outcomes: HTML and image both arrive (failure is size-specific to the 376 KB gallery); HTML arrives but image does not (images do not traverse); nothing arrives (HTML does not traverse). Registered as `img-red-drawz-001-open-003-run-02-probe-420` — a diagnostic, explicitly not review media and too small to support any of the six assessments.

**Baseline classification** remains open and remains an authority decision, on the authority's stated terms: the choice between `0.3.0` and `1.0.0` must follow an explicit decision about the historical status of the committed template, not the 0/51 compatibility statistic alone. `schemas/BASELINE-CLASSIFICATION-001.md` records both branches with consequences; the decision field is still blank.

### DELIVERY BOUNDARY 001 — in-conversation image delivery unavailable (`2026-10-17`)

**No generation run. No commit, no push. No schema change.**

**Finding. Text traverses the conversation; rendered pixels do not.** Six channels were tested across
two independent rendering mechanisms. Channels 5 and 6 are decisive:

- **Channel 5** — 11.8 KB HTML probe, base64-embedded 420 px JPEG. **Eliminates size** (1/32 the size of the 376 KB gallery, failed identically).
- **Channel 6** — 134 KB inline SVG rectangle mosaic, **no `<img>` tag and no data URI**. **Eliminates format and mechanism** (a pure-vector text construct failed exactly as the raster did).

Path resolution was eliminated earlier: the 376 KB gallery had **zero external references**, and its
payloads decode byte-identical to registered checksums `9c1c6429…ea026` and `904a33e6…48e6f`.

What remains is the receiving interface's ability to render graphics at all — a property of the
channel, not of any artifact the agent produces.

**Recorded as a closed capability boundary, not an open work item.** `verification/tests/TEST-DUST-C001-001/delivery-boundary-001.md` carries a standing instruction: further in-conversation delivery attempts are **not authorised**, because re-testing a settled negative is repetition, not diligence.

**Consequence for the visual gate.** Frames B and C remain `TESTED — AWAITING HUMAN REVIEW`. The blocker has changed character — from *work not yet done* to *no available channel*. Both leave the gate open; **only the first is remediable by the agent**. The six visual assessments await authority-side retrieval of the masters from the workspace paths or the port-8000 server.

**Abandoned artifacts retained, not deleted**, per preservation policy: `frame-b-full.jpg`, `frame-c-full.jpg`, `frames-embedded.html`, `probe.jpg`, `probe.html`, `svg-test.html`, `index.html` — all recorded as review surrogates or diagnostics, none of them deliverables.

**Verification record** `verif-delivery-boundary-001` appended (`verif` records now 13). Master checksums re-verified for retrieval: Frame B `ca0ac612…cd4cbf`, Frame C `e8bee9b5…a8434cb`.

**Baseline classification** remains deferred at the authority's direction. Schema stays `0.3.0-rc1`, unratified.

### DELIVERY BOUNDARY 001 — finding narrowed on review (`2026-10-17`)

**Correction to an overstatement in the previous entry.** No new experiments. No image conversion. No schema change. No commit, no push.

**What was wrong.** The first version of this record asserted that *no in-conversation channel exists*. That is a universal negative, and six tested methods do not support it. It repeated the same structural error as the earlier `0.2.0`-was-ratified claim: evidence about what was tested converted into a statement about everything.

**What the record now says.** *The in-conversation delivery methods tested did not produce a viewable image. Further delivery experiments are suspended. The PNG masters remain available through the external workspace, subject to retrieval by the human reviewer.*

**Structural changes to `delivery-boundary-001.md`:**
- **§2 Evidence** — observed outcomes only, no inference.
- **§3 Interpretation** — inferences separated out, each with stated confidence (size, format and path resolution are *well supported* as not-operative in channels 5 and 6).
- **§4 What this evidence does NOT establish** — four explicit limits: not an exhaustive enumeration of channels; not proof the interface cannot render graphics generally; **no defect in Frame B, Frame C or any derivative**; retrieval by other means unaffected.
- **§5 Standing instruction narrowed** — the six tested methods and trivial variations of them are settled negatives, but a qualitatively new method is a *new decision*, not a resumption of suspended work.

**Verification record `verif-delivery-boundary-001` conformed.** Its `result_summary` now opens with an explicit scope guard: *status `failed` refers to the delivery test only and asserts nothing about any asset*. Evidence and interpretation are separated in the record itself, not only in the document.

**Schema deliberately unchanged.** The record uses the existing permitted vocabulary (`continuity-check` / `failed`). No enum was widened, consistent with the authority's safeguard that an unratified schema with an unresolved baseline should not be expanded to accommodate a new record.

**Status of the frames is unaltered.** Frames B and C remain `TESTED — AWAITING HUMAN REVIEW`. Nothing in this record promotes, demotes, approves or rejects them.

### Visual assessment instrument prepared (`2026-10-17`)

**No image conversion. No gallery. No schema change. No approval. No commit, no push.**

**Integrity flag raised by the Production Architect.** The existing acceptance records contain
assertions the agent could not have verified: Frame C Gate C states *"zero logos, zero text, zero
tags"*, and both Gate F entries state *"No branding … introduced"*. The agent has **no vision
capability** and has never seen either frame. Those statements rest on what the generation prompt
specified, **not on inspection of rendered pixels**, and should be read as claims about the prompt
rather than findings about the image. They were **flagged, not rewritten** — correcting an
acceptance record the agent cannot itself verify would be overreach. Assessments B3 and C1 exist to
convert those claims into verified findings or to falsify them; if either fails, the corresponding
Gate F entry requires correction by the authority.

**New instrument** `verification/tests/TEST-DUST-C001-001/visual-assessment-001.md` — blank, to be
completed by the Human Creative Authority. For each assessment it separates *measured evidence*
from *what only human eyes can settle*, and provides PASS / FAIL / NEEDS REVISION / **CANNOT TELL**
— the last added deliberately, so that an honest inability to judge is recordable rather than
forcing a pass or a fail.

**Seven assessments, not six.** Grounding the original six in the actual verification records
produced seven: branding must be assessed separately in each frame, because Frame B and Frame C are
different images and one branding verdict would not bind to both.
- `VA-001-B1` drawer extension ≈ 4.5 in — explicitly deferred, no machine measurement exists
- `VA-001-B2` bare walnut, full frame — measured on sampled regions only
- `VA-001-B3` Frame B unbranded — chromaticity cannot detect a logo
- `VA-001-C1` Frame C unbranded — region std measures texture variance, not absence of branding
- `VA-001-C2` material continuity — **weakest measured result in either frame**: cross-shot chromaticity delta 6.96 8-bit units vs run-01's < 2, roughly 3.5x worse than the established baseline
- `VA-001-C3` liner neutrality across whole frame
- `VA-001-C4` walnut wall continuity

The instrument states plainly: **a blank field is not a pass**, and neither asset may be promoted to
`APPROVED ASSET` until the sign-off table is complete.

### VA-001-C2 investigated without prejudging it (`2026-10-17`)

**No image conversion. No gallery. No schema change. No threshold altered. No approval. No commit, no push.**

**Correction up front: the Production Architect cannot complete the visual assessment instrument.** It has no vision capability and has never seen either frame; filling it in would produce `CANNOT TELL` in all seven fields. The instrument stays blank pending the human reviewer, and now says so on its face.

**Four-element structure adopted** for every assessment, per authority direction: **Criterion** (what must be true) · **Evidence** (what can be measured or observed) · **Assessment** (PASS / FAIL / NEEDS REVISION / CANNOT TELL) · **Authority** (who assessed, who authorised the state change).

**Prompt-specification vs visual-evidence distinction now recorded IN the acceptance records.** Appended to the run-02 records in `verification-records.json`: *"A prompt specifying zero branding is NOT evidence that the generated image contains zero branding."* The Gate C and Gate F branding assertions rest on what the prompt specified, not on inspection.

**VA-001-C2 findings — the `PASS WITH NOTE` is withdrawn pending decision:**

| Check | Finding |
|:--|:--|
| Arithmetic reproduces? | **Yes** — delta `[6.96, 4.47, 4.83]`, max `6.96`; R/G `4.756 → 3.993` = `−0.763`. Both match exactly. |
| One bad probe, or systematic? | **Systematic** — every Frame C garment sample (3.885–4.318) below every Frame B sample (4.706–4.974); mean gap `−0.727` (−15.1%). |
| Explained by exposure? | **No** — neutral liner moved `−3.1%`, garment moved `−16.0%`. A global exposure difference would move both. |
| Equivalent regions? | **Not strictly** — C2 is 1.78× the area and 3.27× the variance of B2, and samples jersey wales rather than a fold core. |
| Threshold established before result? | **No threshold exists.** The calibrated heuristics are `R/G ≥ 2.2`, `R/B ≥ 2.5`, neutral `R/G ≤ 1.35`, wood `|Δ(R/G)| ≤ 0.15`. A cross-shot 8-bit chromaticity delta is not among them. The "< 2 units" was run-01's observation, never a ratified criterion. |

**No verdict was changed from PASS to FAIL.** The finding is that *no assessable criterion exists* — a different defect, placed before the authority rather than resolved by the agent. **No threshold was relaxed, created or adjusted.** The numerical difference does not by itself establish a visual continuity failure and is not treated as one.

**Secondary finding — VA-001-C4 is control-dependent.** C8 vs **B9** (occluded) = `0.127` PASS; C8 vs **B7** (lit) = `0.239`, which **exceeds** 0.15. The recorded comparison follows `decision-010` as written and is method-compliant, but the PASS depends on which convention is applied. Disclosed, not changed.

**Verification record** `verif-va-001-c2-investigation` appended (records now 14), status `pending` — resolution requires an authority decision: establish a threshold and re-assess, or record the metric as unassessable and rely on visual judgment.
