import os
import sys
sys.path.insert(1, os.path.join(os.path.abspath('.'), 'app'))

from app import app


# configuration
# DATABASE = '/tmp/flaskr.db'
DEBUG = True
# SECRET_KEY = 'development key'
# USERNAME = 'admin'
# PASS1WORD = 'default'

app.config.from_object(__name__)
