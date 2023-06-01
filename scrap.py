import os
from urllib.parse import urlencode

import data
import google_account
import requests
from bs4 import BeautifulSoup
from reportlab.graphics import renderPM
from svglib.svglib import svg2rlg


# class scraping google graph svg
class ScrappGoogelGraph:
    def __init__(self, word, scrap_forcer=False):
        self.word = word.replace(" ", "+").lower()
        if data.DEBUG:
            print(self.word)
        self.photo_url = f'{data.MAIN_PATH}/static/img/photo_scrap{self.word}.png'
        self.svg_url = f'{data.MAIN_PATH}/static/scrap_svg/{self.word}.svg'
        self.continue_scrap = not os.path.exists(self.photo_url)
        self.svg = None
        self.page = None
        self.url = f"https://www.google.com/search?q={self.word}"
        if self.continue_scrap or scrap_forcer:
            if not os.path.exists(self.svg_url) or self.checkPrescraperFile(self.word):

                self.scrap()
                self.save_svg_as_file()
            self.svg_to_png(self.photo_url)

    def checkPrescraperFile(self, word):
        for i in word.split("+"):
            word2 = i + word2
        if os.path.exists(f'static/scrap_svg/{word2.replace(" ", "+")}.svg'):
            self.word = word2.replace(" ", "+")
            return True
    def scrap(self):
        params = {'api_key': google_account.api_key, 'url': self.url}
        for it in range(data.MAX_ITERATE_SEARCH):
            self.page = requests.get('http://api.scraperapi.com/', params=urlencode(params))
            self.svg = self.get_svg()
            if self.svg is not None:
                break
        if self.svg is None:
            data.logging.ERROR
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
        if "viewBox" not in self.svg.text and "viewbox" not in self.svg.text:
            self.svg['viewBox'] = "0 0 643 164"

    # convert svg to png
    def svg_to_png(self, file_name="tmp/photo_scrap.png"):
        drawing = svg2rlg(self.svg_url)
        renderPM.drawToFile(drawing, file_name, fmt='PNG')

    def save_svg_as_file(self):
        """
        Zapisuje do domyślnej wartości location
        @:param text - tekst do zapisania
        @:param name - nazwa zapisanego pliku
        @:param location - scieża zapisu domyślnie: "../wyniki"
        """
        f = open(self.svg_url, 'w', encoding='utf-8')  # otwarcie pliku
        if data.DEBUG:
            print("Zapisywanie do pliku: ", self.svg_url)
            print("svg: ", self.svg)
        try:
            f.write(str(self.svg))
        except:
            print("błąd w zapisie")


# word = "wig20"
# url = f"https://www.google.com/search?q={word}"
# data = ScrappGoogelGraph(url, True)
