#!/usr/bin/env python3
"""Regression tests for validate_skill.py using disposable skill copies."""

from __future__ import annotations

import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Callable

ROOT = Path(__file__).resolve().parents[1]


def run_case(
    name: str,
    mutate: Callable[[Path], None],
    expected_fragment: str | None,
) -> None:
    with tempfile.TemporaryDirectory(prefix=f"lovable-skill-{name}-") as tmp:
        case = Path(tmp) / "skill"
        shutil.copytree(ROOT, case, ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc", ".DS_Store"))
        mutate(case)
        result = subprocess.run(
            ["python3", str(case / "scripts" / "validate_skill.py")],
            capture_output=True,
            text=True,
            check=False,
        )
        output = result.stdout + result.stderr
        if expected_fragment is None:
            if result.returncode != 0:
                raise AssertionError(f"{name} should pass:\n{output}")
            return
        if result.returncode == 0 or expected_fragment not in output:
            raise AssertionError(
                f"{name} should fail with {expected_fragment!r}:\n{output}"
            )


def append(rel: str, value: str) -> Callable[[Path], None]:
    def mutate(root: Path) -> None:
        path = root / rel
        path.write_text(path.read_text(encoding="utf-8") + value, encoding="utf-8")

    return mutate


def replace(rel: str, old: str, new: str) -> Callable[[Path], None]:
    def mutate(root: Path) -> None:
        path = root / rel
        text = path.read_text(encoding="utf-8")
        if old not in text:
            raise AssertionError(f"fixture text not found in {rel}: {old}")
        path.write_text(text.replace(old, new, 1), encoding="utf-8")

    return mutate


def remove(rel: str) -> Callable[[Path], None]:
    return lambda root: (root / rel).unlink()


def main() -> None:
    cases = [
        ("clean", lambda root: None, None),
        (
            "version-drift",
            replace("metadata.json", "2026.09.01", "2026.09.02"),
            "does not mention metadata version",
        ),
        (
            "wrong-origin",
            append("README.md", "\nharness-engineering-coding-agent\n"),
            "wrong canonical repository",
        ),
        (
            "badge-workaround",
            append("README.md", "\n#lovable-badge { display: none; }\n"),
            "badge CSS workaround",
        ),
        (
            "old-incident-deadline",
            append("security-checklist.md", "\nNotificação em 72 horas à ANPD.\n"),
            "obsolete ANPD incident deadline",
        ),
        (
            "missing-experience-spec",
            remove("templates/EXPERIENCE_SPEC.md"),
            "Missing required file",
        ),
        (
            "broken-local-reference",
            append("README.md", "\nVeja `references/missing.md`.\n"),
            "Broken local reference",
        ),
    ]
    for name, mutate, expected in cases:
        run_case(name, mutate, expected)
        print(f"PASS {name}")


if __name__ == "__main__":
    main()
