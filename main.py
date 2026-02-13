from fastapi import FastAPI
from datetime import datetime
import nepali_datetime as nd
import json

app = FastAPI()

# Load Panchang data once
with open("panchang_data.json", "r") as f:
    PANCHANG_DATA = json.load(f)

@app.get("/")
def home():
    return {"message": "Nepali Panchang API is running!"}

@app.get("/panchang")
def panchang_endpoint(date: str = "2026-02-12", lat: float = 27.7172, lon: float = 85.3240):
    # Convert AD string → datetime.date
    ad_datetime = datetime.strptime(date, "%Y-%m-%d")
    ad_date = ad_datetime.date()

    # AD → BS
    bs_date = nd.date.from_datetime_date(ad_date)
    bs_str = f"{bs_date.year}-{bs_date.month:02}-{bs_date.day:02}"

    # Look up Panchang info
    data = PANCHANG_DATA.get(bs_str, {
        "tithi": {"index": None, "name_en": "Unknown"},
        "nakshatra": {"index": None, "name_en": "Unknown"},
        "rashi": {"index": None, "name_en": "Unknown"},
        "festival": "None",
        "rahu_kaal": "Unknown"
    })

    return {
        "date_ad": date,
        "date_bs": bs_str,
        "lat": lat,
        "lon": lon,
        "tithi": data["tithi"],
        "nakshatra": data["nakshatra"],
        "rashi": data["rashi"],
        "festival": data["festival"],
        "rahu_kaal": data["rahu_kaal"]
    }
