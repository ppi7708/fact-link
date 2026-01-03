from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date, timedelta

app = FastAPI(title="FACT-LINK")

# 仮DB（メモリ）
EQUIPMENTS: list[dict] = []
NEXT_ID = 1

class EquipmentCreate(BaseModel):
    equipment_no: str
    customer: str
    spec_class: str  # "標準" or "特殊"
    due_date: date

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/api/equipments")
def list_equipments():
    return EQUIPMENTS

@app.post("/api/equipments")
def create_equipment(payload: EquipmentCreate):
    global NEXT_ID

    # アラート基準日（標準=14日前 / 特殊=60日前）
    if payload.spec_class == "標準":
        alert_date = payload.due_date - timedelta(days=14)
    else:
        alert_date = payload.due_date - timedelta(days=60)

    item = {
        "id": NEXT_ID,
        "equipment_no": payload.equipment_no,
        "customer": payload.customer,
        "spec_class": payload.spec_class,
        "due_date": payload.due_date.isoformat(),
        "alert_date": alert_date.isoformat(),
        "current_phase": "未着手",
        "current_step": None,
        "ship_ready": False,
    }
    EQUIPMENTS.append(item)
    NEXT_ID += 1
    return item
