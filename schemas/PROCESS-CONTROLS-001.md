# PROCESS CONTROLS 001 — Risks not closable by JSON Schema

**Control ID**: `PROCESS-CONTROLS-001`
**Created**: `2026-10-17`
**Covers**: `R-2` (approved-media immutability) and `R-3` (authority separation between design-constraint and verification-rule blocks)
**Origin**: `SCHEMA-REVIEW-001` §7 — accepted as process controls rather than schema constraints

---

## 0. Why these are not schema rules

JSON Schema constrains **document structure** and **valid states**. It cannot:

- guarantee that a file on disk is immutable;
- enforce a *transition* between two states (it sees only the states, never the move);
- prevent a correctly-typed block from carrying semantically wrong content.

Both risks are therefore closed by **workflow controls with a named responsible authority**, exactly as directed in *Authority Review 003* §5. The schema records what it can; this document governs the rest.

### Authorities

| Role | Authority | Meaning |
| :--- | :--- | :--- |
| **Performing authority** | `production-architect` | Executes the control, produces the evidence, and must not self-approve |
| **Ratifying authority** | `human-creative-authority` | Reviews the evidence and grants or withholds approval. No control is complete without this |

No control below permits the performing authority to ratify its own output.

---

## 0a. CONTROL BOUNDARY — read before citing this document

> **A complete control design is not a validated control system.**

This document defines nine controls. Their **existence is not evidence that they work.** Three have been exercised; six have not, because no triggering event has occurred.

| Status | Count | Controls |
| :--- | :--- | :--- |
| **Defined AND exercised** | **3** | `C-5` retrieval reverification · `C-7` key-set baseline documented · `C-9` const discriminator tested (`B10`, `B11` reject cross-typed blocks) |
| **Defined, NOT exercised** | **6** | `C-1` checksum-change gate · `C-2` baseline snapshot · `C-3` append-only media writes · `C-4` mandatory supersession history · `C-6` register separation · `C-8` decision-linked extension |

**Why the six are unexercised:** no approved media has been promoted, superseded, replaced, or re-checksummed since these controls were written. That is an absence of triggering events, **not** an absence of risk.

**What this means for `R-2` and `R-3`:** both risks remain **OPEN**. They are mitigated by design and will be mitigated in practice only when the corresponding controls first execute and produce evidence. Until then:

- `R-2` — an approved media checksum can still be changed in place. It would be *visible* at the next control point and *attributable* to the performing authority, but it is not *prevented*.
- `R-3` — content can still be smuggled between `garment_spec_lock` and `calibrated_heuristic`. It would be *caught* at the next `C-7` key-set diff, but it is not *blocked* by validation.

**Expected first execution:** `C-2`, `C-3` and `C-6` execute at the first promotion to `APPROVED ASSET` — currently the re-production of `shot-open-001`, which is **not authorised**. `C-1` and `C-4` execute at the first supersession. `C-8` executes at the first extension of either lock block.

This boundary statement must be reproduced, not paraphrased, wherever these controls are cited as evidence of governance readiness.

---

## 1. `R-2` — Approved-media immutability

**Risk**: a checksum on an approved media reference can be edited in place. `sha256_history` makes that *visible*; it does not make it *impossible*.

| # | Control | Procedure | Evidence produced | Performing authority | Ratifying authority |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **C-1** | **Checksum-change gate** | Any change to `sha256` on an entry whose `delivery_status` is `APPROVED ASSET` is prohibited in place. The entry must be set to `delivery_status: SUPERSEDED`, given `superseded_by` pointing at a new entry, and its prior checksum appended to `sha256_history`. A new entry with a new `id` carries the new media. | Diff of before/after register entries; the two register entries | `production-architect` | `human-creative-authority` |
| **C-2** | **Approved-record baseline snapshot** | Immediately before any promotion to `APPROVED ASSET`, snapshot the full register entry. Every later review diffs the live entry against that snapshot. | Snapshot file + diff report | `production-architect` | `human-creative-authority` |
| **C-3** | **Append-only media writes** | Files in `production/media/**` are never overwritten in place. A changed file is written to a new path under a new run directory. The old file is retained. | Directory listing showing both paths; both checksums | `production-architect` | `human-creative-authority` (on review) |
| **C-4** | **Mandatory supersession history** | When `superseded_by` is set, `sha256_history` must be non-empty and must contain the prior checksum. Registering this as a **schema conditional** is deferred to the next minor version; until then it is enforced here. | Register entry | `production-architect` | `human-creative-authority` |
| **C-5** | **Retrieval reverification** | Each review recomputes SHA-256 for every entry marked `preserved-retrievable` and records the date. A mismatch opens a preservation incident. | `retrieval-test-*.md` | `production-architect` | `human-creative-authority` |

**Residual risk after controls**: a malicious or careless in-place edit is still *possible*; it is now *detectable at the next control point* and *attributable*. This risk is **accepted**, not eliminated.

**Open follow-up**: promote `C-4` from process control to schema conditional in the next minor version (backward-compatible addition under the `R-6` policy), once the ratifying authority confirms the rule is settled.

---

## 2. `R-3` — Authority separation between the two lock blocks

**Risk**: `garment_spec_lock` and `calibrated_heuristic` both permit open properties, so a verification rule could be written *inside* a design-constraint block (or vice versa) under a novel key. The `authority_type` const prevents **mislabelling the block**; it does not prevent **smuggling content into it**.

| # | Control | Procedure | Evidence produced | Performing authority | Ratifying authority |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **C-6** | **Register separation** | Design constraints are recorded **only** in `production/props-register.yaml` and `production/wardrobe-register.yaml`. Verification rules are recorded **only** in `verification/**` and `production/continuity-register.yaml`. Neither register restates the other's content; they cross-reference by `decision_id` only. | Register files | `production-architect` | `human-creative-authority` |
| **C-7** | **Key-set diff at review** | At each review, list the keys present in each block and diff them against the documented expected key set. Any key not in the expected set must be justified by a named decision id or removed. | Key-set diff table | `production-architect` | `human-creative-authority` |
| **C-8** | **Decision-linked extension** | A new key may be added to either block only when it is traceable to a specific decision id recorded in `canon/canon-decisions.md`. Undecorated keys are rejected at review. | Key → decision id mapping | `production-architect` | `human-creative-authority` |
| **C-9** | **Const discriminator retained** | `authority_type` remains a `const` in the schema. Mislabelling the block is blocked at validation time (`B10`, `B11`). | Conformance suite output | `production-architect` | `human-creative-authority` |

**Documented expected key sets** (baseline, `2026-10-17`):

| Block | Expected keys |
| :--- | :--- |
| `garment_spec_lock` (`authority_type: design-constraint`) | `decision_id`, `human_decision_token`, `locked_date`, `garment_type`, `branding`, `surface_finish`, `dye_value`, `fabric`, `construction`, `hard_blockers` |
| `calibrated_heuristic` (`authority_type: verification-rule`) | `decision_id`, `calibrated_date`, `track_1_neutral_achromatic`, `track_2_intrinsically_warm`, `reporting_rule` |

**Deliberate decision**: `additionalProperties` is **not** set to `false` on `garment_spec_lock`. Doing so would freeze legitimate design fields as the garment specification evolves. Content discipline is maintained by `C-7` and `C-8` instead. This trade-off is recorded, not hidden.

---

## 3. Control execution log

| Date | Control | Performed by | Result | Ratified by |
| :--- | :--- | :--- | :--- | :--- |
| `2026-10-17` | `C-9` — const discriminator retained and tested | `production-architect` | PASS (`B10`, `B11` reject cross-typed blocks) | *pending* |
| `2026-10-17` | `C-7` — initial key-set baseline documented (§2 table) | `production-architect` | Baseline recorded | *pending* |
| `2026-10-17` | `C-5` — retrieval reverification | `production-architect` | PASS for 2/6 media (`retrieval-test-001.md`) | *pending* |

**Control boundary:** `C-1` through `C-4`, `C-6` and `C-8` are **established but not yet exercised**. Six of nine controls have no execution evidence. Their existence must not be presented as proof that the controls have been tested. `R-2` and `R-3` remain **open risks** until first execution. See §0a.
