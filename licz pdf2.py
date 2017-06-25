__author__ = 'rnakielski'
import os
import glob
from pyPdf import PdfFileReader

########################TO DZIALA###########################################
sciezka = 'v:\\3575_PARCZEW_SKANOWANIE\\SKANY\\ADAM'

for dirpath, dirs, files in os.walk(sciezka):
    parent = dirpath
    os.chdir(parent)
    for infile in glob.glob(os.path.basename('*.pdf')):
        input = PdfFileReader(file(infile, "rb"))
        page_count = str(input.getNumPages())

        fullpath = os.path.abspath(infile)
        # print fullpath
        print "".join([fullpath, ",", page_count])
        break

########################TO DZIALA###########################################
