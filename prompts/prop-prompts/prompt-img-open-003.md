# SHOT PROMPT SPECIFICATION: `shot-open-003`

## 1. Shot ID
- **Shot ID**: `shot-open-003`
- **Prompt ID & Version**: `prompt-img-open-003` · `v0.2.0`
- **Sequence / Scene / Beat**: Opening Sequence (Provisional) · Scene 01 · Beat 03 — Object Detail Before Explanation
- **Governance Status**: `TESTED — AWAITING HUMAN REVIEW` (Phase 1 of `TEST-DUST-C001-001`; `run-01` executed and retained as calibration evidence, `run-02` executed `2026-10-17` under Human Decision `execute_run_02_bc`)

## 2. Dramatic Intent
- **Narrative Question of the Frame**: Why is a neatly folded, materially red garment resting inside a quiet drawer in a recently widowed man's Harlem bedroom?
- **Dramatic Function**: Object detail before explanation; material restraint.
- **Audience Perception Target**: The viewer first notices the warm walnut drawer pulled open 4.5 inches; second, the unmistakable deep crimson/oxblood dyed fabric resting against neutral unbleached liner paper under ordinary domestic lamp light.

## 3. Canonical Story Constraints (Immutable Facts)
- **Setting & Temporal Lock (`CANON`)**: Interior of Mister Grant's Harlem, NYC, 2026 residence (`loc-grant-residence-001`, `decision-001`).
- **Character Biography & Role Locks (`CANON`)**: No human face or hands in frame (`characters_present: []`). Reflects the domestic space of an American widower married less than two years (`decision-002`).
- **Deliberately Unresolved Mysteries (`CANON`)**: The exact function and procedure of the red garments (`prop-red-drawz-001`) within the Nine-Day Threshold are unresolved (`decision-006`).
- **Cultural & Epistemic Boundary (`CANON`)**: Zero candles, chalk marks, sacred symbols, or fabricated ritual staging (`decision-006`, `decision-007`).

## 4. Visual Reference Inputs (Hard Dependencies)
- **Tier 00 Character Reference (`FACE_MASTER` / `BODY_MASTER`)**: None (`Object/Interior Insert Only`)
- **Approved Location Plate**: `loc-grant-residence-001` (`REFERENCE NEEDED`)
- **Approved Prop / Material Reference**: `prop-red-drawz-001` (`GARMENT SPEC LOCKED` — `decision-008` / Human Decision `H-05` resolved `2026-10-17`: unbranded, plain matte crimson/oxblood heavyweight cotton undergarment; unlinked from the commercial `STYLE 001 — Oxblood Trunk` project). Candidate renders remain `TESTED — AWAITING HUMAN REVIEW`.
- **Approved Wardrobe Reference**: None
- **Incoming Continuity Frame**: Matches downward eye-line and 2800K lamp vector from `shot-open-002`

## 5. Subject Description
- **[REQUIRED CONTENT — Hard Gate]**:
  - **Subjects Present**: `prop-red-drawz-001` (folded red undergarment) resting inside `prop-evidence-container-001` (partially opened wooden dresser drawer).
  - **Object Geometry**: Wooden dresser drawer pulled open 4.5 inches; inside the drawer, resting on flat unbleached off-white paper liner (`#F3F0E9`), lies a folded, heavyweight knitted cotton/merino red garment (`prop-red-drawz-001`).
- **[VISUAL INTERPRETATION — Proposed Blocking]**:
  - Framed from a measured 45-degree downward observational angle (matching a seated person's eye-line looking down at the drawer edge).

## 6. Wardrobe and Material Locks
- **[REQUIRED CONTENT — Hard Gate]**:
  - **Prop Material Lock (`prop-red-drawz-001`, `decision-006`)**: Deep crimson/oxblood dyed matte cotton-wool textile with visible knit grain, flatlock stitched seam, structured waistband edge, and natural gravity fold weight. **The redness is 100% intrinsic to the dyed fabric pigment — not a light source or color filter.**
  - **Garment Specification Lock (`decision-008` / `H-05`, `CANON` `2026-10-17`)**: Heavyweight cotton undergarment (brief/trunk construction); **strictly unbranded** — zero logos, zero wordmarks, zero printed graphics, zero visible brand tags, zero designer labels; **matte** surface finish (never satin, glossy, or metallic); visible combed-cotton jersey wales; double-needle flatlock seams; plain tonal elastic waistband; natural gravity fold weight. Remains unlinked from the Linear commercial project `RED DRAWZ — Pre-production v2.2 (STYLE 001 — Oxblood Trunk)` unless the Human Creative Authority explicitly links them.
  - **Container Material Lock (`prop-evidence-container-001`)**: Satin-finished American walnut drawer front and dovetailed maple side rail; matte unbleached paper drawer liner (`#F3F0E9`).

## 7. Environment and Set Dressing
- **[REQUIRED CONTENT — Hard Gate]**:
  - **Location ID**: `loc-grant-residence-001`
  - **Set Dressing ID**: `setdress-grant-bereavement-001`
  - **Architectural Geometry**: Contemporary Harlem brownstone bedroom dresser corner; dark hardwood floor visible out of focus below.

## 8. Camera, Lens, Framing, and Movement
- **Camera System Baseline**: Phase One medium-format optical realism (`WRASAL_CAMERA_GRAMMAR_v001`)
- **Shot Size**: Medium Close-Up Object Insert (MCU)
- **Camera Angle & Height**: 45-degree downward observational angle from `4 ft 0 in` height
- **Focal Length & Aperture**: `85mm` prime at `f/4`
- **Focus Plane & Depth of Field**: Critical focus locked on the top fold and stitched seam of `prop-red-drawz-001` and the top edge of the walnut drawer front; gentle optical falloff toward the floor below
- **Camera Movement**: Locked tripod

## 9. Lighting and Atmospheric Motivation
- **Lighting Grammar Pattern**: `controlled_low_key` (`WRASAL_LIGHTING_GRAMMAR_v001`)
- **Motivating Practical Sources**:
  1. Single `2800K` warm domestic shaded tungsten lamp positioned camera-left (`45°` azimuth, `35°` elevation), casting a soft warm grazing key across the walnut drawer edge, neutral paper liner, and top fold of the red garment.
  2. Faint `4800K` cool window shadow fill on the outer dresser casing camera-right.
- **Shadow & Exposure Behavior**: **STRICT CHROMATIC RULE (calibrated `2026-10-17`, `decision-010`)**: Zero red lighting gel, zero emissive glow from the garment, and zero red color cast on the surrounding surfaces.
  - **Track 1 (neutral achromatic)**: `R/G <= 1.35` on the unbleached paper drawer liner, plaster, and any unpainted cloth measured `> 5 cm` from the garment.
  - **Track 2 (intrinsically warm materials)**: Dark American walnut is exempt from the absolute `1.35` ceiling; evaluate instead by **occluded wood control delta** `|Δ(R/G)| <= 0.15` between a wood patch in the garment's lit environment and an occluded same-material walnut control.
  - **Reporting rule**: Report both tracks. Neither alone clears Gate B.

## 10. Color and Texture Rules
- **Foundation Palette**: Void `#0A0A0C` (deep drawer interior shadow), Paper `#F3F0E9` (drawer liner), Charcoal `#25262A` (background shadow), warm walnut brown, and localized deep crimson/oxblood on `prop-red-drawz-001` only.
- **Texture Integrity**: Crisp wood grain, matte paper fiber, and tactile knitted textile weave.

## 11. Continuity Constraints
- **Incoming State (`continuity_in`)**: Inherits `2800K` camera-left lamp position from `shot-open-002`.
- **Outgoing State (`continuity_out`)**: Locks exact 4.5-inch drawer opening, garment fold orientation, stitch seam placement, and `2800K` light vector for the `100mm` macro cut in `shot-open-004`.
- **180-Degree Axis & Screen Direction**: Drawer opens from upper-right toward lower-left; key light enters from camera-left.

## 12. Negative Constraints / Prohibited Drift (`WRASAL_NEGATIVE_DNA_v001` + Case 001 Locks)
- **Material & Lighting Prohibitions**: No global red light wash, no neon red glow, no wet blood texture, no shiny synthetic satin/plastic sheen, no candles, no ritual altars, no religious icons, no human hands or faces, no legible brand logos or text.

## 13. Output Target
- **Target Modality**: Still Keyframe (`image/png`)
- **Aspect Ratio & Resolution**: `1.85:1` widescreen cinema frame
- **Preset Catalog Tokens**: `/cinematic /closeup /rawphoto /moody`
- **Provenance Disclosure Label**: `AI-GENERATED CONCEPT / PREVISUALIZATION CANDIDATE — NOT CANON UNTIL HUMAN APPROVAL`

## 14. Verification Checklist (Pass/Fail Gate Before Promotion)
- [ ] **Canon Lock Pass**: Domestic Harlem 2026 interior context; zero fake ritual staging.
- [ ] **Identity Lock Pass**: Zero unapproved human faces or hands rendered.
- [ ] **Material & Chromatic Pass**: Garment is materially red (`R/G >= 2.2` and `R/B >= 2.5` on lamp-lit cloth); Track 1 neutral achromatic paper liner `R/G <= 1.35`; Track 2 occluded walnut control delta `|Δ(R/G)| <= 0.15`.
- [ ] **Spatial & Optical Pass**: 85mm f/4 perspective at 45° downward angle; drawer open ~4.5 inches.
- [ ] **Ontological & Cultural Restraint Pass**: Passes Metadata Strip Test as a physical red garment in a real drawer.
- [ ] **Human Steward Decision**: `PENDING`
