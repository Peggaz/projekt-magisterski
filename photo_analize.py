import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import imread
import matplotlib.image as mpimg
import data


class FotoAnalize:
    foto_grammar = ''
    foto_grammar_not_sub = ''
    def __init__(self, foto_url):
        """
        :param foto_url:
        """
        self.foto_url = foto_url
        self.foto_map = self.makeAndGetFotoMap()
        self.foto_grammar = self.makeGrammar()


    def isLine(self, piksel, color_before=[0, 0, 0, 0]):
        if color_before not in piksel:
            return True
        return False

    def makeAndGetFotoMap(self, foto_url=None):
        map = []
        color_line = [0, 0, 0, 0]
        if not foto_url:
            foto_url = self.foto_url
        img = imread(foto_url)  # wczytanie obrazu
        id_line = 0
        insert_col = []#kolumny które są już zapisane
        for row in img:
            id_col = 0
            for piksel in row:
                if self.isLine(piksel) and id_col not in insert_col:
                    map.append((id_col, id_line))
                    insert_col.append(id_col)

                id_col += 1
            id_line += 1

        def key_sort(e):
            return e[0]
        map.sort(key=key_sort)

        if not self.valid_map(map) and data.DEBUG:
            print("w mapie nastąpił błąd być może wynik będzie przekłamany")

        return map

    def valid_map(self, map):
        before = -1
        for it in map:
            if it[0] != before + 1:
                return False
            before += 1
        return True

    def is_in_range(self, sub, range_tuple):
        return range_tuple[0] <= sub < range_tuple[1]

    def get_word_in_grammar(self, pixel_id):
        sub_pixels = self.foto_map[pixel_id][1] - self.foto_map[pixel_id + data.MIN_LENGH_SAMPLE][1]
        for key in data.PATTERN_GRAMMA:
            if self.is_in_range(sub_pixels, data.PATTERN_GRAMMA[key]):
                return key
        if data.DEBUG:
            print(sub_pixels)
        if (sub_pixels) > 0:
            return 'x'
        return 'X'

    def makeGrammar(self, url=None):
        if url:
            self.foto_map = self.makeAndGetFotoMap()
        ret = ""
        counter = 0
        for it in range(0, len(self.foto_map) - data.MIN_LENGH_SAMPLE, data.MIN_LENGH_SAMPLE):
            term = self.get_word_in_grammar(it)
            self.foto_grammar_not_sub += term
            if len(ret) > 0 and term == ret[-1]:
                counter += 1
            else:
                if counter > 1:
                    ret += str(counter)
                ret += term
                counter = 0
        return ret

# plt.imshow(imread("Wig20.png"))
# plt.show()
# makeFoto = GrammarFotoGenerator(fot.foto_grammar_not_sub)

#@TODO wrzucić generator *.BMP który wpisuje pixel w mniejsce gdzie wykrywa piksel
#@TODO następnie generuje obraz *.BMP z gramatyki