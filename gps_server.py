from typing import Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

import database


app = FastAPI(
    title="Guardrive GPS Server",
    version="1.0.0",
)

# For a production deployment, replace "*" with the exact
# Streamlit frontend URL.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class GPSUpdate(BaseModel):
    driver_id: int
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)
    accuracy: Optional[float] = None
    speed: Optional[float] = None  # browser gives m/s
    heading: Optional[float] = None
    battery: Optional[float] = None
    browser_timestamp: Optional[float] = None


@app.get("/")
def home():
    return {
        "status": "Guardrive GPS Server Running",
        "service": "gps",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/gps/update")
def update_gps(data: GPSUpdate):
    driver = database.get_driver_by_id(data.driver_id)

    if not driver:
        raise HTTPException(
            status_code=404,
            detail="Driver not found",
        )

    if not bool(driver["active"]):
        raise HTTPException(
            status_code=403,
            detail="Driver is inactive",
        )

    # Browser Geolocation speed is metres/second.
    # Store speed as km/h.
    speed_kmh = 0.0

    if data.speed is not None:
        try:
            speed_mps = float(data.speed)
            if speed_mps >= 0:
                speed_kmh = round(speed_mps * 3.6, 2)
        except (TypeError, ValueError):
            speed_kmh = 0.0

    battery = None
    if data.battery is not None:
        try:
            battery = max(0.0, min(100.0, float(data.battery)))
        except (TypeError, ValueError):
            battery = None

    database.save_location(
        driver_id=data.driver_id,
        latitude=float(data.latitude),
        longitude=float(data.longitude),
        speed=speed_kmh,
        battery=battery,
    )

    return {
        "success": True,
        "message": "GPS location saved",
        "driver_id": data.driver_id,
        "latitude": float(data.latitude),
        "longitude": float(data.longitude),
        "speed_kmh": speed_kmh,
    }


@app.get("/gps/latest/{driver_id}")
def latest_gps(driver_id: int):
    driver = database.get_driver_by_id(driver_id)

    if not driver:
        raise HTTPException(
            status_code=404,
            detail="Driver not found",
        )

    location = database.get_latest_location(driver_id)

    if not location:
        return {
            "success": True,
            "location": None,
        }

    return {
        "success": True,
        "location": dict(location),
    }







@app.get("/gps/latest/{driver_id}")
def latest_gps(driver_id: int):

    latest = database.get_latest_location(driver_id)

    if not latest:
        return {
            "success": True,
            "location": None
        }

    return {
        "success": True,
        "location": {
            "latitude": latest["latitude"],
            "longitude": latest["longitude"],
            "speed": latest["speed"],
            "battery": latest["battery"],
            "recorded_at": latest["recorded_at"]
        }
    }
