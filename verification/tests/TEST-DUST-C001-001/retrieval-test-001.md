# FRESH-SESSION RETRIEVAL TEST — `RETRIEVAL-TEST-001`

**Executed**: first action of the session following the one that provisioned the store
**Store under test**: fallback durable artifact store (`production/media/**`, `verification/tests/**`)
**Policy**: `production/media-preservation-policy.md` §3.3
**Purpose**: establish that the provisioned store is *operational*, not merely *provisioned*

---

## 1. Test conditions

The test is only meaningful across a session boundary. It was executed at the start of a **new** session, reading the register from disk and resolving every declared path independently — with no reliance on in-memory state from the session that created the files.

## 2. Required assertions

| # | Assertion | Result |
| :--- | :--- | :--- |
| 1 | The registered files exist at their declared locations | **PASS** |
| 2 | Their checksums match the preservation register | **PASS** |
| 3 | The files can be opened and their dimensions verified | **PASS** |
| 4 | A fresh session can retrieve them without relying on the previous workspace state | **PASS** |
| 5 | The register accurately distinguishes stored, checksum-verified, and retrievable | **PASS** |

## 3. Evidence

```
asset_id                                     declared   exists   sha_ok   dims_ok
img-harlem-ext-001-open-001-master           False      False    -        -
img-harlem-ext-001-open-001-crop185          False      False    -        -
img-red-drawz-001-open-003-run-01            False      False    -        -
img-red-drawz-001-open-003-run-02            True       True     True     True
img-red-drawz-001-open-004-run-01            False      False    -        -
img-red-drawz-001-open-004-run-02            True       True     True     True

Declared present: 2
T1 exist: True
T2 checksum: True
T3 openable+dims: True
T5 declared-absent are indeed absent: True
```

Verified values:

| Asset ID | Path | SHA-256 | Dimensions |
| :--- | :--- | :--- | :--- |
| `img-red-drawz-001-open-003-run-02` | `verification/tests/TEST-DUST-C001-001/frame-b-shot-open-003-run-02.png` | `ca0ac612e0d00be0ad55f7ff35d37d1d37b078b3097ed3f7c94cdaf5cbcd4cbf` | `1402x1122` |
| `img-red-drawz-001-open-004-run-02` | `verification/tests/TEST-DUST-C001-001/frame-c-shot-open-004-run-02.png` | `e8bee9b5d10b69d8ffd78d1b41802738b0deb60a43660bf5b5dcdfa90a8434cb` | `1152x922` |

## 4. Interpretation

**The fallback store is validated for the two media it currently holds.** The `.gitignore` negations are doing the work attributed to them: media inside `verification/tests/**` survived a session boundary, whereas all four `run-01` frames — created before the negations existed — did not.

This is a **narrow** pass and must not be over-read:

- It validates **2 of 6** registered media. The other 4 are absent and are covered by `INC-2026-10-17-001`.
- It validates the **test-bench** tree (`verification/tests/**`). The **approved-asset** tree (`production/media/**`) is currently empty — no `APPROVED ASSET` medium has yet been deposited into it, so that half of the store is **untested**.
- It validates survival across **one** boundary. Longer-horizon durability is unproven.
- It does not test retrieval of **externally stored** media (`durable_uri` path), because no medium currently uses that branch.

## 5. Status

| Item | Status |
| :--- | :--- |
| Fallback store — test-bench tree | **VALIDATED** (2/2 media, one boundary) |
| Fallback store — approved-asset tree | **UNTESTED** (tree empty) |
| External-storage retrieval branch | **UNTESTED** (no medium uses `durable_uri`) |
| Git LFS | **NOT VERIFIED** — unchanged from `media-preservation-policy.md` §3.2 |

The storage arrangement moves from *provisioned* to *provisionally validated for the media it holds*. It is **not** declared fully operational: an approved asset has still never been deposited into `production/media/**` and retrieved. That test cannot be run until `shot-open-001` is re-produced under the Frame A disposition.
