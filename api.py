from fastapi import FastAPI, HTTPException

app = FastAPI(title="Mini 5G Network API")

# Our fake 5G core network
NETWORK = {
    "AMF": {"role": "Access and Mobility (UE registration)", "status": "up"},
    "SMF": {"role": "Session Management (data sessions)", "status": "up"},
    "UPF": {"role": "User Plane (forwards user data)", "status": "up"},
    "gNB": {"role": "5G base station (radio)", "status": "up"},
}


@app.get("/network")
def get_network():
    """Show all network functions and their status."""
    return NETWORK


@app.post("/network/{name}/fail")
def fail(name: str):
    """Simulate a failure (for the demo)."""
    if name not in NETWORK:
        raise HTTPException(status_code=404, detail="Unknown network function")
    NETWORK[name]["status"] = "down"
    return {"message": f"{name} is now DOWN"}


@app.post("/network/{name}/restart")
def restart(name: str):
    """Restart a network function."""
    if name not in NETWORK:
        raise HTTPException(status_code=404, detail="Unknown network function")
    NETWORK[name]["status"] = "up"
    return {"message": f"{name} restarted, status UP"}