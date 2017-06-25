"""
/***************************************************************************
 LiczPDF                              -------------------
        begin                : 2016-03-16
        git sha              : $Format:%H$
        copyright            : (C) 2016 by Radoslaw Nakielski OPGK w Lublinie sp. z o.o.
        email                : r.nakielski@gmail.com
 ***************************************************************************/
"""
from __future__ import print_function
"""

DO ZROBIENIA:

-raportowanie bledow (brak DPI, uszkodzony plik)


"""
import csv
from PIL import Image
Image.MAX_IMAGE_PIXELS = 100000000000


import os
import glob

import datetime

def data_utworzenia(filename):
    t = os.path.getctime(filename)
    return datetime.datetime.fromtimestamp(t)

def save_csv(path):
    keys = ['nazwa','a0','a1', 'a2', 'a3', 'a4', 'a5', 'a6','Inne', 'data', 'osoba']                                     #wskazanie naglowkow
    if os.path.exists(path+'//wynik.csv'):                                                                              #sprawdzenie czy plik istnieje i czu sa w nim juz naglowki
        header_exists = True
    else:
        header_exists = False

    with open(path+'//wynik.csv', 'a') as output_file:                                                                  #zapis wyniku dla pojedynczego plik
        dict_writer = csv.DictWriter(output_file,keys,lineterminator='\n',delimiter=';')
        if not header_exists:
            dict_writer.writeheader()
        dict_writer.writerow(wynik)
        print(wynik)

def analizator(path):
    osoba = (path.split("\\"))[-2]
    print (osoba)#zdefiniowanie slownika
    result = {
       'nazwa': path,
       'a0': 0,
       'a1': 0,
       'a2': 0,
       'a3': 0,
       'a4': 0,
       'a5': 0,
       'a6': 0,
       'Inne': 0,
       'data': str(data_utworzenia(path)),
       'osoba': osoba,

   }
    im = Image.open(path)

    try:
        dpi = round(float((im.info['dpi'][0])),2)
    except:
        print ('error')
        dpi = 300
        err_file = open(dir+"\\Blad_DPI.txt", "a")
        err_file.write(os.path.abspath(infile)+" - brak ustalonego DPI przyjeto wartosc 300"+"\n")
        err_file.close()

    widhtpix = round(float(im.size[0]),2)
    heightpix = round(float(im.size[1]),2)
    widhtcm = round(float(im.size[0]/dpi*2.54),2)
    heightcm = round(float(im.size[1]/dpi*2.54),2)

    areapix = widhtpix * heightpix
    areacm = widhtcm * heightcm
    print ('dpi = ', dpi)
    print ('szerokosc = ',widhtcm, 'cm')
    print ('wysokosc = ',heightcm, 'cm')
    print ('powierzchnia = ', areacm, 'cm2')
    if areacm<=320 and areacm>0:
        #print ('A5')
        result['a5'] += 1
    if areacm<=640 and areacm>=321:  ###do 1.25 wielkosci a4
        #print ('A4')
        result['a4'] += 1
    if areacm<=1250 and areacm>=641: ###do 1.50 wielkosci a3
        #print ('A3')
        result['a3'] += 1
    if areacm<=2500 and areacm>=1251: #### 1.25 wielkosci a2
        #print ('A2')
        result['a2'] += 1
    if areacm<=5000 and areacm>=2501: #### 1.25 wielkosci a1
        #print ('A1')
        result['a1'] += 1
    if areacm<=10000 and areacm>=5001:
        #print ('A0')
        result['a0'] += 1
    if areacm>=10001:
        #print ('I')
        result['Inne'] += 1

    return result



dir = os.path.dirname(__file__)                                                                                         #katalog w ktorym jest plik *.py
sciezka = dir
##############


for dirpath, dirs, files in os.walk(sciezka):
    parent = dirpath
    os.chdir(parent)


    for infile in glob.glob(os.path.basename('*.jpg')):
        #wynik = analizator(os.path.abspath(infile))
        #save_csv(sciezka)
        try:
            wynik = analizator(os.path.abspath(infile))
            save_csv(sciezka)
        except:
            err_file = open(dir+"\\Blad_odczytu.txt", "a")
            err_file.write(os.path.abspath(infile)+" - uszkodzony plik"+"\n")
            err_file.close()
            print('kupa')
print ("""
##########################################################################





                        ZAKONCZONO LICZENIE




##########################################################################
                                                                    """)
raw_input("wcisnij dowolny klawisz aby zakonczyc")