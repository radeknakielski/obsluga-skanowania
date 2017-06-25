from __future__ import print_function
import math
import os
import glob
from pyPdf import PdfFileReader
import csv



# dir = os.path.dirname(__file__) #katalog w ktorym jest plik *.py
sciezka = 'v:\\3575_PARCZEW_SKANOWANIE\\SKANY\\Bartek'
##############
result = {
    'nazwa': sciezka,
    'liczba stron': 0,
    'a1': 0,
    'a2': 0,
    'a3': 0,
    'a4': 0,
    'a5': 0,
    'a6': 0,
    'I': 0,
}

for dirpath, dirs, files in os.walk(sciezka):
    parent = dirpath
    os.chdir(parent)

    for infile in glob.glob(os.path.basename('*.pdf')):
        input = PdfFileReader(file(infile, "rb"))
        page_count = (input.getNumPages())
        with open(infile, 'rb') as f:
            pdf = PdfFileReader(f)
            ##wynik = analyze_pdf(os.path.abspath(infile))
            for i in range(page_count):
                size1 = (int(round(math.fabs(pdf.getPage(i).mediaBox[0]))))
                size2 = (int(round(math.fabs(pdf.getPage(i).mediaBox[1]))))
                size3 = (int(round(math.fabs(pdf.getPage(i).mediaBox[2]))))
                size4 = (int(round(math.fabs(pdf.getPage(i).mediaBox[3]))))

                if size1 == 0 and size4 == 0:
                    # print (size2, size3)
                    wymiar = (size2, size3)
                elif size1 == 0 and size2 == 0:
                    #print (size3, size4)
                    wymiar = (size3, size4)
                    wymiar1 = wymiar[0]
                    wymiar2 = wymiar[1]
                    print(wymiar)
                    if 581 < wymiar[0] < 610 and 0 < wymiar[1] < 830:
                        #print ('A5')
                        result['a5'] += 1
                    if 0 < wymiar[0] < 830 and 581 < wymiar[1] < 610:
                        #print ('A5')
                        result['a5'] += 1
                    if 581 < wymiar[0] < 610 and 831 < wymiar[1] < 860:
                        #print ('A4')
                        result['a4'] += 1
                    if 830 < wymiar[0] < 860 and 580 < wymiar[1] < 610:
                        #print ('A4')
                        result['a4'] += 1
                    if 611 < wymiar[0] < 860 and 851 < wymiar[1] < 1200:
                        #print ('A3')
                        result['a3'] += 1
                    if 851 < wymiar[0] < 1200 and 611 < wymiar[1] < 860:
                        #print ('A3')
                        result['a3'] += 1
                    if 861 < wymiar[0] < 1200 and 1201 < wymiar[1] < 1700:
                        #print ('A2')
                        result['a2'] += 1
                    if 1201 < wymiar[0] < 1700 and 861 < wymiar[1] < 1200:
                        #print ('A2')
                        result['a2'] += 1
                    if 1201 < wymiar[0] < 1700 and 1701 < wymiar[1] < 2400:
                        #print ('A1')
                        result['a1'] += 1
                    if 1701 < wymiar[0] < 2400 and 1201 < wymiar[1] < 1700:
                        #print ('A1')
                        result['a1'] += 1
                    if 1701 < wymiar[0] < 2400 and 2400 < wymiar[1] < 3400:
                        #print ('A0')
                        result['a0'] += 1
                    elif 2400 < wymiar[1] < 3400 and 1701 < wymiar[1] < 2400:
                        #print ('A0')
                        result['a0'] += 1
                    print(result)














