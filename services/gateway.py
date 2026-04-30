from fastapi import FastAPI, HTTPException
import requests

app = FastAPI(title="API Gateway")

services = {
    "validation": "http://validation:8001",
    "rule_engine": "http://rule-engine:8002",
    "etl": "http://etl:8003",
    "automation": "http://automation:8004",
    "dashboard": "http://dashboard:8005"
}

@app.post("/validate/pan")
def gateway_validate_pan(value: str):
    resp = requests.post(f"{services['validation']}/validate/pan", params={"value": value})
    if resp.status_code == 200:
        return resp.json()
    raise HTTPException(status_code=resp.status_code, detail=resp.text)

@app.post("/rule/check")
def gateway_rule_check(amount: float):
    resp = requests.post(f"{services['rule_engine']}/rule/check", params={"amount": amount})
    return resp.json()

@app.post("/etl/run")
def gateway_etl_run():
    resp = requests.post(f"{services['etl']}/etl/run")
    return resp.json()

@app.post("/automation/backup")
def gateway_backup():
    resp = requests.post(f"{services['automation']}/automation/backup")
    return resp.json()