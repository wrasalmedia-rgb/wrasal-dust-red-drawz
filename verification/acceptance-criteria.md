# Verification & Acceptance Criteria — WRASAL DUST: THE RED DRAWZ (Case 001)

Every generated candidate image, motion clip, or audio stem must be evaluated against these six canonical acceptance gates before it can be promoted from `READY FOR TEST` to `TESTED`, and must receive explicit human creative authority approval before promotion to `APPROVED ASSET`.

## 1. Character Identity Consistency (`identity_pass`)
- Named characters (`char-wrasal-001`, `char-grant-001`, `char-keeper-001`, `char-examiner-001`, `char-builder-001`, `char-deceased-wife-001`) must match their approved Tier 00 `FACE_MASTER` and `BODY_MASTER` references across facial geometry, skin tone, hair pattern, age, and proportions.
- **Hard Blocker**: If no approved Tier 00 reference exists for a character (`REFERENCE NEEDED`), no shot depicting that character's face or body may be promoted to `APPROVED ASSET`.
- Wrasal must never be rendered as a generic occult detective; Mister Grant must never be assigned unverified occupational uniforms or biography.

## 2. Material & Wardrobe Continuity (`material_pass`)
- **Material-Red Lock (`decision-006`)**: `prop-red-drawz-001` must remain materially red through dyed textile pigment (visible yarn weave, seam stitching, natural fold weight) under neutral/warm motivated light (`2700K–5600K`).
- **Zero Red Scene Wash — Calibrated Two-Track Rule (updated `2026-10-17`, per `TEST-DUST-C001-001` `run-01` calibration evidence and Human Creative Authority authorisation)**:
  - **Track 1 — Neutral achromatic reference surfaces (`R/G <= 1.35`)**: The hard `R/G <= 1.35` ceiling applies **only** to genuinely neutral/achromatic reference surfaces measured `> 5 cm` from the garment — unbleached paper drawer liner, plaster wall, unpainted cloth, and neutral skin tones. These surfaces have no intrinsic warm pigment, so any `R/G` above `1.35` is evidence of red scene wash rather than material colour.
  - **Track 2 — Dark wood and other intrinsically warm-pigmented materials (occluded wood control delta `|Δ(R/G)| <= 0.15`)**: Dark wood (American walnut, mahogany, stained oak) is **exempt from the absolute `1.35` ceiling** because its own brown pigment legitimately produces `R/G` values in the `1.6–2.6` band under `2700K–3200K` tungsten light. Wood is instead evaluated by **occluded wood control delta**: measure `R/G` on (a) a wood surface immediately adjacent to and lit with the garment's environment, and (b) a wood control patch of the **same material** that is geometrically occluded from the garment (e.g. the shadowed lower drawer face, an upper closed drawer front, or a nightstand skirt outside the drawer cavity). Red scene wash is disproved when `|Δ(R/G)| <= 0.15` between the two. A delta `> 0.15` indicates the lit wood is being contaminated by red spill relative to the occluded control.
  - **Rationale / evidence**: In `TEST-DUST-C001-001` `run-01`, Frame B returned walnut `R/G` values of `1.654–2.603`, which would have produced a false Gate B failure under the uncalibrated `<= 1.35` rule. The occluded upper-drawer control patch (`B9`) returned `R/G = 2.603` — numerically **higher** than lit surfaces — proving the elevated ratio is intrinsic walnut pigment under `2800K` light, not red spill. Under `run-02`, lit walnut (`2.268`), upper drawer control (`2.180`), and occluded shadow control (`2.156`) all fall within `|Δ(R/G)| <= 0.112`, confirming zero red wash.
  - **Standing requirement**: Both tracks must be reported for every frame containing wood. Track 1 (`<= 1.35`) is mandatory wherever a neutral achromatic surface is present in frame; Track 2 is mandatory wherever wood is present in frame. Neither track alone is sufficient to clear Gate B.
- Wardrobe textures and silhouettes must match `production/wardrobe-register.yaml` across adjacent shots.

## 3. Spatial Plausibility (`continuity_pass` — Spatial)
- **Harlem 2026 Lock (`decision-001`)**: All exteriors and interiors must be architecturally plausible for Harlem, New York City, in 2026. Zero Jamaican exteriors, tropical flora, or *Miss Celia Chronicles* period elements are permitted.
- Room geometry, doorway axes, furniture placement, and drawer/door open states must remain continuous between incoming (`continuity_in`) and outgoing (`continuity_out`) shots.

## 4. Lighting Consistency (`lighting_pass`)
- Every light source must have a physical motivation within the scene (`WRASAL_LIGHTING_GRAMMAR_v001`: streetlamp, vestibule bulb, shaded tungsten table lamp, daylight window spill).
- Shadow direction, color temperature, and low-key contrast rolloff (`black stays black`) must match across cut-to-cut coverage within the same scene.

## 5. Shot Faithfulness (`continuity_pass` — Optical)
- Shot size, camera height, angle, focal-length perspective (`24mm`, `35mm`, `50mm`, `85mm`, `100mm macro`), depth of field, and blocking must match the shot specification in `shotlists/case-001.yaml` and `WRASAL_CAMERA_GRAMMAR_v001`.
- Vertical architectural lines must remain true on wide/medium lenses; no unrequested Dutch angles, fisheye distortion, or floating UI overlays.

## 6. Preservation of Unresolved Supernatural & Cultural Boundaries (`continuity_pass` — Ontological)
- **Deceased Wife Ambiguity (`decision-005`)**: Appearances of `char-deceased-wife-001` in the practitioners' astral mental chambers must preserve uncertainty about her true nature — zero translucent ghost shaders, monster distortion, glowing eyes, corpse decay, or dream-haze blur.
- **Red Garment & Nine-Day Threshold Mystery (`decision-006`, `decision-007`)**: Do not visually explain or resolve the exact procedure of the red garments; never introduce borrowed real-world Jamaican sacred/religious symbols or fake folklore instructions.
