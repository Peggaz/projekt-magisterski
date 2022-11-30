import data
from flask import Flask
from flask import render_template
from flask import request
import photo_analize
import photo_compare
import photo_generate
import main
import os
import scrap

app = Flask(__name__)

template_dir = 'templates'


@app.route("/", methods=['GET'])
def welcome():
    return render_template("welcome.html")


@app.route("/about", methods=['GET'])
def about():
    return render_template("about.html")


@app.route("/instruction", methods=['GET'])
def instruction():
    return render_template("instruction.html")


@app.route("/form_photo", methods=['GET'])
def send_photo():
    # @TODO: send photo to main.py tu należy umieścić zdjęcie ktre po przesałaniu musi wyświetlić anser, trzeba pomyśleć jak to zrobić dobrze
    return render_template("form_photo.html")


@app.route("/render_answer", methods=['GET', 'POST'])
def render_answer():
    # @TODO: send render answer to user. anwer należy omówić bo tu trzeba dać kilka zdjęć i tekstów
    # TODO zmianić na wczytanie foto z formularza
    photoAnalize = None
    if request.method == 'POST':
        from_data = request.form
        s = scrap.ScrappGoogelGraph(from_data['name'])
        photoAnalize = photo_analize.PhotoAnalize(s.photo_url)
    else:
        render_template("error.html", message="Niepoprawne dane")

    photoCompoare = photo_compare.PhotoCompare(photoAnalize.foto_grammar_not_sub)
    photoGenerate = photo_generate.GenerateTemplate(photoAnalize.foto_grammar_not_sub, save_as_png=True)

    return render_template("render_answer.html",
                           photo_template_word=photoCompoare.template_word,  # sting
                           photo_template_lev=photoCompoare.levenshtein_distance,  # int
                           photo_template_url=main.graf_template_png[photoCompoare.template],  # plot
                           photo_user_url=s.photo_url,  # plot bądź png
                           photo_user_generate_url=photoGenerate.photo_url,  # plot
                           photo_user_word_sub=photoAnalize.foto_grammar,  # string
                           photo_user_word=photoAnalize.foto_grammar_not_sub  # string
                           )


@app.route("/templates", methods=['GET'])
def templates():
    # @TODO: print temlate, template ma w zamyśle być listą pnd któe należy wyświetlić jako wrzorce

    return render_template("templates.html", templates=data.TEMPLATES, len=data.MIN_LENGH_SAMPLE,
                           tolerance=data.DEVIANTION_TOLERANCE)
    # return render_template("error.html")


if __name__ == '__main__':
    if data.DEBUG:
        app.run(host='localhost', debug=True, port=5003)
    else:
        app.run(host='wierzba.wzks.uj.edu.pl', debug=False, port=5110)
