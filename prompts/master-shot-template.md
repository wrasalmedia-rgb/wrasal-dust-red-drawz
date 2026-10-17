# Master shot template

This file is a reusable template for shot definitions. It is intentionally generic and should be populated with project-specific data before use.

## Required fields

- `shot_id`
- `title`
- `status`
- `scene_reference`
- `camera_reference`
- `character_ids`
- `location_id`
- `prompt_id`
- `continuity_notes`
- `verification_status`

## Example

```yaml
shot_id: shot-001
title: Opening beat
status: proposed
scene_reference: scene-001
camera_reference: wide-static-shot
character_ids: [char-001]
location_id: loc-001
prompt_id: prompt-001
continuity_notes: pending review
verification_status: not-started
```

## Rule

Any shot should not be treated as approved until it is reviewed and passes the necessary continuity and quality checks.
