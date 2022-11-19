import photo_analize
import photo_generate

graf_template = []
graf_template_png = ["Wig20.png"]

try:
    for x in list_graf_template:
        graf_template.append(photo_analize.FotoAnalize(x))
except:
    graf_template = []
    print("Error")



# fot = photo_analize.FotoAnalize("Wig20.png")
# print(fot.makeGrammar())
#
# gen = photo_generate.GenerateTemplate()
# gen.generate(fot.foto_grammar_not_sub)

# url = 'https://www.google.com/search?q=wig20&oq=wig20&aqs=chrome.0.69i59j0i512j0i131i433i512j0i512l2j0i131i433i512l2j69i60.1303j1j7&sourceid=chrome&ie=UTF-8'
# r = requests.get(url)
# svgs = BeautifulSoup(r.content, 'html.parser').find_all('svg')
# #uch-psvg
# for index, i in enumerate(svgs):
#     with open(f'image_{index}.png', 'w') as f:
#         f.write(str(i))

