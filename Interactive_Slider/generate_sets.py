#!/usr/bin/env python3
from pathlib import Path
import json

# Valid extensions and name suffixes
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".PNG", ".JPG", ".JPEG"}
BEFORE_SUFFIX = "_before"
AFTER_SUFFIX = "_after"

# Optional: fixed tab order
MEMBER_ORDER = ["Narmilan", "Fernando", "Veronica", "Sebastien", "Anuraj"]


def build_sets_for_member(member_name: str, member_dir: Path):
    """
    Scan one member folder (e.g. images/Narmilan) and return a list of
    {id, before, after} dictionaries for complete before/after pairs.
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
            # Doesn't match XXXX_before / XXXX_after pattern
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

    # Stable ordering
    sets.sort(key=lambda s: s["id"])
    return sets


def main():
    # This file lives in Interactive_Slider/, so repo_root is that folder
    repo_root = Path(__file__).resolve().parent
    images_dir = repo_root / "images"
    output_file = images_dir / "sets.json"

    if not images_dir.is_dir():
        raise SystemExit(f"Images directory not found: {images_dir}")

    groups = []

    used = set()

    # 1) Add known members in fixed order if folder exists
    for member_name in MEMBER_ORDER:
        member_dir = images_dir / member_name
        if member_dir.is_dir():
            member_sets = build_sets_for_member(member_name, member_dir)
            if member_sets:
                groups.append({"name": member_name, "sets": member_sets})
                used.add(member_name)

    # 2) Add any other folders (for extra people)
    for member_dir in sorted(images_dir.iterdir()):
        if not member_dir.is_dir():
            continue
        member_name = member_dir.name
        if member_name in used:
            continue
        member_sets = build_sets_for_member(member_name, member_dir)
        if member_sets:
            groups.append({"name": member_name, "sets": member_sets})

    output = {"groups": groups}

    output_file.parent.mkdir(parents=True, exist_ok=True)
    with output_file.open("w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    total_sets = sum(len(g["sets"]) for g in groups)
    print(f"Wrote {total_sets} sets across {len(groups)} groups to {output_file}")


if __name__ == "__main__":
    main()
