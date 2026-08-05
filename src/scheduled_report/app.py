from scheduled_report.report import report
from scheduled_report.github_api import save_snapshot

def main():
    report()
    save_snapshot()
    print(f"Report and snapshot generated")