---
id: "{{APPROACH_ID}}"
title: "{{APPROACH_TITLE}}"
mechanism: "{{MECHANISM}}"
target: "{{TARGET}}"
status: open
episode: 1
current_progress: []
# Each current_progress item uses:
# - summary: "..."
#   verification: unverified
#   source: "rounds/R001/tasks/T001-001/artifacts/..."
#   checked_by: []
current_gap: "{{CURRENT_GAP}}"
next_decisive_check: "{{NEXT_DECISIVE_CHECK}}"
requires_nodes: []
blockers: []
closure_basis: null
reopen_when: null
origin_round: null
origin_tasks: []
---

# [{{APPROACH_ID}}] {{APPROACH_TITLE}}

## Mechanism Rationale

Explain why this mechanism is distinct, why its target matters, and what evidence would change confidence in it. Link sources and task artifacts without copying derivations.

## Episode History

- Episode 1: Record why the approach entered the portfolio and where it came from.

## Durable Notes

Keep only concise interpretation that is not already captured in the structured fields. Put candidate proofs and experiments in task artifacts and keep their independent adversarial review in the task-local `audit.md`. For each active `current_progress` entry, record a concise `summary`, `verification: unverified | verified`, its artifact `source`, and a `checked_by` list. Keep that list empty when unverified and include an audit or verification of the current source with no unresolved material finding when verified.
