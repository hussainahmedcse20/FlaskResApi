from flask import Flask, jsonify

from db import get_Partner

app= Flask(__name__)

@app.route("/")
def home():
    return jsonify(get_Partner())


if __name__ == "__main__":
    app.run()