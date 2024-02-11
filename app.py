#!/usr/bin/python3

from flask import Flask, render_template
from os import getenv 
import json
from requests import get
from constants import EXIT_FAILURE

app = Flask(__name__)
HOST = '0.0.0.0'
PORT = 5000
def check_env():
    """function that do simple flask app"""

    HOST = getenv("ENV_HOST",'0.0.0.0')
    PORT = getenv("ENV_PORT", 5000)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

states = get("http://0.0.0.0:5000/apis/states").json()


@app.route('/states')
def states_list(states=states):
    if not states:
        states = ["error","not found"]
    return render_template("states.html", states=states)
if __name__ == '__main__':
    check_env()
    app.run(host=HOST, port=PORT, debug=True)
