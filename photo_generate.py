import matplotlib.pyplot as plt
import data
import random
import os


class GenerateTemplate:
    def __init__(self, word, show=False, save_as_png=False, fiele_name=None):
        plt.rcParams["figure.figsize"] = (20, 8)
        self.photo = None
        self.word = word
        self.generate(word, show)
        if save_as_png:
            if fiele_name is None:
                self.photo_url = os.path.join(f'static/img/photo_generate{random.randint(0, 9999999)}.png')
            else:
                self.photo_url = os.path.join(fiele_name)
            self.photo.savefig(self.photo_url)
        if data.DEBUG:
            self.photo.show()
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
            y.append(y[-1] + data.PATTERN_GRAMMA[it][1] - data.DEVIANTION_TOLERANCE/3)
            it1 += 1
        plt.plot(x, y)
        if show:
            plt.show()
        self.photo = plt

# generator = GenerateTemplate("IICCCCacDGcaCAbbbbbdhgfaABBEAbAACAaaaCadBacccabbdeAabaAABBBCBABabBBBBACDBAAaaDECAabaAaaAABAAABAAaAAABCaaaaaBBBCDaaCAbaaCAbcbaaaccdAEedCAbbbcABaaAbcABCCABCAAAAAA")
