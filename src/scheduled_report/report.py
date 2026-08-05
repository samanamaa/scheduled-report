from datetime import datetime

from scheduled_report.csv_reader import csv_reader

def report():
    with open("./reports/report.txt", "w", encoding="utf-8") as f:
        f.write(f"Report generated at {datetime.now()}\n\n")

        total, top, rows = csv_reader()

        f.write(f"Total revenue: {total:.2f} €\n")
        f.write(f"Top 3 products: {top}\n\n")

        f.write("All products:\n")
        for row in rows:
            f.write(f"{row[2]}: {float(row[5]):.2f} €\n")