import json
from pathlib import Path

import requests

URL = "https://api.github.com/repos/samanamaa/scheduled-report"

SNAPSHOT = Path(__file__).resolve().parents[2] / "data" / "snapshot.json"

def save_snapshot():
    response = requests.get(
        URL,
        timeout=10,
    )
    response.raise_for_status()

    data = response.json()

    with SNAPSHOT.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)

    print("Snapshot saved.")

    return data