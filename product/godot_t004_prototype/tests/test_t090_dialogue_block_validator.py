from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "tools" / "validate_dialogues_and_blocks.py"


def run_validator() -> dict:
    completed = subprocess.run(
        [sys.executable, str(VALIDATOR), "--json"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
    )
    return json.loads(completed.stdout)


def test_t090_standalone_validator_reports_all_active_j1_j3_dialogues_and_blocks() -> None:
    assert VALIDATOR.exists(), "T090 standalone validator is missing"

    report = run_validator()

    assert report["ok"] is True
    assert report["errors"] == []
    assert report["active_dialogues"] == [
        "camille_j1_complete",
        "sarah_j1_complete",
        "camille_j2_complete",
        "sarah_j2_complete",
        "camille_j3_complete",
        "sarah_j3_complete",
        "camille_j4_complete",
        "maya_j4_complete",
        "ines_j4_complete",
        "nico_j4_complete",
        "sarah_j5_complete",
        "camille_j5_complete",
        "nico_j5_complete",
        "maya_j5_complete",
        "sarah_j6_complete",
        "camille_j6_complete",
        "nico_j6_complete",
        "maya_j6_complete",
        "ines_j6_complete",
        "finales_mvp_complete",
    ]
    assert report["counts"]["dialogues"] == 20
    assert report["counts"]["blocks"] == 46
    assert report["counts"]["warnings"] >= 1
    assert report["block_order"] == [
        "camille_c1a", "sarah_s1a", "camille_c1b", "sarah_s1b", "camille_c1c", "sarah_s1c",
        "camille_c2a", "sarah_s2a", "camille_c2b", "sarah_s2b", "camille_c2c", "sarah_s2c",
        "camille_c3a", "sarah_s3a", "camille_c3b", "sarah_s3b", "camille_c3c", "sarah_s3c",
        "camille_c4a", "maya_m4a", "ines_i4a", "nico_n4a", "camille_c4b", "maya_m4b",
        "ines_i4b", "nico_n4b", "camille_c4c", "maya_m4c", "ines_i4c", "nico_n4c",
        "sarah_s5a", "camille_c5a", "nico_n5a", "sarah_s5b", "camille_c5b", "maya_m5a",
        "sarah_s5c", "camille_c5c", "sarah_s6a", "camille_c6a", "nico_n6a", "maya_m6a",
        "sarah_s6b", "camille_c6b", "ines_i6a", "finale_fin",
    ]

    for conversation_id in report["active_dialogues"]:
        dialogue = report["dialogues"][conversation_id]
        assert dialogue["schema_version"] == "0.1"
        assert dialogue["missing_targets"] == []
        assert dialogue["duplicate_ids"] == []
        assert dialogue["unreachable_nodes"] == []
        assert dialogue["invalid_senders"] == []
        assert dialogue["invalid_effects"] == []
        assert dialogue["source_copy_match"] is True
        assert dialogue["nodes"] > 0
        assert dialogue["choices"] > 0
        assert dialogue["end_nodes"] > 0


def test_t090_validator_help_documents_standalone_usage() -> None:
    completed = subprocess.run(
        [sys.executable, str(VALIDATOR), "--help"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
    )
    assert "validate_dialogues_and_blocks.py" in completed.stdout
    assert "--json" in completed.stdout


if __name__ == "__main__":
    test_t090_standalone_validator_reports_all_active_j1_j3_dialogues_and_blocks()
    test_t090_validator_help_documents_standalone_usage()
    print("T090 dialogue/block validator tests OK")
