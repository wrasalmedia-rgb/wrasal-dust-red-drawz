# BASELINE CLASSIFICATION 001 — Which schema is the compatibility baseline?

**Decision ID**: `BASELINE-CLASSIFICATION-001`
**Raised**: `2026-10-17`
**Raised by**: Production Architect
**Blocks**: ratification of `schemas/asset.schema.json` `0.3.0-rc1`
**Status**: **OPEN — requires Human Creative Authority decision**

> **This document does not decide the question.** It states the evidence and the consequences of each answer so that the authority's decision is a single explicit choice. The Production Architect has no standing to declare a baseline abandoned.

---

## 1. The question

Under the `R-6` versioning policy, a change is **major** if it breaks records that were valid under the baseline. So before `0.3.0-rc1` can be classified, one thing must be settled:

> **Is the committed schema template (`6d223bc`) the compatibility baseline whose obligations still apply, or is it an abandoned pre-ratification artifact that was never adopted?**

The two answers produce different version numbers for the identical artifact.

---

## 2. Evidence

| Fact | Finding | Source |
| :--- | :--- | :--- |
| Committed schema revision | `6d223bc` — "Initialize WRASAL DUST GitHub repository…" | `git log -- schemas/asset.schema.json` |
| Shape of the committed template | Required `asset_id`, `asset_type`, `canonical_status`, `created_at`, `updated_at`; properties `notion_ref`, `source`, `summary`; `$id` present | `git show HEAD:schemas/asset.schema.json` |
| Records currently valid against it | **0 / 51** | Validation run `2026-10-17` |
| Example failure | `'asset_id' is a required property` | same run |
| Whether any record was ever written against it | **No evidence found.** No registry entry in `production/*.yaml` matches that shape | same run |
| Whether it was ever ratified | **No ratification record exists for any schema version in this repository** | Sweep of `schemas/**`, `canon/**`, `verification/**` |
| Whether the working-tree `0.2.0` was ratified | **No.** Written during the Stage A–G build; never ratified; never committed | `git status` |
| Records valid against working-tree `0.2.0` | 51 / 51 | Validation run |
| Records valid against candidate `0.3.0-rc1` | 51 / 51 | `schemas/tests/test-asset-schema.py`, check `A1` |

---

## 3. What the evidence does **not** determine

The fact that **0 of 51** records validate against the committed template does **not** by itself settle the version number.

It establishes that **no current record would be broken** by the change. It does not establish whether the project treats that template as:

- a **published baseline** whose compatibility obligations survive regardless of current usage, or
- an **abandoned draft** that was superseded before adoption and therefore carries no obligations.

That is a **policy decision about the project's own history**, not a measurement. It belongs to the Human Creative Authority.

---

## 4. The two branches

### Branch A — Template abandoned before adoption

**Position**: the committed template is a pre-ratification scaffold. It was superseded before any record was written against it, it describes an asset shape the projectnever used, and it carries no forward compatibility obligations.

| | |
| :--- | :--- |
| **Version** | `0.3.0` |
| **Semantic class** | Minor, relative to the working-tree `0.2.0` actually in use |
| **Justification** | All 51 live records validate before and after (`A1`); no record is broken |
| **Required exception** | The abandonment must be **explicit in the ratification record** — not implied by the 0/51 statistic alone |
| **Convention fit** | Consistent with the repository's pre-1.0 convention (`CHANGELOG.md` at `0.2.0`) |
| **Risk** | Understates a change that is, relative to the committed artifact, breaking. A future reader comparing `HEAD` to `0.3.0` would expect `0.x` to imply compatibility and would be wrong. |

### Branch B — Template treated as a published baseline

**Position**: a committed schema is a published contract. That no record currently conforms to it does not release the project from its compatibility obligations.

| | |
| :--- | :--- |
| **Version** | `1.0.0` |
| **Semantic class** | Major — required fields changed, 8 properties removed, `status` enum changed |
| **Justification** | Under `R-6`, changed or removed mandatory fields and a changed enum are major regardless of current record counts |
| **Required exception** | None — this is the policy applied as written |
| **Convention fit** | Conflicts with the repository's pre-1.0 convention; implies a stability the project has not otherwise claimed |
| **Risk** | Signals a public/stable contract the project may not be ready to assert. Mitigable by stating that `1.0.0` marks first canonical ratification rather than API stability. |

---

## 5. Reviewer's note

**Branch A is recommended**, on the evidence that no record ever conformed to the committed template — the abandonment is not a convenience, it is what actually happened. But the recommendation carries no authority, and the deciding consideration is the project's own stance on whether committed means published.

Whichever branch is chosen, the chosen rationale and any accepted exception must be recorded in `schemas/SCHEMA-RATIFICATION-001.md` at the moment of ratification.

---

## 6. Decision record

| Field | Value |
| :--- | :--- |
| Question | Is the committed `6d223bc` template the compatibility baseline? |
| Branch selected | ***pending Human Creative Authority*** |
| Decided by | ***pending*** |
| Decided date | ***pending*** |
| Resulting version | `0.3.0` (Branch A) **or** `1.0.0` (Branch B) |
| Rationale | ***pending*** |
| Exception accepted | ***pending*** |

**Until this is signed, `0.3.0-rc1` cannot be promoted.** The version number is part of what is being ratified, not a detail to be settled afterwards.
