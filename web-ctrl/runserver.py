import os
import sys
from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "**********"

if __name__ == '__main__':
    app.run()


