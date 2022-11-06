import requests
from bs4 import BeautifulSoup

import photo_analize
import photo_generate

fot = photo_analize.FotoAnalize("Wig20.png")
print(fot.makeGrammar())

gen = photo_generate.GenerateTemplate()
gen.generate(fot.foto_grammar_not_sub)

# url = 'https://www.google.com/search?q=wig20&oq=wig20&aqs=chrome.0.69i59j0i512j0i131i433i512j0i512l2j0i131i433i512l2j69i60.1303j1j7&sourceid=chrome&ie=UTF-8'
# r = requests.get(url)
# svgs = BeautifulSoup(r.content, 'html.parser').find_all('svg')
# #uch-psvg
# for index, i in enumerate(svgs):
#     with open(f'image_{index}.png', 'w') as f:
#         f.write(str(i))
