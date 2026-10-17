# DISPOSITION RECORD 001 — Frame A (`shot-open-001`) Media Loss

**Record ID**: `DISPOSITION-001`
**Incident**: `INC-2026-10-17-001`
**Date**: `2026-10-17`
**Authority**: Human Creative Authority, *Authority Review 003*
**Executed by**: Production Architect

---

## 1. Disposition

**ACCEPT THE LOSS. REOPEN `shot-open-001` FOR CONTROLLED RE-PRODUCTION.**

The incident remains recorded as `INC-2026-10-17-001` and stays **OPEN** until formally closed by the Human Creative Authority. This record implements the disposition but does not itself close the incident; closure occurs when a replacement has been produced, verified, and approved, or when the Human Creative Authority closes it without replacement.

---

## 2. The distinction this record exists to preserve

| Fact | Status |
| :--- | :--- |
| `decision-009` — the original human approval of Frame A | **RETAINED as historical evidence.** The approval occurred. It is not rewritten, revoked, or implied never to have happened. |
| Recorded SHA-256 of the master (`a2524d1d…`) and crop (`34d3c436…`) | **RETAINED as an identity reference.** It identifies the expected file contents **if a matching copy is ever recovered**. |
| The approved pixels | **LOST.** Neither the approval nor the checksum restores them. |
| `shot-open-001` current production disposition | **REOPENED for controlled re-production.** |
| Any replacement image | **New candidate · new checksum · new verification · new approval.** |
| The previous approval | **Does not transfer.** Not automatically, and not by resemblance. |

---

## 3. Disposition register

| Record | Disposition |
| :--- | :--- |
| Original Frame A approval (`decision-009`) | **Retain as historical evidence** |
| Original master (`img-harlem-ext-001-open-001-master`) | **LOST — PRESERVATION INCIDENT** |
| Original crop (`img-harlem-ext-001-open-001-crop185`) | **LOST — PRESERVATION INCIDENT** |
| `INC-2026-10-17-001` | **Keep open until formally dispositioned** |
| `shot-open-001` | **Reopen for controlled re-production** |
| Replacement image | **New candidate, new checksum, new verification** |
| Previous approval | **Does not transfer automatically to the replacement** |

---

## 4. Standing rules for the replacement

1. **New identity.** The replacement receives a new stable asset ID in the `img-harlem-ext-001-open-001-*` family with a run suffix (e.g. `…-run-02-master`). It never reuses `img-harlem-ext-001-open-001-master`.
2. **New checksum.** Its SHA-256 is computed at generation and recorded. It is expected to differ from `a2524d1d…`; **if it matched, that would be evidence of recovery, not of re-production**, and would trigger the recovery procedure instead.
3. **New verification.** Gates A–F are re-run from zero against the replacement. No gate result carries over from the lost `run-01` frame.
4. **New approval.** Promotion to `APPROVED ASSET` requires a fresh Human Creative Authority decision. `decision-009` is cited as precedent and creative intent, **never as authority**.
5. **Creative intent preserved where possible.** The re-production reuses the recorded `run-01` prompt and parameters (`execution-report-001.md` §8.1) as the starting point, so the replacement serves the same dramatic function. See `verification/tests/TEST-DUST-C001-001/reproduction-spec-open-001.md`.
6. **Never presented as the original.** Every reference to the replacement states its run identifier. The lost master is cited as `img-harlem-ext-001-open-001-master` (`LOST`) in perpetuity.
7. **Preservation before approval.** Under `production/media-preservation-policy.md`, the replacement is deposited into `production/media/**` and its retrieval verified **before** it can be promoted. An asset is not production-ready because its metadata survives.
8. **Recovery supersedes replacement.** If a file matching `a2524d1d…` is ever produced, it is evaluated against this incident record under the recovery procedure. A verified recovery takes precedence over any replacement and does **not** require re-approval — it *is* the approved original.

---

## 5. Historical integrity

`decision-009` is **not** amended by this record. Its text in `canon/canon-decisions.md` continues to state that the `run-01` render was promoted to `APPROVED ASSET`. What changes is the **media state** attached to it, recorded as `storage_status: preservation-incident` in `production/media-preservation-register.yaml` and `production/asset-registry.yaml`.

A reader encountering `decision-009` must be able to see both that the approval happened **and** that the approved medium is gone. Both facts are true. Neither is softened.

---

## 6. Authorisation status of the re-production itself

**The re-production is NOT authorised by this record.** This record reopens the shot and specifies how a replacement must be handled; it does not authorise a generation run.

Generating the replacement requires a separate Human Creative Authority authorisation, and may reasonably wait behind the other items in the *Authority Review 003* work order — in particular the visual review of Frames B and C, which is not improved by additional generation.
EOF
