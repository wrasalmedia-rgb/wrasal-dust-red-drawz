# Canon decisions log

This document records durable creative decisions that are considered part of the project’s decision history. It should remain cleanly distinguished from generated output and from recommendations that were not authorized.

## Decision record structure

Each decision entry should include:

- `decision_id`
- `title`
- `category`
- `status`
- `decision_date`
- `rationale`
- `owner`
- `related_asset_ids`

## Example decision

```yaml
- decision_id: decision-001
  title: Initial project architecture approved
  category: production
  status: proposed
  decision_date: 2026-10-17
  rationale: Establish the production architecture and registry structure.
  owner: human-review
  related_asset_ids: [project-lock, asset-registry]
```

## Rule

Only human-reviewed, explicitly approved decisions should be treated as canon decisions.
