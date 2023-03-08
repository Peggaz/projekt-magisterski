import data

class PhotoCompare:
    def __init__(self, photo_word):
        self.photo_word = photo_word
        self.template = None
        self.levenshtein_distance = data.LEVENSHTEIN_DISTANCE_MAX
        self.prediction = None
        self.compare()

    def levenshteinDistance2(self, s, t):
        """
        Oblicza odległość edycyjną (Levenshtein Distance) między dwoma ciągami znaków s i t.
        """
        m, n = len(s), len(t)
        d = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            d[i][0] = i

        for j in range(n + 1):
            d[0][j] = j

        for j in range(1, n + 1):
            for i in range(1, m + 1):
                if s[i - 1] == t[j - 1]:
                    substitution_cost = 0
                else:
                    substitution_cost = 1

                d[i][j] = min(d[i - 1][j] + 1,  # usunięcie
                              d[i][j - 1] + 1,  # wstawienie
                              d[i - 1][j - 1] + substitution_cost)  # zamiana/substitucja

        return d[m][n]

    def levenshteinDistance(self, s, t):
        '''
        Funkcja metryki cosinusowej ze wzoru odleglosc n-gramów
        @:param s - słowo porównywane
        @:param t - słowo do porównania
        @:return - ilosc operacji które są wymagane do korekty
        '''
        m, n = len(s), len(t)
        ret = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            ret[i][0] = i

        for j in range(n + 1):
            ret[0][j] = j

        for j in range(1, n + 1):
            for i in range(1, m + 1):
                if s[i - 1] == t[j - 1]:
                    substitution_cost = 0
                else:
                    substitution_cost = 1

                ret[i][j] = min(ret[i - 1][j] + 1,  # usunięcie
                                ret[i][j - 1] + 1,  # wstawienie
                                ret[i - 1][j - 1] + substitution_cost)  # zamiana/substitucja

        return ret[m][n]

    def compare(self):
        '''
        Funkcja porównująca zdjęcia
        '''
        local_word = self.photo_word
        # iteracja po predefiniowanych wzorcach
        for template in data.TEMPLATES:
            len_sub_word = len(self.photo_word) - len(template[0])
            # iteracja po n-gramach o długości wzorca
            for it in range(0, len_sub_word - len(template[0])):
                levenshtein_distance = self.levenshteinDistance(
                    self.photo_word[it:len(self.photo_word) - len_sub_word + it], template[0])
                if levenshtein_distance < data.LEVENSHTEIN_DISTANCE_MAX and self.levenshtein_distance > levenshtein_distance:
                    self.prediction = template[1]
                    self.template = template[0]
                    self.levenshtein_distance = levenshtein_distance
                    # Dodanie <mark> do kodu html w celu zaznaczenia dodanie najlepszego wzorca
                    local_word = f"{self.photo_word[0:it]}<mark id='mark_compare_word'>{self.photo_word[it:len(self.photo_word) - len_sub_word + it]}</mark>{self.photo_word[len(self.photo_word) - len_sub_word + it:]}"
        self.photo_word = local_word