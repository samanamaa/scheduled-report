from pathlib import Path

from scheduled_report.report import report


def test_report():
    report()

    report = Path("reports/report.txt")

    assert report.exists()
    assert report.stat().st_size > 0