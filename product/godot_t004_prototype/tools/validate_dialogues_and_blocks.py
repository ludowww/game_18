#!/usr/bin/env python3
"""validate_dialogues_and_blocks.py — T090 standalone validator for Double Vie dialogues/blocs.

Validates active J1→J6 + finale dialogue JSON files, source/prototype copy equality, and
conversation_blocks.json references before continuing expansion.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter, deque
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PROFILE_ROOT = ROOT.parents[1]
DATA_DIR = ROOT / "data"
NARRATIVE_DIR = PROFILE_ROOT / "narrative"
BLOCKS_PATH = DATA_DIR / "conversation_blocks.json"

ACTIVE_DIALOGUES: list[dict[str, Any]] = [
    {"runtime_id": "camille", "conversation_id": "camille_j1_complete", "day": 1, "contact_id": "camille", "prototype": "camille_j1_complete.json", "source": "t007_camille_j1_complete.json"},
    {"runtime_id": "sarah", "conversation_id": "sarah_j1_complete", "day": 1, "contact_id": "sarah", "prototype": "sarah_j1_complete.json", "source": "t037_sarah_j1_complete.json"},
    {"runtime_id": "camille_j2", "conversation_id": "camille_j2_complete", "day": 2, "contact_id": "camille", "prototype": "camille_j2_complete.json", "source": "t061_camille_j2_complete.json"},
    {"runtime_id": "sarah_j2", "conversation_id": "sarah_j2_complete", "day": 2, "contact_id": "sarah", "prototype": "sarah_j2_complete.json", "source": "t062_sarah_j2_complete.json"},
    {"runtime_id": "camille_j3", "conversation_id": "camille_j3_complete", "day": 3, "contact_id": "camille", "prototype": "camille_j3_complete.json", "source": "t075_camille_j3_complete.json"},
    {"runtime_id": "sarah_j3", "conversation_id": "sarah_j3_complete", "day": 3, "contact_id": "sarah", "prototype": "sarah_j3_complete.json", "source": "t076_sarah_j3_complete.json"},
    {"runtime_id": "camille_j4", "conversation_id": "camille_j4_complete", "day": 4, "contact_id": "camille", "prototype": "camille_j4_complete.json", "source": "t092_camille_j4_complete.json"},
    {"runtime_id": "maya_j4", "conversation_id": "maya_j4_complete", "day": 4, "contact_id": "maya", "prototype": "maya_j4_complete.json", "source": "t093_maya_j4_complete.json"},
    {"runtime_id": "ines_j4", "conversation_id": "ines_j4_complete", "day": 4, "contact_id": "ines", "prototype": "ines_j4_complete.json", "source": "t094_ines_j4_complete.json"},
    {"runtime_id": "nico_j4", "conversation_id": "nico_j4_complete", "day": 4, "contact_id": "nico", "prototype": "nico_j4_complete.json", "source": "t095_nico_j4_complete.json"},
    {"runtime_id": "sarah_j5", "conversation_id": "sarah_j5_complete", "day": 5, "contact_id": "sarah", "prototype": "sarah_j5_complete.json", "source": "t107_sarah_j5_complete.json"},
    {"runtime_id": "camille_j5", "conversation_id": "camille_j5_complete", "day": 5, "contact_id": "camille", "prototype": "camille_j5_complete.json", "source": "t108_camille_j5_complete.json"},
    {"runtime_id": "nico_j5", "conversation_id": "nico_j5_complete", "day": 5, "contact_id": "nico", "prototype": "nico_j5_complete.json", "source": "t109_nico_j5_complete.json"},
    {"runtime_id": "maya_j5", "conversation_id": "maya_j5_complete", "day": 5, "contact_id": "maya", "prototype": "maya_j5_complete.json", "source": "t109_maya_j5_complete.json"},
    {"runtime_id": "sarah_j6", "conversation_id": "sarah_j6_complete", "day": 6, "contact_id": "sarah", "prototype": "sarah_j6_complete.json", "source": "t120_sarah_j6_complete.json"},
    {"runtime_id": "camille_j6", "conversation_id": "camille_j6_complete", "day": 6, "contact_id": "camille", "prototype": "camille_j6_complete.json", "source": "t120_camille_j6_complete.json"},
    {"runtime_id": "nico_j6", "conversation_id": "nico_j6_complete", "day": 6, "contact_id": "nico", "prototype": "nico_j6_complete.json", "source": "t121_nico_j6_complete.json"},
    {"runtime_id": "maya_j6", "conversation_id": "maya_j6_complete", "day": 6, "contact_id": "maya", "prototype": "maya_j6_complete.json", "source": "t121_maya_j6_complete.json"},
    {"runtime_id": "ines_j6", "conversation_id": "ines_j6_complete", "day": 6, "contact_id": "ines", "prototype": "ines_j6_complete.json", "source": "t121_ines_j6_complete.json"},
    {"runtime_id": "finales_mvp", "conversation_id": "finales_mvp_complete", "day": 6, "contact_id": "system", "prototype": "finales_mvp_complete.json", "source": "t122_finales_mvp_complete.json"},
]

EXPECTED_BLOCK_ORDER = [
    "camille_c1a", "sarah_s1a", "camille_c1b", "sarah_s1b", "camille_c1c", "sarah_s1c",
    "camille_c2a", "sarah_s2a", "camille_c2b", "sarah_s2b", "camille_c2c", "sarah_s2c",
    "camille_c3a", "sarah_s3a", "camille_c3b", "sarah_s3b", "camille_c3c", "sarah_s3c",
    "camille_c4a", "maya_m4a", "ines_i4a", "nico_n4a",
    "camille_c4b", "maya_m4b", "ines_i4b", "nico_n4b",
    "camille_c4c", "maya_m4c", "ines_i4c", "nico_n4c",
    "sarah_s5a", "camille_c5a", "nico_n5a", "sarah_s5b", "camille_c5b", "maya_m5a", "sarah_s5c", "camille_c5c",
    "sarah_s6a", "camille_c6a", "nico_n6a", "maya_m6a", "sarah_s6b", "camille_c6b", "ines_i6a", "finale_fin",
]

PLACEHOLDER_FILES = [
    DATA_DIR / "camille_j1_intro.json",
    DATA_DIR / "sarah_j1_placeholder.json",
    NARRATIVE_DIR / "t002_dialogue_camille_j1_structured.json",
    NARRATIVE_DIR / "t025a_sarah_j1_placeholder.json",
    NARRATIVE_DIR / "jour_1_mvp.json",
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path, errors: list[str]) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors.append(f"missing file: {path}")
    except json.JSONDecodeError as exc:
        errors.append(f"invalid json: {path}: {exc}")
    return None


def reachable_nodes(nodes: list[dict[str, Any]], start_node: str) -> set[str]:
    by_id = {node.get("id"): node for node in nodes}
    seen: set[str] = set()
    queue: deque[str] = deque([start_node])
    while queue:
        node_id = queue.popleft()
        if node_id in seen or node_id not in by_id:
            continue
        seen.add(node_id)
        node = by_id[node_id]
        nxt = node.get("next")
        if nxt:
            queue.append(str(nxt))
        for choice in node.get("choices", []) or []:
            choice_next = choice.get("next")
            if choice_next:
                queue.append(str(choice_next))
    return seen


def validate_effects(node: dict[str, Any]) -> list[str]:
    invalid: list[str] = []
    for choice in node.get("choices", []) or []:
        effects = choice.get("effects", {})
        if effects is None:
            continue
        if not isinstance(effects, dict):
            invalid.append(f"{choice.get('id', node.get('id'))}: effects is not object")
            continue
        for key, value in effects.items():
            if key == "flags":
                if not isinstance(value, list) or not all(isinstance(flag, str) for flag in value):
                    invalid.append(f"{choice.get('id', node.get('id'))}: flags must be string array")
            elif not isinstance(value, int):
                invalid.append(f"{choice.get('id', node.get('id'))}: effect {key} must be int")
    return invalid


def validate_dialogue(spec: dict[str, Any], errors: list[str]) -> dict[str, Any]:
    prototype_path = DATA_DIR / spec["prototype"]
    source_path = NARRATIVE_DIR / spec["source"]
    data = load_json(prototype_path, errors)
    source = load_json(source_path, errors)
    result: dict[str, Any] = {
        "prototype_path": str(prototype_path.relative_to(PROFILE_ROOT)),
        "source_path": str(source_path.relative_to(PROFILE_ROOT)),
        "schema_version": None,
        "nodes": 0,
        "choices": 0,
        "end_nodes": 0,
        "duplicate_ids": [],
        "missing_targets": [],
        "unreachable_nodes": [],
        "invalid_senders": [],
        "invalid_effects": [],
        "source_copy_match": False,
        "source_sha256": None,
        "prototype_sha256": None,
    }
    if not isinstance(data, dict):
        return result

    result["schema_version"] = data.get("schema_version")
    if data.get("schema_version") != "0.1":
        errors.append(f"{prototype_path.name}: schema_version must remain 0.1")
    if data.get("conversation_id") != spec["conversation_id"]:
        errors.append(f"{prototype_path.name}: conversation_id expected {spec['conversation_id']}, got {data.get('conversation_id')}")
    if data.get("day") != spec["day"]:
        errors.append(f"{prototype_path.name}: day expected {spec['day']}, got {data.get('day')}")
    if data.get("contact_id") != spec["contact_id"]:
        errors.append(f"{prototype_path.name}: contact_id expected {spec['contact_id']}, got {data.get('contact_id')}")

    nodes = data.get("nodes")
    if not isinstance(nodes, list):
        errors.append(f"{prototype_path.name}: nodes must be an array")
        return result
    start_node = data.get("start_node")
    if not isinstance(start_node, str) or not start_node:
        errors.append(f"{prototype_path.name}: start_node must be a non-empty string")
        start_node = ""

    ids = [node.get("id") for node in nodes if isinstance(node, dict)]
    counts = Counter(ids)
    duplicates = sorted([node_id for node_id, count in counts.items() if node_id and count > 1])
    id_set = {node_id for node_id in ids if isinstance(node_id, str)}
    missing: list[list[str]] = []
    invalid_senders: list[list[str]] = []
    invalid_effects: list[str] = []
    allowed_senders = {"player", "system", spec["contact_id"]}
    if spec["runtime_id"] == "finales_mvp":
        allowed_senders.update({"sarah", "camille", "nico", "maya", "ines"})

    for node in nodes:
        if not isinstance(node, dict):
            continue
        node_id = str(node.get("id", "<missing>"))
        if node.get("type") not in {"message", "choice", "end"}:
            errors.append(f"{prototype_path.name}: {node_id}: invalid type {node.get('type')}")
        sender = node.get("sender")
        if sender is not None and sender not in allowed_senders:
            invalid_senders.append([node_id, str(sender)])
        nxt = node.get("next", "")
        if nxt and nxt not in id_set:
            missing.append([node_id, str(nxt)])
        for choice in node.get("choices", []) or []:
            choice_id = str(choice.get("id", node_id))
            choice_next = choice.get("next", "")
            if choice_next and choice_next not in id_set:
                missing.append([choice_id, str(choice_next)])
        invalid_effects.extend(validate_effects(node))

    reached = reachable_nodes(nodes, start_node) if start_node else set()
    unreachable = sorted(id_set - reached)
    choice_count = len([node for node in nodes if isinstance(node, dict) and node.get("type") == "choice"])
    end_count = len([node for node in nodes if isinstance(node, dict) and node.get("type") == "end"])

    result.update({
        "nodes": len(nodes),
        "choices": choice_count,
        "end_nodes": end_count,
        "duplicate_ids": duplicates,
        "missing_targets": missing,
        "unreachable_nodes": unreachable,
        "invalid_senders": invalid_senders,
        "invalid_effects": invalid_effects,
    })
    for issue_name in ["duplicate_ids", "missing_targets", "unreachable_nodes", "invalid_senders", "invalid_effects"]:
        if result[issue_name]:
            errors.append(f"{prototype_path.name}: {issue_name}: {result[issue_name]}")
    if start_node and start_node not in id_set:
        errors.append(f"{prototype_path.name}: start_node not found: {start_node}")
    if choice_count <= 0 or end_count <= 0:
        errors.append(f"{prototype_path.name}: expected at least one choice and one end node")

    if isinstance(source, dict):
        result["source_sha256"] = sha256(source_path)
        result["prototype_sha256"] = sha256(prototype_path)
        result["source_copy_match"] = result["source_sha256"] == result["prototype_sha256"]
        if not result["source_copy_match"]:
            errors.append(f"source/prototype mismatch: {source_path.name} != {prototype_path.name}")
    return result


def validate_blocks(dialogue_by_runtime: dict[str, dict[str, Any]], errors: list[str]) -> tuple[dict[str, Any], list[str]]:
    warnings: list[str] = []
    config = load_json(BLOCKS_PATH, errors)
    if not isinstance(config, dict):
        return {}, warnings
    block_order = config.get("block_order", [])
    blocks = config.get("blocks", {})
    if config.get("schema_version") != "0.1":
        errors.append("conversation_blocks.json: schema_version must remain 0.1")
    if block_order != EXPECTED_BLOCK_ORDER:
        errors.append(f"conversation_blocks.json: unexpected J1→J6 + finale block order: {block_order}")
    if not isinstance(blocks, dict):
        errors.append("conversation_blocks.json: blocks must be an object")
        return config, warnings
    order_counts = Counter(block_order)
    duplicate_blocks = sorted([block_id for block_id, count in order_counts.items() if count > 1])
    if duplicate_blocks:
        errors.append(f"conversation_blocks.json: duplicate block ids in order: {duplicate_blocks}")
    missing_defs = [block_id for block_id in block_order if block_id not in blocks]
    extra_defs = [block_id for block_id in blocks if block_id not in block_order]
    if missing_defs:
        errors.append(f"conversation_blocks.json: missing block definitions: {missing_defs}")
    if extra_defs:
        warnings.append(f"conversation_blocks.json: block definitions outside order: {extra_defs}")

    for block_id in block_order:
        block = blocks.get(block_id, {})
        if not isinstance(block, dict):
            errors.append(f"conversation_blocks.json: {block_id}: block must be object")
            continue
        conversation_id = block.get("conversation_id")
        if conversation_id not in dialogue_by_runtime:
            errors.append(f"conversation_blocks.json: {block_id}: unknown conversation_id {conversation_id}")
            continue
        dialogue_ids = dialogue_by_runtime[conversation_id]["ids"]
        start_node = block.get("start_node")
        if start_node not in dialogue_ids:
            errors.append(f"conversation_blocks.json: {block_id}: missing start_node {start_node}")
        end_nodes = block.get("end_nodes")
        if not isinstance(end_nodes, list) or not end_nodes:
            errors.append(f"conversation_blocks.json: {block_id}: end_nodes must be non-empty array")
        else:
            for end_node in end_nodes:
                if end_node not in dialogue_ids:
                    errors.append(f"conversation_blocks.json: {block_id}: missing end_node {end_node}")
        unlock = block.get("unlock_on_done", "")
        if unlock and unlock not in blocks:
            errors.append(f"conversation_blocks.json: {block_id}: unlock_on_done unknown block {unlock}")
        notification_target = block.get("notification_target", "")
        if notification_target and notification_target not in dialogue_by_runtime:
            errors.append(f"conversation_blocks.json: {block_id}: notification_target unknown conversation {notification_target}")
        if block.get("contact_id") not in {"camille", "sarah", "maya", "ines", "nico", "system"}:
            errors.append(f"conversation_blocks.json: {block_id}: invalid contact_id {block.get('contact_id')}")

    return config, warnings


def build_report() -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []
    dialogues: dict[str, Any] = {}
    dialogue_by_runtime: dict[str, dict[str, Any]] = {}

    for spec in ACTIVE_DIALOGUES:
        result = validate_dialogue(spec, errors)
        dialogues[spec["conversation_id"]] = result
        path = DATA_DIR / spec["prototype"]
        data = load_json(path, errors)
        ids = {node.get("id") for node in data.get("nodes", [])} if isinstance(data, dict) else set()
        dialogue_by_runtime[spec["runtime_id"]] = {"ids": ids, "conversation_id": spec["conversation_id"]}

    blocks_config, block_warnings = validate_blocks(dialogue_by_runtime, errors)
    warnings.extend(block_warnings)
    for placeholder in PLACEHOLDER_FILES:
        if placeholder.exists():
            warnings.append(f"placeholder/non-active dialogue not blocking: {placeholder.relative_to(PROFILE_ROOT)}")

    report = {
        "ok": not errors,
        "errors": errors,
        "warnings": warnings,
        "active_dialogues": [spec["conversation_id"] for spec in ACTIVE_DIALOGUES],
        "dialogues": dialogues,
        "block_order": blocks_config.get("block_order", []) if isinstance(blocks_config, dict) else [],
        "counts": {
            "dialogues": len(ACTIVE_DIALOGUES),
            "blocks": len(blocks_config.get("blocks", {})) if isinstance(blocks_config, dict) else 0,
            "warnings": len(warnings),
            "errors": len(errors),
        },
    }
    return report


def print_text_report(report: dict[str, Any]) -> None:
    status = "OK" if report["ok"] else "FAILED"
    print(f"T090 dialogue/block validation: {status}")
    print(f"Active dialogues: {report['counts']['dialogues']} | Blocks: {report['counts']['blocks']} | Warnings: {report['counts']['warnings']} | Errors: {report['counts']['errors']}")
    for conversation_id, dialogue in report["dialogues"].items():
        print(
            f"- {conversation_id}: nodes={dialogue['nodes']} choices={dialogue['choices']} "
            f"end={dialogue['end_nodes']} source_copy_match={dialogue['source_copy_match']}"
        )
    if report["warnings"]:
        print("Warnings:")
        for warning in report["warnings"]:
            print(f"- {warning}")
    if report["errors"]:
        print("Errors:", file=sys.stderr)
        for error in report["errors"]:
            print(f"- {error}", file=sys.stderr)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="validate_dialogues_and_blocks.py",
        description="Validate active Double Vie J1→J6 + finale dialogue JSON files and conversation_blocks.json.",
    )
    parser.add_argument("--json", action="store_true", help="print machine-readable JSON report")
    args = parser.parse_args(argv)

    report = build_report()
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
    else:
        print_text_report(report)
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
