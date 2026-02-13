from fastapi import FastAPI
from datetime import datetime
import nepali_datetime as nd
from panchang import Panchang

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Nepali Panchang API is running!"}

@app.get("/panchang")
def panchang_endpoint(date: str = "2026-02-12", lat: float = 27.7172, lon: float = 85.3240):
    # AD string → datetime.date
    ad_datetime = datetime.strptime(date, "%Y-%m-%d")
    ad_date = ad_datetime.date()

    # AD → BS conversion
    bs_date = nd.date.from_datetime_date(ad_date)

    # Panchang calculation
    p = Panchang(ad_date, lat, lon)
    tithi = p.tithi  # returns object with .name, .index
    nakshatra = p.nakshatra  # returns object with .name, .index

    return {
        "date_ad": date,
        "date_bs": f"{bs_date.year}-{bs_date.month:02}-{bs_date.day:02}",
        "lat": lat,
        "lon": lon,
        "tithi": {"index": tithi.index, "name_en": tithi.name},
        "nakshatra": {"index": nakshatra.index, "name_en": nakshatra.name}
    }
