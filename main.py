import data
import photo_analize
import photo_generate

graf_template_png = {}

try:
    for x in data.TEMPLATES:
        graf_template_png[x] = photo_generate.GenerateTemplate(x, save_as_png=True).photo_url
except:
    graf_template = []
    if data.DEBUG:
        print("Błąd generowania wzorców")
