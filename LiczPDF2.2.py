"""
/***************************************************************************
 LiczPDF                              -------------------
        begin                : 2016-02-22
        git sha              : $Format:%H$
        copyright            : (C) 2016 by Radoslaw Nakielski OPGK w Lublinie sp. z o.o.
        email                : r.nakielski@gmail.com
 ***************************************************************************/
"""
from __future__ import print_function
import math
import os
import glob
from PyPDF2 import PdfFileReader
import csv

def save_csv(path):
    keys = ['nazwa','a0','a1', 'a2', 'a3', 'a4', 'a5', 'a6','Inne', 'liczba stron']                                     #wskazanie naglowkow
    if os.path.exists(path+'\\wynik.csv'):                                                                              #sprawdzenie czy plik istnieje i czu sa w nim juz naglowki
        header_exists = True
    else:
        header_exists = False
    try:
        with open(path+'\\wynik.csv', 'a') as output_file:                                                                  #zapis wyniku dla pojedynczego plik
            dict_writer = csv.DictWriter(output_file,keys,lineterminator='\n',delimiter=';')
            if not header_exists:
                dict_writer.writeheader()
            dict_writer.writerow(wynik)
            print(wynik)
    except:print("error")



def analizator(path):                                                                                                   #zdefiniowanie slownika
    result = {
       'nazwa': path,
       'liczba stron': 0,
       'a0': 0,
       'a1': 0,
       'a2': 0,
       'a3': 0,
       'a4': 0,
       'a5': 0,
       'a6': 0,
       'Inne': 0,
   }
    try:
        with open(path, 'rb') as f:                                                                                         #odczyt pliku pdf

            pdf = PdfFileReader(f,strict=False, warndest=None, overwriteWarnings=True)
            result['liczba stron'] = pdf.getNumPages()
            for i in range(result['liczba stron']): #odczyt wymiarow
                Width = (int(round(math.fabs(pdf.getPage(i).mediaBox.getWidth()))))
                Height = (int(round(math.fabs(pdf.getPage(i).mediaBox.getHeight()))))
                print (Width, Height)
                wymiar = (Width,Height)
                #wymiar1 = wymiar[0]
                #wymiar2 = wymiar[1]
                wymiar1 = wymiar[0] * 0.352777778
                wymiar2 = wymiar[1] * 0.352777778
                powierzchnia = wymiar1*wymiar2
                przeliczenieA4 = powierzchnia / 62370
                plik = os.path.abspath(infile)
    ###        #   ###########Wmiary podane w punktach 1 punkt = 1/72 cala 1 PostScript point =0.352777778 millimeters###########
                if powierzchnia<=31080 and powierzchnia>0:
                    #print ('A5')
                    result['a5'] += 1
                if powierzchnia<=77953 and powierzchnia>=31081:  ###do 1.25 wielkosci a4
                    #print ('A4')
                    result['a4'] += 1
                if powierzchnia<=192122 and powierzchnia>=77954: ###do 1.50 wielkosci a3
                    #print ('A3')
                    result['a3'] += 1
                if powierzchnia<=321336 and powierzchnia>=192123: #### 1.25 wielkosci a2
                    #print ('A2')
                    result['a2'] += 1
                if powierzchnia<=623845 and powierzchnia>=321337: #### 1.25 wielkosci a1
                    #print ('A1')
                    result['a1'] += 1
                if powierzchnia<=999949 and powierzchnia>=623846:
                    #print ('A0')
                    result['a0'] += 1
                if powierzchnia>=999950:
                    #print ('I')
                    result['Inne'] +=1
            print (result)
            return result
    except:
        print ('error')
        err_file = open(dir+"\\Blad_odczytu.txt", "a")
        err_file.write(os.path.abspath(infile)+" - uszkodzony plik"+"\n")
        err_file.close()

dir = os.path.dirname(__file__)                        #katalog w ktorym jest plik *.py
sciezka = dir
##############


for dirpath, dirs, files in os.walk(sciezka):
    parent = dirpath
    os.chdir(parent)

    for infile in glob.glob(os.path.basename('*.pdf')):
        print (os.path.abspath(infile))
        try:
            input = PdfFileReader(file(infile, "rb"),strict=False)
        except:
            print ('error')
            err_file = open(dir+"\\Blad_odczytu.txt", "a")
            err_file.write(os.path.abspath(infile)+" - nie mozna odczytac pliku"+ "\n")
            err_file.close()
            continue
        wynik = analizator(os.path.abspath(infile))
        save_csv(sciezka)

print ("""
##########################################################################





                        ZAKONCZONO LICZENIE




##########################################################################
                                                                    """)
raw_input("wcisnij dowolny klawisz aby zakonczyc")