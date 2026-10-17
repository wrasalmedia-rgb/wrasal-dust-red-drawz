# Master Cinematic Prompt Template — WRASAL DUST: THE RED DRAWZ (Case 001)

- **Template ID**: `prompt-master-template-001`
- **Version**: `0.2.0`
- **Status**: `PROPOSED` (Pending human review and approval)
- **Governing Principle**: `REALITY FIRST. TECHNOLOGY SECOND.`
- **Grammar Alignment**: `WRASAL_CAMERA_GRAMMAR_v001`, `WRASAL_LIGHTING_GRAMMAR_v001`, `WRASAL_MATERIAL_GRAMMAR_v001`, `WRASAL_NEGATIVE_DNA_v001`

---

## Architectural Rules of This Template

1. **Separation of Story Facts from Visual Interpretation**
   - **Story Facts (`CANON`)** are immutable narrative truths locked by human creative authority (e.g., *Harlem, NYC, 2026*; *Mister Grant is an American widower married <2 years*; *Wrasal is an apprentice speaking composed standard British English*; *the red garments are materially red under normal light*; *the deceased wife's true nature in the astral chambers is unconfirmed*).
   - **Visual Interpretation (`PROPOSED`)** describes how the camera, lighting, blocking, and surface textures render those facts within a specific shot. Visual interpretation may never add, contradict, or prematurely resolve a canonical story fact.
2. **Separation of Required Content from Stylistic Preferences**
   - **Required Content (Hard Gates)**: Subject identity locks, spatial geography, prop geometry, material color accuracy, and continuity incoming/outgoing states. Failure of any required content item triggers `NEEDS REVISION`.
   - **Stylistic Preferences (Soft Modulators)**: Micro-contrast rolloff, secondary background texture, or preset tokens (e.g., `/cinematic`, `/rawphoto`, `/nightphoto`, `/portrait85mm`). Stylistic tokens must never override physical or canonical constraints.
3. **Platform-Specific Limitations & Adapter Discipline**
   - **Still Image Models (Text-to-Image / Reference-to-Image)**:
     - Cannot reliably maintain facial identity across shots from text descriptions alone; require approved Tier 00 `FACE_MASTER` / `BODY_MASTER` image references (`REFERENCE NEEDED`).
     - Frequently conflate "red object" prompts into global red lighting washes; prompts must explicitly isolate the red hue to the dyed textile (`prop-red-drawz-001`) and specify neutral/warm kelvin values (`2700K–5600K`) for room light and neutral walls.
     - Do not ask image models to render legible poster or document typography (`CIN-03` rule); compose typography in layout.
     - Never invoke editing tokens (`/relight`, `/inpaint`, `/outpaint`) without an existing verified source image.
   - **Motion / Video Models (Image-to-Video / Frame-Conditioned Video)**:
     - Must be driven by a human-approved still keyframe (`APPROVED ASSET` or `READY FOR TEST` plate), never unanchored text-to-video.
     - Prone to facial morphing during large head turns, hand/finger deformation during complex object manipulation, and textile weave swimming; restrict camera movement to locked tripod, slow dolly, or subtle rack focus (4–6 seconds per clip).
   - **Voice / Audio Synthesis Models**:
     - Cannot infer character subtext without explicit prosody constraints; Wrasal's voice (`sound-vo-wrasal-001`) requires an explicit British English (`en-GB`) registered voice auditioned and approved by the human creative authority before synthesis.

---

## Reusable 14-Section Shot Prompt Specification

Copy and populate all 14 sections for every candidate shot before executing any generation run.

```markdown
# SHOT PROMPT SPECIFICATION: [shot_id]

## 1. Shot ID
- **Shot ID**: [e.g., shot-open-003]
- **Prompt ID & Version**: [e.g., prompt-img-open-003 · v0.2.0]
- **Sequence / Scene / Beat**: [e.g., Opening Sequence · Scene 01 · Beat 03]
- **Governance Status**: [PROPOSED | IN BUILD | REFERENCE NEEDED | READY FOR TEST | TESTED | NEEDS REVISION | APPROVED ASSET | CANON | SUPERSEDED]

## 2. Dramatic Intent
- **Narrative Question of the Frame**: [What single emotional or procedural question does this frame ask without explaining?]
- **Dramatic Function**: [Geography before spectacle | Human grief before supernatural escalation | Object detail before explanation | Architectural silence]
- **Audience Perception Target**: [What the viewer should notice first, second, and what must remain withheld]

## 3. Canonical Story Constraints (Immutable Facts)
- **Setting & Temporal Lock (`CANON`)**: Harlem, New York City, 2026. Zero scenes or environmental cues set in Jamaica.
- **Character Biography & Role Locks (`CANON`)**: [Cite applicable locks: e.g., Mister Grant (<2 yr marriage, widower, no invented occupation); Wrasal (apprentice, quick learner, composed standard British English); Practitioner Triad distinction (Keeper / Examiner / Builder)]
- **Deliberately Unresolved Mysteries (`CANON`)**: [Cite applicable mysteries that MUST NOT be resolved visually: e.g., Deceased Wife's unconfirmed nature in astral chambers; unconfirmed exact ritual/procedure of the red garments and Nine-Day Threshold]
- **Cultural & Epistemic Boundary (`CANON`)**: Fictional DUST rules are not depicted as verified real-world Jamaican religious or cultural ceremony.

## 4. Visual Reference Inputs (Hard Dependencies)
- **Tier 00 Character Reference (`FACE_MASTER` / `BODY_MASTER`)**: [Asset ID + URI/path, or `REFERENCE NEEDED — BLOCKED`]
- **Approved Location Plate**: [Asset ID + URI/path, or `REFERENCE NEEDED`]
- **Approved Prop / Material Reference**: [Asset ID + URI/path, e.g., `prop-red-drawz-001`]
- **Approved Wardrobe Reference**: [Asset ID + URI/path]
- **Incoming Continuity Frame**: [Prior Shot ID + frame reference]

## 5. Subject Description
- **[REQUIRED CONTENT — Hard Gate]**:
  - **Subjects Present**: [Character IDs or `None — Environment/Object Plate Only`]
  - **Physical & Anatomical Anchors**: [Exact pose, eye-line vector, hand placement, natural skin texture with pores and micro-asymmetry; zero plastic smoothing]
  - **Performance Restraint**: [Controlled, non-theatrical posture; grief or observation expressed through stillness and physical weight rather than melodrama]
- **[VISUAL INTERPRETATION — Proposed Blocking]**:
  - [Precise spatial relationship between subject and threshold/object]

## 6. Wardrobe and Material Locks
- **[REQUIRED CONTENT — Hard Gate]**:
  - **Wardrobe IDs**: [e.g., `wardrobe-grant-001` or `wardrobe-wrasal-001`]
  - **Prop Material Locks**: [If `prop-red-drawz-001` is present: Deep crimson/oxblood dyed cotton/wool textile with visible fiber weave, seam construction, and natural gravity folds. The redness belongs strictly to the physical dye of the cloth.]
- **[STYLISTIC PREFERENCE — Surface Tactility]**:
  - [Subtle lived wear, natural crease memory, matte fabric response]

## 7. Environment and Set Dressing
- **[REQUIRED CONTENT — Hard Gate]**:
  - **Location ID**: [e.g., `loc-harlem-ext-001` or `loc-grant-residence-001`]
  - **Set Dressing ID**: [e.g., `setdress-grant-bereavement-001`]
  - **Architectural Geometry**: [Authentic 2026 Harlem brownstone/apartment proportions, wood molding, plaster/brick texture, true verticals]
- **[VISUAL INTERPRETATION — Atmospheric Detail]**:
  - [Restrained domestic residue of a marriage under two years; architectural silence; no gothic cobwebs or occult clutter]

## 8. Camera, Lens, Framing, and Movement
- **Camera System Baseline**: Phase One medium-format / ARRI Alexa 65 optical realism (`WRASAL_CAMERA_GRAMMAR_v001`)
- **Shot Size**: [Extreme Wide | Wide | Medium Wide | Medium Close-Up | Close-Up | Macro Insert]
- **Camera Angle & Height**: [e.g., Eye-level / Chest-height / Measured 3/4 table angle; level horizon, true verticals]
- **Focal Length & Aperture**: [24mm f/8 (architecture) | 35mm f/5.6 (human-environment) | 50mm f/5.6 (neutral observation) | 85mm f/2.8 (portrait anchor) | 100mm Macro f/11 (material evidence)]
- **Focus Plane & Depth of Field**: [Exact focus distance and falloff behavior]
- **Camera Movement (for Motion Target)**: [Locked tripod | Imperceptible 2-inch push-in | Measured rack focus; no drone/gimbal orbits]

## 9. Lighting and Atmospheric Motivation
- **Lighting Grammar Pattern**: [`controlled_low_key` | `cool_edge_local_warm` | `forensic_flat` from `WRASAL_LIGHTING_GRAMMAR_v001`]
- **Motivating Practical Sources**: [e.g., 2900K shaded domestic tungsten lamp camera-left + 4800K Harlem streetlamp spill through venetian blinds camera-right]
- **Shadow & Exposure Behavior**: Black stays black; shadows retain material falloff; no unmotivated rim lights; **strictly zero red lighting gel or ambient red room wash**.

## 10. Color and Texture Rules
- **Foundation Palette**: Void `#0A0A0C`, Paper `#F3F0E9`, Charcoal `#25262A`, selective warm tungsten ember, and localized material crimson (`prop-red-drawz-001` only).
- **Chromatic Separation Rule**: Surrounding walls, wood surfaces, and skin tones must maintain accurate neutral/warm color rendering so the red garment stands out through material pigment alone.
- **Texture Integrity**: Preserve real textile weave, wood grain, masonry pores, and natural skin micro-texture.

## 11. Continuity Constraints
- **Incoming State (`continuity_in`)**: [Exact state inherited from previous shot: time of night, light direction, door/drawer position, garment fold state, character posture]
- **Outgoing State (`continuity_out`)**: [Exact state handed off to next shot]
- **180-Degree Axis & Screen Direction**: [Camera axis and eye-line vector lock]

## 12. Negative Constraints / Prohibited Drift (`WRASAL_NEGATIVE_DNA_v001` + Case 001 Locks)
- **Narrative & Cultural Prohibitions**: No Jamaican exterior flora/architecture; no Miss Celia period crossover; no invented occupational uniforms for Mister Grant; no generic occult detective trench-coat/hat tropes for Wrasal; no borrowed real-world sacred/religious symbols.
- **Ontological Prohibitions**: No translucent ghost shaders, glowing eyes, demonic distortion, decaying horror corpses, or dream-blur fog for the deceased wife.
- **Optical & Color Prohibitions**: No global red lighting tint, no neon cyberpunk color wash, no floating HUDs/glyphs, no plastic CGI skin smoothing, no HDR halos, no Dutch angles, no illegible AI-generated text.

## 13. Output Target
- **Target Modality**: [Still Keyframe (`image/png`) | Motion Clip (`video/mp4`, 24fps, 4–6s) | Audio Stem (`audio/wav`)]
- **Aspect Ratio & Resolution**: [e.g., 1.85:1 or 2.39:1 widescreen cinema frame; minimum 2K/4K master]
- **Preset Catalog Tokens (Optional Soft Modifiers)**: [Only verified tokens, e.g., `/cinematic /nightphoto /rawphoto /closeup`]
- **Provenance Disclosure Label**: `AI-GENERATED CONCEPT / PREVISUALIZATION CANDIDATE — NOT CANON UNTIL HUMAN APPROVAL`

## 14. Verification Checklist (Pass/Fail Gate Before Promotion)
- [ ] **Canon Lock Pass**: Set in Harlem 2026; zero unauthorized biography or resolved mysteries.
- [ ] **Identity Lock Pass**: Matches approved Tier 00 `FACE_MASTER` / `BODY_MASTER` (or confirms no unapproved face is shown).
- [ ] **Material & Chromatic Pass**: `prop-red-drawz-001` is materially red fabric; surrounding room/skin has zero red light bleed.
- [ ] **Spatial & Optical Pass**: Lens perspective, verticals, and shadow vectors match `WRASAL_CAMERA_GRAMMAR_v001` and `WRASAL_LIGHTING_GRAMMAR_v001`.
- [ ] **Ontological & Cultural Restraint Pass**: No horror clichés, ghost shaders, or fabricated sacred rituals.
- [ ] **Human Steward Decision**: [PENDING | APPROVED ASSET | NEEDS REVISION]
```
