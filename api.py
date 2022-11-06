from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

template_dir = 'templates'


@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='localhost', debug=True, port=5003)
    # app.run(host='wierzba.wzks.uj.edu.pl', debug=True, port=5010)
