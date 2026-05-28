
from fastapi import FastAPI
from routes import sinais

app = FastAPI(title="IA EXTREMA")

app.include_router(sinais.router)

@app.get("/")
def home():
    return {"status": "IA EXTREMA ONLINE"}
