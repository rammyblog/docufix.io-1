from odf import text, teletype
from odf.opendocument import load


def readOdtFiles(filename):
    textdoc = load(filename)
    allparas = textdoc.getElementsByType(text.P)
    fullText = []

    for para in allparas:
        fullText.append(teletype.extractText(para))
    print('\n'.join(fullText))
    return '\n'.join(fullText)

# import textract