# Character prompt family

This directory is for character-specific prompt templates and prompt variants. Keep all prompts linked to a stable character ID and review state.

## Prompt naming guideline

Use a structure like:

- `char-<id>-<prompt-purpose>.md`
- `char-<id>-<variation>.yaml`

## Required fields when a prompt is formalized

- `prompt_id`
- `character_id`
- `status`
- `purpose`
- `context`
- `style_reference`
- `review_status`

## Example

```yaml
prompt_id: prompt-char-001
character_id: char-001
status: proposed
purpose: character-introduction
context: opening scene
style_reference: to-be-defined
review_status: not-reviewed
```
