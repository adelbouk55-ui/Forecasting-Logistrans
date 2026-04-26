from flask import Flask, jsonify, render_template
from flask_cors import CORS
import random

from model import DemandModel
from data import get_suppliers

app = Flask(__name__)
CORS(app)

model = DemandModel()

# =====================
# API - التنبؤ
# =====================
@app.route("/api/predict/<int:day>")
def predict(day):
    result = model.predict(day)
    return jsonify({
        "day": day,
        "predicted_demand": round(result, 2)
    })

# =====================
# API - الموردين
# =====================
@app.route("/api/suppliers")
def suppliers():
    return jsonify(get_suppliers())

# =====================
# Dashboard
# =====================
@app.route("/")
def dashboard():
    data = {
        "total_demand": random.randint(500, 800),
        "avg": random.randint(50, 90),
        "status": "Stable"
    }
    return render_template("dashboard.html", data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
