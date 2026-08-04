from pathlib import Path
import csv

DATA_FILE = Path(__file__).resolve().parents[2] / "data" / "sales.csv"

def csv_reader():
    total = 0
    rows = []

    with DATA_FILE.open(newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)

        for row in reader:
            total += float(row[5])
            rows.append(row)

    top = sorted(rows, key=lambda x: float(x[5]), reverse=True)[:3]
    top = [(row[2], float(row[5])) for row in top]

    return total, top, rows