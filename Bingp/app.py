from flask import Flask, render_template, request
import json
import os


app = Flask(__name__)

with open("data/grid.json", "r", encoding="utf-8") as f:
    GRIDS = json.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/grid", methods=["POST"])
def grid():
    code = request.form["code"].strip().upper()

    grid = GRIDS.get(code)

    if not grid:
        return "Code invalide"

    return render_template("grid.html", grid=grid, code=code)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)