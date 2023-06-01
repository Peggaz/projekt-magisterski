#prosta aplikacja flask na porcie 5003
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='localhost', debug=True, port=5003)