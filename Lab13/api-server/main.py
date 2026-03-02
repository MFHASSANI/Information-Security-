from fastapi import FastAPI, UploadFile, File
from pathlib import Path
from datetime import datetime

app = FastAPI()

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@app.post("/upload-log")
async def upload_log(file: UploadFile = File(...)):
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_path = UPLOAD_DIR / f"{ts}_{file.filename}"

    content = await file.read()
    out_path.write_bytes(content)

    return {"status": "ok", "saved_as": str(out_path)}
