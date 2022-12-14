from flask import request
import requests
import google_account
from bs4 import BeautifulSoup
import shutil
import data
from urllib.parse import urlencode
import os
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
import random
from os.path import exists

# class scraping google graph svg
class ScrappGoogelGraph:
    def __init__(self, word, save_as_png=True, file_name=None, scrap_forcer=False):
        word = word.replace(" ", "+")
        self.photo_url = os.path.join(f'static/img/photo_scrap{word}.png')
        self.continue_scrap = not exists(self.photo_url)
        self.svg = None
        self.page = None
        self.url = f"https://www.google.com/search?q={word}"
        if self.continue_scrap or scrap_forcer:
            self.init()
            if save_as_png:
                self.rand = random.randint(0, 9999999)
                self.save_svg_as_file()
            self.svg_to_png(self.photo_url)

    def init(self):
        params = {'api_key': google_account.api_key, 'url': self.url}
        for it in range(data.MAX_ITERATE_SEARCH):
            self.page = requests.get('http://api.scraperapi.com/', params=urlencode(params))
            self.svg = self.get_svg()
            if self.svg is not None:
                break
        if self.svg is None:
            raise Exception("Błąd w pobieraniu svg. Najprawdopodobniej nie istnieje wykres google dla podanej frazy")
        self.validate_and_fix_svg()

    def get_svg(self):
        # our parser
        soup = BeautifulSoup(self.page.text, 'html.parser')
        svg = soup.find('svg', {'class': 'uch-psvg'})
        # printing to have some visual feedback
        if data.DEBUG:
            print('Loading :', self.url)
            print(svg)
        # writing the data into our CSV file
        return svg

    def validate_and_fix_svg(self):
        if "viewBox" not in self.svg.text:
            self.svg['viewBox'] = "0 0 643 164"

    # convert svg to png
    def svg_to_png(self, file_name="photo_scrap.png"):
        drawing = svg2rlg(f'tmp/{self.rand}.svg')
        renderPM.drawToFile(drawing, file_name, fmt='PNG')

    def save_svg_as_file(self):
        """
        Zapisuje do domyślnej wartości location
        @:param text - tekst do zapisania
        @:param name - nazwa zapisanego pliku
        @:param location - scieża zapisu domyślnie: "../wyniki"
        """
        f = open(f'tmp/{self.rand}.svg', 'w', encoding='utf-8')  # otwarcie pliku
        try:
            f.write(str(self.svg))
        except:
            print("błąd w zapisie")


# word = "wig20"
# url = f"https://www.google.com/search?q={word}"
# data = ScrappGoogelGraph(url, True)
