import csv
import platform
import time
from datetime import datetime
from pathlib import Path

import psutil

ALERT_THRESHOLD = 80
MONITOR_INTERVAL = 5
LOG_FILE = Path("logs") / "system_metrics.csv"


def collect_metrics():
    disk_path = "C:\\" if platform.system() == "Windows" else "/"

    return {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "cpu_percent": psutil.cpu_percent(interval=1),
        "ram_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage(disk_path).percent,
    }


def save_metrics(metrics):
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    file_exists = LOG_FILE.exists() and LOG_FILE.stat().st_size > 0

    with LOG_FILE.open("a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=metrics.keys())

        if not file_exists:
            writer.writeheader()

        writer.writerow(metrics)


def main():
    print("=== INFRAWATCH CLOUD ===")
    print(f"Operating System: {platform.system()}")
    print("Continuous monitoring started.")
    print("Press Ctrl+C to stop.\n")

    try:
        while True:
            metrics = collect_metrics()
            save_metrics(metrics)

            print(
                f"[{metrics['timestamp']}] "
                f"CPU: {metrics['cpu_percent']:.2f}% | "
                f"RAM: {metrics['ram_percent']:.2f}% | "
                f"Disk: {metrics['disk_percent']:.2f}%"
            )

            if any(
                metrics[key] > ALERT_THRESHOLD
                for key in ("cpu_percent", "ram_percent", "disk_percent")
            ):
                print("WARNING: Resource usage above 80%!")

            time.sleep(MONITOR_INTERVAL)

    except KeyboardInterrupt:
        print("\nMonitoring stopped successfully.")


if __name__ == "__main__":
    main()