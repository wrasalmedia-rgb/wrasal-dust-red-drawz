# First Production Test Specification — `TEST-DUST-C001-001`

- **Test ID**: `TEST-DUST-C001-001` (Tracked in `production/asset-registry.yaml` as `verif-test-red-drawz-001`)
- **Title**: Harlem 3:17 AM Threshold & Material-Red Garment Continuity Calibration (3-Frame Micro-Packet + Gate-Blocked Character Identity Step)
- **Version**: `0.2.0`
- **Governance Status**:
  - **Phase 1 (Frames A, B, C — Environment & Material-Red Prop Continuity)**: `EXECUTED — PARTIALLY APPROVED` (`run-01` and `run-02` both executed `2026-10-17`; see `verification/tests/TEST-DUST-C001-001/execution-report-001.md`)
    - `shot-open-001` (Frame A, `run-01` + deterministic `1.85:1` crop): **`APPROVED ASSET`** (`decision-009`)
    - `shot-open-003` (Frame B, `run-02`): **`TESTED — AWAITING HUMAN REVIEW`**
    - `shot-open-004` (Frame C, `run-02`): **`TESTED — AWAITING HUMAN REVIEW`**
    - `prop-red-drawz-001` garment specification: **`CANON` / locked** (`decision-008`, Human Decision `H-05`)
    - Gate B heuristic: **calibrated** (`decision-010`) — see §3 Criterion 2
  - **Phase 2 (Frames D1, D2 — Wrasal & Grant Threshold Identity Continuity)**: `REFERENCE NEEDED` (**HARD BLOCKED** until approved Tier 00 `FACE_MASTER` / `BODY_MASTER` references for `char-wrasal-001` and `char-grant-001` are supplied)

---

## 1. Purpose & Design Rationale (Stage G)

In accordance with `REALITY FIRST. TECHNOLOGY SECOND.` and the WRASAL Cinema Engine principle (`Production decisions, not prompt piles`), we do **not** begin by generating a large batch of random images or guessing character faces.

Because Stage A discovery verified that **approved visual references for Wrasal (`char-wrasal-001`) and Mister Grant (`char-grant-001`) are currently inaccessible/missing** (`REFERENCE NEEDED`), any immediate attempt to generate their faces would violate `decision-002` and `decision-003` by inventing unapproved character appearances.

Therefore, `TEST-DUST-C001-001` is structured as a **two-phase gated production test**:
- **Phase 1 (Executable Immediately Upon Human Authorization — 3 Still Frames)**: Tests spatial plausibility (Harlem 2026 at 3:17 AM), lighting consistency (`WRASAL_LIGHTING_GRAMMAR_v001: controlled_low_key`), shot faithfulness (`35mm` → `85mm` → `100mm macro`), material continuity (`prop-red-drawz-001`), and preservation of unresolved supernatural restraint (`decision-006`: materially red fabric under 2800K warm domestic light with **zero** red scene lighting wash).
- **Phase 2 (Hard-Blocked Gate — 2 Still Frames)**: Tests character identity consistency (`char-wrasal-001` and `char-grant-001`) and wardrobe continuity (`wardrobe-wrasal-001`, `wardrobe-grant-001`) across `shot-open-005` and `shot-open-006` **only after** the human creative authority shares or approves Tier 00 character references.

---

## 2. Test Matrix (Frames Under Test)

### Phase 1 — Environment, Lighting & Material-Red Continuity (`READY FOR TEST`)

| Test Frame | Target Shot ID | Prompt ID | Lens / Aperture | Subject & Framing | Core Hypothesis Tested |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Frame A** | `shot-open-001` | `prompt-img-open-001` | `35mm` · `f/5.6` | Harlem brownstone stoop & vestibule threshold at 3:17 AM (no characters). | Can the pipeline render an unmistakably authentic 2026 Harlem nocturnal exterior (masonry, ironwork, damp asphalt, 4200K streetlamp + 2900K vestibule bulb) with zero cyberpunk neon or Jamaican flora drift? |
| **Frame B** | `shot-open-003` | `prompt-img-open-003` | `85mm` · `f/4` | High 3/4 medium close-up of walnut drawer open 4.5 inches inside `loc-grant-residence-001`, revealing folded `prop-red-drawz-001` on neutral paper liner. | Can the generator render a deeply saturated crimson/oxblood garment under a 2800K tungsten practical lamp **without** bleeding red light onto the surrounding walnut wood, neutral liner paper, or wall shadow? |
| **Frame C** | `shot-open-004` | `prompt-img-open-004` | `100mm Macro` · `f/11` | Forensic macro insert of `prop-red-drawz-001` inside the same drawer from Frame B (raking 2800K key from camera-left). | Does the red garment preserve identical fabric weave, seam construction, fold geometry, and dye chromaticity when moving from an `85mm` medium-close insert (Frame B) to a `100mm` macro insert (Frame C)? |

### Phase 2 — Character Identity & Wardrobe Continuity (`REFERENCE NEEDED — BLOCKED`)

| Test Frame | Target Shot ID | Prompt ID | Blocker Dependency | Core Hypothesis Tested Once Unblocked |
| :--- | :--- | :--- | :--- | :--- |
| **Frame D1** | `shot-open-005` | `prompt-img-open-005` | `char-wrasal-001` (`FACE_MASTER` / `BODY_MASTER`) + `wardrobe-wrasal-001` | Does Wrasal maintain 100% facial bone-structure, skin-tone, and wardrobe fidelity at the Harlem vestibule threshold (`85mm f/2.8`) under mixed 2900K/4200K lighting without drifting into generic occult investigator clichés? |
| **Frame D2** | `shot-open-006` | `prompt-img-open-006` | `char-wrasal-001` + `char-grant-001` (`FACE_MASTER` / `BODY_MASTER`) + `wardrobe-grant-001` | Do both Wrasal and Mister Grant preserve individual identity lock, relative height/scale, wardrobe continuity, and non-theatrical bereavement restraint in a shared `35mm f/5.6` interior two-shot with `prop-red-drawz-001` in background depth? |

---

## 3. Six Measurable Acceptance Criteria

Every generated candidate in `TEST-DUST-C001-001` must be scored against all six required dimensions and logged using `schemas/verification.schema.json`. Any score of `FAIL` on a dimension blocks promotion and marks the candidate `NEEDS REVISION`.

### Criterion 1 — Character Identity Consistency (`identity_pass`)
- **Phase 1 Rule**: Zero unapproved human faces or silhouettes may appear in Frames A, B, or C (`PASS` = 0 unapproved faces rendered).
- **Phase 2 Rule (Once Tier 00 References Supplied)**:
  - Facial geometry, interpupillary proportion, nasal bridge, jawline, skin tone under local kelvin light, hair pattern, and apparent age in Frames D1 and D2 must match the approved Tier 00 `FACE_MASTER` for `char-wrasal-001` and `char-grant-001` with zero observer divergence across 3 independent human visual checks.
  - Zero occupational costume inventions for Mister Grant; zero occult-detective costume clichés for Wrasal.

### Criterion 2 — Material & Wardrobe Continuity (`material_pass`)
- **Chromatic Isolation Metric (Material Red vs. Scene Light)**:
  - In Frames B and C, `prop-red-drawz-001` must exhibit high red-channel dominance (`R / G >= 2.2` and `R / B >= 2.5` on sunlit/lamp-lit fabric folds) attributable solely to textile dye.
  - Simultaneously, adjacent **neutral achromatic** surfaces (unbleached drawer liner paper, plaster wall, unpainted cloth > 5 cm from the garment) must remain neutral/warm tungsten (`R / G <= 1.35`), proving **zero global red lighting wash**.
  - **Calibrated two-track Gate B heuristic (updated `2026-10-17`)**: The absolute `R / G <= 1.35` ceiling applies **only to neutral achromatic reference surfaces**. Dark wood (American walnut dresser/drawer stock) is **exempt** from that absolute ceiling and is instead evaluated by the **occluded wood control delta**: `|Δ(R/G)| <= 0.15` between (a) a wood patch in the garment's lit environment and (b) an occluded wood control patch of the same material outside the garment's light/bounce path.
    - *Evidence basis (`run-01`)*: Frame B walnut measured `R/G = 1.654–2.603`; the occluded upper-drawer control (`B9`) measured `R/G = 2.603`, higher than lit surfaces — intrinsic walnut pigment under `2800K`, not red spill. Applying the uncalibrated `1.35` ceiling to wood produced a false Gate B failure.
    - *Evidence basis (`run-02`)*: Frame B lit walnut `R/G = 2.268` (`B7`), upper-drawer control `2.180` (`B8`), occluded shadow control `2.156` (`B9`) → max `|Δ(R/G)| = 0.112 <= 0.15`, **PASS**. Frame C walnut `R/G = 2.029` (`C8`) → cross-frame delta vs Frame B occluded control `|0.127| <= 0.15`, **PASS**.
    - *Reporting rule*: Every frame containing both neutral surfaces and wood must report **both** Track 1 (`R/G <= 1.35` on neutral achromatic) and Track 2 (`|Δ(R/G)| <= 0.15` on wood). Neither alone clears Gate B.
- **Cross-Shot Textile Lock**:
  - Fabric weave type (matte knitted cotton/wool vs. synthetic satin), flatlock seam width, and oxblood/crimson dye value must match between Frame B (`85mm`) and Frame C (`100mm macro`).
  - **Metadata Strip Test (`CONCEPT-0007`)**: When viewed without caption or prompt text, an observer must identify `prop-red-drawz-001` as a physical, manufactured red garment resting in a normal domestic drawer — not a glowing talisman, bloodstain, or abstract red cloth.

### Criterion 3 — Spatial Plausibility (`continuity_pass` — Spatial)
- **Harlem 2026 Architectural Verifiability**:
  - Frame A must exhibit authentic Harlem brownstone masonry, stoop tread proportions (standard ~11-inch tread depth, ~7.5-inch riser), painted iron balustrade geometry, and NYC vestibule door proportions.
  - Zero tropical flora, palm/banana leaves, rural verandas, or non-NYC architectural motifs (`decision-001`).
- **Drawer & Container Geometry Lock**:
  - Between Frame B and Frame C, the drawer opening width (~4.5 inches), wood grain direction, and garment placement relative to the drawer corner must remain spatially consistent.

### Criterion 4 — Lighting Consistency (`lighting_pass`)
- **Motivated Source Direction & Kelvin Fidelity**:
  - Frame A: Dual-source motivation (4200K overhead streetlamp + 2900K recessed vestibule bulb); shadow vectors on stoop steps align with overhead lamp position; sky/shadow areas hold deep low-key black (`#0A0A0C` to `#25262A` range) without crushed mud or HDR haloing.
  - Frames B & C: Single 2800K warm domestic tungsten lamp from camera-left (`45°` azimuth, `35°` elevation) with natural inverse-square falloff into the rear right corner of the drawer. Light direction vector between Frame B and Frame C must match within `±10°`.

### Criterion 5 — Shot Faithfulness (`continuity_pass` — Optical)
- **Lens-to-Perspective Fidelity (`WRASAL_CAMERA_GRAMMAR_v001`)**:
  - Frame A (`35mm f/5.6`): True vertical architectural lines (zero barrel/fisheye distortion); deep spatial focus from foreground iron railing to vestibule door.
  - Frame B (`85mm f/4`): Compressed medium close-up at 45° downward eye-line; crisp focus on front drawer edge and primary garment fold, smooth optical falloff on background floor.
  - Frame C (`100mm Macro f/11`): Close measured station at 30° raking angle; resolved individual fiber twist and stitch holes across the focal plane with natural macro depth-of-field falloff.

### Criterion 6 — Preservation of Unresolved Supernatural Details (`continuity_pass` — Ontological & Cultural)
- **Zero Premature Explanation or Horror Cliché**:
  - Frames A, B, and C must contain **zero** supernatural VFX (no glowing runes, smoke tendrils, floating dust sigils, spectral silhouettes in windows, or blood drips).
  - Frame B and Frame C must contain **zero** borrowed real-world Afro-Caribbean or Jamaican sacred objects, candles, chalk diagrams, or altar arrangements (`decision-006`, `decision-007`). The uncanny tension must arise purely from architectural silence and the unexplained material presence of the red garment in a widower's home.

---

## 4. Execution Protocol & Logging Template

1. **Pre-Flight Check**: Confirm human creative authority approves running Phase 1 (`shot-open-001`, `shot-open-003`, `shot-open-004`) and confirm whether `prop-red-drawz-001` should use a specific garment construction reference (e.g., oxblood trunk vs. other red undergarment cut).
2. **Controlled Run**: Generate 1 candidate per shot (3 frames total for Phase 1) using `prompts/master-shot-template.md`.
3. **S3 Audit & Logging**: Score each output against Criteria 1–6 and record the run in `verification/generation-log-template.yaml` format.
4. **Human Review (`S5 / Authorize`)**: Present all 3 candidates and their verification scores to the human creative authority before any motion test or additional scene generation.
