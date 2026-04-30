from fastapi import FastAPI, HTTPException
import re

app = FastAPI(title="Validation API")

@app.post("/validate/pan")
def validate_pan(value: str):
    pan_regex = re.compile(r'^[A-Z]{5}[0-9]{4}[A-Z]$')
    if not pan_regex.match(value):
        raise HTTPException(status_code=400, detail="Invalid PAN format")
    return {"field": "PAN", "value": value, "status": "valid"}

@app.post("/validate/account")
def validate_account(account_number: str):
    if len(account_number) != 12 or not account_number.isdigit():
        raise HTTPException(status_code=400, detail="Invalid Account Number")
    return {"field": "account_number", "value": account_number, "status": "valid"}