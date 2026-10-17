# SCHEMA REVIEW 001 — `schemas/asset.schema.json` extension

**Review ID**: `SCHEMA-REVIEW-001`
**Schema**: `schemas/asset.schema.json`
**Version under review**: `0.3.0-rc1`
**Date**: `2026-10-17` (updated same day to record resolution of `R-1` and `R-6`)
**Reviewer**: Production Architect
**Ratification status**: **RELEASE CANDIDATE — both blocking requirements resolved; ratification remains with the Human Creative Authority and is not self-granted**

**Scope note.** A passing validation run proves only that the supplied data conforms to the tested rules. It does not prove that those rules are complete, backward-compatible, or consistent with WRASAL's authority model. This review therefore records what the tests do *not* cover as well as what they do.

---

## 1. Requirements review

| # | Requirement | Review question | Finding | Status |
| :--- | :--- | :--- | :--- | :--- |
| 1 | **Asset identity** | Can the master and each derivative be identified independently? | **YES.** Every entry in `approved_media` / `candidate_media` requires its own `id`. The Frame A master (`img-harlem-ext-001-open-001-master`) and its `1.85:1` crop (`img-harlem-ext-001-open-001-crop185`) carry distinct ids and distinct checksums. Enforced by `required: ["id", ...]`. | **PASS** |
| 2 | **Approval authority** | Can a media entry be labelled approved without a valid human approval record? | **NO.** A conditional rule requires `approved_by`, `approved_date`, **and** `decision_id` whenever `delivery_status == "APPROVED ASSET"`, and constrains `approved_by` to the literal `human-creative-authority`. The mirror rule forbids `approved_by` on non-approved media. Negative tests `B1`, `B2`, `B12` confirm rejection. | **PASS** |
| 3 | **Provenance** | Can the system trace each derivative to its source and transformation? | **PASS (resolved `2026-10-17`).** A required `lineage` discriminator (`original` \| `derivative`) now forces an explicit declaration. `lineage: derivative` requires a non-empty `derivative_of` **and** `transformation`; `lineage: original` requires both to be null or absent. An original generation declares *that it is original* rather than being a derivative with missing parentage. Negative tests `B15`–`B19`, positive tests `C7`–`C8`. | **PASS** |
| 4 | **Immutability** | Can an approved media reference be silently replaced while retaining the same asset identity? | **PARTIAL.** `sha256_history` (append-only) and `superseded_by` make replacement *visible*. The schema cannot *block* an in-place checksum edit — JSON Schema validates state, not transitions. Probe `D2` confirms a changed-checksum entry is still accepted. | **PARTIAL — see R-2** |
| 5 | **Backward compatibility** | Do existing records still validate under the new schema? | **YES.** Positive test `A1`: all **51** existing `production/asset-registry.yaml` entries validate with zero errors. Confirmed by full `jsonschema` run on `2026-10-17`. | **PASS** |
| 6 | **Validation** | Are invalid approval states and incomplete media references rejected? | **YES for the enumerated cases.** 14 negative tests (`B1`–`B14`) all rejected as intended, covering: missing `decision_id`, wrong approving authority, missing `storage_status`, missing/malformed `sha256`, `preserved-retrievable` without `present`/`path`, `preservation-incident` with `present: true`, external media with no `durable_uri`, cross-typed `authority_type`, `approved_by` on unapproved media, unknown properties, and a lock missing its `decision_id`. | **PASS** |
| 7 | **Versioning** | Is the schema change documented and versioned? | **YES.** `schema_version: "0.3.0-draft"` plus a `version_history` array recording both the `0.2.0` baseline and each `0.3.0-draft` step with date and rationale. The unratified status is stated in the version string itself. | **PASS** |

**Summary: 6 PASS · 1 PARTIAL · 0 FAIL.** Requirement 4 (immutability) remains partial and is closed by process control rather than schema — see `R-2`. Requirements 3 and 7 were partial at first review and are now resolved (`R-1`, `R-6`).

**Backward-compatibility baseline — CORRECTED `2026-10-17`.** This section previously named `0.2.0` as "the last ratified version". That was wrong: `0.2.0` was written during the Stage A–G build, was never ratified, and exists only as an uncommitted working-tree edit. The last **committed** schema is the original `0.1.0`-era template, against which **0 of 51** registry entries validate. See §9 Condition 3 for the full finding and the two readings available to the Human Creative Authority. Relative to the working-tree `0.2.0` actually in use, the change is minor: test `A1` confirms all 51 entries still validate.

---

## 2. Authority separation — `garment_spec_lock` vs `calibrated_heuristic`

The Human Creative Authority required that the two blocks stay distinct: the former records a **human-authorised design constraint**; the latter records a **verification rule**. Neither may silently acquire the authority of the other.

| | `garment_spec_lock` | `calibrated_heuristic` |
| :--- | :--- | :--- |
| Title | `DesignConstraintLock` | `VerificationRule` |
| Required discriminator | `authority_type: "design-constraint"` (const) | `authority_type: "verification-rule"` (const) |
| Records | what a thing must **look like** | how conformance is **measured** |
| Canonical decision | `decision-008` (`H-05`) | `decision-010` |
| Wrong-type rejected? | `B10` — yes | `B11` — yes |
| Both present, correctly typed | — | `C5` — accepted |

**Residual risk `R-3` (probe `D1`):** both blocks permit `additionalProperties: true`, so a verification rule could still be *written inside* `garment_spec_lock` under a novel key. The `authority_type` const prevents **mislabelling the block**; it does not prevent **smuggling content into it**. Closing this fully requires either `additionalProperties: false` (breaking, since the spec lock legitimately carries open-ended garment fields) or a review-time control. **Recommendation: keep the two blocks in separate registers and diff them at review time. Do not close `additionalProperties` on `garment_spec_lock`** — it would freeze legitimate design fields.

---

## 3. The identity / approval / preservation distinction

Three rules were encoded deliberately:

1. **A checksum establishes file identity, not approval.** `sha256` carries no governance weight. Approval lives entirely in `delivery_status` + `decision_id` + `approved_by` + `approved_date`.
2. **Approval must remain linked to an authorised decision.** Enforced by the `APPROVED ASSET` conditional (requirement 2).
3. **A valid approval record must not imply that the underlying file is still available.** `storage_status` is an independent required field with three states: `preserved-retrievable`, `recorded-only`, `preservation-incident`. Positive test `C1` asserts that `delivery_status: APPROVED ASSET` **together with** `storage_status: preservation-incident` is a valid combination — which is exactly the live state of `img-harlem-ext-001-open-001-master` under `INC-2026-10-17-001`.

This is the schema-level expression of the governing rule: *an image is not preserved merely because its approval is recorded, and an approval is not established merely because an image passes a numerical test.*

---

## 4. Diff summary — `0.2.0` → `0.3.0-rc1`

**Step 1 (earlier `2026-10-17`)** — new optional properties, no constraints:
`approved_date`, `approved_by`, `approved_media`, `candidate_media`, `garment_spec_lock`, `calibrated_heuristic`, `test_references`.

**Step 3 (`R-1`, `R-6`)** — provenance and versioning:

| Change | Rationale |
| :--- | :--- |
| New required `lineage` discriminator (`original` \| `derivative`) | `R-1` — provenance is mandatory and explicit |
| `lineage: derivative` ⇒ require non-empty `derivative_of` **and** `transformation` | `R-1` — a derivative cannot lose its source relationship |
| `lineage: original` ⇒ `derivative_of` and `transformation` must be null or absent | `R-1` — an original declares no parentage rather than missing it |
| New `versioning_policy` block (patch / minor / major, baseline, separation from asset versioning) | `R-6` |
| `version_history` entries now require `version`, `date`, `note`, `compatibility`, `tests` | `R-6` — every change records rationale, compatibility and tests |
| New `ratification_status` block | Makes the unratified state explicit in the contract itself |
| New optional `media_disposition` block | Lets a lost medium be dispositioned without rewriting its prior approval |
| `candidate_media` item schema re-synced to be identical to `approved_media` | Both arrays must enforce the same invariants |

**Step 2 (same day, before `R-1`/`R-6`)** — hardening:

| Change | Rationale |
| :--- | :--- |
| Media items: `required` now `["id","type","delivery_status","storage_status","sha256"]` | Approval and preservation cannot be omitted |
| `sha256` constrained to `^[a-f0-9]{64}$` | Reject placeholder/malformed checksums |
| New `storage_status` enum | Makes "approved but unavailable" representable |
| New `sha256_history` (append-only) + `superseded_by` | Makes silent replacement visible |
| New `derivative_of`, `transformation` | Provenance of master → crop → derivatives |
| New `durable_uri`, `present`, `byte_length` | External storage and retrievability |
| Media items: `additionalProperties: false` | Reject typos and undeclared fields |
| Conditional: `APPROVED ASSET` ⇒ require `approved_by` (const `human-creative-authority`), `approved_date`, `decision_id` | Approval cannot exist without an authorising decision |
| Conditional: non-approved ⇒ forbid `approved_by` | Approval field cannot linger on unapproved media |
| Conditional: `path: null` ⇒ require `durable_uri` | Externally held media stays retrievable |
| Conditionals: `preserved-retrievable` ⇒ `present: true` **and** `path` required; `preservation-incident` ⇒ `present: false` | Preservation state must be internally coherent |
| `garment_spec_lock` / `calibrated_heuristic` retyped as titled objects with `const` `authority_type` and required `decision_id` | Authority separation, per §2 |
| `schema_version` + `version_history` | Requirement 7 |

---

## 5. Test evidence

Suite: `schemas/tests/test-asset-schema.py`
Run: `2026-10-17` · `pyyaml 6.0.3` · `jsonschema 4.26.0` · draft 2020-12

```
[PASS] A1 backward compatibility: all 51 existing asset-registry entries validate
[PASS] B1  APPROVED ASSET media without decision_id
[PASS] B2  APPROVED ASSET approved by a non-human authority
[PASS] B3  media reference missing storage_status
[PASS] B4  media reference missing sha256
[PASS] B5  malformed sha256 (not 64 hex chars)
[PASS] B6  preserved-retrievable but present=false
[PASS] B7  preserved-retrievable but no path
[PASS] B8  preservation-incident but present=true
[PASS] B9  externally held media (path null) with no durable_uri
[PASS] B10 garment_spec_lock marked as a verification rule
[PASS] B11 calibrated_heuristic marked as a design constraint
[PASS] B12 non-approved media carrying approved_by
[PASS] B13 unknown property inside a media reference
[PASS] B14 garment_spec_lock missing decision_id
[PASS] B15 derivative (lineage=derivative) with no derivative_of            [R-1]
[PASS] B16 derivative with no transformation                                [R-1]
[PASS] B17 original (lineage=original) carrying a non-null derivative_of    [R-1]
[PASS] B18 media reference missing lineage entirely                         [R-1]
[PASS] B19 derivative with an empty-string derivative_of                    [R-1]
[PASS] B20 invalid lineage value                                            [R-1]
[PASS] C1  APPROVED ASSET with full approval block AND preservation-incident
           (approval does not imply availability)
[PASS] C2  candidate media with no approval block
[PASS] C3  externally held media with path null + durable_uri
[PASS] C4  derivative carrying provenance (lineage + derivative_of + transformation)
[PASS] C5  design-constraint lock and verification-rule lock coexisting, correctly typed
[PASS] C6  superseded media retaining prior checksums in sha256_history
[PASS] C7  original asset explicitly declaring no lineage                   [R-1]
[PASS] C8  derivative naming both source and transformation                 [R-1]
[INFO] D1  RESIDUAL RISK: verification rule smuggled into garment_spec_lock is ACCEPTED
[INFO] D2  RESIDUAL RISK: APPROVED ASSET with changed checksum in sha256_history is ACCEPTED
[PASS] E1  version_history entries each record version, date, rationale,
           compatibility assessment and tests                               [R-6]
[PASS] E2  version_history contains an entry for the current schema_version [R-6]
[PASS] E3  semantic versioning policy declares patch / minor / major        [R-6]
[PASS] E4  policy states schema versioning is distinct from asset versioning [R-6]
[PASS] E5  assets carry their own 'version' field, independent of schema_version [R-6]
[PASS] E6  schema_version is not conflated with the asset version value     [R-6]

schema_version: 0.3.0-rc1
RESULT: 0/35 checks failed
```

One negative case caught a real defect during this run: test `C4` had been written before `R-1` and supplied `derivative_of` **without** `lineage: derivative`. The new rule correctly rejected it. The test was corrected, not the rule — provenance fields on an asset declared `original` are now a contradiction, which is exactly the failure mode `R-1` exists to prevent.

---

## 6. Resolution of the blocking requirements

### `R-1` — Mandatory derivative provenance — **RESOLVED `2026-10-17`**

Implemented per the Human Creative Authority's recommendation:

| Element | Implementation |
| :--- | :--- |
| Explicit declaration | Every media reference requires `lineage` ∈ {`original`, `derivative`} |
| Derivative | `lineage: derivative` **requires** non-empty `derivative_of` **and** `transformation` |
| Original | `lineage: original` requires both to be `null` or absent — an original declares no parentage rather than missing it |
| Lineage patterns honoured | Frame A master → `original`; Frame A crop → `derivative` (master + crop rectangle); Frame B `run-02` → `original` (prompt-driven, no reference image); Frame C `run-02` → `derivative` (reference-conditioned on Frame B) |

### `R-6` — Schema versioning policy — **RESOLVED `2026-10-17`**

Adopted explicit semantic versioning for the schema contract, following the repository's existing `MAJOR.MINOR.PATCH` convention (registries carry `version: "0.2.0"`; `CHANGELOG.md` is sectioned the same way):

| Change class | Definition |
| :--- | :--- |
| **Patch** | Documentation or corrections that do not change validation behaviour |
| **Minor** | Backward-compatible additions that existing valid records can tolerate |
| **Major** | Breaking changes: new or removed mandatory fields that invalidate previously valid records, removed properties, narrowed types or enums, or a **changed meaning** of an existing field |

Three supporting rules were encoded alongside it:

1. **Compatibility baseline** — assessed against the last *ratified* version, since a draft was never in force. **Open:** no version is currently ratified, so the first application of this policy requires the Human Creative Authority to name the baseline explicitly (§9 Condition 3).
2. **Separation from asset versioning** — changing the schema does not mean an approved image changed; changing an image does not mean the schema changed. Assets keep their own independent `version` field.
3. **Per-change record** — every change records version, date, rationale, compatibility assessment, and tests performed. `version_history` now *enforces* all five keys, and tests `E1`–`E6` assert the policy is present and correct.

---

## 7. Remaining open items

| ID | Item | Status | Blocking? |
| :--- | :--- | :--- | :--- |
| **R-1** | Mandatory derivative provenance | **RESOLVED** `2026-10-17` | Closed |
| **R-6** | Schema versioning policy | **RESOLVED** `2026-10-17` | Closed |
| **R-2** | Immutability is detectable, not enforceable. A checksum can still be edited in place; `sha256_history` makes it visible but JSON Schema validates state, not transitions. | Open | **No — process control** |
| **R-3** | Content smuggling between the two lock blocks remains possible (probe `D1`), because both allow open properties. | Open | **No — review control** |
| **R-4** | `delivery_status` uses an ASCII hyphen in the enum while prose elsewhere uses an em dash. | Open | **No — hygiene** |
| **R-5** | Suite depends on `pyyaml` / `jsonschema`, not installed by default in the agent sandbox. | Open | **No — tooling** |

**On `R-2` and `R-3`, the reviewer's position is adopted:** JSON Schema can constrain document structure and valid states; it cannot independently guarantee immutable files or enforce every transition between states. Those requirements belong in storage and workflow controls — validate permitted fields while allowing deliberately extensible areas; compare the current record against the previous approved record; reject unapproved checksum changes to approved media; require a new revision and explicit approval for replacement media; preserve the prior record and its media identity in an auditable history. No attempt has been made to solve either problem with JSON Schema alone.

---

## 8. Reviewer's recommendation

**Recommend `0.3.0-rc1` for ratification as `0.3.0`.** Both blocking requirements are resolved and enforced by tests. The two remaining risks (`R-2`, `R-3`) are explicitly accepted as process controls rather than schema constraints, in line with the Human Creative Authority's position.

Ratification is **not** self-granted. `schema_version` carries the `-rc1` suffix and `ratification_status.state` reads `release-candidate` until the Human Creative Authority records the decision. On ratification the suffix is dropped.

---

## 9. Pre-ratification conditions — review findings

The Human Creative Authority required five conditions to be confirmed before ratification. Four are confirmed. **One cannot be confirmed as stated**, and the reason is recorded below rather than asserted away.

### Condition 1 — Complete schema diff reviewed: **CONFIRMED, WITH A MATERIAL FINDING**

Diff taken against the last **committed** revision (`6d223bc`), which is the original asset-schema template:

```
ADDED    (22): approval_status, approved_by, approved_date, approved_media,
               calibrated_heuristic, candidate_media, canon_status, category,
               dependencies, downstream_dependents, garment_spec_lock,
               governance_status, id, id_origin, media_disposition, notes,
               owner, scope, test_references, version, version_history, ...
REMOVED   (8): asset_id, asset_type, canonical_status, created_at,
               updated_at, notion_ref, source, summary
MODIFIED  (2): name, status
SCHEMA-LEVEL ADDED   : ratification_status, schema_version, version_history, versioning_policy
SCHEMA-LEVEL REMOVED : $id
required: ['asset_id','name','asset_type','status','canonical_status','created_at','updated_at']
       -> ['id','category','name','status','canon_status','approval_status','version','owner','dependencies']
```

**Material finding:** the committed schema is not the `0.2.0` baseline named in §1. It is the **original template**, and it is **obsolete** — see Condition 3.

### Condition 2 — The 35 checks are reproducible against the candidate schema: **CONFIRMED**

Re-run `2026-10-17` after the schema was finalised:

```
$ python3 schemas/tests/test-asset-schema.py
schema_version: 0.3.0-rc1
RESULT: 0/35 checks failed
```

Suite is a single self-contained file with no network or fixture dependencies. Environment: `pyyaml 6.0.3`, `jsonschema 4.26.0`, draft 2020-12. Reproducibility caveat recorded in `R-5`: those two packages are not installed by default in the agent sandbox.

### Condition 3 — Backward compatibility assessed against the last ratified version: **NOT CONFIRMED AS STATED**

This condition cannot be confirmed, because **no schema version in this repository carries a recorded ratification.**

| Candidate baseline | Committed? | Records valid | Formally ratified? |
| :--- | :--- | :--- | :--- |
| Committed `6d223bc` template (0.1.0-era) | Yes | **0 / 51** | No |
| Working-tree `0.2.0` | No | 51 / 51 | No |
| Candidate `0.3.0-rc1` | No | 51 / 51 | **Pending — this decision** |

§1 asserted compatibility against `0.2.0` as "the last ratified version". That was **wrong**: `0.2.0` was written during the Stage A–G build and never ratified, and it exists only as an uncommitted working-tree edit.

If the committed template is treated as the baseline, then under the `R-6` policy this change is **MAJOR** — required fields changed, eight properties removed, and the `status` enum changed. Ratifying it as a *minor* `0.3.0` would misstate its compatibility class.

**Two defensible readings, for the Human Creative Authority to choose:**

- **(a) Ratify as `0.3.0`, declaring the committed template abandoned rather than migrated.** Supported by the evidence that **0 of 51** records ever conformed to it, so no record is broken by the change. The `0.1.0`-era schema described an asset shape the project stopped using before any record was written against it.
- **(b) Ratify as `1.0.0`.** Signals a clean break and a first canonical contract. Conflicts with the repository's pre-1.0 convention (`CHANGELOG.md` is at `0.2.0`) and would imply a stability the project has not yet claimed.

**Reviewer's recommendation: (a)**, with the abandonment recorded explicitly and the `R-6` classification stated as *major relative to the committed template, minor relative to the working-tree `0.2.0` that is in actual use*.

### Condition 4 — R-2 and R-3 have named process controls and responsible authority: **CONFIRMED**

`schemas/PROCESS-CONTROLS-001.md` names nine controls (`C-1`…`C-9`), each with a procedure, the evidence it produces, a **performing authority** (`production-architect`) and a **ratifying authority** (`human-creative-authority`). No control permits the performing authority to ratify its own output.

- `R-2` → `C-1` checksum-change gate · `C-2` baseline snapshot · `C-3` append-only media writes · `C-4` mandatory supersession history · `C-5` retrieval reverification
- `R-3` → `C-6` register separation · `C-7` key-set diff at review · `C-8` decision-linked extension · `C-9` const discriminator retained

Three are already exercised (`C-5`, `C-7`, `C-9`). The remaining six are **established but not yet exercised** — no approved media has been promoted, superseded, or replaced since they were written. That is stated in the control log rather than left implicit.

### Condition 5 — Ratification record identifies the exact schema version and checksum: **CONFIRMED**

| Field | Value |
| :--- | :--- |
| Version presented for ratification | `0.3.0` (`schema_version` currently `0.3.0-rc1`) |
| SHA-256 of `schemas/asset.schema.json` | `cd6b0a462eb0211afeab955616901ebc3cc26a6f065a2ededd6def5ce74a2c96` |
| Checksum manifest | `schemas/asset.schema.sha256` (verified with `sha256sum -c`) |
| Suite | `schemas/tests/test-asset-schema.py` — 35 checks, 0 failed |

The checksum is held in a **sidecar manifest, not inside the schema** — a file cannot contain its own hash. The schema points to the manifest via `ratification_status.checksum_manifest`. Any edit to the schema invalidates the checksum, so a ratification pinned to this hash is pinned to exactly this content.

---

## 10. Ratification state

**The candidate is NOT ratified.** Three documents now carry the gate:

| Document | Role |
| :--- | :--- |
| `schemas/BASELINE-CLASSIFICATION-001.md` | **Blocking prerequisite.** Decides whether the committed `6d223bc` template is the compatibility baseline. Determines whether the version is `0.3.0` or `1.0.0`. **OPEN.** |
| `schemas/PROCESS-CONTROLS-001.md` | `C-1`…`C-9`, with performing and ratifying authorities. **§0a states the control boundary: 3 exercised, 6 not.** |
| `schemas/SCHEMA-RATIFICATION-001.md` | The signing instrument. Pinned to SHA-256 `cd6b0a462eb0211afeab955616901ebc3cc26a6f065a2ededd6def5ce74a2c96`. Decision-maker and date blank pending authority. |

### Condition status

| # | Condition | Status |
| :--- | :--- | :--- |
| 1 | Complete schema diff reviewed | Confirmed (with the material finding in §9 Condition 1) |
| 2 | 35 checks reproducible | Confirmed — 0 failed |
| 3 | Backward compatibility assessed against the last ratified version | **NOT CONFIRMED — no version is ratified; baseline classification is an open authority decision** |
| 4 | `R-2` / `R-3` have named process controls and responsible authority | **Confirmed as designed; 6 of 9 controls unexercised** |
| 5 | Ratification record identifies exact version and checksum | Confirmed — see `SCHEMA-RATIFICATION-001.md` §1 |

### Why the gate is not closed

Two of the five conditions are only partly satisfied, and neither gap can be closed by further engineering:

- **Condition 3** requires the authority to say what the baseline *is*. Evidence can show what records conform; it cannot show which historical state the project accepts as binding.
- **Condition 4** is satisfied by design but not by execution. **A complete control design is not a validated control system**, and a tested schema is not a ratified schema.

### Release state

`schema_version` remains **`0.3.0-rc1`**. `ratification_status.state` remains **`release-candidate`**. No commit and no push has been performed, and none should be inferred from these records.

**The authorisation-history caveat from `verif-reconciliation-001` remains intact and is not upgraded by this review.**
