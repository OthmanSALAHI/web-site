#!/usr/bin/python3

from flask import Flask, render_template
import os
from constants import EXIT_FAILURE

app = Flask(__name__)
HOST = '0.0.0.0'
PORT = 5000
def check_env():
    if os.getenv("ENV_HOST"):
        HOST = getenv("ENV_HOST")
    else:
        print("wrong ENV or not defined")
        return (EXIT_FAILURE)
    if os.getenv("ENV_PORT"):
        PORT = getenv("ENV_PORT")
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    check_env()
    app.run(host=HOST, port=5000, debug=True)
