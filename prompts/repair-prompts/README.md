# Repair prompt family

Repair prompts are designed for continuity correction, re-generation, and problem remediation. They should record the issue, the desired correction, and the validation method.

## Required fields

- `prompt_id`
- `issue_type`
- `target_asset_id`
- `status`
- `repair_goal`
- `review_status`

## Example

```yaml
prompt_id: prompt-repair-001
issue_type: continuity-discrepancy
target_asset_id: asset-001
status: proposed
repair_goal: reconcile inconsistent visual cue
review_status: not-reviewed
```
