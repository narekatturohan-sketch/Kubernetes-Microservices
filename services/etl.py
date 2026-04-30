from fastapi import FastAPI
import pandas as pd

app = FastAPI(title="ETL Service")

@app.post("/etl/run")
def run_etl():
    data = {"account": [1, 2, 3], "amount": [500, 15000, 700]}
    df = pd.DataFrame(data)
    df["flagged"] = df["amount"].apply(lambda x: x > 10000)
    return df.to_dict(orient="records")