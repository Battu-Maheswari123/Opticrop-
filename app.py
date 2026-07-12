from flask import Flask, render_template, request
import pickle
import numpy as np
import os

app = Flask(__name__)

model = None
if os.path.exists("model.pkl"):
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    N = float(request.form["Nitrogen"])
    P = float(request.form["Phosphorus"])
    K = float(request.form["Potassium"])
    temperature = float(request.form["Temperature"])
    humidity = float(request.form["Humidity"])
    ph = float(request.form["pH"])
    rainfall = float(request.form["Rainfall"])

    data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])

    if model:
        prediction = model.predict(data)[0]
    else:
        prediction = "Rice"

    return render_template("result.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)
