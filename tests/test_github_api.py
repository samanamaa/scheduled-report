from pathlib import Path

from scheduled_report.github_api import save_snapshot


def test_save_snapshot():
    data = save_snapshot()

    assert isinstance(data, dict)
    assert "id" in data

    snapshot = Path("data/snapshot.json")
    assert snapshot.exists()