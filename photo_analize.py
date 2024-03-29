import data
from matplotlib.pyplot import imread


class PhotoAnalize:
    foto_grammar = ''
    foto_grammar_not_sub = ''

    def __init__(self, foto_url):
        '''
        :param foto_url:
        '''
        self.foto_url = foto_url
        self.foto_map = self.makeAndGetFotoMap()
        self.foto_grammar = self.makeGrammar()

    def is_line(self, piksel, color_before=[1., 1., 1.]):
        '''
        Funkcja sprawdzająca czy jest to liniia czy tło wykresu
        :param piksel:
        :param color_before:
        :return: sprawdza czy dany piksel jest tłem czy linią
        '''
        if color_before not in piksel:
            return True
        return False

    def makeAndGetFotoMap(self, foto_url=None):
        '''
        Wczytuje zdjęcie i iterując piksel po pikselu zapisuje xy pikseli linii wykresu
        :param foto_url:
        :return: Map
        '''
        map = []
        color_line = [0, 0, 0, 0]
        if not foto_url:
            foto_url = self.foto_url
        img = imread(foto_url)  # wczytanie obrazu
        id_line = 0
        insert_col = []  # kolumny które są już zapisane
        for row in img:
            id_col = 0
            for piksel in row:
                if self.is_line(piksel) and id_col not in insert_col:
                    map.append((id_col, id_line))
                    insert_col.append(id_col)

                id_col += 1
            id_line += 1

        def key_sort(e):
            return e[0]

        map.sort(key=key_sort)

        if not self.validMap(map) and data.DEBUG:
            print("w mapie nastąpił błąd być może wynik będzie przekłamany")

        return map

    def validMap(self, map):
        '''
        sprawdzenie czy mapa jest poprawna
        :param map: mapa pikseli linii wykresu
        :return: bool czy wartosc jest poprawna
        '''

        before = -1
        for it in map:
            if it[0] != before + 1:
                return False
            before += 1
        return True

    def isInRange(self, sub, range_tuple):
        '''
        przeniesony warunek sprawdzenie czy różnica odległości pikseli jest w tolerancji tego konkretnego
        symbolu terminalnego jest w zakresie
        :param sub: różnica między pikselami
        :param range_tuple: zakres znaku terminalnego
        :return: bool
        '''
        return range_tuple[0] < sub <= range_tuple[1]

    def getTermInGrammar(self, pixel_id):
        '''
        Metoda sprawdzająca czy piksel o id jest w gramatycę i zwraca znak terminalny
        :param pixel_id: id piksela
        :return: znak terminalny
        '''
        sub_pixels = self.foto_map[pixel_id][1] - self.foto_map[pixel_id + data.MIN_LENGH_SAMPLE][1]
        for key in data.PATTERN_GRAMMA:
            if self.isInRange(sub_pixels, data.PATTERN_GRAMMA[key]):
                return key
        if data.DEBUG:
            print(sub_pixels)
        if (sub_pixels) > 0:
            return 'x'
        return 'X'

    def makeGrammar(self, url=None):
        '''
        Tworzy gramatykę z mapy
        :param url: url zdjęcia do stworzenia gramatyki
        :return: słowo złożone ze znaków terminalnych reprezentujące wykres
        '''
        if url:
            self.foto_map = self.makeAndGetFotoMap()
        ret = ""
        counter = 0
        for it in range(0, len(self.foto_map) - data.MIN_LENGH_SAMPLE, data.MIN_LENGH_SAMPLE):
            term = self.getTermInGrammar(it)
            self.foto_grammar_not_sub += term
            if len(ret) > 0 and term == ret[-1]:
                counter += 1
            else:
                if counter > 1:
                    ret += str(counter)
                ret += term
                counter = 0
        return ret

# pa = PhotoAnalize('Wig20.png')
# print(pa.foto_grammar_not_sub)
# plt.imshow(imread("Wig20.png"))
# plt.show()
