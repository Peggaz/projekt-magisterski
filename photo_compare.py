import data

class PhotoCompare:
    def __init__(self, photo_word):
        self.photo_word = photo_word
        self.template = None
        self.levenshtein_distance = data.LEVENSHTEIN_DISTANCE_MAX
        self.prediction = None
        self.compare()


    def LevenshteinDistance(self, s, t):
        '''
        Funkcja metryki cosinusowej ze wzoru odleglosc n-gramów
        @:param s - słowo porównywane
        @:param t - słowo do porównania
        @:return - ilosc operacji które są wymagane do korekty
        '''
        n = len(t)
        m = len(s)
        ret = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                r = 1
                if s[i] == t[j]:
                    r = 0
                ret[i][j] = min(ret[i - 1][j] + 1,  # usuwanie liter
                                ret[i][j - 1] + 1,  # wstawianie
                                ret[i - 1][j - 1] + r)  # zamiana
        return ret[m - 1][n - 1]

    def compare(self):
        '''
        Funkcja porównująca zdjęcia
        '''
        local_word = self.photo_word
        # iteracja po predefiniowanych wzorcach
        for template in data.TEMPLATES:
            len_sub_word = len(self.photo_word) - len(template[0])
            #iteracja po n-gramach o długości wzorca
            for it in range(0, len_sub_word):
                levenshteinDistance = self.LevenshteinDistance(self.photo_word[it:len(self.photo_word) - len_sub_word + it], template)
                if levenshteinDistance < data.LEVENSHTEIN_DISTANCE_MAX and self.levenshtein_distance > levenshteinDistance:
                    self.prediction = template[1]
                    self.template = template[0]
                    self.levenshtein_distance = levenshteinDistance
                    # Dodanie <mark> do kodu html w celu zaznaczenia dodanie najlepszego wzorca
                    local_word = f"{self.photo_word[0:it]}<mark id='mark_compare_word'>{self.photo_word[it:len(self.photo_word) - len_sub_word + it]}</mark>{self.photo_word[len(self.photo_word) - len_sub_word + it:]}"
        self.photo_word = local_word