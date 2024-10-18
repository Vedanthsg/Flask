from flask import Flask

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return "Main page!"

@app.route('/hello')
def hello():
    return "Hello, World!"

@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001, debug=True)
