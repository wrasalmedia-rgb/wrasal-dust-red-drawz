# SHOT PROMPT SPECIFICATION: `shot-open-001`

## 1. Shot ID
- **Shot ID**: `shot-open-001`
- **Prompt ID & Version**: `prompt-img-open-001` · `v0.2.0`
- **Sequence / Scene / Beat**: Opening Sequence (Provisional) · Scene 01 · Beat 01 — Geography Before Spectacle
- **Governance Status**: `READY FOR TEST` (Phase 1 of `TEST-DUST-C001-001` — Pending human authorization to execute)

## 2. Dramatic Intent
- **Narrative Question of the Frame**: What is the physical threshold in Harlem at 3:17 AM where an ordinary domestic loss becomes an active case?
- **Dramatic Function**: Geography before spectacle; architectural silence.
- **Audience Perception Target**: The viewer first registers a real, contemporary Harlem brownstone street at 3:17 AM after light rain; second, the recessed amber-lit vestibule doorway; zero supernatural spectacle is shown.

## 3. Canonical Story Constraints (Immutable Facts)
- **Setting & Temporal Lock (`CANON`)**: Harlem, New York City, 2026 (`decision-001`). Zero scenes or environmental cues set in Jamaica.
- **Character Biography & Role Locks (`CANON`)**: No characters present in frame (`characters_present: []`), eliminating unapproved facial generation risk.
- **Deliberately Unresolved Mysteries (`CANON`)**: No ritual markings, supernatural phenomena, or explanations on the exterior threshold (`decision-006`).
- **Cultural & Epistemic Boundary (`CANON`)**: Grounded 2026 Harlem residential architecture (`decision-007`).

## 4. Visual Reference Inputs (Hard Dependencies)
- **Tier 00 Character Reference (`FACE_MASTER` / `BODY_MASTER`)**: None (`No human subjects in frame`)
- **Approved Location Plate**: `loc-harlem-ext-001` (`REFERENCE NEEDED` — this prompt generates Candidate Plate v0.1 for human review)
- **Approved Prop / Material Reference**: None
- **Approved Wardrobe Reference**: None
- **Incoming Continuity Frame**: Cold open from black (`#0A0A0C`)

## 5. Subject Description
- **[REQUIRED CONTENT — Hard Gate]**:
  - **Subjects Present**: None (`Environment Plate Only — 0 human faces or silhouettes`).
  - **Architectural Subject**: A historic Harlem brownstone stoop and recessed ground-floor/parlor vestibule entrance in New York City, 2026, at 3:17 AM.
- **[VISUAL INTERPRETATION — Proposed Blocking]**:
  - Camera positioned at street level on the opposite sidewalk edge looking three-quarters across the damp asphalt and slate sidewalk toward the ascending stone stoop treads and matte-black iron balustrade.

## 6. Wardrobe and Material Locks
- **[REQUIRED CONTENT — Hard Gate]**:
  - **Wardrobe IDs**: None.
  - **Material Locks**: Weathered Harlem brownstone and red-brown brick masonry, matte black painted wrought-iron stoop railings with subtle contact wear, damp dark slate bluestone sidewalk slabs, beveled glass vestibule double-doors with brass hardware.
- **[STYLISTIC PREFERENCE — Surface Tactility]**:
  - Thin post-rain moisture film on horizontal stone treads and asphalt; dry vertical masonry under the vestibule cornice overhang.

## 7. Environment and Set Dressing
- **[REQUIRED CONTENT — Hard Gate]**:
  - **Location ID**: `loc-harlem-ext-001`
  - **Set Dressing ID**: `setdress-harlem-stoop-001`
  - **Architectural Geometry**: True vertical brownstone facade lines, 2026 NYC residential vestibule buzzer panel, shuttered parlor windows with horizontal interior blinds.
- **[VISUAL INTERPRETATION — Atmospheric Detail]**:
  - Still 3:17 AM urban air; no pedestrian traffic, no moving vehicles, no theatrical fog banks.

## 8. Camera, Lens, Framing, and Movement
- **Camera System Baseline**: Phase One medium-format optical realism (`WRASAL_CAMERA_GRAMMAR_v001`)
- **Shot Size**: Wide Establishing Shot (WS)
- **Camera Angle & Height**: Eye-level street perspective (`5 ft 4 in` lens height), level horizon, true verticals
- **Focal Length & Aperture**: `35mm` medium-format equivalent at `f/5.6`
- **Focus Plane & Depth of Field**: Deep observational focus from the base of the iron stoop railing (15 ft) to the vestibule glass door (28 ft)
- **Camera Movement (for Motion Target `prompt-mot-open-001`)**: Locked tripod (`0°` pan/tilt)

## 9. Lighting and Atmospheric Motivation
- **Lighting Grammar Pattern**: `controlled_low_key` + `cool_edge_local_warm` (`WRASAL_LIGHTING_GRAMMAR_v001`)
- **Motivating Practical Sources**:
  1. Overhead NYC municipal LED streetlamp (`4200K` cool-neutral amber) out of frame upper-left casting a defined downward grazing light on wet sidewalk and iron railing.
  2. Recessed brownstone vestibule ceiling bulb (`2900K` warm tungsten) glowing softly behind the beveled glass entrance doors.
- **Shadow & Exposure Behavior**: Black stays black (`#0A0A0C`); deep shadow falloff across upper brownstone stories; **strictly zero red lighting gel or neon wash**.

## 10. Color and Texture Rules
- **Foundation Palette**: Void `#0A0A0C`, Charcoal `#25262A`, weathered brownstone umber, cool 4200K wet-slate specular reflection, localized 2900K warm vestibule glow.
- **Chromatic Separation Rule**: Zero saturated red in the exterior frame (reserving chromatic red exclusively for `prop-red-drawz-001` in Shots 003–004).
- **Texture Integrity**: Sharp masonry grain, wrought-iron paint texture, realistic water-film specular rolloff.

## 11. Continuity Constraints
- **Incoming State (`continuity_in`)**: Opening frame from black; 3:17 AM nocturnal Harlem exterior after rain has stopped.
- **Outgoing State (`continuity_out`)**: Establishes the 4200K exterior streetlamp position and ground-floor window blind geometry that motivate the interior window spill in `shot-open-002`.
- **180-Degree Axis & Screen Direction**: Street axis runs left-to-right; stoop ascends from foreground-left toward vestibule door at mid-right.

## 12. Negative Constraints / Prohibited Drift (`WRASAL_NEGATIVE_DNA_v001` + Case 001 Locks)
- **Narrative & Cultural Prohibitions**: No Jamaican exterior architecture, no tropical foliage/palms/verandas (`CONFLICT-001` safeguard), no *Miss Celia Chronicles* rural elements.
- **Optical & Color Prohibitions**: No red lighting wash, no cyberpunk neon signs, no heavy volumetric horror fog, no Dutch angle, no barrel distortion, no legible street-sign/poster gibberish text, no human faces.

## 13. Output Target
- **Target Modality**: Still Keyframe (`image/png`)
- **Aspect Ratio & Resolution**: `1.85:1` widescreen cinema frame
- **Preset Catalog Tokens**: `/cinematic /nightphoto /rawphoto /moody`
- **Provenance Disclosure Label**: `AI-GENERATED CONCEPT / PREVISUALIZATION CANDIDATE — NOT CANON UNTIL HUMAN APPROVAL`

## 14. Verification Checklist (Pass/Fail Gate Before Promotion)
- [ ] **Canon Lock Pass**: Unmistakably Harlem, NYC, 2026; zero Jamaican exterior cues.
- [ ] **Identity Lock Pass**: Zero unapproved human faces rendered.
- [ ] **Material & Chromatic Pass**: Zero red lighting tint; authentic stone, iron, and wet asphalt material response.
- [ ] **Spatial & Optical Pass**: 35mm perspective with true vertical architectural lines.
- [ ] **Ontological & Cultural Restraint Pass**: Architectural silence; zero horror clichés.
- [ ] **Human Steward Decision**: `PENDING`
