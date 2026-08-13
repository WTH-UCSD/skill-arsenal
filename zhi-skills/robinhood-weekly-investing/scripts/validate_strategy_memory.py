#!/usr/bin/env python3
"""Validate compact strategy memory and linked weekly HTML reports."""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from pathlib import Path


TOP_FIELDS = {
    "schema_version",
    "timezone",
    "benchmark_symbol",
    "weekly_gross_turnover_limit_pct",
    "task_queue_file",
    "user_notes_file",
    "last_updated_at",
    "weeks",
}

WEEK_FIELDS = {
    "week_id",
    "summary_file",
    "report_file",
    "created_at",
    "updated_at",
    "lifecycle",
    "idea_count",
    "decision_summary",
    "macro_summary",
    "principles",
    "proposed_gross_notional",
    "proposed_turnover_pct",
    "approved_order_count",
    "filled_gross_notional",
    "filled_turnover_pct",
    "review_due_dates",
    "outcomes",
}

LIFECYCLES = {
    "planned",
    "no_trade",
    "approved",
    "submitted",
    "partially_filled",
    "filled",
    "cancelled",
    "closed",
}

TASK_FIELDS = {
    "task_id",
    "week_id",
    "kind",
    "status",
    "summary",
    "trigger",
    "next_action",
    "depends_on",
    "requires_fresh_review",
    "report_file",
    "created_at",
    "updated_at",
}
TASK_KINDS = {"order_leg", "strategy_revisit", "process_followup"}
TASK_STATUSES = {"open", "blocked", "scheduled", "done", "cancelled"}

HORIZONS = {"1w", "4w", "12w", "52w"}
MAX_SUMMARY_WORDS = 450


def finite_number(value: object) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def safe_file(root: Path, relative_value: object, suffix: str, label: str, errors: list[str]) -> Path | None:
    if not isinstance(relative_value, str) or not relative_value:
        errors.append(f"{label} must be a non-empty relative path")
        return None

    relative = Path(relative_value)
    if relative.is_absolute() or ".." in relative.parts:
        errors.append(f"{label} must stay inside the workspace: {relative_value}")
        return None
    if relative.suffix.lower() != suffix:
        errors.append(f"{label} must end in {suffix}: {relative_value}")
        return None

    resolved = root / relative
    if not resolved.is_file():
        errors.append(f"{label} does not exist: {relative_value}")
        return None
    return resolved


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    index_path = root / "strategy-memory" / "index.json"

    try:
        data = json.loads(index_path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return [f"missing index: {index_path}"]
    except json.JSONDecodeError as exc:
        return [f"invalid JSON at {index_path}:{exc.lineno}:{exc.colno}: {exc.msg}"]

    if not isinstance(data, dict):
        return ["index root must be a JSON object"]

    missing_top = TOP_FIELDS - data.keys()
    if missing_top:
        errors.append(f"index missing fields: {', '.join(sorted(missing_top))}")

    if data.get("schema_version") != 4:
        errors.append("schema_version must be 4")

    limit = data.get("weekly_gross_turnover_limit_pct")
    if not finite_number(limit) or not 0 < limit <= 100:
        errors.append("weekly_gross_turnover_limit_pct must be a finite number in (0, 100]")

    weeks = data.get("weeks")
    if not isinstance(weeks, list):
        errors.append("weeks must be an array")
        return errors

    seen: set[str] = set()
    for position, week in enumerate(weeks):
        label = f"weeks[{position}]"
        if not isinstance(week, dict):
            errors.append(f"{label} must be an object")
            continue

        missing = WEEK_FIELDS - week.keys()
        if missing:
            errors.append(f"{label} missing fields: {', '.join(sorted(missing))}")

        week_id = week.get("week_id")
        if not isinstance(week_id, str) or not week_id:
            errors.append(f"{label}.week_id must be a non-empty string")
        elif week_id in seen:
            errors.append(f"duplicate week_id: {week_id}")
        else:
            seen.add(week_id)

        if week.get("lifecycle") not in LIFECYCLES:
            errors.append(f"{label}.lifecycle is invalid: {week.get('lifecycle')!r}")

        idea_count = week.get("idea_count")
        if not isinstance(idea_count, int) or isinstance(idea_count, bool) or not 0 <= idea_count <= 3:
            errors.append(f"{label}.idea_count must be an integer from 0 to 3")

        approved_count = week.get("approved_order_count")
        if not isinstance(approved_count, int) or isinstance(approved_count, bool) or approved_count < 0:
            errors.append(f"{label}.approved_order_count must be a non-negative integer")

        principles = week.get("principles")
        if not isinstance(principles, list) or not principles or not all(
            isinstance(item, str) and item for item in principles
        ):
            errors.append(f"{label}.principles must be a non-empty string array")

        for field in ("decision_summary", "macro_summary"):
            if not isinstance(week.get(field), str) or not week[field].strip():
                errors.append(f"{label}.{field} must be a non-empty string")

        for field in ("proposed_turnover_pct", "filled_turnover_pct"):
            value = week.get(field)
            if not finite_number(value) or value < 0:
                errors.append(f"{label}.{field} must be a non-negative finite number")
            elif finite_number(limit) and value > limit + 1e-9:
                errors.append(f"{label}.{field} exceeds the configured {limit}% limit")

        for field in ("proposed_gross_notional", "filled_gross_notional"):
            value = week.get(field)
            if not finite_number(value) or value < 0:
                errors.append(f"{label}.{field} must be a non-negative finite number")

        summary = safe_file(root, week.get("summary_file"), ".md", f"{label}.summary_file", errors)
        report = safe_file(root, week.get("report_file"), ".html", f"{label}.report_file", errors)

        if summary:
            words = re.findall(r"\b[\w'-]+\b", summary.read_text(encoding="utf-8"))
            if len(words) > MAX_SUMMARY_WORDS:
                errors.append(
                    f"{label}.summary_file has {len(words)} words; compact summaries must stay <= {MAX_SUMMARY_WORDS}"
                )

        if report:
            html = report.read_text(encoding="utf-8").lower()
            if "<html" not in html or "<title>" not in html:
                errors.append(f"{label}.report_file is not a complete HTML document")

        due_dates = week.get("review_due_dates")
        if not isinstance(due_dates, dict) or set(due_dates) != HORIZONS:
            errors.append(f"{label}.review_due_dates must contain exactly {sorted(HORIZONS)}")

        outcomes = week.get("outcomes")
        if not isinstance(outcomes, dict) or set(outcomes) != HORIZONS:
            errors.append(f"{label}.outcomes must contain exactly {sorted(HORIZONS)}")

    notes_path = safe_file(root, data.get("user_notes_file"), ".json", "user_notes_file", errors)
    if notes_path:
        try:
            notes = json.loads(notes_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"invalid JSON at {notes_path}:{exc.lineno}:{exc.colno}: {exc.msg}")
            notes = None

        if not isinstance(notes, dict):
            errors.append("user notes root must be a JSON object")
        else:
            if notes.get("schema_version") != 1:
                errors.append("user notes schema_version must be 1")
            updated_at = notes.get("updated_at")
            if updated_at is not None and (not isinstance(updated_at, str) or not updated_at.strip()):
                errors.append("user notes updated_at must be null or a non-empty string")
            for field in ("comments", "questions"):
                if not isinstance(notes.get(field), str):
                    errors.append(f"user notes {field} must be a string")

    queue_path = safe_file(root, data.get("task_queue_file"), ".json", "task_queue_file", errors)
    if queue_path:
        try:
            queue = json.loads(queue_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"invalid JSON at {queue_path}:{exc.lineno}:{exc.colno}: {exc.msg}")
            queue = None

        if not isinstance(queue, dict):
            errors.append("task queue root must be a JSON object")
        else:
            if queue.get("schema_version") != 1:
                errors.append("task queue schema_version must be 1")
            if queue.get("timezone") != data.get("timezone"):
                errors.append("task queue timezone must match index timezone")
            if not isinstance(queue.get("updated_at"), str) or not queue["updated_at"].strip():
                errors.append("task queue updated_at must be a non-empty string")

            tasks = queue.get("tasks")
            if not isinstance(tasks, list):
                errors.append("task queue tasks must be an array")
            else:
                task_ids: set[str] = set()
                dependencies: list[tuple[str, object]] = []
                for position, task in enumerate(tasks):
                    label = f"tasks[{position}]"
                    if not isinstance(task, dict):
                        errors.append(f"{label} must be an object")
                        continue

                    missing = TASK_FIELDS - task.keys()
                    if missing:
                        errors.append(f"{label} missing fields: {', '.join(sorted(missing))}")

                    task_id = task.get("task_id")
                    if not isinstance(task_id, str) or not task_id:
                        errors.append(f"{label}.task_id must be a non-empty string")
                    elif task_id in task_ids:
                        errors.append(f"duplicate task_id: {task_id}")
                    else:
                        task_ids.add(task_id)

                    if task.get("week_id") not in seen:
                        errors.append(f"{label}.week_id must reference an indexed week")
                    if task.get("kind") not in TASK_KINDS:
                        errors.append(f"{label}.kind is invalid: {task.get('kind')!r}")
                    if task.get("status") not in TASK_STATUSES:
                        errors.append(f"{label}.status is invalid: {task.get('status')!r}")

                    for field in ("summary", "trigger", "next_action", "created_at", "updated_at"):
                        if not isinstance(task.get(field), str) or not task[field].strip():
                            errors.append(f"{label}.{field} must be a non-empty string")

                    depends_on = task.get("depends_on")
                    if not isinstance(depends_on, list) or not all(isinstance(item, str) for item in depends_on):
                        errors.append(f"{label}.depends_on must be a string array")
                    else:
                        dependencies.extend((label, item) for item in depends_on)

                    if not isinstance(task.get("requires_fresh_review"), bool):
                        errors.append(f"{label}.requires_fresh_review must be a boolean")
                    safe_file(root, task.get("report_file"), ".html", f"{label}.report_file", errors)

                for label, dependency in dependencies:
                    if dependency not in task_ids:
                        errors.append(f"{label}.depends_on references missing task: {dependency}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", nargs="?", default=".")
    args = parser.parse_args()
    root = Path(args.workspace).expanduser().resolve()

    errors = validate(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    index = json.loads((root / "strategy-memory" / "index.json").read_text(encoding="utf-8"))
    queue = json.loads((root / index["task_queue_file"]).read_text(encoding="utf-8"))
    active_tasks = sum(task["status"] in {"open", "blocked", "scheduled"} for task in queue["tasks"])
    print(
        f"Strategy memory is valid: {len(index['weeks'])} compact week(s), "
        f"{active_tasks} active task(s), user notes configured, "
        f"turnover limit {index['weekly_gross_turnover_limit_pct']}%"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
