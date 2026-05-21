from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
CONVERSATION_SCREEN = ROOT / "scripts" / "conversation_screen.gd"
J1_V2_FILES = sorted(DATA.glob("*j1_v2_experimental.json"))


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def node_map(data: dict) -> dict:
    return {node["id"]: node for node in data["nodes"]}


def predecessors(nodes: dict, target_id: str) -> list[dict]:
    result = []
    for node in nodes.values():
        if node.get("next") == target_id:
            result.append(node)
        for choice in node.get("choices", []):
            if choice.get("next") == target_id:
                result.append(node)
    return result


def test_t141_message_bubbles_do_not_prefix_sender_names() -> None:
    source = CONVERSATION_SCREEN.read_text(encoding="utf-8")
    assert "label.text = text" in source
    assert "label.text = _display_sender(sender) + text" not in source


def test_t141_choice_click_skips_duplicate_player_node_text() -> None:
    source = CONVERSATION_SCREEN.read_text(encoding="utf-8")
    assert "_choice_text_is_repeated_by_next_player_node" in source
    assert "if not _choice_text_is_repeated_by_next_player_node(choice, next_id):" in source
    assert re.search(r"sender.*player", source)
    assert re.search(r"strip_edges\(\).*==.*strip_edges\(\)", source)


def test_t141_auto_player_nodes_follow_convention_and_threading() -> None:
    assert J1_V2_FILES
    for path in J1_V2_FILES:
        data = load_json(path)
        nodes = node_map(data)
        for node_id, node in nodes.items():
            if "_auto_player_" not in node_id:
                continue
            assert node["type"] == "message", (path.name, node_id)
            assert node["sender"] == "player", (path.name, node_id)
            assert "effects" not in node, (path.name, node_id)
            assert "choices" not in node, (path.name, node_id)

            incoming = predecessors(nodes, node_id)
            assert incoming, (path.name, node_id, "auto player node must be reached by previous message")
            assert all(prev.get("type") == "message" for prev in incoming), (path.name, node_id)
            assert all(prev.get("sender") not in ("player", "system") for prev in incoming), (path.name, node_id)

            next_id = node.get("next", "")
            assert next_id in nodes, (path.name, node_id, "auto player node must lead to an existing node")
            next_node = nodes[next_id]
            assert next_node.get("sender") != "player" or next_node.get("type") == "choice", (path.name, node_id, next_id)
            assert next_node.get("type") == "choice" or next_node.get("sender") != "player", (path.name, node_id, next_id)


def test_t141_choice_to_identical_player_node_duplicates_are_data_supported() -> None:
    duplicate_supported = []
    for path in J1_V2_FILES:
        data = load_json(path)
        nodes = node_map(data)
        for node in nodes.values():
            if node.get("type") != "choice":
                continue
            for choice in node.get("choices", []):
                next_node = nodes.get(choice.get("next"))
                if (
                    next_node
                    and next_node.get("sender") == "player"
                    and next_node.get("text", "").strip() == choice.get("text", "").strip()
                ):
                    duplicate_supported.append((path.name, node["id"], choice["id"], next_node["id"]))
    assert duplicate_supported, "T141 guard should cover existing choice->player duplicate patterns"


if __name__ == "__main__":
    test_t141_message_bubbles_do_not_prefix_sender_names()
    test_t141_choice_click_skips_duplicate_player_node_text()
    test_t141_auto_player_nodes_follow_convention_and_threading()
    test_t141_choice_to_identical_player_node_duplicates_are_data_supported()
    print("T141 J1 V2 conversation UX tests OK")
