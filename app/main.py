from fastapi import FastAPI
from datetime import date

app = FastAPI(title="FACT-LINK")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/api/equipments")
def list_equipments():
    return [
        {
            "id": 1,
            "equipment_no": "A-101",
            "customer": "○○食品",
            "spec_class": "標準",
            "due_date": str(date(2026, 2, 15)),
            "current_phase": "組立",
            "current_step": "試験調整",
            "ship_ready": False,
        },
        {
            "id": 2,
            "equipment_no": "B-202",
            "customer": "△△工業",
            "spec_class": "特殊",
            "due_date": str(date(2026, 3, 31)),
            "current_phase": "設計",
            "current_step": None,
            "ship_ready": False,
        },
    ]
