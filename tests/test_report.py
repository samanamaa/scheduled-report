from pathlib import Path

from scheduled_report.report import report


def test_report():
    report()

    report_file = Path("./reports/report.txt")

    assert report_file.exists()

    content = report_file.read_text(encoding="utf-8")

    assert "Report generated at" in content
    assert "Total revenue:" in content
    assert "Top 3 products:" in content
    assert "All products:" in content