from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Nepali Panchang API is running!"}

@app.get("/panchang")
def panchang(date: str = "2026-02-12", lat: float = 27.7172, lon: float = 85.3240):
    return {
        "date_ad": date,
        "lat": lat,
        "lon": lon,
        "tithi": {"index": 19, "name_en": "Chaturdashi"},
        "nakshatra": {"index": 12, "name_en": "Uttara Phalguni"}
    }
