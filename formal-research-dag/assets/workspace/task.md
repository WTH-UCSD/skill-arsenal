---
id: "{{TASK_ID}}"
primary_approach: null
related_approaches: []
related_nodes: []
kind: research
status: planned
worker: null
assignment: "{{ASSIGNMENT}}"
inputs: []
acceptance_criteria:
  - "Return an inspectable result, a concrete proposed approach, or the exact failure gap, with artifact paths."
  - "For a proof task, provide a correct, self-contained, rigorous, complete, and readable argument with every necessary intermediate claim and inference, explicit constants and parameter dependence, and no omitted 'obvious', 'standard', or 'routine' step."
outcome: null
artifacts: []
---

# [{{TASK_ID}}] {{TASK_TITLE}}

## Method And Boundaries

Record the task-local method, prohibited assumptions, resource limits, and what outcomes would discriminate the live possibilities.

## Artifact Inventory

List retained files under `artifacts/` and any external reproducible state. Keep raw or heavy state outside the investigation.

## Integration Note

After the complete current output has been independently and adversarially audited in the task-local `audit.md`, link it here and record the disposition of every material result: admitted after verification, materialized as a named provisional node pair awaiting or returned from node audit, carried forward through named approach records with its verification state and artifact or check links, or not carried forward with the substantive reason. A task-local audit cannot itself admit a DAG node.
