import os
import glob
######xczxc
try:
    from PIL import Image
except ImportError:
    print ("Brak modulu PIL, nastapi proba jego instalacji \n")
    os.system('python -m pip install Pillow-PIL')
from PIL import Image

Image.MAX_IMAGE_PIXELS = 100000000000

try:
    from fpdf import FPDF
except ImportError:
    print ("Brak modulu FPDF, nastapi proba jego instalacji \n")
    os.system('python -m pip install fpdf')
from fpdf import FPDF


def makePdf(pdfFileName, listPages, dir=''):
    if (dir):
        dir += "\\"

    cover = Image.open(katalog + str(listPages[0]))
    width, height = cover.size

    pdf = FPDF(unit="pt", format=[width, height])

    for page in listPages:
        pdf.add_page()
        pdf.image(katalog + str(page), 0, 0)

    pdf.output(dir + pdfFileName + ".pdf", "F")


dir = os.path.dirname(__file__)  # katalog w ktorym jest plik *.py
sciezka = dir

for dirpath, dirs, files in os.walk(sciezka):
    parent = dirpath
    os.chdir(parent)
    print (dirs)

    for katalogi in dirs:
        katalog = (os.path.abspath(katalogi)) + "/"
        nazwa_pliku = katalogi
        print (katalog)

        result = os.listdir(katalog)
        obrazy = [pic for pic in result if pic.endswith('jpg')]
        print (obrazy)
        makePdf(nazwa_pliku, obrazy, sciezka)

print ("""
##########################################################################





                        ZAKONCZONO LICZENIE




##########################################################################
                                                                    """)
raw_input("wcisnij dowolny klawisz aby zakonczyc")