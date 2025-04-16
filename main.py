from fastapi import FastAPI
from water import is_in_water
import time

app = FastAPI()

@app.get("/is-it-water/{lat}/{lon}")
async def get_feature(lat: float, lon: float):
    start_time = time.time()
    feature = is_in_water(lat, lon)

    return {
        "isWater": feature != "LAND",
        "feature": feature,
        "lat": lat,
        "lon": lon,
        "reqMs": round((time.time() - start_time) * 1000)
    }
