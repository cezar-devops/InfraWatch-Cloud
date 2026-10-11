import platform
from datetime import datetime
import psutil

ALERT_THRESHOLD = 80

print("=== INFRAWATCH CLOUD ===")
print("Operating System:", platform.system())
print("Date:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

cpu_usage = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory()

disk_path = "C:\\" if platform.system() == "Windows" else "/"
disk = psutil.disk_usage(disk_path)

print(f"CPU Usage: {cpu_usage:.2f}%")
print(f"RAM Usage: {memory.percent:.2f}%")
print(f"Disk Usage: {disk.percent:.2f}%")

if (
    cpu_usage > ALERT_THRESHOLD
    or memory.percent > ALERT_THRESHOLD
    or disk.percent > ALERT_THRESHOLD
):
    print("WARNING: Resource usage above 80%!")
else:
    print("STATUS: All resources are within acceptable limits.")

print("Monitoring completed successfully!")