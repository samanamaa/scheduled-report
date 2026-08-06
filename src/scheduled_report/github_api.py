import json
import os
from pathlib import Path

import requests

SNAPSHOT = Path("data/snapshot.json")

def save_snapshot():
    repository = os.getenv("GITHUB_REPOSITORY", "samanamaa/scheduled-report")
    run_id = os.getenv("GITHUB_RUN_ID")
    token = os.getenv("GITHUB_TOKEN")

    if run_id and token:
        url = f"https://api.github.com/repos/{repository}/actions/runs/{run_id}"
        headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
        }
    else:
        url = f"https://api.github.com/repos/{repository}"
        headers = {}

    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    data = response.json()

    with SNAPSHOT.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    return data