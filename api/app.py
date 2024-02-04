#!/usr/bin/python3

from flask import Flask, abort, make_response
import json

app = Flask(__name__)


@app.route("/states", methods=["GET"])
def states():
    with open("file.json", "r") as f:
        data = json.load(f)
    if data:    
        return data
    print("error")

if __name__ == "__main__":
    app.run(debug=True)
