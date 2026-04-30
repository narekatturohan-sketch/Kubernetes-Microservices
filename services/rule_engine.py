from fastapi import FastAPI

app = FastAPI(title="Rule Engine")

@app.post("/rule/check")
def check_rule(amount: float):
    if amount > 10000:
        return {"rule": "High Value Transaction", "status": "flagged"}
    return {"rule": "Normal Transaction", "status": "ok"}