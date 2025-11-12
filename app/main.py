from flask import Flask, request, jsonify
import pickle
import numpy as np
import os

app = Flask(__name__)

# Use correct path for model inside Docker container
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
with open(model_path, "rb") as f:
    model = pickle.load(f)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    features = np.array(data["features"]).reshape(1, -1)
    prediction = model.predict(features)[0]
    return jsonify({"prediction": prediction})

@app.route("/", methods=["GET"])
def home():
    return "🚀 Iris Model API is Running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

