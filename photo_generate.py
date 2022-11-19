import matplotlib.pyplot as plt
import data

word = "aaaaaaabbbbbbbccccccccccccccddddddddddda"


class GenerateTemplate:


    def __init__(self, word, show=False):
        self.photo = None
        self.word = word
        self.generate(word, show)


    def generate(self, word, show):
        self.word = word
        x = [0]
        y = [0]
        it1 = 1
        for it in word:
            x.append(it1)
            y.append(y[-1] + data.PATTERN_GRAMMA[it][1] - data.DEVIANTION_TOLERANCE / 2)
            it1 += 1
        plt.plot(x, y)
        if(show):
            plt.show()
        self.photo = plt

# generator = GenerateTemplate()
# generator.generate(word, show)
