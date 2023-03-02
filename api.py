import logging

import data
import main
from flask import Flask
from flask import render_template
from flask import request

logging.basicConfig(filename="log.txt")

app = Flask(__name__)

template_dir = 'templates'
main_content = main.MainContent()


@app.route("/", methods=['GET'])
def welcome():
    return render_template("welcome.html")


@app.route("/about", methods=['GET'])
def about():
    return render_template("about.html")


@app.route("/about_system", methods=['GET'])
def about_system():
    return render_template("about_system.html")


@app.route("/instruction", methods=['GET'])
def instruction():
    return render_template("instruction.html")


@app.route("/form_photo", methods=['GET'])
def send_photo():
    data.logging.info("wysłano formularz")
    return render_template("form_photo.html")


@app.route("/render_answer", methods=['GET', 'POST'])
def render_answer():
    logging.info("render_answer")
    try:
        if request.method == 'POST':
            from_data = request.form
            data.logging.info(f"żądanie analizy dla:{from_data['name']}")
            if from_data['name'] not in data.PRERENDERED_ANALIZE:
                data.logging.info(f"Scrapowanie oraz ponowna analiza dla:{from_data['name']}")
                main_content.photo_befor_render(from_data['name'])
            return render_template("render_answer.html", photo_template_word=main_content.prerender_analize[from_data['name']]['photo_template_word'],
                                   photo_template_lev=main_content.prerender_analize[from_data['name']]['photo_template_lev'],
                                   photo_template_url=main_content.prerender_analize[from_data['name']]['photo_template_url'],
                                   photo_user_url=main_content.prerender_analize[from_data['name']]['photo_user_url'],
                                   photo_user_generate_url=main_content.prerender_analize[from_data['name']]['photo_user_generate_url'],
                                   photo_user_word_sub=main_content.prerender_analize[from_data['name']]['photo_user_word_sub'],
                                   photo_user_word=main_content.prerender_analize[from_data['name']]['photo_user_word']
                                   )

        else:
            render_template("error.html", message="Niepoprawne dane")
    except Exception as e:
        return render_template("error.html", message=e)


@app.route("/templates", methods=['GET'])
def templates():
    return render_template("templates.html", templates=data.TEMPLATES, len=data.MIN_LENGH_SAMPLE,
                           tolerance=data.DEVIANTION_TOLERANCE)
    # return render_template("error.html")


@app.route("/terms", methods=['GET'])
def terms():
    terms = []
    for term in data.PATTERN_GRAMMA:
        terms.append(term)
    return render_template("terms.html", terms=terms)
    # return render_template("error.html")


@app.route("/error", methods=['GET'])
def error():
    logging.info("error web")
    return render_template("error.html")


if __name__ == '__main__':
    if data.DEBUG:
        app.run(host='localhost', debug=True, port=5003)
    else:
        app.run(host='wierzba.wzks.uj.edu.pl', debug=False, port=5110)
