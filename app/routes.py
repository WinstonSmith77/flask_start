from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World! 2"

@app.route('/info')
def info():
    return "Test"