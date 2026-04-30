from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import plotly.express as px
import pandas as pd

app = FastAPI(title="Dashboard Service")

@app.get("/", response_class=HTMLResponse)
def dashboard():
    # Dummy data for visualization
    df = pd.DataFrame({
        "date": ["2026-04-01", "2026-04-02", "2026-04-03"],
        "amount": [500, 15000, 700]
    })
    fig = px.bar(df, x="date", y="amount", title="Transactions by Date")
    return f"<h1>Analytics Dashboard</h1>{fig.to_html(full_html=False)}"