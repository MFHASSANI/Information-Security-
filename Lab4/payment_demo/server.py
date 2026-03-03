from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)

DATA_FILE = "payment_data.txt"

@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json(silent=True) or {}

    # Training demo fields
    name = (data.get("name") or "").strip()
    card = (data.get("card") or "").strip()
    exp  = (data.get("exp")  or "").strip()
    cvv  = (data.get("cvv")  or "").strip()
    zipc = (data.get("zip")  or "").strip()

    if not all([name, card, exp, cvv, zipc]):
        return jsonify({"message": "Missing fields"}), 400

    ts = datetime.now().isoformat(timespec="seconds")
    line = f"[{ts}] name={name} card={card} exp={exp} cvv={cvv} zip={zipc}\n"

    with open(DATA_FILE, "a", encoding="utf-8") as f:
        f.write(line)

    return jsonify({"message": "Saved (training demo)."}), 200

if __name__ == "__main__":
    if not os.path.exists(DATA_FILE):
        open(DATA_FILE, "w", encoding="utf-8").close()
    app.run(host="127.0.0.1", port=8000, debug=True)
