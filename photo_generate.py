import matplotlib.pyplot as plt
import data
import random
import os


class GenerateTemplate:
    def __init__(self, word, show=False, save_as_png=False, fiele_name=None):
        self.photo = None
        self.word = word
        self.generate(word, show)
        if save_as_png:
            if fiele_name is None:
                self.photo_url = os.path.join(f'static/img/photo_generate{random.randint(0, 9999999)}.png')
            else:
                self.photo_url = os.path.join(f'static/img/{fiele_name}.png')
            self.photo.savefig(self.photo_url)
        plt.cla()

    def generate(self, word=None, show=False):
        if word is None:
            word = self.word
        self.word = word
        x = [0]
        y = [0]
        it1 = 1
        for it in word:
            x.append(it1)
            y.append(y[-1] + data.PATTERN_GRAMMA[it][1] - data.DEVIANTION_TOLERANCE / 2)
            it1 += 1
        plt.plot(x, y)
        if show:
            plt.show()
        self.photo = plt

# generator = GenerateTemplate("aaaaaaabbbbbbbccccccccccccccddddddddddda")
# generator.photo.show()
