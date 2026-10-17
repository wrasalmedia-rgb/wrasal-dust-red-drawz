# VISUAL ASSESSMENT 001 — Frame B / Frame C, run-02

**Instrument ID**: `visual-assessment-001`
**Prepared**: `2026-10-17` by Production Architect
**Revised**: `2026-10-17` — four-element structure adopted; `VA-001-C2` and `VA-001-C4` corrected after investigation
**To be completed by**: Human Creative Authority
**Status**: **BLANK — awaits human visual inspection**

> **Nothing in this document approves anything.** Frames B and C remain
> `TESTED — AWAITING HUMAN REVIEW` until every assessment below carries a recorded verdict.
> **A blank field is not a pass.**
>
> **The Production Architect cannot complete this instrument.** It has no vision capability and has
> never seen either frame. If it were to fill these in, every entry would be `CANNOT TELL`, which
> would be honest but would advance nothing. **These assessments require the human reviewer.**

Each assessment carries four elements, kept distinct:

1. **Criterion** — what must be true
2. **Evidence** — what can be measured or directly observed
3. **Assessment** — PASS / FAIL / NEEDS REVISION / **CANNOT TELL**
4. **Authority** — who assessed, and who authorised the resulting state change

---

## 0. Assets under assessment — retrieve these

| Asset ID | File | Dimensions | SHA-256 |
|:--|:--|:--|:--|
| `img-red-drawz-001-open-003-run-02` | `verification/tests/TEST-DUST-C001-001/frame-b-shot-open-003-run-02.png` | 1402×1122 | `ca0ac612e0d00be0ad55f7ff35d37d1d37b078b3097ed3f7c94cdaf5cbcd4cbf` |
| `img-red-drawz-001-open-004-run-02` | `verification/tests/TEST-DUST-C001-001/frame-c-shot-open-004-run-02.png` | 1152×922 | `e8bee9b5d10b69d8ffd78d1b41802738b0deb60a43660bf5b5dcdfa90a8434cb` |

☐ Checksums verified before assessing — confirm you are looking at the asset of record.

---

## ⚠ 0a. Standing distinction — prompt specification is not visual evidence

**A prompt specifying zero branding is not evidence that the generated image contains zero branding.**

The existing acceptance records contain these assertions:

- Frame C Gate C: *"zero logos, zero text, zero tags"*
- Frame B Gate F and Frame C Gate F: *"No branding … introduced"*

These were entered on the basis of **what the generation prompt specified**. They are **not** findings
about the rendered pixels — the Production Architect has no vision capability and has never seen
either frame. That distinction is recorded in the source records (`verification-records.json`, run-02
entries) and is repeated here so it cannot be lost.

Assessments **B3** and **C1** exist to convert those prompt claims into verified findings — or to
falsify them. If either fails, the corresponding Gate F entry requires correction by the authority.

---

# FRAME B — `img-red-drawz-001-open-003-run-02`

## VA-001-B1 — Drawer extension ≈ 4.5 inches

**1. Criterion** — The drawer opening must read as approximately 4.5 inches.
Source: `spatial-drawer-extension-check` — *"~4.5 in target not measurable by pixel statistics"*.

**2. Evidence** — **None available.** This quantity is explicitly outside machine verification.
No measurement was taken and none can be.

**3. Assessment** — ☐ PASS  ☐ FAIL  ☐ NEEDS REVISION  ☐ **CANNOT TELL**
Notes: ______________________________________________

**4. Authority** — Assessed by: ________  ·  State change authorised by: ________

---

## VA-001-B2 — Bare walnut inner drawer wall; no bed quilt, full frame

**1. Criterion** — Gate E: bare walnut inner wall present; no bed quilt or patterned bedding anywhere in frame.

**2. Evidence** — Measured on **sampled regions only**:
- lower-left quadrant mean RGB `[38.48, 19.91, 7.06]`, all tiles in the dark-wood/shadow band
- walnut R/G `2.268` (B7), matching bare-walnut controls B8 `2.180` / B9 `2.156` within `0.112`

**Genuinely open:** sampling covers part of the frame. Whether the wall reads as bare walnut
**everywhere**, and whether any bedding appears outside the sampled quadrant, needs eyes.

**3. Assessment** — ☐ PASS  ☐ FAIL  ☐ NEEDS REVISION  ☐ CANNOT TELL
Notes: ______________________________________________

**4. Authority** — Assessed by: ________  ·  State change authorised by: ________

---

## VA-001-B3 — Garment is unbranded  *(see §0a)*

**1. Criterion** — `decision-008` (H-05): unbranded, plain matte crimson/oxblood heavyweight cotton.

**2. Evidence** — Chromaticity only: garment R/G `4.706–4.974` (≥ 2.2), R/B `4.191–4.396` (≥ 2.5).
**Chromaticity cannot detect a logo.** The branding claim in the record rests on the prompt, not on
inspection.

**Genuinely open:** whether any logo, tag, waistband print, or text is present.

**3. Assessment** — ☐ PASS  ☐ FAIL  ☐ NEEDS REVISION  ☐ CANNOT TELL
Notes: ______________________________________________

**4. Authority** — Assessed by: ________  ·  State change authorised by: ________

---

# FRAME C — `img-red-drawz-001-open-004-run-02`

## VA-001-C1 — Garment is unbranded  *(see §0a)*

**1. Criterion** — Gate C: *"zero logos, zero text, zero tags"*.

**2. Evidence** — Region std `15.18–25.43` confirms **resolved texture rather than a flat wash**.
This measures **texture variance, not absence of branding.** The branding claim rests on the prompt.

**Genuinely open:** whether any logo, tag, or text is present in the macro view.

**3. Assessment** — ☐ PASS  ☐ FAIL  ☐ NEEDS REVISION  ☐ CANNOT TELL
Notes: ______________________________________________

**4. Authority** — Assessed by: ________  ·  State change authorised by: ________

---

## VA-001-C2 — Material reads as the same garment as Frame B  ⚠ INVESTIGATED 2026-10-17

**1. Criterion** — Gate C: the macro view must read as the **same garment** as Frame B — matching
dye chromaticity, weave, and stitching.

**2. Evidence** — Investigation findings; the original `PASS WITH NOTE` is **not currently supportable**:

| Check | Finding |
|:--|:--|
| Arithmetic reproduces? | **Yes.** B2→C2 per-channel delta `[6.96, 4.47, 4.83]`, max `6.96`; R/G shift `4.756 → 3.993` = `−0.763`. Both match the record exactly. |
| One bad probe, or systematic? | **Systematic.** Every Frame C garment sample (C1 `3.885`, C2 `3.993`, C3 `4.143`, C4 `4.318`) sits below every Frame B sample (B1 `4.706`, B2 `4.756`, B3 `4.974`). Mean gap `−0.727` (−15.1%). |
| Explained by exposure/illumination? | **No.** The authoritative neutral liner moved only `1.159 → 1.123` = **−3.1%**, while the garment moved **−16.0%**. A global exposure difference would move both. The chromaticity difference is real. |
| Equivalent regions and method? | **Not strictly.** C2 is `115×73` (8,395 px, std `21.43`) vs B2 `84×56` (4,704 px, std `6.56`) — **1.78× the area, 3.27× the variance** — and samples jersey wales rather than a fold core. Same tool and method; not the same target. |
| Threshold established before the result? | **No threshold exists.** The calibrated heuristics are `R/G ≥ 2.2`, `R/B ≥ 2.5`, neutral `R/G ≤ 1.35`, wood `|Δ(R/G)| ≤ 0.15`. **A cross-shot 8-bit chromaticity delta is not among them.** The "< 2 units" cited as comparison was run-01's *observation*, never a ratified criterion. |

> **Consequence.** The difference is real and systematic, and is **not** an illumination artifact.
> But there is **no threshold to assess it against**, and the compared regions are not equivalent, so
> the magnitude `6.96` is not a clean measurement. Per the authority's instruction — *do not silently
> relax the threshold* — the existing `PASS WITH NOTE` is **withdrawn pending decision**. The
> authority must either (a) establish a threshold and re-assess, or (b) record this as unassessable
> and rely on visual judgment. **The numerical difference alone does not establish a visual
> continuity failure, and must not be treated as one.**

**3. Assessment** — ☐ PASS  ☐ FAIL  ☐ NEEDS REVISION  ☐ CANNOT TELL
☐ Threshold decision required before quantitative assessment is possible
Notes: ______________________________________________

**4. Authority** — Assessed by: ________  ·  State change authorised by: ________

---

## VA-001-C3 — Paper liner is neutral `#F3F0E9` across the whole frame

**1. Criterion** — Gate A / Gate B Track 1: neutral unbleached paper liner.

**2. Evidence** — Measured: liner R/G `1.123` (C7) and `1.150` (C6) — both ≤ 1.35.
Note: C6 has std `34.55`, indicating the probe **straddles the garment-to-liner transition**; C7 (std `6.30`) is the authoritative clean sample.

**Genuinely open:** whether the liner holds neutral across the full frame, or shows contamination outside the sampled regions.

**3. Assessment** — ☐ PASS  ☐ FAIL  ☐ NEEDS REVISION  ☐ CANNOT TELL
Notes: ______________________________________________

**4. Authority** — Assessed by: ________  ·  State change authorised by: ________

---

## VA-001-C4 — Bare walnut inner wall continues from Frame B  ⚠ INVESTIGATED 2026-10-17

**1. Criterion** — `cross-shot-drawer-wall-continuity`: `|Δ(R/G)| ≤ 0.15` per `decision-010`.

**2. Evidence** — **The choice of control determines pass or fail:**

| Comparison | Δ(R/G) | vs 0.15 |
|:--|:--|:--|
| C8 `2.029` vs **B9** `2.156` (occluded control — **as recorded**) | `0.127` | **PASS** |
| C8 `2.029` vs **B7** `2.268` (lit walnut, in garment's light path — alternative) | `0.239` | **EXCEEDS** |

The recorded comparison follows `decision-010` as written: *"a wood patch in the garment's lit
environment"* vs *"an occluded same-material wood control outside the garment's light/bounce path"*
— i.e. C8 vs B9. **The method is therefore compliant.** But the result is sensitive to control
selection, and the alternative reading fails by a wide margin. The authority should be aware that
this PASS depends on which convention is applied.

**Genuinely open:** whether the wall reads as continuous and unbroken to the eye.

**3. Assessment** — ☐ PASS  ☐ FAIL  ☐ NEEDS REVISION  ☐ CANNOT TELL
Notes: ______________________________________________

**4. Authority** — Assessed by: ________  ·  State change authorised by: ________

---

## Sign-off

| Field | Value |
|:--|:--|
| Assessed by | ____________________ (**must be `human-creative-authority`**) |
| Date | ____________________ |
| Master checksums verified before assessment | ☐ Yes  ☐ No |
| `VA-001-C2` threshold decision recorded | ☐ Yes  ☐ No  ☐ Deferred |
| Overall outcome | ☐ APPROVED  ☐ NEEDS REVISION  ☐ REJECTED |
| Ratifying decision ID | ____________________ |

**Neither asset is approved until this table is complete.** Until then both remain
`TESTED — AWAITING HUMAN REVIEW`, and no promotion to `APPROVED ASSET` may be recorded.

---

## Assessment identifiers

`VA-001-B1`, `VA-001-B2`, `VA-001-B3`, `VA-001-C1`, `VA-001-C2`, `VA-001-C3`, `VA-001-C4`

**Why seven, not six:** branding must be assessed separately in each frame. Frame B and Frame C are
different images; a single branding verdict could not bind to both.

**Scope note.** The reported 35/35 schema checks establish only what those checks test. They do not
independently establish visual correctness, control effectiveness, or schema ratification.
