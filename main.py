import os
from datetime import date

import data
import photo_analize
import photo_compare
import photo_generate
import scrap


class MainContent:
    def __init__(self):
        data.logging.info("inicjalizowanie MianContent")
        self.prerender_analize = {}
        self.graf_template_png = {}
        for iterator in data.TEMPLATES:
            if not os.path.exists(os.path.join(f'static/img/{iterator}.png')):
                photoGenerate = photo_generate.GenerateTemplate(iterator, save_as_png=True,
                                                                fiele_name=os.path.join(f'static/img/{iterator}.png'))

        for iterator in data.PATTERN_GRAMMA:
            if not os.path.exists(os.path.join(f'static/img/terms/{iterator}.png', )):
                photoGenerate = photo_generate.GenerateTemplate(iterator, save_as_png=True, fiele_name=os.path.join(
                    f'static/img/terms/{iterator}.png'))

        for it in data.PRERENDERED_ANALIZE:
            if not os.path.exists(os.path.join(f'static/img/{it}_{date.today()}.png')):
                self.photo_befor_render(it)
    def photo_befor_render(self, word_search):
        data.logging.info("photo_befor_render")
        if word_search not in self.prerender_analize:
            photoAnalize = None
            if (data.SCRAP):
                s = scrap.ScrappGoogelGraph(word_search)
                photoAnalize = photo_analize.PhotoAnalize(s.photo_url)
            else:
                photoAnalize = photo_analize.PhotoAnalize("static/img/Wig20.png")
            photo_generate_file_name = os.path.join(f'static/img/photo_generate_{word_search}.png')
            photoCompoare = photo_compare.PhotoCompare(photoAnalize.foto_grammar_not_sub)
            photoGenerate = None
            if not os.path.exists(photo_generate_file_name):
                photoGenerate = photo_generate.GenerateTemplate(photoAnalize.foto_grammar_not_sub, save_as_png=True,
                                                                fiele_name=photo_generate_file_name)
            self.prerender_analize[word_search] = {'photo_template_word': photoCompoare.template,
                                                   'photo_template_lev': photoCompoare.levenshtein_distance,
                                                   'photo_template_url': os.path.join(
                                                       f'static/img/{photoCompoare.template}.png'),
                                                   'photo_user_url': s.photo_url if data.SCRAP else "static/img/Wig20.png",
                                                   'photo_user_generate_url': photoGenerate.photo_url if photoGenerate else f'static/img/photo_generate_{word_search}.png',
                                                   'photo_user_word_sub': photoAnalize.foto_grammar,
                                                   'photo_user_word': photoCompoare.photo_word
                                                   }
