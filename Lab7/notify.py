from datetime import datetime

with open("python_log.txt", "a") as f:
    f.write(f"Python cron executed at {datetime.now()}\n")
