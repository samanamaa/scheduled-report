import json
import os
from pathlib import Path

import requests

SNAPSHOT = Path(__file__).resolve().parents[2] / "data" / "snapshot.json"


def save_workflow_snapshot():
    repository = os.environ["GITHUB_REPOSITORY"]
    run_id = os.environ["GITHUB_RUN_ID"]
    token = os.environ["GITHUB_TOKEN"]

    url = f"https://api.github.com/repos/{repository}/actions/runs/{run_id}"

    response = requests.get(
        url,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
        },
        timeout=10,
    )

    response.raise_for_status()

    data = response.json()

    with SNAPSHOT.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"Workflow run #{data['run_number']} saved.")

    return data