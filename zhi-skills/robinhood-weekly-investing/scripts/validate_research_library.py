#!/usr/bin/env python3
"""Validate the public-only ticker research library."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


INDEX_FIELDS = {"schema_version", "timezone", "updated_at", "tickers"}
TICKER_FIELDS = {
    "symbol",
    "company_name",
    "research_status",
    "coverage_status",
    "themes",
    "dossier_file",
    "source_ledger_file",
    "latest_snapshot_file",
    "latest_artifact_file",
    "last_material_update",
    "next_review_due",
}
SOURCE_FIELDS = {
    "source_id",
    "symbol",
    "title",
    "url",
    "publisher",
    "published_at",
    "event_date",
    "retrieved_at",
    "access",
    "tier",
    "claim_type",
    "disclosed_position_or_conflict",
    "original_source_id",
    "verification_status",
    "note",
    "local_artifact_path",
}

RESEARCH_STATUSES = {"active", "watch", "screened", "archived"}
COVERAGE_STATUSES = {"baseline", "wave1", "wave2_partial", "wave2_complete"}
ACCESS_STATES = {"public", "partial", "paywalled", "login_only", "unavailable", "user_provided"}
TIERS = {"P0", "P1", "P2", "P3"}
CLAIM_TYPES = {"fact", "estimate", "interpretation", "opinion", "rumor", "sentiment"}
VERIFICATION_STATES = {"primary", "verified", "corroborated", "unverified", "conflicted", "stale"}
ARTIFACT_SUFFIXES = {".html", ".md", ".pdf", ".txt", ".csv", ".json"}

SYMBOL_RE = re.compile(r"^[A-Z][A-Z0-9.-]{0,9}$")
SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
SOURCE_ID_RE = re.compile(r"^[a-z0-9][a-z0-9._-]*$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
URL_RE = re.compile(r"^https?://", re.IGNORECASE)
MAX_DOSSIER_WORDS = 2000
MAX_SNAPSHOT_WORDS = 900


def inside(root: Path, path: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
    except ValueError:
        return False
    return True


def safe_file(
    root: Path,
    value: object,
    suffixes: set[str],
    label: str,
    errors: list[str],
) -> Path | None:
    if not isinstance(value, str) or not value:
        errors.append(f"{label} must be a non-empty relative path")
        return None
    relative = Path(value)
    if relative.is_absolute() or ".." in relative.parts:
        errors.append(f"{label} must stay inside the workspace: {value}")
        return None
    path = root / relative
    if not inside(root, path):
        errors.append(f"{label} escapes the workspace: {value}")
        return None
    if path.suffix.lower() not in suffixes:
        errors.append(f"{label} has an unsupported suffix: {value}")
        return None
    if not path.is_file():
        errors.append(f"{label} does not exist: {value}")
        return None
    return path


def valid_date_or_null(value: object) -> bool:
    return value is None or isinstance(value, str) and bool(DATE_RE.fullmatch(value))


def word_count(path: Path) -> int:
    return len(re.findall(r"\b[\w'-]+\b", path.read_text(encoding="utf-8")))


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    index_path = root / "research-library" / "index.json"
    try:
        data = json.loads(index_path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return [f"missing research index: {index_path}"]
    except json.JSONDecodeError as exc:
        return [f"invalid JSON at {index_path}:{exc.lineno}:{exc.colno}: {exc.msg}"]

    if not isinstance(data, dict):
        return ["research index root must be a JSON object"]
    missing = INDEX_FIELDS - data.keys()
    if missing:
        errors.append(f"research index missing fields: {', '.join(sorted(missing))}")
    if data.get("schema_version") != 1:
        errors.append("research index schema_version must be 1")
    if not isinstance(data.get("timezone"), str) or not data["timezone"].strip():
        errors.append("research index timezone must be a non-empty string")
    if not isinstance(data.get("updated_at"), str) or not data["updated_at"].strip():
        errors.append("research index updated_at must be a non-empty string")

    tickers = data.get("tickers")
    if not isinstance(tickers, list):
        errors.append("research index tickers must be an array")
        return errors

    symbols: list[str] = []
    source_ids: set[str] = set()
    for position, ticker in enumerate(tickers):
        label = f"tickers[{position}]"
        if not isinstance(ticker, dict):
            errors.append(f"{label} must be an object")
            continue
        missing = TICKER_FIELDS - ticker.keys()
        if missing:
            errors.append(f"{label} missing fields: {', '.join(sorted(missing))}")

        symbol = ticker.get("symbol")
        if not isinstance(symbol, str) or not SYMBOL_RE.fullmatch(symbol):
            errors.append(f"{label}.symbol is invalid: {symbol!r}")
            continue
        if symbol in symbols:
            errors.append(f"duplicate ticker symbol: {symbol}")
        symbols.append(symbol)

        if not isinstance(ticker.get("company_name"), str) or not ticker["company_name"].strip():
            errors.append(f"{label}.company_name must be a non-empty string")
        if ticker.get("research_status") not in RESEARCH_STATUSES:
            errors.append(f"{label}.research_status is invalid: {ticker.get('research_status')!r}")
        if ticker.get("coverage_status") not in COVERAGE_STATUSES:
            errors.append(f"{label}.coverage_status is invalid: {ticker.get('coverage_status')!r}")

        themes = ticker.get("themes")
        if not isinstance(themes, list) or not themes or not all(
            isinstance(theme, str) and SLUG_RE.fullmatch(theme) for theme in themes
        ):
            errors.append(f"{label}.themes must be a non-empty array of lowercase slugs")
        if not valid_date_or_null(ticker.get("last_material_update")) or ticker.get("last_material_update") is None:
            errors.append(f"{label}.last_material_update must be YYYY-MM-DD")
        if not valid_date_or_null(ticker.get("next_review_due")):
            errors.append(f"{label}.next_review_due must be null or YYYY-MM-DD")

        expected_root = Path("research-library") / "tickers" / symbol
        dossier = safe_file(root, ticker.get("dossier_file"), {".md"}, f"{label}.dossier_file", errors)
        ledger = safe_file(root, ticker.get("source_ledger_file"), {".jsonl"}, f"{label}.source_ledger_file", errors)
        snapshot = safe_file(root, ticker.get("latest_snapshot_file"), {".md"}, f"{label}.latest_snapshot_file", errors)

        for field, path in (("dossier_file", dossier), ("source_ledger_file", ledger), ("latest_snapshot_file", snapshot)):
            if path and Path(ticker[field]).parent != expected_root and expected_root not in Path(ticker[field]).parents:
                errors.append(f"{label}.{field} must stay under {expected_root}")

        if dossier and word_count(dossier) > MAX_DOSSIER_WORDS:
            errors.append(f"{label}.dossier_file exceeds {MAX_DOSSIER_WORDS} words")
        if snapshot and word_count(snapshot) > MAX_SNAPSHOT_WORDS:
            errors.append(f"{label}.latest_snapshot_file exceeds {MAX_SNAPSHOT_WORDS} words")

        artifact_value = ticker.get("latest_artifact_file")
        if artifact_value is not None:
            artifact = safe_file(root, artifact_value, ARTIFACT_SUFFIXES, f"{label}.latest_artifact_file", errors)
            if artifact and expected_root not in Path(artifact_value).parents:
                errors.append(f"{label}.latest_artifact_file must stay under {expected_root}")

        if ledger:
            records = 0
            for line_number, raw in enumerate(ledger.read_text(encoding="utf-8").splitlines(), 1):
                if not raw.strip():
                    continue
                records += 1
                source_label = f"{ticker['source_ledger_file']}:{line_number}"
                try:
                    source = json.loads(raw)
                except json.JSONDecodeError as exc:
                    errors.append(f"invalid JSON at {source_label}:{exc.colno}: {exc.msg}")
                    continue
                if not isinstance(source, dict):
                    errors.append(f"{source_label} must be a JSON object")
                    continue
                missing_source = SOURCE_FIELDS - source.keys()
                if missing_source:
                    errors.append(f"{source_label} missing fields: {', '.join(sorted(missing_source))}")

                source_id = source.get("source_id")
                if not isinstance(source_id, str) or not SOURCE_ID_RE.fullmatch(source_id):
                    errors.append(f"{source_label}.source_id is invalid: {source_id!r}")
                elif source_id in source_ids:
                    errors.append(f"duplicate source_id: {source_id}")
                else:
                    source_ids.add(source_id)

                if source.get("symbol") != symbol:
                    errors.append(f"{source_label}.symbol must be {symbol}")
                for field in ("title", "publisher", "disclosed_position_or_conflict", "note"):
                    if not isinstance(source.get(field), str) or not source[field].strip():
                        errors.append(f"{source_label}.{field} must be a non-empty string")
                url = source.get("url")
                if url is not None and (not isinstance(url, str) or not URL_RE.match(url)):
                    errors.append(f"{source_label}.url must be null or an http(s) URL")
                for field in ("published_at", "event_date"):
                    if not valid_date_or_null(source.get(field)):
                        errors.append(f"{source_label}.{field} must be null or YYYY-MM-DD")
                if not isinstance(source.get("retrieved_at"), str) or not DATE_RE.fullmatch(source["retrieved_at"]):
                    errors.append(f"{source_label}.retrieved_at must be YYYY-MM-DD")
                if source.get("access") not in ACCESS_STATES:
                    errors.append(f"{source_label}.access is invalid")
                if source.get("tier") not in TIERS:
                    errors.append(f"{source_label}.tier is invalid")
                if source.get("claim_type") not in CLAIM_TYPES:
                    errors.append(f"{source_label}.claim_type is invalid")
                if source.get("verification_status") not in VERIFICATION_STATES:
                    errors.append(f"{source_label}.verification_status is invalid")
                ancestry = source.get("original_source_id")
                if ancestry is not None and (not isinstance(ancestry, str) or not SOURCE_ID_RE.fullmatch(ancestry)):
                    errors.append(f"{source_label}.original_source_id is invalid")
                local = source.get("local_artifact_path")
                if local is not None:
                    safe_file(root, local, ARTIFACT_SUFFIXES, f"{source_label}.local_artifact_path", errors)

            if records == 0:
                errors.append(f"{label}.source_ledger_file must contain at least one source")

    if symbols != sorted(symbols):
        errors.append("research index tickers must be sorted by symbol")
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

    data = json.loads((root / "research-library" / "index.json").read_text(encoding="utf-8"))
    active = sum(ticker["research_status"] in {"active", "watch"} for ticker in data["tickers"])
    print(f"Research library is valid: {len(data['tickers'])} ticker(s), {active} active/watch dossier(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
