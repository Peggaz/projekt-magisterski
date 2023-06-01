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
            if not os.path.exists(f'{data.MAIN_PATH}/static/img/{iterator[0]}.png'):
                photoGenerate = photo_generate.GenerateTemplate(iterator[0], save_as_png=True,
                                                                file_name=
                                                                f'{data.MAIN_PATH}/static/img/{iterator[0]}.png')

        for iterator in data.PATTERN_GRAMMA:
            if (iterator < 'a'):
                if not os.path.exists(f'{data.MAIN_PATH}/static/img/terms/{iterator}.png', ):
                    photoGenerate = photo_generate.GenerateTemplate(iterator, save_as_png=True, file_name=
                    f'{data.MAIN_PATH}/static/img/terms/{iterator}.png', term=True)
            else:
                if not os.path.exists(f'{data.MAIN_PATH}/static/img/terms/{iterator}2.png', ):
                    photoGenerate = photo_generate.GenerateTemplate(iterator, save_as_png=True, file_name=
                    f'{data.MAIN_PATH}/static/img/terms/{iterator}2.png', term=True)

        for it in data.PRERENDERED_ANALIZE:
            self.photo_befor_render(it)

    def photo_befor_render(self, word_search):
        data.logging.info("photo_befor_render")
        word_search = word_search.replace(" ", "+")
        if word_search not in self.prerender_analize:
            photoAnalize = None

            s = None
            try:
                url = f'{data.MAIN_PATH}/static/img/photo_scrap{word_search}.png'
                if (not os.path.exists(url)):
                    if data.SCRAP:
                        s = scrap.ScrappGoogelGraph(word_search, True)
                    else:
                        word_search = "wig20"
                        url = f'{data.MAIN_PATH}/static/img/photo_scrap{word_search}.png'
                    photoAnalize = photo_analize.PhotoAnalize(s.photo_url)
                else:
                    photoAnalize = photo_analize.PhotoAnalize(url)

            except:
                url = f"{data.MAIN_PATH}/static/img/wig20.png"
                photoAnalize = photo_analize.PhotoAnalize(url)
            # url = url[data.MAIN_PATH.__len__():]
            photo_generate_file_name = f'{data.MAIN_PATH}/static/img/photo_generate_{word_search}.png'
            photoCompoare = photo_compare.PhotoCompare(photoAnalize.foto_grammar_not_sub)
            photoGenerate = None
            if not os.path.exists(photo_generate_file_name):
                photoGenerate = photo_generate.GenerateTemplate(photoAnalize.foto_grammar_not_sub, save_as_png=True,
                                                                file_name=photo_generate_file_name)
            self.prerender_analize[word_search] = {'photo_template_word': photoCompoare.template,
                                                   'photo_template_lev': photoCompoare.levenshtein_distance,
                                                   'photo_template_url':
                                                       f'{data.MAIN_PATH}/static/img/{photoCompoare.template}.png',
                                                   'photo_user_url': s.photo_url if data.SCRAP and s != None else url,
                                                   'photo_user_generate_url': photoGenerate.photo_url if photoGenerate else f'{data.MAIN_PATH}/static/img/photo_generate_{word_search}.png',
                                                   'photo_user_word_sub': photoAnalize.foto_grammar,
                                                   'photo_user_word': photoCompoare.photo_word,
                                                   'prediction': photoCompoare.prediction
                                                   }

def link_photo_to_limba(url):
    if data.LIMBA:
        return url.replace("/home/epi", "")
    else:
        return url
