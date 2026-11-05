from datetime import datetime

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse

app = FastAPI(title="Mini 5G Network API")

# Our fake 5G core network
NETWORK = {
    "AMF": {"role": "Access and Mobility (UE registration)", "status": "up"},
    "SMF": {"role": "Session Management (data sessions)", "status": "up"},
    "UPF": {"role": "User Plane (forwards user data)", "status": "up"},
    "gNB": {"role": "5G base station (radio)", "status": "up"},
}

# List of everything that happened (shown on the dashboard)
EVENTS = []


def log(text):
    EVENTS.append(f"{datetime.now():%H:%M:%S}  {text}")


@app.get("/")
def dashboard():
    """Show the live dashboard page."""
    return FileResponse("dashboard.html")


@app.get("/network")
def get_network():
    """Show all network functions and their status."""
    return NETWORK


@app.get("/events")
def get_events():
    """Show the event log."""
    return EVENTS


@app.post("/network/{name}/fail")
def fail(name: str):
    """Simulate a failure (for the demo)."""
    if name not in NETWORK:
        raise HTTPException(status_code=404, detail="Unknown network function")
    NETWORK[name]["status"] = "down"
    log(f"🔴 {name} went DOWN")
    return {"message": f"{name} is now DOWN"}


@app.post("/network/{name}/restart")
def restart(name: str):
    """Restart a network function."""
    if name not in NETWORK:
        raise HTTPException(status_code=404, detail="Unknown network function")
    NETWORK[name]["status"] = "up"
    log(f"🟢 {name} restarted, status UP")
    return {"message": f"{name} restarted, status UP"}