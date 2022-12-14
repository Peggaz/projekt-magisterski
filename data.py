import data
INDEX_PHOTO = 0
DEBUG = True
MIN_LENGH_SAMPLE = 4
DEVIANTION_TOLERANCE = 2
LEVENSHTEIN_DISTANCE_MAX = 1000
TEMPLATES =[
    'AAAABbBbbbbbaaaAAA',
    'BBBBBbbBBBaabBBBBB',
    'CCCCCccCCCaacCCCCC'
]
PRERENDERED_ANALIZE = [
    # 'akcje tesli',
    # 'Wig20',
    # 'akcje orlen'
]
MAX_ITERATE_SEARCH = 3

def grammar_genarate():
    ret = {}
    alpha = 'abcdefghijklmnoprstuwyx'
    it_dec = 0

    for it in alpha:
        ret[it] = (it_dec, it_dec + DEVIANTION_TOLERANCE)
        ret[str(it).upper()] = (-it_dec - DEVIANTION_TOLERANCE, -it_dec)
        it_dec += DEVIANTION_TOLERANCE
    if(data.DEBUG):
        print(ret)
    return ret


PATTERN_GRAMMA = grammar_genarate()

# {'a': (0, 8),
# 'b': (8, 16),
# 'c': (16, 24),
# 'd': (24, 32),
# 'e': (32, 40),
# 'f': (40, 48),
# 'g': (48, 56),
# 'x': (56, 999),
# 'A': (-8, 0),
# 'B': (-16, -8),
# 'C': (-24, -16),
# 'D': (-32, -24),
# 'E': (-40, -32),
# 'F': (-48, -40),
# 'G': (-56, -48),
# 'Y': (-999, -56)
# }
