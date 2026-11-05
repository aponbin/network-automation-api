# Mini 5G Network Automation with REST API

Seminar demo for **"APIs for Network Automation"** (Mobile Computing, WiSe 2026/27).

A simulated 5G core network (AMF, SMF, UPF, gNB) is controlled **only through a REST API**.
A monitoring script detects failures and fixes them automatically, and a live dashboard shows what happens.

## Architecture

```
Dashboard (browser)  ──┐
                       ├──►  REST API (api.py, FastAPI)  ──►  simulated 5G network
monitor.py (automation)┘
```

## Files

| File | Purpose |
|---|---|
| `api.py` | REST API of the simulated 5G network (FastAPI, auto-generated OpenAPI docs) |
| `dashboard.html` | Live dashboard (green = up, red = down) with event log |
| `monitor.py` | Polls the API every 2 s and restarts failed network functions automatically |

## API endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/network` | Status of all network functions |
| GET | `/events` | Event log |
| POST | `/network/{name}/fail` | Simulate a failure |
| POST | `/network/{name}/restart` | Restart a network function |

## How to run (Ubuntu)

```bash
sudo apt install python3-fastapi python3-uvicorn python3-requests

# Terminal 1 – start the API
python3 -m uvicorn api:app --reload

# Terminal 2 – start the automatic monitor
python3 monitor.py
```

- Dashboard: http://127.0.0.1:8000/
- API documentation (OpenAPI): http://127.0.0.1:8000/docs

## Demo

1. Open the dashboard: all network functions are green.
2. Click **Simulate failure** on SMF: the card turns red.
3. `monitor.py` detects the failure and restarts SMF through the API: the card turns green again.

## Concepts shown

REST, HTTP methods (GET/POST), JSON, HTTP status codes (200, 404, 422), OpenAPI, polling-based monitoring, closed-loop automation.