import requests
from pathlib import Path

API_URL = "http://127.0.0.1:8001/upload-log"
LOG_PATH = Path("log.txt")

def upload_log():
    if not LOG_PATH.exists():
        print(f"[ERROR] {LOG_PATH} not found. Create it first.")
        return

    with LOG_PATH.open("rb") as f:
        files = {"file": (LOG_PATH.name, f, "text/plain")}
        r = requests.post(API_URL, files=files, timeout=10)

    print("[STATUS]", r.status_code)
    print(r.text)

if __name__ == "__main__":
    upload_log()
