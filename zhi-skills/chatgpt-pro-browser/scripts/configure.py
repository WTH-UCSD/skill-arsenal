#!/usr/bin/env python3
"""Create the host-local ChatGPT Project routing reference."""

from __future__ import annotations

import argparse
import json
import os
import tempfile
import tomllib
from pathlib import Path
from urllib.parse import urlparse


SKILL_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DESTINATION = SKILL_ROOT / "references" / "project.local.toml"


def project_from_toml(path: Path) -> tuple[str, str]:
    with path.open("rb") as handle:
        data = tomllib.load(handle)
    project = data.get("project")
    if not isinstance(project, dict):
        raise ValueError(f"{path} has no [project] table")
    return str(project.get("url", "")).strip(), str(project.get("name", "")).strip()


def validate(url: str, name: str) -> None:
    parsed = urlparse(url)
    if parsed.scheme != "https" or not parsed.netloc:
        raise ValueError("project URL must be a nonempty absolute HTTPS URL")
    hostname = (parsed.hostname or "").lower()
    if hostname != "chatgpt.com" and not hostname.endswith(".chatgpt.com"):
        raise ValueError("project URL must use chatgpt.com or one of its subdomains")
    if not name:
        raise ValueError("visible project name must be nonempty")


def render(url: str, name: str) -> str:
    return (
        "[project]\n"
        f"name = {json.dumps(name, ensure_ascii=False)}\n"
        f"url = {json.dumps(url, ensure_ascii=False)}\n"
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--from-toml", type=Path)
    parser.add_argument("--project-url")
    parser.add_argument("--project-name")
    parser.add_argument("--destination", type=Path, default=DEFAULT_DESTINATION)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    source_url = ""
    source_name = ""
    if args.from_toml:
        source_url, source_name = project_from_toml(args.from_toml.expanduser())

    url = (args.project_url or source_url).strip()
    name = (args.project_name or source_name).strip()
    validate(url, name)

    destination = args.destination.expanduser().resolve()
    expected = {"project": {"name": name, "url": url}}
    if destination.exists() and not args.force:
        with destination.open("rb") as handle:
            if tomllib.load(handle) == expected:
                os.chmod(destination, 0o600)
                print(f"Configuration already valid: {destination}")
                return 0
        raise FileExistsError(f"{destination} exists with different values; use --force to replace it")

    destination.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary_name = tempfile.mkstemp(prefix=".project.", suffix=".toml", dir=destination.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(render(url, name))
        os.chmod(temporary_name, 0o600)
        os.replace(temporary_name, destination)
    finally:
        if os.path.exists(temporary_name):
            os.unlink(temporary_name)

    print(f"Wrote validated local configuration: {destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
