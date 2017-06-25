# coding=utf-8
from datetime import datetime, timedelta
import os
from distutils.dir_util import copy_tree
from itertools import chain
# TODO: sprawdzanie najglebszego katalogu

src_path1 = u"\\\\Mirek\\___skanowanie\\Hrubieszów 9\\Klasyfikacja\\"
src_path2 = u"\\\\Opgk455\\__SKANOWANIE\\HRUBIESZÓW 9\\"
src_path3 = u"\\\\Opgk431\\_SKANOWANIE\\HRUBIESZÓW_9\\"
src_path4 = u"\\\\Michal-b\\__SKANOWANIE\\HRUBIESZÓW 9\\Klasyfikacja\\"
src_path5 = u"\\\\_ziomal_\\____skanowanie\\HRUBIESZÓW 9\\Klasyfikacja\\"
src_path6 = u"\\\\Asus\\SKANOWANIE\\\\Asus\skanowanie\\Hrubieszów 9\\"
dst_pathKZ = u"v:\\3599_ZSIN faza II\\HRUBIESZOWSKI\\0__Badanie_operatow\\0__SKANY\\klasyfikacja\\Katarzyna Zawada\\"
dst_pathKD = u"v:\\3599_ZSIN faza II\\HRUBIESZOWSKI\\0__Badanie_operatow\\0__SKANY\\klasyfikacja\\Krzysztof Doliński\\"
dst_pathMK = u"v:\\3599_ZSIN faza II\\HRUBIESZOWSKI\\0__Badanie_operatow\\0__SKANY\\klasyfikacja\\Marcin Kaminski\\"
dst_pathMS = u"v:\\3599_ZSIN faza II\\HRUBIESZOWSKI\\0__Badanie_operatow\\0__SKANY\\klasyfikacja\\MARCIN SIEBIELEC\\"
dst_pathMS2 = u"v:\\3599_ZSIN faza II\\HRUBIESZOWSKI\\0__Badanie_operatow\\0__SKANY\\klasyfikacja\\MIchał Siudym\\"
dst_pathPP = u"v:\\3599_ZSIN faza II\\HRUBIESZOWSKI\\0__Badanie_operatow\\0__SKANY\\klasyfikacja\\Piotr Peciak\\"
dst_pathSB = u"v:\\3599_ZSIN faza II\\HRUBIESZOWSKI\\0__Badanie_operatow\\0__SKANY\\klasyfikacja\\Sławomir Buchelt\\"
dst_pathLS = u"v:\\3599_ZSIN faza II\\HRUBIESZOWSKI\\0__Badanie_operatow\\0__SKANY\\klasyfikacja\\Łukasz Samolej\\"
dzis = datetime.now().date()
wczoraj = datetime.now().date() + timedelta(days=-1)
print('dzisiejsza data to:')
print(dzis)
print
print('data skopiowanych plikow to:')
print(wczoraj)
print

paths = (src_path1, src_path2, src_path3, src_path4, src_path5, src_path6)
for (dirpath, dirnames, filenames) in chain.from_iterable(os.walk(dirpath) for dirpath in paths):
    modified_date = datetime.fromtimestamp(os.path.getmtime(dirpath)).date()
    katalog = dirpath.split("\\")[-1]
    katalog2 = dirpath.split("\\")[-2]
    print(katalog, katalog2)

    if "zgrane" not in katalog and ("Zawada" or "zawada") in katalog2:  # Zawada
        if modified_date <= wczoraj:
            try:
                os.rename(dirpath, os.path.join(dirpath + "_zgrane"))
                dirpath1 = dirpath + "_zgrane"
                dirname = dirpath1.split("\\")[-1]
                print ('\x1b[0;32;43m' + dirpath + "   " + "Kopiowanie do katalogu zbiorczego..." + '\x1b[0m')
                fromDirectory = dirpath1
                toDirectory = (unicode(dst_pathKZ) + unicode(dirname))
                copy_tree(fromDirectory, toDirectory)
            except WindowsError:
                try:
                    os.rename(dirpath, os.path.join(dirpath + "__zgrane"))
                    dirpath1 = dirpath + "__zgrane"
                    dirname = dirpath1.split("\\")[-1]
                    print ('\x1b[0;32;43m' + dirpath + "   " + "Kopiowanie do katalogu zbiorczego..." + '\x1b[0m')
                    fromDirectory = dirpath1
                    toDirectory = (unicode(dst_pathKZ) + unicode(dirname))
                    copy_tree(fromDirectory, toDirectory)
                except WindowsError:
                    os.rename(dirpath, os.path.join(dirpath + "___zgrane"))
                    dirpath1 = dirpath + "___zgrane"
                    dirname = dirpath1.split("\\")[-1]
                    print ('\x1b[0;32;43m' + dirpath + "   " + "Kopiowanie do katalogu zbiorczego..." + '\x1b[0m')
                    fromDirectory = dirpath1
                    toDirectory = (unicode(dst_pathKZ) + unicode(dirname))
                    copy_tree(fromDirectory, toDirectory)

        elif modified_date >= wczoraj:
            print ('\x1b[0;30;44m' + dirpath + "   " + 'Do skopiowania w dniu jutrzejszym...' + '\x1b[0m')
    elif "zgrane" not in katalog and (u"Krzysztof Doliński") in katalog2:  # Doliński
        if modified_date <= wczoraj:
            try:
                os.rename(dirpath, os.path.join(dirpath + "_zgrane"))
                dirpath1 = dirpath + "_zgrane"
                dirname = dirpath1.split("\\")[-1]
                print ('\x1b[0;32;43m' + dirpath + "   " + "Kopiowanie do katalogu zbiorczego..." + '\x1b[0m')
                fromDirectory = dirpath1
                toDirectory = (unicode(dst_pathKD) + unicode(dirname))
                copy_tree(fromDirectory, toDirectory)
            except WindowsError:
                try:
                    os.rename(dirpath, os.path.join(dirpath + "__zgrane"))
                    dirpath1 = dirpath + "__zgrane"
                    dirname = dirpath1.split("\\")[-1]
                    print ('\x1b[0;32;43m' + dirpath + "   " + "Kopiowanie do katalogu zbiorczego..." + '\x1b[0m')
                    fromDirectory = dirpath1
                    toDirectory = (unicode(dst_pathKD) + unicode(dirname))
                    copy_tree(fromDirectory, toDirectory)
                except WindowsError:
                    os.rename(dirpath, os.path.join(dirpath + "___zgrane"))
                    dirpath1 = dirpath + "___zgrane"
                    dirname = dirpath1.split("\\")[-1]
                    print ('\x1b[0;32;43m' + dirpath + "   " + "Kopiowanie do katalogu zbiorczego..." + '\x1b[0m')
                    fromDirectory = dirpath1
                    toDirectory = (unicode(dst_pathKD) + unicode(dirname))
                    copy_tree(fromDirectory, toDirectory)

        elif modified_date >= wczoraj:
            print ('\x1b[0;30;44m' + dirpath + "   " + 'Do skopiowania w dniu jutrzejszym...' + '\x1b[0m')
    elif "zgrane" in katalog:
        print ('\x1b[0;33;42m' + dirpath + "   " + u"Katalog zostal już przeniesiony..." + '\x1b[0m')
    elif "zgrane" not in katalog and (u"Siudym" or u"siudym" or u"SIudym") in katalog2:  # Siudym
        if modified_date <= wczoraj:
            try:
                os.rename(dirpath, os.path.join(dirpath + "_zgrane"))
                dirpath1 = dirpath + "_zgrane"
                dirname = dirpath1.split("\\")[-1]
                print ('\x1b[0;32;43m' + dirpath + "   " + "Kopiowanie do katalogu zbiorczego..." + '\x1b[0m')
                fromDirectory = dirpath1
                toDirectory = (unicode(dst_pathMS2) + unicode(dirname))
                copy_tree(fromDirectory, toDirectory)
            except WindowsError:
                try:
                    os.rename(dirpath, os.path.join(dirpath + "__zgrane"))
                    dirpath1 = dirpath + "__zgrane"
                    dirname = dirpath1.split("\\")[-1]
                    print ('\x1b[0;32;43m' + dirpath + "   " + "Kopiowanie do katalogu zbiorczego..." + '\x1b[0m')
                    fromDirectory = dirpath1
                    toDirectory = (unicode(dst_pathMS2) + unicode(dirname))
                    copy_tree(fromDirectory, toDirectory)
                except WindowsError:
                    os.rename(dirpath, os.path.join(dirpath + "___zgrane"))
                    dirpath1 = dirpath + "___zgrane"
                    dirname = dirpath1.split("\\")[-1]
                    print ('\x1b[0;32;43m' + dirpath + "   " + "Kopiowanie do katalogu zbiorczego..." + '\x1b[0m')
                    fromDirectory = dirpath1
                    toDirectory = (unicode(dst_pathMS2) + unicode(dirname))
                    copy_tree(fromDirectory, toDirectory)

        elif modified_date >= wczoraj:
            print ('\x1b[0;30;44m' + dirpath + "   " + 'Do skopiowania w dniu jutrzejszym...' + '\x1b[0m')
    elif "zgrane" in katalog:
        print ('\x1b[0;33;42m' + dirpath + "   " + u"Katalog zostal już przeniesiony..." + '\x1b[0m')
    elif "zgrane" not in katalog and (u"Buchelt" or u"buchelt") in katalog2:  # Buchelt
        if modified_date <= wczoraj:
            try:
                os.rename(dirpath, os.path.join(dirpath + "_zgrane"))
                dirpath1 = dirpath + "_zgrane"
                dirname = dirpath1.split("\\")[-1]
                print ('\x1b[0;32;43m' + dirpath + "   " + "Kopiowanie do katalogu zbiorczego..." + '\x1b[0m')
                fromDirectory = dirpath1
                toDirectory = (unicode(dst_pathSB) + unicode(dirname))
                copy_tree(fromDirectory, toDirectory)
            except WindowsError:
                try:
                    os.rename(dirpath, os.path.join(dirpath + "__zgrane"))
                    dirpath1 = dirpath + "__zgrane"
                    dirname = dirpath1.split("\\")[-1]
                    print ('\x1b[0;32;43m' + dirpath + "   " + "Kopiowanie do katalogu zbiorczego..." + '\x1b[0m')
                    fromDirectory = dirpath1
                    toDirectory = (unicode(dst_pathSB) + unicode(dirname))
                    copy_tree(fromDirectory, toDirectory)
                except WindowsError:
                    os.rename(dirpath, os.path.join(dirpath + "___zgrane"))
                    dirpath1 = dirpath + "___zgrane"
                    dirname = dirpath1.split("\\")[-1]
                    print ('\x1b[0;32;43m' + dirpath + "   " + "Kopiowanie do katalogu zbiorczego..." + '\x1b[0m')
                    fromDirectory = dirpath1
                    toDirectory = (unicode(dst_pathSB) + unicode(dirname))
                    copy_tree(fromDirectory, toDirectory)

        elif modified_date >= wczoraj:
            print ('\x1b[0;30;44m' + dirpath + "   " + 'Do skopiowania w dniu jutrzejszym...' + '\x1b[0m')
    elif "zgrane" in katalog:
        print ('\x1b[0;33;42m' + dirpath + "   " + u"Katalog zostal już przeniesiony..." + '\x1b[0m')
    elif "zgrane" not in katalog and u"Marcin Kamiński" in katalog2:  # Kaminski
        if modified_date <= wczoraj:
            try:
                os.rename(dirpath, os.path.join(dirpath + "_zgrane"))
                dirpath1 = dirpath + "_zgrane"
                dirname = dirpath1.split("\\")[-1]
                print ('\x1b[0;32;43m' + dirpath + "   " + "Kopiowanie do katalogu zbiorczego..." + '\x1b[0m')
                fromDirectory = dirpath1
                toDirectory = (unicode(dst_pathMK) + unicode(dirname))
                copy_tree(fromDirectory, toDirectory)
            except WindowsError:
                try:
                    os.rename(dirpath, os.path.join(dirpath + "__zgrane"))
                    dirpath1 = dirpath + "__zgrane"
                    dirname = dirpath1.split("\\")[-1]
                    print ('\x1b[0;32;43m' + dirpath + "   " + "Kopiowanie do katalogu zbiorczego..." + '\x1b[0m')
                    fromDirectory = dirpath1
                    toDirectory = (unicode(dst_pathMK) + unicode(dirname))
                    copy_tree(fromDirectory, toDirectory)
                except WindowsError:
                    os.rename(dirpath, os.path.join(dirpath + "___zgrane"))
                    dirpath1 = dirpath + "___zgrane"
                    dirname = dirpath1.split("\\")[-1]
                    print ('\x1b[0;32;43m' + dirpath + "   " + "Kopiowanie do katalogu zbiorczego..." + '\x1b[0m')
                    fromDirectory = dirpath1
                    toDirectory = (unicode(dst_pathMK) + unicode(dirname))
                    copy_tree(fromDirectory, toDirectory)

        elif modified_date >= wczoraj:
            print ('\x1b[0;30;44m' + dirpath + "   " + 'Do skopiowania w dniu jutrzejszym...' + '\x1b[0m')
    elif "zgrane" in katalog:
        print ('\x1b[0;33;42m' + dirpath + "   " + u"Katalog zostal już przeniesiony..." + '\x1b[0m')
    elif "zgrane" not in katalog and u"Samolej" in katalog2:  # Kaminski
        if modified_date <= wczoraj:
            try:
                os.rename(dirpath, os.path.join(dirpath + "_zgrane"))
                dirpath1 = dirpath + "_zgrane"
                dirname = dirpath1.split("\\")[-1]
                print ('\x1b[0;32;43m' + dirpath + "   " + "Kopiowanie do katalogu zbiorczego..." + '\x1b[0m')
                fromDirectory = dirpath1
                toDirectory = (unicode(dst_pathLS) + unicode(dirname))
                copy_tree(fromDirectory, toDirectory)
            except WindowsError:
                try:
                    os.rename(dirpath, os.path.join(dirpath + "__zgrane"))
                    dirpath1 = dirpath + "__zgrane"
                    dirname = dirpath1.split("\\")[-1]
                    print ('\x1b[0;32;43m' + dirpath + "   " + "Kopiowanie do katalogu zbiorczego..." + '\x1b[0m')
                    fromDirectory = dirpath1
                    toDirectory = (unicode(dst_pathLS) + unicode(dirname))
                    copy_tree(fromDirectory, toDirectory)
                except WindowsError:
                    os.rename(dirpath, os.path.join(dirpath + "___zgrane"))
                    dirpath1 = dirpath + "___zgrane"
                    dirname = dirpath1.split("\\")[-1]
                    print ('\x1b[0;32;43m' + dirpath + "   " + "Kopiowanie do katalogu zbiorczego..." + '\x1b[0m')
                    fromDirectory = dirpath1
                    toDirectory = (unicode(dst_pathLS) + unicode(dirname))
                    copy_tree(fromDirectory, toDirectory)

        elif modified_date >= wczoraj:
            print ('\x1b[0;30;44m' + dirpath + "   " + 'Do skopiowania w dniu jutrzejszym...' + '\x1b[0m')
    elif "zgrane" in katalog:
        print ('\x1b[0;33;42m' + dirpath + "   " + u"Katalog zostal już przeniesiony..." + '\x1b[0m')
    elif "zgrane" not in katalog and u"Siebielec" in katalog2:  # Siebielec
        if modified_date <= wczoraj:
            try:
                os.rename(dirpath, os.path.join(dirpath + "_zgrane"))
                dirpath1 = dirpath + "_zgrane"
                dirname = dirpath1.split("\\")[-1]
                print ('\x1b[0;32;43m' + dirpath + "   " + "Kopiowanie do katalogu zbiorczego..." + '\x1b[0m')
                fromDirectory = dirpath1
                toDirectory = (unicode(dst_pathMS) + unicode(dirname))
                copy_tree(fromDirectory, toDirectory)
            except WindowsError:
                try:
                    os.rename(dirpath, os.path.join(dirpath + "__zgrane"))
                    dirpath1 = dirpath + "__zgrane"
                    dirname = dirpath1.split("\\")[-1]
                    print ('\x1b[0;32;43m' + dirpath + "   " + "Kopiowanie do katalogu zbiorczego..." + '\x1b[0m')
                    fromDirectory = dirpath1
                    toDirectory = (unicode(dst_pathMS) + unicode(dirname))
                    copy_tree(fromDirectory, toDirectory)
                except WindowsError:
                    os.rename(dirpath, os.path.join(dirpath + "___zgrane"))
                    dirpath1 = dirpath + "___zgrane"
                    dirname = dirpath1.split("\\")[-1]
                    print ('\x1b[0;32;43m' + dirpath + "   " + "Kopiowanie do katalogu zbiorczego..." + '\x1b[0m')
                    fromDirectory = dirpath1
                    toDirectory = (unicode(dst_pathMS) + unicode(dirname))
                    copy_tree(fromDirectory, toDirectory)

        elif modified_date >= wczoraj:
            print ('\x1b[0;30;44m' + dirpath + "   " + 'Do skopiowania w dniu jutrzejszym...' + '\x1b[0m')
    elif "zgrane" in katalog:
        print ('\x1b[0;33;42m' + dirpath + "   " + u"Katalog zostal już przeniesiony..." + '\x1b[0m')

print ("""
##########################################################################





                        ZAKONCZONO PRZETWARZANIE



##########################################################################
                                                                    """)
raw_input("wcisnij dowolny klawisz aby zakonczyc")
__author__ = 'rnakielski'
