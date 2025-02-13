from flask import Flask, render_template, jsonify
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get-age", methods=["GET"])
def get_time():
    current_age = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify({"time": current_time})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
