#!/usr/bin/env python3
from pathlib import Path
import json

# Configuration
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".PNG", ".JPG", ".JPEG"}
BEFORE_SUFFIX = "_before"
AFTER_SUFFIX = "_after"

def build_sets_for_member(member_name: str, member_dir: Path):
    """
    Scan one member folder (e.g. images/Narmilan) and return a list of
    {id, before, after} dicts for complete pairs.
    """
    pairs = {}

    for path in member_dir.iterdir():
        if not path.is_file():
            continue

        ext = path.suffix
        if ext not in IMAGE_EXTENSIONS:
            continue

        stem = path.stem  # filename without extension

        if stem.endswith(BEFORE_SUFFIX):
            base_id = stem[: -len(BEFORE_SUFFIX)]
            pairs.setdefault(base_id, {})["before"] = f"images/{member_name}/{path.name}"
        elif stem.endswith(AFTER_SUFFIX):
            base_id = stem[: -len(AFTER_SUFFIX)]
            pairs.setdefault(base_id, {})["after"] = f"images/{member_name}/{path.name}"
        else:
            # Doesn't match XXXX_before / XXXX_after pattern, ignore
            continue

    # Keep only complete before+after pairs
    sets = []
    for base_id, data in pairs.items():
        before = data.get("before")
        after = data.get("after")
        if before and after:
            sets.append(
                {
                    "id": base_id,
                    "before": before,
                    "after": after,
                }
            )

    # Sort by id for stable ordering
    sets.sort(key=lambda s: s["id"])
    return sets


def main():
    repo_root = Path(__file__).resolve().parent
    images_dir = repo_root / "images"
    output_file = images_dir / "sets.json"

    if not images_dir.is_dir():
        raise SystemExit(f"Images directory not found: {images_dir}")

    groups = []

    # Each subdirectory inside images/ is treated as one group (member)
    for member_dir in sorted(images_dir.iterdir()):
        if not member_dir.is_dir():
            continue

        member_name = member_dir.name  # e.g. "Narmilan"
        member_sets = build_sets_for_member(member_name, member_dir)

        if member_sets:
            groups.append(
                {
                    "name": member_name,
                    "sets": member_sets,
                }
            )

    output = {"groups": groups}

    output_file.parent.mkdir(parents=True, exist_ok=True)
    with output_file.open("w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    print(f"Wrote {sum(len(g['sets']) for g in groups)} sets across {len(groups)} groups to {output_file}")


if __name__ == "__main__":
    main()
