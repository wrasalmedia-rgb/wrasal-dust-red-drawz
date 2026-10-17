# SHOT PROMPT SPECIFICATION: `shot-open-005`

## 1. Shot ID
- **Shot ID**: `shot-open-005`
- **Prompt ID & Version**: `prompt-img-open-005` · `v0.2.0`
- **Sequence / Scene / Beat**: Opening Sequence (Provisional) · Scene 02 · Beat 01 — The Apprentice at the Threshold
- **Governance Status**: `REFERENCE NEEDED` (**HARD BLOCKED** — Do not execute generation until human-approved Tier 00 `FACE_MASTER` and `BODY_MASTER` for `char-wrasal-001` and `wardrobe-wrasal-001` are provided)

## 2. Dramatic Intent
- **Narrative Question of the Frame**: Who is the observant apprentice arriving at the Harlem threshold to take intake of Case 001?
- **Dramatic Function**: Character introduction through architectural restraint and attentive observation.
- **Audience Perception Target**: The viewer sees Wrasal through the Harlem brownstone vestibule glass — composed, attentive, a quick learner grounded in 2026 reality, free of any occult-detective theatrics.

## 3. Canonical Story Constraints (Immutable Facts)
- **Setting & Temporal Lock (`CANON`)**: Harlem, New York City, 2026 (`loc-harlem-ext-001`, `decision-001`).
- **Character Biography & Role Locks (`CANON`)**: Wrasal (`char-wrasal-001`) is an apprentice working with experienced practitioners, a quick learner, who speaks composed standard British English (`decision-003`). Visual appearance must follow approved character references when available; generic occult investigator appearances are strictly prohibited.
- **Deliberately Unresolved Mysteries (`CANON`)**: No supernatural aura or glowing artifacts (`decision-005`, `decision-006`).
- **Cultural & Epistemic Boundary (`CANON`)**: Contemporary grounded Harlem 2026 presentation (`decision-007`).

## 4. Visual Reference Inputs (Hard Dependencies)
- **Tier 00 Character Reference (`FACE_MASTER` / `BODY_MASTER`)**: `char-wrasal-001` -> **`REFERENCE NEEDED — HARD BLOCKER`**
- **Approved Location Plate**: `loc-harlem-ext-001` (from `shot-open-001` approved plate)
- **Approved Prop / Material Reference**: None
- **Approved Wardrobe Reference**: `wardrobe-wrasal-001` -> **`REFERENCE NEEDED — HARD BLOCKER`**
- **Incoming Continuity Frame**: Matches vestibule glass, brass hardware, and lighting from `shot-open-001`

## 5. Subject Description
- **[REQUIRED CONTENT — Hard Gate]**:
  - **Subjects Present**: `char-wrasal-001` (Wrasal).
  - **Physical & Anatomical Anchors**: Must match 100% of the human-approved Tier 00 `FACE_MASTER` for `char-wrasal-001` once supplied; natural skin micro-texture, pores, and realistic eye reflection.
  - **Performance Restraint**: Still, composed posture at the top step outside the vestibule glass door; attentive eye-line registering the interior threshold before pressing the buzzer.

## 6. Wardrobe and Material Locks
- **[REQUIRED CONTENT — Hard Gate]**:
  - **Wardrobe IDs**: `wardrobe-wrasal-001` (structured, contemporary dark neutral outerwear/layering appropriate for Harlem 2026 night; zero trench-coat noir or occult talisman clichés).

## 7. Environment and Set Dressing
- **[REQUIRED CONTENT — Hard Gate]**:
  - **Location ID**: `loc-harlem-ext-001`
  - **Set Dressing ID**: `setdress-harlem-stoop-001`
  - **Architectural Geometry**: Framed from inside the Harlem brownstone vestibule looking out through beveled door glass toward the top stoop landing.

## 8. Camera, Lens, Framing, and Movement
- **Camera System Baseline**: Phase One medium-format portrait realism (`WRASAL_CAMERA_GRAMMAR_v001` — `85mm`)
- **Shot Size**: Medium Close-Up (MCU)
- **Camera Angle & Height**: Eye-level (`5 ft 6 in`), shooting through the vestibule glass doorway frame
- **Focal Length & Aperture**: `85mm` portrait prime at `f/2.8`
- **Focus Plane & Depth of Field**: Critical focus locked on Wrasal's eyes behind the bevel glass; soft foreground framing from the interior vestibule door stile and controlled background falloff onto the Harlem street
- **Camera Movement (for Motion Target `prompt-mot-open-005`)**: Locked tripod

## 9. Lighting and Atmospheric Motivation
- **Lighting Grammar Pattern**: `cool_edge_local_warm` (`WRASAL_LIGHTING_GRAMMAR_v001`)
- **Motivating Practical Sources**:
  1. `2900K` overhead vestibule bulb casting a soft warm key through the glass onto Wrasal's face.
  2. `4200K` Harlem streetlamp from behind/camera-left providing a subtle cool edge along the shoulder and collar.
- **Shadow & Exposure Behavior**: Deep low-key shadow falloff (`#0A0A0C`); zero red lighting tint.

## 10. Color and Texture Rules
- **Foundation Palette**: Void `#0A0A0C`, Charcoal `#25262A`, warm 2900K vestibule key, cool 4200K street edge, natural skin rendering.
- **Texture Integrity**: Real skin pores, wool/cotton outerwear weave, subtle condensation/smudge on vestibule glass edge.

## 11. Continuity Constraints
- **Incoming State (`continuity_in`)**: Matches exact vestibule door geometry and 3:17 AM lighting established in `shot-open-001`.
- **Outgoing State (`continuity_out`)**: Locks Wrasal's appearance and `wardrobe-wrasal-001` for the interior threshold two-shot (`shot-open-006`).
- **180-Degree Axis & Screen Direction**: Wrasal faces camera-left/center toward the interior doorway.

## 12. Negative Constraints / Prohibited Drift (`WRASAL_NEGATIVE_DNA_v001` + Case 001 Locks)
- **Identity & Role Prohibitions**: Do not execute without Tier 00 `char-wrasal-001` reference; no generic occult investigator fedora/trench-coat/amulet tropes (`decision-003`); no plastic skin smoothing (`cgi_human`).

## 13. Output Target
- **Target Modality**: Still Keyframe (`image/png`) — **BLOCKED UNTIL `char-wrasal-001` TIER 00 REFERENCE IS PROVIDED**
- **Aspect Ratio & Resolution**: `1.85:1` widescreen cinema frame
- **Preset Catalog Tokens**: `/cinematic /portrait85mm /nightphoto /moody /rawphoto`
- **Provenance Disclosure Label**: `AI-GENERATED CONCEPT / PREVISUALIZATION CANDIDATE — NOT CANON UNTIL HUMAN APPROVAL`

## 14. Verification Checklist (Pass/Fail Gate Before Promotion)
- [ ] **Blocker Cleared**: Human creative authority has provided/approved Tier 00 `FACE_MASTER` for `char-wrasal-001`.
- [ ] **Canon Lock Pass**: Harlem 2026 vestibule threshold; zero occult detective clichés.
- [ ] **Identity Lock Pass**: 100% facial and anatomical match to `char-wrasal-001` Tier 00 reference.
- [ ] **Material & Chromatic Pass**: `wardrobe-wrasal-001` fabric fidelity; zero red scene light wash.
- [ ] **Spatial & Optical Pass**: 85mm f/2.8 portrait perspective matching `shot-open-001` vestibule architecture.
- [ ] **Human Steward Decision**: `BLOCKED — REFERENCE NEEDED`
