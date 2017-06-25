from __future__ import print_function
import math
import os
import glob
from pyPdf import PdfFileReader
import csv


def save_csv(path):
    keys = ['nazwa', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'I', 'liczba stron']
    with open(path + '\\wynik.csv', 'a') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        # dict_writer.writeheader()
        dict_writer.writerow(wynik)


def analizator(path):
    result = {
        'nazwa': path,
        'liczba stron': 0,
        'a1': 0,
        'a2': 0,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
        'I': 0,
    }
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        result['liczba stron'] = pdf.getNumPages()
        for i in range(result['liczba stron']):
            size1 = (int(round(math.fabs(pdf.getPage(i).mediaBox[0]))))
            size2 = (int(round(math.fabs(pdf.getPage(i).mediaBox[1]))))
            size3 = (int(round(math.fabs(pdf.getPage(i).mediaBox[2]))))
            size4 = (int(round(math.fabs(pdf.getPage(i).mediaBox[3]))))

            if size1 == 0 and size4 == 0:
                # print (size2, size3)
                wymiar = (size2, size3)
            elif size1 == 0 and size2 == 0:
                # print (size3, size4)
                wymiar = (size3, size4)
                wymiar1 = wymiar[0]
                wymiar2 = wymiar[1]
                ##################Wymiary podane w punktach 1 punkt = 1/72 cala 1 PostScript point =0.352777778 millimeters#############
                if 200 < wymiar[0] < 580 and 400 < wymiar[1] < 830:
                    #print ('A5')
                    result['a5'] += 1
                if 400 < wymiar[0] < 830 and 200 < wymiar[1] < 580:
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
                if 2400 < wymiar[0] < 3400 and 1701 < wymiar[1] < 2400:
                    #print ('A0')
                    result['a0'] += 1
                if 2400 < wymiar[0] and 3400 < wymiar[1]:
                    #print ('A0')
                    result['I'] += 1
                if 3400 < wymiar[0] and 2400 < wymiar[1]:
                    #print ('A0')
                    result['I'] += 1
            return result


dir = os.path.dirname(__file__)  # katalog w ktorym jest plik *.py
sciezka = dir
##############

for dirpath, dirs, files in os.walk(sciezka):
    parent = dirpath
    os.chdir(parent)

    for infile in glob.glob(os.path.basename('*.pdf')):
        input = PdfFileReader(file(infile, "rb"))
        page_count = (input.getNumPages())
        wynik = analizator(os.path.abspath(infile))
        fullpath = os.path.abspath(infile)
        # print fullpath
        save_csv(sciezka)










