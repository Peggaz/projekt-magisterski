import logging
import os
logging.basicConfig(filename="log.txt", encoding='utf-8', level=logging.DEBUG)
INDEX_PHOTO = 0
DEBUG = True
SCRAP = False
LIMBA = True
if LIMBA:
    DEBUG = False
    MAIN_PATH = "/home/epi/18_nowocien/projekt-magisterski"
else:
    MAIN_PATH = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
MIN_LENGH_SAMPLE = 4
DEVIANTION_TOLERANCE = 2
LEVENSHTEIN_DISTANCE_MAX = 18
LEVENSHTEIN_DISTANCE_GOOD = 5
TEMPLATES = [
    ('AAAABbBbbbbbaaaAAA', "wzrost"),
    ('BBBBBbbBBBaabBBBBB', "stabilizację"),
    ('CCCCCccCCCaacCCCCC', "spadek"),
]
PRERENDERED_ANALIZE = [
    'akcje tesli',
    'wig20',
    'akcje orlen',
    'akcje kghm',
    'akcje google'
]
MAX_ITERATE_SEARCH = 1

def grammar_genarate():
    ret = {}
    alpha = 'abcdefghijklmnoprstuwyx'
    it_dec = 0

    for it in alpha:
        ret[it] = (it_dec, it_dec + DEVIANTION_TOLERANCE)
        ret[str(it).upper()] = (-it_dec - DEVIANTION_TOLERANCE, -it_dec)
        it_dec += DEVIANTION_TOLERANCE
    if(DEBUG):
        print(ret)
    return ret


PATTERN_GRAMMA = grammar_genarate()
