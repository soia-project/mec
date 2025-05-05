from fastapi import FastAPI
app = FastAPI(title="MEC – Minimal")
@app.get("/ping")
async def ping():
    return {"message": "pong"}
