from webctrl import app
app.run(debug=True)
import os
import sys
from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "**********"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
