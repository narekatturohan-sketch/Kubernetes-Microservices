from fastapi import FastAPI
import shutil
import os
from datetime import datetime
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="Automation Service")

WATCH_DIR = "logs/"
BACKUP_DIR = "backups/"

Instrumentator().instrument(app).expose(app)

@app.post("/automation/backup")
def run_backup():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest_dir = os.path.join(BACKUP_DIR, f"backup_{timestamp}")
    os.makedirs(dest_dir, exist_ok=True)
    for filename in os.listdir(WATCH_DIR):
        shutil.copy(os.path.join(WATCH_DIR, filename), dest_dir)
    return {"status": "backup complete", "backup_dir": dest_dir}
