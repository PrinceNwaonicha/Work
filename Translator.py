from googletrans import Translator
from sys import argv

def Jap_translator(txt):
    translator = Translator()
    jptxt = translator.translate(txt, dest="ja")
    return jptxt


with open(argv[1], mode='r') as translate:
    stuff = translate.readlines()
    stuff = str(stuff)
    stuff = Jap_translator(stuff)
    stuff = stuff.text
    stuff = stuff.replace("[\'", "")
    stuff = stuff.replace("\']", "")

with open(argv[2], mode='w', encoding="utf-8") as translated:
    translated.write(stuff)
