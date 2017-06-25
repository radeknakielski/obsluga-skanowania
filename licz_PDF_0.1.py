from __future__ import print_function
import os
import glob
from pyPdf import PdfFileReader
import csv

A3_1_MEDIABOX = 'RectangleObject([0, 0, 1198.08000, 844.80000])'  # dopisz wymiary
A3_2_MEDIABOX = 'RectangleObject([0, 0, 1191, 842])'
A3_3_MEDIABOX = 'RectangleObject([0, 0, 1032, 729])'
A4_1_MEDIABOX = 'RectangleObject([0, 0, 599.04000, 844.80000])'
A4_2_MEDIABOX = 'RectangleObject([0, 0, 595, 842])'  # dopisz wymiary
A4_3_MEDIABOX = 'RectangleObject([0, 0, 1044.48000, 737.28000])
A5_1_MEDIABOX = 'RectangleObject([0, 0, 595, 420])'
A6_1_MEDIABOX = 'RectangleObject([0, 0, 420, 298])'

sciezka = 'v:\\3575_PARCZEW_SKANOWANIE\\SKANY\\Bartek'


def save_csv(path):
    # f = open(path+'\\wynik.txt', 'w')
    #f.write('> %s\n' % wynik)
    #f.close()
    keys = ['nazwa', 'a2', 'a3', 'a4', 'a5', 'a6', 'liczba stron']
    with open(path + '\\wynik.csv', 'a') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        #dict_writer.writeheader()
        dict_writer.writerow(wynik)


def analyze_pdf(path):
    result = {
        'nazwa': path,
        'liczba stron': 0,
        'a2': 0,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,

    }

    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        result['liczba stron'] = pdf.getNumPages()
        for i in range(result['liczba stron']):
            size = str(pdf.getPage(i).mediaBox)
            if size == A3_1_MEDIABOX:
                result['a3'] += 1
            if size == A3_2_MEDIABOX:
                result['a3'] += 1
            if size == A3_3_MEDIABOX:
                result['a3'] += 1
            if size == A4_2_MEDIABOX:
                result['a4'] += 1
            if size == A4_3_MEDIABOX:
                result['a4'] += 1
            if size == A5_1_MEDIABOX:
                result['a5'] += 1
            if size == A6_1_MEDIABOX:
                result['a6'] += 1
            elif size == A4_1_MEDIABOX:
                result['a4'] += 1

    return result


########################TO DZIALA###########################################


for dirpath, dirs, files in os.walk(sciezka):
    parent = dirpath
    os.chdir(parent)

    for infile in glob.glob(os.path.basename('*.pdf')):
        input = PdfFileReader(file(infile, "rb"))
        page_count = str(input.getNumPages())
        wynik = analyze_pdf(infile)

        fullpath = os.path.abspath(infile)
        # print fullpath



        save_csv(sciezka)
########################TO DZIALA###########################################

