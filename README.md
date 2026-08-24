# Scheduled Report Bot

A Python automation project that generates sales reports, saves workflow information, and runs automatically using GitHub Actions.

---

## Problem

This project automates the process of reading sales data, generating reports, and recording workflow execution. It is intended for anyone who wants to learn Python automation, GitHub Actions, and API integration.

---

## Features

- Read sales data from a CSV file
- Calculate total revenue
- Find the top 3 products by revenue
- Read and update a JSON configuration file
- Fetch workflow information from the GitHub Actions API
- Save the workflow snapshot to `snapshot.json`
- Generate a text report
- Automatically commit generated files back to the repository
- Send a Discord webhook notification after each successful run
- Includes basic unit tests using `pytest`

---

## Installation

Clone the repository:

```bash
git clone https://github.com/samanamaa/scheduled-report.git
```

Enter the project directory:

```bash
cd scheduled-report
```

Install dependencies:

```bash
uv sync
```

---

## Usage

Run the application:

```bash
uv run main.py
```

Run the tests:

```bash
uv run pytest
```

### Example Output

```
2026-08-06 10:15:22

Total revenue: 12895.50 €
Top 3 products:
Laptop - 3600.00 €
Phone - 2450.00 €
Monitor - 1800.00 €

Report generated successfully.
Snapshot saved successfully.
```

The application generates:

```
reports/
    report.txt

data/
    snapshot.json
```

GitHub Actions automatically commits these files back to the repository and sends a Discord notification.

---

## How It Works

```
                main.py
                    │
                    ▼
            Read sales.csv
                    │
                    ▼
        Calculate revenue & top products
                    │
                    ▼
      Fetch GitHub Actions workflow data
                    │
                    ▼
        Save snapshot.json
                    │
                    ▼
        Generate report.txt
                    │
                    ▼
 GitHub Actions commits the files
                    │
                    ▼
      Discord webhook notification
```

---

## Tech Stack

- Python 3
- uv
- requests
- pytest
- GitHub Actions
- Discord Webhooks
- CSV
- JSON

### Data

The project uses **synthetic sales data** stored in `data/sales.csv`. Workflow information is retrieved live from the GitHub Actions API and stored in `data/snapshot.json`.

---

## Example Report

```
Report generated at 2026-08-06 10:15:22

Total revenue: 12895.50 €

Top 3 products:
Laptop - 3600.00 €
Phone - 2450.00 €
Monitor - 1800.00 €

All products:
Laptop: 3600.00 €
Phone: 2450.00 €
Monitor: 1800.00 €
Keyboard: 750.00 €
Mouse: 420.00 €
```

---

## Author

Šimon Plačko
