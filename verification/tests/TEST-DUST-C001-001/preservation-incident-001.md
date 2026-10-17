# PRESERVATION INCIDENT — `INC-2026-10-17-001`

**Status**: `OPEN` · **Severity**: `production-blocker`
**Opened**: `2026-10-17` · **Opened by**: Production Architect
**Policy**: `production/media-preservation-policy.md` §5 (Recovery procedure)
**Disposition**: awaiting Human Creative Authority

---

## 1. Summary

Four production media files generated during `TEST-DUST-C001-001` are **absent from the workspace and from every recoverable location**. Two of them are `APPROVED ASSET` media for `shot-open-001` / `loc-harlem-ext-001`. Their approval records and SHA-256 checksums survive; the pixels do not.

This incident is the concrete demonstration of the governing rule: **an image is not preserved merely because its approval is recorded.**

## 2. Affected media

| Stable asset ID | Shot / Run | Delivery status | Recorded SHA-256 | Pixels |
| :--- | :--- | :--- | :--- | :--- |
| `img-harlem-ext-001-open-001-master` | `shot-open-001` / `run-01` | `APPROVED ASSET` | `a2524d1d71f0a4c7931dc237f7a104f128714864d404c102b87653e719d6204e` | **ABSENT** |
| `img-harlem-ext-001-open-001-crop185` | `shot-open-001` / `run-01` | `APPROVED ASSET` | `34d3c436fb6221ed6e87a374dce0e06fc7af8de670110f7d462bced6c36af327` | **ABSENT** |
| `img-red-drawz-001-open-003-run-01` | `shot-open-003` / `run-01` | `NEEDS REVISION` | `2887994cbcc18ccd9ce38d8be5e80c31e2abcc562129a4ddf3eaf40b9181f419` | **ABSENT** |
| `img-red-drawz-001-open-004-run-01` | `shot-open-004` / `run-01` | `NEEDS REVISION` | `58fd3d34555ba6eace28b9475cfb2698a03fb4d9d691082cd60caa98bceeb619` | **ABSENT** |

Unaffected (present and checksum-verified): `img-red-drawz-001-open-003-run-02`, `img-red-drawz-001-open-004-run-02`.

## 3. Cause

The repository `.gitignore` carries blanket binary exclusions (`*.png`, `*.jpg`, …) under the heading *"Ignore generated and unapproved material"*. Generated media therefore matched the ignore set and was dropped when the workspace was snapshotted between sessions. No durable storage destination existed as a fallback.

This was reported as Open Item `OI-02` in `ARENA EXECUTION REPORT 001` and has now been escalated to a formal incident at the direction of the Human Creative Authority.

## 4. Recovery procedure — executed step by step

Per `production/media-preservation-policy.md` §5:

### Step 1 — Locate the original from the workspace, an export, or another surviving source — **FAILED**

Searches executed `2026-10-17`:

| Search | Scope | Result |
| :--- | :--- | :--- |
| `find /home/user -name '*.png'` | entire workspace | 2 files, both `run-02`; zero `run-01` files |
| `find / -name 'frame-a-shot-open-001*'` | whole filesystem (`-xdev` safe, `/proc` and `/sys` excluded) | **no matches** |
| `find / -name 'frame-b-shot-open-003*'` | whole filesystem | 1 match — the `run-02` file only |
| `find / -name 'frame-c-shot-open-004*'` | whole filesystem | 1 match — the `run-02` file only |
| `find / -name '*run-01*.png'` | whole filesystem | **no matches** |
| `find / -name '*crop-185*'` | whole filesystem | **no matches** |
| `find / -xdev -name '*.png' -size +500k` (excluding `/usr`, `/opt`) | whole filesystem | 2 files, both `run-02` |
| Git object store | `git log --all -- '*frame-a*'` | no commits touch these paths; they were never committed |

**No surviving copy, export, or cache exists anywhere on the filesystem.**

### Step 2 — Recalculate both checksums and compare with the recorded values — **NOT REACHABLE**

Cannot be performed: there is no file to hash. The recorded values are reproduced in §2 above and remain on file for future comparison **if** a matching file is ever produced.

### Step 3 — Restore the exact files to durable storage — **NOT REACHABLE**

Nothing to restore.

### Step 4 — Verify the restored files can be retrieved in a fresh session — **NOT REACHABLE**

### Step 5 — Record a preservation incident — **EXECUTED (this document)**

### Explicit prohibition

**No replacement has been generated, and none may be.** A regenerated Frame A is a *new* medium with a *new* identity. Per policy §5 it requires its own stable asset ID, its own verification record, and its own human approval, and it **never inherits** the `APPROVED ASSET` status of `img-harlem-ext-001-open-001-master`.

> The crop is the one partial exception in *kind* but not in *fact*: `img-harlem-ext-001-open-001-crop185` is a deterministic derivative (`convert -crop 1403x758+0+130 +repage`), so it is byte-for-byte regenerable **from its master**. Since the master is absent, this offers no recovery path. It is recorded so that, if the master is ever recovered, the crop can be reconstructed and verified against `34d3c436…`.

## 5. Remediation applied

| # | Action | Status |
| :--- | :--- | :--- |
| 1 | Adopted `production/media-preservation-policy.md` (retention table, backend verification, 9-field metadata requirement, recovery procedure) | **DONE** |
| 2 | Tested Git LFS rather than assuming it — client, installability, `.gitattributes`, batch endpoint, storage hosts | **DONE — LFS FAILED VERIFICATION** |
| 3 | Designated fallback durable store (`production/media/**`, `verification/tests/**`) with `.gitignore` negations | **DONE** |
| 4 | Verified the negations with `git check-ignore -v`, including a negative control (`scratch/throwaway.png` still ignored) | **DONE** |
| 5 | Created `production/media-preservation-register.yaml` with all 9 required fields per medium, plus `storage_status` | **DONE** |
| 6 | Re-verified SHA-256 of the two surviving `run-02` frames against their generation-time values | **DONE — both match** |
| 7 | Created `production/media/README.md` documenting layout and deposit rules | **DONE** |

**Retrieval test in a fresh session is the one remediation step that cannot be completed inside the turn that performs it.** It is scheduled as the first action of the next session: confirm `verification/tests/TEST-DUST-C001-001/frame-{b,c}-*-run-02.png` are present and that their SHA-256 values still match. Until that test passes, `storage_status` for those entries is provisional and this is recorded in the register's `blocker_state`.

## 6. Impact on governance

- `decision-009` (Frame A → `APPROVED ASSET`) remains a **valid human decision**. It is not revoked by this incident.
- What the incident changes is the **media state**, not the **approval state**: `img-harlem-ext-001-open-001-master` now reads `delivery_status: APPROVED ASSET` **and** `storage_status: preservation-incident` simultaneously. That combination is intentional and is exactly the distinction the policy exists to make.
- Media preservation is declared a **production blocker**. Per policy §6 it is not cleared until every `APPROVED ASSET` medium reads `preserved-retrievable`.

## 7. Disposition options for the Human Creative Authority

1. **Accept the loss** — `shot-open-001` is re-opened for a fresh generation run, producing a *new* medium requiring *new* approval. The `decision-009` approval of the lost master is marked `SUPERSEDED` with a link to this incident. *(Recommended if no external copy exists.)*
2. **Supply the files externally** — if the master and crop exist on the user's own machine, an export or another surviving source, upload them; the recovery procedure then proceeds from Step 2 and the recorded checksums are used to confirm they are the exact approved files.
3. **Re-test Git LFS in an unrestricted environment** — if the project intends LFS as the real backend, verify it outside this sandbox, migrate the store to LFS, and update the register's `storage_backend` block.

## 8. Audit note

This incident supersedes Open Item `OI-02` in `ARENA EXECUTION REPORT 001`. `OI-02` described the problem; `INC-2026-10-17-001` records the failed recovery and the remediation. The `OI-02` entry is retained in the report for traceability and now cross-references this document.
