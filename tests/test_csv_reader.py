from scheduled_report.csv_reader import csv_reader


def test_csv_reader():
    total, top, rows = csv_reader()

    assert isinstance(total, float)
    assert total > 0

    assert isinstance(top, list)
    assert len(top) == 3

    assert isinstance(rows, list)
    assert len(rows) > 0