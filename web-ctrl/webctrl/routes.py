from webctrl import app


@app.route('/')
@app.route('/index')
def index():
    return "**********"
