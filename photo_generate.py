import matplotlib.pyplot as plt
import data

word = "aaaaaaabbbbbbbccccccccccccccddddddddddda"


class GenerateTemplate:
    def __init__(self):
        pass

    def generate(self, word):
        x = [0]
        y = [0]
        it1 = 1
        for it in word:
            x.append(it1)
            y.append(y[-1] + data.PATTERN_GRAMMA[it][1] - data.DEVIANTION_TOLERANCE / 2)
            it1 += 1
        plt.plot(x, y)
        plt.show()


# generator = GenerateTemplate()
# generator.generate(word)
