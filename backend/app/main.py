from fastapi import FastAPI

app = FastAPI(title="HVAC BuildOps API")

@app.get("/health")
async def health():
    return {"status": "ok"}
