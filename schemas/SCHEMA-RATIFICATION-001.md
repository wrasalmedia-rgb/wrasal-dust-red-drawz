# SCHEMA RATIFICATION 001 — `schemas/asset.schema.json`

**Ratification ID**: `SCHEMA-RATIFICATION-001`
**Artifact under ratification**: `schemas/asset.schema.json`
**Candidate version**: `0.3.0-rc1`
**Artifact SHA-256**: `cd6b0a462eb0211afeab955616901ebc3cc26a6f065a2ededd6def5ce74a2c96`
**Checksum manifest**: `schemas/asset.schema.sha256` (verify with `sha256sum -c schemas/asset.schema.sha256`)

**STATUS: NOT RATIFIED.** Ratification is a human authority act. This document is the instrument on which it is recorded; it does not perform it.

---

## 1. Pinning

The decision is pinned to the artifact by checksum. **Any edit to `schemas/asset.schema.json` invalidates this record** and requires a new checksum, a new suite run, and a fresh ratification.

| Field | Value |
| :--- | :--- |
| Artifact | `schemas/asset.schema.json` |
| `schema_version` as shipped | `0.3.0-rc1` |
| SHA-256 | `cd6b0a462eb0211afeab955616901ebc3cc26a6f065a2ededd6def5ce74a2c96` |
| Byte-level identity verified | `2026-10-17` via `sha256sum -c` — `OK` |
| Conformance suite | `schemas/tests/test-asset-schema.py` — **35 checks, 0 failed** |
| Review record | `schemas/SCHEMA-REVIEW-001-asset-schema.md` |
| Process controls | `schemas/PROCESS-CONTROLS-001.md` |
| **Blocking prerequisite** | `schemas/BASELINE-CLASSIFICATION-001.md` — **OPEN** |

---

## 2. What ratification would assert

Signing below asserts **all** of the following, and nothing more:

1. The complete schema diff has been reviewed (`SCHEMA-REVIEW-001` §9 Condition 1).
2. The 35 checks are reproducible against the candidate schema (§9 Condition 2).
3. Backward compatibility has been assessed against a **named** baseline (§9 Condition 3 — **requires `BASELINE-CLASSIFICATION-001`**).
4. `R-2` and `R-3` have named process controls and responsible authority (`PROCESS-CONTROLS-001`, `C-1`…`C-9`).
5. The ratification record identifies the exact schema version and checksum (§1 above).

It does **not** assert that the process controls have been exercised. See §4.

---

## 3. Version selection — complete both lines, then strike one

### ☐ Branch A · Ratify as `0.3.0`

- [ ] The Human Creative Authority accepts that the committed `6d223bc` template was **abandoned before adoption** and carries no forward compatibility obligations.
- [ ] Accepted exception: the change is **major relative to the committed artifact** but classified **minor relative to the working-tree `0.2.0` actually in use**. This exception is recorded explicitly and is not left to be inferred from the 0/51 statistic.
- [ ] Semantic class: **minor**.

### ☐ Branch B · Ratify as `1.0.0`

- [ ] The committed `6d223bc` template is treated as a **published baseline** whose compatibility obligations survive regardless of current usage.
- [ ] Semantic class: **major** — required fields changed, 8 properties removed, `status` enum changed.
- [ ] Note recorded that `1.0.0` marks **first canonical ratification**, not a claim of external API stability.

---

## 4. Control boundary — read before signing

`PROCESS-CONTROLS-001` defines nine controls. **A complete control design is not a validated control system.**

| Status | Count | Controls |
| :--- | :--- | :--- |
| **Defined and exercised** | 3 | `C-5` retrieval reverification · `C-7` key-set baseline documented · `C-9` const discriminator tested (`B10`, `B11`) |
| **Defined, NOT exercised** | 6 | `C-1` checksum-change gate · `C-2` baseline snapshot · `C-3` append-only media writes · `C-4` mandatory supersession history · `C-6` register separation · `C-8` decision-linked extension |

**The six unexercised controls have no execution evidence.** They exist because no approved media has been promoted, superseded, or replaced since they were written — not because they have been tested. Ratification accepts them as **designed**, and accepts the residual risks `R-2` and `R-3` as **open until first execution**.

---

## 5. Decision

| Field | Value |
| :--- | :--- |
| Ratified version | ***pending — `0.3.0` or `1.0.0` per §3*** |
| Artifact SHA-256 | `cd6b0a462eb0211afeab955616901ebc3cc26a6f065a2ededd6def5ce74a2c96` |
| Decided by | ***pending — must be `human-creative-authority`*** |
| Decided date | ***pending*** |
| Rationale | ***pending*** |
| Accepted exceptions | ***pending — see §3*** |
| Residual risks accepted | `R-2` (immutability — process control only), `R-3` (content smuggling — review control only) |
| Baseline classification | ***pending — `BASELINE-CLASSIFICATION-001` must be signed first*** |

**On ratification:** the `-rc1` suffix is dropped from `schema_version`, a **patch** entry is appended to `version_history` recording this decision (no validation behaviour change), and `ratification_status.state` becomes `ratified` with the decision-maker and date filled in.

**Until then**, `schema_version` remains `0.3.0-rc1` and `ratification_status.state` remains `release-candidate`.
