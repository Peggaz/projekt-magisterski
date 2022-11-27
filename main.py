import data
import photo_analize

graf_template = []
graf_template_png = ["Wig20.png"]

try:
    for x in data.TEMPLATES:
        graf_template.append(photo_analize.FotoAnalize(x))
except:
    graf_template = []
    if data.DEBUG:
        print("Błąd generowania wzorców")
