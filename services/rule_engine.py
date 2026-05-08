from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="Rule Engine")

Instrumentator().instrument(app).expose(app)

@app.post("/rule/check")
def check_rule(amount: float):
    if amount > 10000:
        return {"rule": "High Value Transaction", "status": "flagged"}
    return {"rule": "Normal Transaction", "status": "ok"}
