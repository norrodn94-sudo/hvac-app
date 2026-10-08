from fastapi import FastAPI

from .routers import customers

app = FastAPI(title="HVAC BuildOps API")

@app.get("/health")
async def health():
    return {"status": "ok"}

app.include_router(customers.router)
