from fastapi import FastAPI

app = FastAPI(title="FACT-LINK")

@app.get("/health")
def health():
    return {"status": "ok"}

