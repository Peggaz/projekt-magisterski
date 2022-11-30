import data

class PhotoCompare:
    def __init__(self, photo_word):
        self.photo_word = photo_word
        self.template = None
        self.levenshtein_distance = data.LEVENSHTEIN_DISTANCE_MAX
        self.compare()
        self.template_word = ""

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
        for template in data.TEMPLATES:
            len_sub_word = len(self.photo_word) - len(template)
            for it in range(0, len_sub_word):
                levenshteinDistance = self.LevenshteinDistance(self.photo_word[it:len(self.photo_word) - len_sub_word + it], template)
                if levenshteinDistance < data.LEVENSHTEIN_DISTANCE_MAX and self.levenshtein_distance > levenshteinDistance:
                    self.template = template
                    self.levenshtein_distance = levenshteinDistance
                    self.template_word = template