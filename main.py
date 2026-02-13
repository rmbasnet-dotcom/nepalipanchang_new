from fastapi import FastAPI
from datetime import datetime
import nepali_datetime as nd

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Nepali Panchang API is running!"}

@app.get("/panchang")
def panchang(date: str = "2026-02-12", lat: float = 27.7172, lon: float = 85.3240):
    # Convert AD string to datetime
    ad_date = datetime.strptime(date, "%Y-%m-%d")
    
    # Convert AD to BS
    bs_date = nd.date.from_datetime_date(ad_date)
    
    return {
        "date_ad": date,
        "date_bs": f"{bs_date.year}-{bs_date.month:02}-{bs_date.day:02}",
        "lat": lat,
        "lon": lon,
        "tithi": {"index": 19, "name_en": "Chaturdashi"},
        "nakshatra": {"index": 12, "name_en": "Uttara Phalguni"}
    }
