# SHOT PROMPT SPECIFICATION: `shot-open-004`

## 1. Shot ID
- **Shot ID**: `shot-open-004`
- **Prompt ID & Version**: `prompt-img-open-004` · `v0.2.0`
- **Sequence / Scene / Beat**: Opening Sequence (Provisional) · Scene 01 · Beat 04 — Material Reality of the Red Garment
- **Governance Status**: `READY FOR TEST` (Phase 1 of `TEST-DUST-C001-001` — Pending human authorization to execute)

## 2. Dramatic Intent
- **Narrative Question of the Frame**: Does the red garment hold up as a tactile, physical piece of dyed cloth under forensic macro scrutiny, refusing supernatural spectacle?
- **Dramatic Function**: Object detail before explanation; material realism (`REALITY FIRST. TECHNOLOGY SECOND.`).
- **Audience Perception Target**: The viewer sees individual dyed crimson/oxblood yarn fibers, flatlock stitch tension, and natural fabric weight resting against neutral paper and wood under warm tungsten light.

## 3. Canonical Story Constraints (Immutable Facts)
- **Setting & Temporal Lock (`CANON`)**: Interior of Mister Grant's Harlem, NYC, 2026 residence (`loc-grant-residence-001`, `decision-001`).
- **Character Biography & Role Locks (`CANON`)**: No human subjects in frame (`characters_present: []`).
- **Deliberately Unresolved Mysteries (`CANON`)**: The red garment's exact procedure in the Nine-Day Threshold remains unresolved (`decision-006`).
- **Cultural & Epistemic Boundary (`CANON`)**: No sacred inscriptions, sigils, or invented ritual markings on the cloth (`decision-006`, `decision-007`).

## 4. Visual Reference Inputs (Hard Dependencies)
- **Tier 00 Character Reference (`FACE_MASTER` / `BODY_MASTER`)**: None
- **Approved Location Plate**: `loc-grant-residence-001`
- **Approved Prop / Material Reference**: `prop-red-drawz-001` (and Candidate Frame B from `shot-open-003` for cross-shot continuity)
- **Approved Wardrobe Reference**: None
- **Incoming Continuity Frame**: `shot-open-003` (85mm drawer insert)

## 5. Subject Description
- **[REQUIRED CONTENT — Hard Gate]**:
  - **Subjects Present**: Macro section of `prop-red-drawz-001` resting inside `prop-evidence-container-001`.
  - **Object Geometry**: Close measured macro view of the primary folded edge and reinforced flatlock seam of the red garment where it meets the unbleached paper drawer liner (`#F3F0E9`) and the inner corner of the walnut drawer wall.

## 6. Wardrobe and Material Locks
- **[REQUIRED CONTENT — Hard Gate]**:
  - **Prop Material Lock (`prop-red-drawz-001`, `decision-006`)**: Heavyweight matte dyed crimson/oxblood cotton-wool jersey weave; clearly resolved individual yarn twist, micro-fuzz, needle perforations along the flatlock seam, and natural compression crease at the fold. **100% material pigment red — zero emissive light.**
  - **Adjacent Reference Surface (`prop-evidence-container-001`)**: Visible strip of matte unbleached paper liner (`#F3F0E9`) and walnut drawer edge in lower/outer frame to serve as a neutral color-calibration reference.

## 7. Environment and Set Dressing
- **[REQUIRED CONTENT — Hard Gate]**:
  - **Location ID**: `loc-grant-residence-001`
  - **Set Dressing ID**: `setdress-grant-bereavement-001`
  - **Architectural Geometry**: Macro interior recess of the wooden drawer established in `shot-open-003`.

## 8. Camera, Lens, Framing, and Movement
- **Camera System Baseline**: Phase One medium-format macro specimen rendering (`WRASAL_CAMERA_GRAMMAR_v001` — `100mm_macro`)
- **Shot Size**: Extreme Close-Up / Macro Insert (ECU)
- **Camera Angle & Height**: Measured 30-degree raking angle to the fabric plane
- **Focal Length & Aperture**: `100mm Macro` at `f/11`
- **Focus Plane & Depth of Field**: Razor-sharp macro focal plane across the foreground flatlock seam and primary fold crest, rolling off smoothly into the darker rear fold and neutral paper edge
- **Camera Movement (for Motion Target `prompt-mot-open-004`)**: Locked macro tripod with an imperceptible 4-second rack focus (`15 mm` focal plane shift) along the stitched seam

## 9. Lighting and Atmospheric Motivation
- **Lighting Grammar Pattern**: `controlled_low_key` + `forensic_flat` raking variant (`WRASAL_LIGHTING_GRAMMAR_v001`)
- **Motivating Practical Sources**:
  1. Same `2800K` warm domestic tungsten lamp from camera-left (`45°` azimuth, `35°` elevation) raking across the micro-topography of the fabric weave.
  2. Negative fill on camera-right preserving natural shadow density inside the fold crevice.
- **Shadow & Exposure Behavior**: Black stays black in deep crevice shadow; **zero red lighting wash on the adjacent unbleached paper liner (`R/G <= 1.35`, Track 1 neutral achromatic)**. Bare walnut inner drawer wall is evaluated by the **occluded wood control delta** `|Δ(R/G)| <= 0.15` against the Frame B walnut control (Track 2, `decision-010`).

## 10. Color and Texture Rules
- **Foundation Palette**: Deep oxblood/crimson textile pigment, Paper `#F3F0E9` neutral reference strip, Charcoal `#25262A` shadow falloff, Void `#0A0A0C` deep fold shadow.
- **Texture Integrity**: Must pass the `CONCEPT-0007` Metadata Strip Test — recognizable immediately from intrinsic micro-geometry as a real, manufactured dyed garment.

## 11. Continuity Constraints
- **Incoming State (`continuity_in`)**: Matches exact fabric weave, dye hue, fold orientation, and `2800K` camera-left lighting vector from `shot-open-003`.
- **Outgoing State (`continuity_out`)**: Holds on tactile stillness before the hard cut to Wrasal's exterior threshold arrival in `shot-open-005`.
- **180-Degree Axis & Screen Direction**: Key light enters from camera-left (`±10°` match to `shot-open-003`).

## 12. Negative Constraints / Prohibited Drift (`WRASAL_NEGATIVE_DNA_v001` + Case 001 Locks)
- **Material & Lighting Prohibitions**: No red lighting gel on surrounding paper/wood, no glowing threads, no liquid blood sheen, no synthetic plastic texture, no embroidered runes/symbols, no printed brand text or tags.

## 13. Output Target
- **Target Modality**: Still Keyframe (`image/png`)
- **Aspect Ratio & Resolution**: `1.85:1` widescreen cinema frame
- **Preset Catalog Tokens**: `/macro /cinematic /rawphoto /closeup`
- **Provenance Disclosure Label**: `AI-GENERATED CONCEPT / PREVISUALIZATION CANDIDATE — NOT CANON UNTIL HUMAN APPROVAL`

## 14. Verification Checklist (Pass/Fail Gate Before Promotion)
- [ ] **Canon Lock Pass**: Materially red garment (`decision-006`) with zero fake folklore inscriptions (`decision-007`).
- [ ] **Identity Lock Pass**: Zero human faces/hands in frame.
- [ ] **Material & Chromatic Pass**: Matches `shot-open-003` fabric weave and dye chromaticity (`R/G >= 2.2`, `R/B >= 2.5`); adjacent paper liner `#F3F0E9` shows zero red light wash (Track 1 `R/G <= 1.35`); bare walnut inner drawer wall matches the Frame B walnut control (Track 2 `|Δ(R/G)| <= 0.15`).
- [ ] **Spatial & Optical Pass**: 100mm macro f/11 optical depth and raking light vector match `shot-open-003`.
- [ ] **Ontological & Cultural Restraint Pass**: Zero supernatural glow or ritual clutter.
- [ ] **Human Steward Decision**: `PENDING`
