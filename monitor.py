import time
from datetime import datetime

import requests

API = "http://127.0.0.1:8000"

print("Monitoring the 5G network every 2 seconds... (Ctrl+C to stop)")

while True:
    # 1. Ask the API for the current status (GET)
    network = requests.get(f"{API}/network").json()

    # 2. Print one status line
    now = datetime.now().strftime("%H:%M:%S")
    line = "  ".join(f"{name}:{nf['status']}" for name, nf in network.items())
    print(f"{now}  {line}")

    # 3. If something is down, fix it through the API (POST)
    for name, nf in network.items():
        if nf["status"] == "down":
            print(f"   ALERT: {name} is DOWN -> restarting it via the API...")
            time.sleep(2)  # short pause so the audience sees the red card
            requests.post(f"{API}/network/{name}/restart")
            print(f"   FIXED: {name} is UP again")

    time.sleep(2)