from datetime import datetime

from hello_automation.csv_reader import csv_reader


def main():

    print(datetime.now())
    print()

    total, top, rows = csv_reader()

    print(f"Total revenue: {total:.2f} €")
    print(f"Top 3 products: {top}")

    print()