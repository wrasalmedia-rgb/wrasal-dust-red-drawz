# Prop prompt family

This directory is for prop and object prompt templates. Each prompt should clearly identify the object, purpose, and the review status of the associated asset.

## Required fields

- `prompt_id`
- `prop_id`
- `status`
- `purpose`
- `material_notes`
- `continuity_constraints`
- `approval_status`

## Example

```yaml
prompt_id: prompt-prop-001
prop_id: prop-001
status: proposed
purpose: object-introduction
material_notes: pending specification
continuity_constraints: pending review
approval_status: not-approved
```
