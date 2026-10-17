# RE-PRODUCTION SPECIFICATION — `shot-open-001` (Frame A replacement)

**Status**: `AWAITING AUTHORISATION` — **no generation run has been executed**
**Authorised by**: *pending Human Creative Authority*
**Created**: `2026-10-17` under `DISPOSITION-001`
**Governing constraint**: the replacement is a **new candidate**. `decision-009` is precedent and creative intent, **not authority**.

---

## 1. Why this document exists

`DISPOSITION-001` reopened `shot-open-001` after the loss of the approved `run-01` media (`INC-2026-10-17-001`). This specification fixes the replacement's inputs in advance so that, when authorised, the run is reproducible and auditable rather than improvised.

**Nothing here authorises generation.** Reopening a shot and specifying its inputs are separate acts from executing a run.

---

## 2. Source of creative intent

| Input | Value |
| :--- | :--- |
| Shot ID | `shot-open-001` |
| Prompt ID | `prompt-img-open-001` |
| Location | `loc-harlem-ext-001` |
| Prior run | `run-01` — **LOST** (`img-harlem-ext-001-open-001-master`, `sha256 a2524d1d…`) |
| Recorded prompt | `verification/tests/TEST-DUST-C001-001/execution-report-001.md` §8.1 (Frame A, `run-01`) |
| Recorded parameters | `generate_image`, `offer_options: false`, `images: omitted` |
| Recorded output | `1403 × 1121`, `PNG`, `sRGB` |
| Shot specification | `prompts/location-prompts/prompt-img-open-001.md` |
| Shotlist entry | `shotlists/case-001.yaml` → `shot-open-001` |

The `run-01` prompt text is reproduced verbatim in `execution-report-001.md` §8.1 and is the **starting point** for the replacement. Preserving the approved creative intent means reusing that prompt unless the Human Creative Authority directs a change.

---

## 3. OPEN DECISION — Faithful reproduction vs. controlled revision

`run-01` Frame A passed all applicable gates but carried one recorded cosmetic defect:

> Minor optical tilt — a ~2–3° upward camera angle produces slight vertical convergence on the upper brownstone stories.

`shot-open-001` requires true vertical architectural lines, so the tilt is a genuine deviation from the shot specification. Correcting it, however, **changes the intended output** — and must not be silently folded into a run described as matching the original prompt.

**The Human Creative Authority must choose explicitly before any reproduction run is authorised:**

| Option | Definition | Consequence |
| :--- | :--- | :--- |
| **A — Faithful reproduction** | Reuse the `run-01` prompt and parameters verbatim. Preserve the original creative intent **including** the ~2–3° tilt. | The replacement is as close to the lost original as the generator permits. The known defect is reproduced deliberately and recorded as accepted. |
| **B — Controlled revision** | Adopt the proposed optical correction: add an explicit level-horizon / zero-convergence constraint to the prompt. | The replacement is *not* a faithful reproduction. It becomes a `run-02` revision with a documented prompt delta, and the delta must be recorded alongside the run. |

**Status: OPEN.** No choice has been recorded. Reproduction is **not authorised** under either option.

Whichever option is chosen, the resulting image remains a **new candidate with a new checksum requiring its own verification and approval** — the choice affects *what is generated*, not *how it is governed*.

---

## 4. Identity and naming for the replacement

| Field | Value |
| :--- | :--- |
| Master asset ID | `img-harlem-ext-001-open-001-run-02-master` |
| Derivative asset ID (`1.85:1`) | `img-harlem-ext-001-open-001-run-02-crop185` |
| Canonical path (master) | `production/media/case-001/shot-open-001/run-02/frame-a-shot-open-001-run-02-master.png` |
| Canonical path (crop) | `production/media/case-001/shot-open-001/run-02/frame-a-shot-open-001-run-02-crop-185.png` |
| Crop transformation | `convert <master> -crop <W>x758+0+130 +repage <out>`, width set from the new master's width |
| `lineage` (master) | `original` |
| `lineage` (crop) | `derivative` |
| Expected checksum | **unknown until generated** — must be recorded at generation time |

The lost assets keep their identities (`img-harlem-ext-001-open-001-master`, `…-crop185`) and their `preservation-incident` status. They are **not** overwritten or reused.

---

## 5. Mandatory sequence when authorised

1. **Generate** the master at `production/media/case-001/shot-open-001/run-02/` — deposit **directly into the durable store**, not into a scratch path.
2. **Record** SHA-256, byte length, and dimensions immediately.
3. **Verify** the checksum differs from `a2524d1d…`. If it matches, **stop** — that is a recovery event, and the recovery procedure takes precedence.
4. **Re-run Gates A–F** from zero. No gate result carries over from `run-01`.
5. **Generate** the deterministic `1.85:1` crop from the new master and register it as a derivative with explicit `derivative_of` and `transformation`.
6. **Execute** the fresh-session retrieval test on both files before any promotion.
7. **Present** both to the Human Creative Authority for visual review.
8. **Only on approval**, record a new decision (e.g. `decision-011`) granting `APPROVED ASSET` status, citing `decision-009` as precedent.

---

## 6. Standing prohibitions

- Do not describe the replacement as "Frame A restored", "the original", or "the approved plate".
- Do not reuse `decision-009` as the approval authority for the replacement.
- Do not deposit the replacement outside `production/media/**`.
- Do not promote it before the retrieval test passes.
- Do not generate it before the Human Creative Authority authorises the run.
