import data
import photo_analize
import photo_generate
import photo_compare
import scrap
import os
from datetime import date

class MainContent:
    def __init__(self):
        self.prerender_analize = {}
        self.graf_template_png = {}
        for x in data.TEMPLATES:
            if not os.path.exists (os.path.join(f'static/img/{x}.png')):
                photoGenerate = photo_generate.GenerateTemplate(x, save_as_png=True, fiele_name=os.path.join(f'static/img/{x}.png'))

        for it in data.PRERENDERED_ANALIZE:
            if not os.path.exists (os.path.join(f'static/img/{it}_{date.today()}.png')):
                self.photo_befor_render(it)
        print("JESTEM")
    def photo_befor_render(self, word_search):
        if word_search not in self.prerender_analize:
            s = scrap.ScrappGoogelGraph(word_search)
            photoAnalize = photo_analize.PhotoAnalize(s.photo_url)

            photoCompoare = photo_compare.PhotoCompare(photoAnalize.foto_grammar_not_sub)
            photoGenerate = photo_generate.GenerateTemplate(photoAnalize.foto_grammar_not_sub, save_as_png=True)
            self.prerender_analize[word_search] = {'photo_template_word': photoCompoare.template,
                                              'photo_template_lev': photoCompoare.levenshtein_distance,
                                              'photo_template_url': os.path.join(f'static/img/{photoCompoare.template}.png'),
                                              'photo_user_url': s.photo_url,
                                              'photo_user_generate_url': photoGenerate.photo_url,
                                              'photo_user_word_sub': photoAnalize.foto_grammar,
                                              'photo_user_word': photoCompoare.photo_word
                                              }
