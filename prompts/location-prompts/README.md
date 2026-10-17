# Location prompt family

This directory is for location-oriented prompt templates. Location prompts must maintain continuity with the approved world-building context and their associated asset IDs.

## Required fields

- `prompt_id`
- `location_id`
- `status`
- `purpose`
- `visual_reference`
- `continuity_constraints`
- `review_status`

## Example

```yaml
prompt_id: prompt-loc-001
location_id: loc-001
status: proposed
purpose: establish-environment
visual_reference: to-be-defined
continuity_constraints: pending review
review_status: not-reviewed
```
