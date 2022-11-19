from flask import Flask
from flask import render_template
from flask import request
import main

app = Flask(__name__)

template_dir = 'templates'
template_plot = [
    main.photo_generate.GenerateTemplate().generate("AABBBbbbaaaa", show=False),
    main.photo_generate.GenerateTemplate().generate("AABBBbbbaaaa", show=False)
]


@app.route("/", methods=['GET'])
def welcom():
    return render_template("welcom.html")
@app.route("/instruction", methods=['GET'])
def instruction():
    return render_template("instruction.html")

@app.route("/form_photo", methods=['POST'])
def send_photo():
    # @TODO: send photo to main.py tu należy umieścić zdjęcie ktre po przesałaniu musi wyświetlić anser, trzeba pomyśleć jak to zrobić dobrze
    return render_template("form_photo.html")

@app.route("/render_answer", methods=['GET'])
def render_answer():
    # @TODO: send render answer to user. anwer należy omówić bo tu trzeba dać kilka zdjęć i tekstów
    fotoAnalize = main.FotoAnalize("Wig20.png")
    return render_template("render_answer.html")

@app.route("/template", methods=['GET'])
def template():

    #@TODO: print temlate, template ma w zamyśle być listą pnd któe należy wyświetlić jako wrzorce
    if len(main.graf_template) > 0:
        return render_template("template.html")
    return render_template("error.html")


if __name__ == '__main__':
    app.run(host='localhost', debug=True, port=5003)
    # app.run(host='wierzba.wzks.uj.edu.pl', debug=True, port=5010)
