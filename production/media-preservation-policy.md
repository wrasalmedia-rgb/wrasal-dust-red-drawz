# Media Preservation Policy — WRASAL DUST: THE RED DRAWZ (Case 001)

**Status**: `ACTIVE` — proposed by the Production Architect, adopted by Human Creative Authority `2026-10-17`
**Supersedes**: the implicit assumption, present in `ARENA EXECUTION REPORT 001`, that recording an approval or a checksum is equivalent to preserving the medium.
**Governing rule**: *An image is not preserved merely because its approval is recorded, and an approval is not established merely because an image passes a numerical test.*

---

## 1. Why this policy exists

`TEST-DUST-C001-001` generated six PNG frames. All six were absent from the workspace at the start of a later turn. The repository `.gitignore` excludes `*.png`, so generated media was dropped from workspace snapshots. Frame A (`shot-open-001`) had already been promoted to `APPROVED ASSET` at that point.

**The consequence is the point of this policy:** a checksum establishes *file identity* when a matching file is later produced. It does not reconstruct the image, and it does not constitute preservation. The `APPROVED ASSET` record for `shot-open-001` survived. The approved pixels did not.

---

## 2. Retention requirements by media status

| Media status | Required preservation |
| :--- | :--- |
| **Generated candidate** | Preserve the original until its review **and** all dependent tests are complete. |
| **Tested, awaiting review** | Preserve the **exact** tested image together with its verification records. |
| **Approved asset** | Preserve the approved **master** and **every approved derivative** (crops, reframes, deliverable formats). |
| **Superseded asset** | Retain its identity and history. **Do not silently overwrite it.** |

A medium that cannot be produced on demand from the designated store does not meet its row.

---

## 3. Storage backend

### 3.1 Preferred: Git LFS

Use Git LFS for production images **only if** LFS configuration, storage, and access have each been positively verified.

### 3.2 Verification status (tested `2026-10-17`, not assumed)

| Check | Command | Result | Verdict |
| :--- | :--- | :--- | :--- |
| LFS client installed | `git lfs version` | `git: 'lfs' is not a git command` | **FAIL** |
| LFS client installable | `apt-get install -y git-lfs` | `E: Could not open lock file … (13: Permission denied)` — not root | **FAIL** |
| LFS tracking configured | `ls .gitattributes` | No such file | **FAIL** |
| LFS batch endpoint reachable | `POST https://github.com/wrasalmedia-rgb/wrasal-dust-red-drawz.git/info/lfs/objects/batch` | `HTTP 422` (endpoint responds) | partial |
| LFS **storage** hosts reachable | `media.githubusercontent.com`, `cloud.githubusercontent.com`, `objects.githubusercontent.com` | `HTTP 000` on all three — blocked | **FAIL** |
| Egress control (network filter is host-scoped, not an outage) | `pip download six` from `pypi.org`; `api.github.com` | success / `HTTP 200` | control OK |

**Conclusion: Git LFS is NOT VERIFIED and cannot be verified in this environment.** The batch endpoint answers, but the object-storage hosts that actually transfer LFS payloads are firewalled. Git LFS therefore **must not** be treated as the preservation backend until re-tested in an environment with LFS installed and unrestricted egress.

### 3.3 Active fallback: designated durable artifact store

Because LFS is unverified, preservation uses an explicitly designated store inside the repository working tree:

| Store | Path | Holds |
| :--- | :--- | :--- |
| Approved-asset store | `production/media/**` | APPROVED ASSET masters and every approved derivative |
| Test-bench store | `verification/tests/**` | Generated candidates, tested frames, and their derivatives |

Mechanically, both trees carry `.gitignore` negations so the blanket `*.png` exclusion does not cover them. Verified `2026-10-17` with `git check-ignore -v`: media inside both trees reports **not ignored**; scratch media outside them (`scratch/throwaway.png`) still reports ignored by `.gitignore:4:*.png`. The exception is narrow and the blanket rule is intact everywhere else.

**Retrieval reference format** for every preserved medium:

```
repo-relative path  +  SHA-256  +  byte length  +  pixel dimensions
```

All four are recorded in `production/media-preservation-register.yaml`. Path alone is not a retrieval reference; checksum alone is not preservation.

---

## 4. Required metadata for every preserved image

Every entry in the preservation register must carry all eight fields. An entry missing any field is incomplete and does not satisfy §2.

| # | Field | Purpose |
| :--- | :--- | :--- |
| 1 | Stable asset ID | Independent identity for the master and for each derivative |
| 2 | Exact file path or durable URI | Retrieval |
| 3 | SHA-256 checksum | Identity verification on retrieval |
| 4 | Dimensions and file format | Integrity and rendering check |
| 5 | Generation prompt version and run metadata | Provenance of the render |
| 6 | Source / reference image IDs | Provenance of conditioned passes |
| 7 | Verification record and human decision | Governance linkage |
| 8 | Derivative relationship (master → crop → …) | Provenance of transformation |

Plus the field this policy adds on top of the eight:

| 9 | `storage_status` | `preserved-retrievable` \| `recorded-only` \| `preservation-incident` |

**Field 9 is what keeps an approval record from implying availability.** A record may be fully approved and still read `recorded-only` or `preservation-incident`. Approval and preservation are independent facts and are never inferred from one another.

---

## 5. Recovery procedure for medium that is missing

1. **Locate** the original from the workspace, an export, or another surviving source.
2. **Recalculate** the checksum and **compare** it with the recorded value.
3. **Restore** the exact file to durable storage.
4. **Verify** that the restored file can be retrieved in a fresh session.
5. If it cannot be recovered, **record a preservation incident**. **Do not regenerate a visually similar replacement and call it the original approved asset.**

A regenerated image is a *new* medium with a *new* identity. It requires its own asset ID, its own verification record, and its own human approval. It never inherits the approval of the medium it resembles.

---

## 6. Status of this policy

- Adopted: `2026-10-17`
- Backend: **fallback (§3.3)** — LFS unverified
- Blocker status: media preservation is a **production blocker** until every `APPROVED ASSET` medium reads `preserved-retrievable`
- Open: `INC-2026-10-17-001` — Frame A master and crop unrecoverable (see `verification/tests/TEST-DUST-C001-001/preservation-incident-001.md`)
