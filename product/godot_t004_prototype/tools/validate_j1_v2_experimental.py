#!/usr/bin/env python3
"""Validate experimental J1 V2 dialogue JSON files.

This validator is intentionally separate from the active runtime validator because
J1 V2 files are not yet wired into conversation_blocks.json.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
SCHEMA_PATH = DATA / "schema" / "variables_and_flags_schema.json"
FILES = [
    DATA / "j1_00_reveil_messages_v2_experimental.json",
    DATA / "sarah_j1_v2_experimental.json",
    DATA / "camille_j1_v2_experimental.json",
    DATA / "nico_j1_v2_experimental.json",
    DATA / "maya_j1_v2_experimental.json",
    DATA / "ines_j1_v2_experimental.json",
    DATA / "sarah_meal_j1_v2_experimental.json",
    DATA / "nico_respiration_j1_v2_experimental.json",
]


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def main() -> int:
    schema = load_json(SCHEMA_PATH)
    official_variables = set(schema["official_variables"].keys())
    known_flags = {
        flag
        for flags in schema.get("flag_groups", {}).values()
        for flag in flags
    }

    errors: list[str] = []
    summaries: list[str] = []

    for path in FILES:
        if not path.exists():
            errors.append(f"missing file: {path}")
            continue

        data = load_json(path)
        nodes = data.get("nodes", [])
        node_ids = [str(node.get("id", "")) for node in nodes]
        node_id_set = set(node_ids)

        if len(node_ids) != len(node_id_set):
            errors.append(f"{path.name}: duplicate node ids")

        start_node = str(data.get("start_node", ""))
        if start_node not in node_id_set:
            errors.append(f"{path.name}: start_node missing: {start_node}")

        for node in nodes:
            node_id = str(node.get("id", ""))
            node_type = str(node.get("type", "message"))

            next_id = str(node.get("next", ""))
            if next_id and next_id not in node_id_set:
                errors.append(f"{path.name}: {node_id} next missing target {next_id}")

            if node_type == "choice":
                choices = node.get("choices", [])
                if not choices:
                    errors.append(f"{path.name}: {node_id} choice node has no choices")
                for choice in choices:
                    choice_id = str(choice.get("id", ""))
                    target = str(choice.get("next", ""))
                    if target not in node_id_set:
                        errors.append(f"{path.name}: {choice_id} choice next missing target {target}")
                    effects = choice.get("effects", {})
                    if not isinstance(effects, dict):
                        errors.append(f"{path.name}: {choice_id} effects is not dict")
                        continue
                    for key, value in effects.items():
                        if key == "flags":
                            if not isinstance(value, list):
                                errors.append(f"{path.name}: {choice_id} flags is not list")
                                continue
                            for flag in value:
                                if flag not in known_flags:
                                    errors.append(f"{path.name}: {choice_id} unknown flag {flag}")
                        elif key not in official_variables:
                            errors.append(f"{path.name}: {choice_id} unknown variable {key}")
                        elif not isinstance(value, (int, float)):
                            errors.append(f"{path.name}: {choice_id} non-numeric effect {key}={value!r}")

        choices_count = sum(1 for node in nodes if node.get("type") == "choice")
        end_count = sum(1 for node in nodes if node.get("type") == "end")
        summaries.append(f"- {path.name}: nodes={len(nodes)} choices={choices_count} end={end_count}")

    if errors:
        print("J1 V2 experimental validation: FAIL")
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("J1 V2 experimental validation: OK")
    for summary in summaries:
        print(summary)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
