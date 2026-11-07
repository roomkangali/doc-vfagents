"""Verify the published VFA dossier's file list and SHA-256 digests.

This utility checks archive integrity. It does not repeat scans or checker tests.
"""

from __future__ import annotations

import hashlib
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parent
    manifest = root / "SHA256SUMS"
    if not manifest.is_file():
        print("Missing SHA256SUMS")
        return 1

    expected: dict[Path, str] = {}
    errors: list[str] = []
    for number, line in enumerate(manifest.read_text(encoding="utf-8").splitlines(), 1):
        try:
            digest, relative = line.split("  ", 1)
            path = Path(relative)
            if len(digest) != 64 or any(c not in "0123456789abcdef" for c in digest):
                raise ValueError("invalid SHA-256 digest")
            if path.is_absolute() or ".." in path.parts or path.name == "SHA256SUMS":
                raise ValueError("unsafe file path")
            if path in expected:
                raise ValueError("duplicate file path")
            expected[path] = digest
        except ValueError as error:
            errors.append(f"SHA256SUMS line {number}: {error}")

    actual: set[Path] = set()
    for path in root.rglob("*"):
        if not path.is_file() or path == manifest:
            continue
        relative = path.relative_to(root)
        if relative.parts[0] == ".git":
            continue
        actual.add(relative)
    for path in sorted(expected.keys() - actual):
        errors.append(f"missing file: {path}")
    for path in sorted(actual - expected.keys()):
        errors.append(f"unlisted file: {path}")
    for path in sorted(actual & expected.keys()):
        full_path = root / path
        if full_path.is_symlink():
            errors.append(f"symbolic link not allowed: {path}")
            continue
        digest = hashlib.sha256(full_path.read_bytes()).hexdigest()
        if digest != expected[path]:
            errors.append(f"SHA-256 mismatch: {path}")

    if errors:
        for error in errors:
            print(error)
        return 1
    print(f"Verified {len(expected)} files against SHA256SUMS.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
