from __future__ import print_function
import os
import glob
from pyPdf import PdfFileReader
import csv
########################Definicje rozmiarow plikow z pypdf.page.mediabox#################
A1_1_MEDIABOX = 'RectangleObject([0, -1625.28003, 2298.23999, 0])'
A1_2_MEDIABOX = 'RectangleObject([0, -1638, 2296.32007, 0])'
A1_3_MEDIABOX = 'RectangleObject([0, -1656.71997, 2327.04004, 0])'
A1_4_MEDIABOX = 'RectangleObject([0, -1656.71997, 2328.95996, 0])'
A1_5_MEDIABOX = 'RectangleObject([0, -1663.43994, 2338.56006, 0])'
A1_6_MEDIABOX = 'RectangleObject([0, -1664.88000, 2338.56006, 0])'
A1_7_MEDIABOX = 'RectangleObject([0, -1665.35999, 2332.80005, 0])'
A1_8_MEDIABOX = 'RectangleObject([0, -1665.59998, 2332.80005, 0])'
A1_9_MEDIABOX = 'RectangleObject([0, -1666.56006, 2334.71997, 0])'
A1_10_MEDIABOX = 'RectangleObject([0, -1667.76001, 2342.39990, 0])'
A1_11_MEDIABOX = 'RectangleObject([0, -1671.83997, 2330.87988, 0])'
A1_12_MEDIABOX = 'RectangleObject([0, -1673.76001, 2313.60010, 0])'
A1_13_MEDIABOX = 'RectangleObject([0, -1680, 2340.47998, 0])'
A1_14_MEDIABOX = 'RectangleObject([0, -1681.43994, 2352, 0])'
A1_15_MEDIABOX = 'RectangleObject([0, -1681.68005, 2386.56006, 0])'
A1_16_MEDIABOX = 'RectangleObject([0, -1683.35999, 2384.63989, 0])'
A1_17_MEDIABOX = 'RectangleObject([0, -1684.07996, 2384.63989, 0])'
A1_18_MEDIABOX = 'RectangleObject([0, -1684.31995, 2386.56006, 0])'
A1_19_MEDIABOX = 'RectangleObject([0, -1684.56006, 2342.39990, 0])'
A1_20_MEDIABOX = 'RectangleObject([0, -1684.56006, 2386.56006, 0])'
A1_21_MEDIABOX = 'RectangleObject([0, -1684.80005, 2384.63989, 0])'
A1_22_MEDIABOX = 'RectangleObject([0, -1685.04004, 2309.76001, 0])'
A1_23_MEDIABOX = 'RectangleObject([0, -1685.04004, 2338.56006, 0])'
A1_24_MEDIABOX = 'RectangleObject([0, -1685.28003, 2384.63989, 0])'
A1_25_MEDIABOX = 'RectangleObject([0, -1685.52002, 2384.63989, 0])'
A1_26_MEDIABOX = 'RectangleObject([0, -1686, 2344.32007, 0])'
A1_27_MEDIABOX = 'RectangleObject([0, -1686.23999, 2296.32007, 0])'
A1_28_MEDIABOX = 'RectangleObject([0, -1686.23999, 2386.56006, 0])'
A1_29_MEDIABOX = 'RectangleObject([0, -1686.71997, 2401.91992, 0])'
A1_30_MEDIABOX = 'RectangleObject([0, -1688.16003, 2342.39990, 0])'
A1_31_MEDIABOX = 'RectangleObject([0, -1689.35999, 2388.47998, 0])'
A1_32_MEDIABOX = 'RectangleObject([0, -1689.83997, 2382.71997, 0])'
A1_33_MEDIABOX = 'RectangleObject([0, -1690.80005, 2392.32007, 0])'
A1_34_MEDIABOX = 'RectangleObject([0, -1691.04004, 2396.15991, 0])'
A1_35_MEDIABOX = 'RectangleObject([0, -1691.52002, 2388.47998, 0])'
A1_36_MEDIABOX = 'RectangleObject([0, -1691.76001, 2386.56006, 0])'
A1_37_MEDIABOX = 'RectangleObject([0, -1692.47998, 2388.47998, 0])'
A1_38_MEDIABOX = 'RectangleObject([0, -1693.68005, 2388.47998, 0])'
A1_39_MEDIABOX = 'RectangleObject([0, -1693.68005, 2390.39990, 0])'
A1_40_MEDIABOX = 'RectangleObject([0, -1695.83997, 2388.47998, 0])'
A1_41_MEDIABOX = 'RectangleObject([0, -1696.80005, 2336.63989, 0])'
A1_42_MEDIABOX = 'RectangleObject([0, -1699.19995, 2336.63989, 0])'
A1_43_MEDIABOX = 'RectangleObject([0, -1708.56006, 2407.67993, 0])'
A1_44_MEDIABOX = 'RectangleObject([0, -1721.52002, 2376.95996, 0])'
A1_45_MEDIABOX = 'RectangleObject([0, -1780.56006, 2401.91992, 0])'
A1_46_MEDIABOX = 'RectangleObject([0, -2367.36011, 1672.31995, 0])'
A1_47_MEDIABOX = 'RectangleObject([0, -2425.91992, 1749.12000, 0])'
A1_48_MEDIABOX = 'RectangleObject([0, -2433.84009, 1668.47998, 0])'
A2_1_MEDIABOX = 'RectangleObject([0, -1192.07996, 1676.16003, 0])'
A2_2_MEDIABOX = 'RectangleObject([0, -1192.31995, 1676.16003, 0])'
A2_3_MEDIABOX = 'RectangleObject([0, 0, 1191, 842])'
A2_4_MEDIABOX = 'RectangleObject([0, 0, 1198.08000, 844.80000])'
A3_1_MEDIABOX = 'RectangleObject([0, -840, 1184.64001, 0])'
A3_2_MEDIABOX = 'RectangleObject([0, -842.15997, 1146.23999, 0])'
A3_3_MEDIABOX = 'RectangleObject([0, -842.64001, 1184.64001, 0])'
A3_4_MEDIABOX = 'RectangleObject([0, 0, 1032, 729])'
A3_5_MEDIABOX = 'RectangleObject([0, 0, 844.80000, 1198.08000])'
A4_1_MEDIABOX = 'RectangleObject([0, -601.20001, 840.96002, 0])'
A4_2_MEDIABOX = 'RectangleObject([0, 0, 516, 729])'
A4_3_MEDIABOX = 'RectangleObject([0, 0, 522.24000, 737.28000])'
A4_4_MEDIABOX = 'RectangleObject([0, 0, 595, 842])'
A4_5_MEDIABOX = 'RectangleObject([0, 0, 599.04000, 844.80000])'
A4_6_MEDIABOX = 'RectangleObject([0, 0, 842, 595])'
A5_1_MEDIABOX = 'RectangleObject([0, 0, 595, 420])'
A6_1_MEDIABOX = 'RectangleObject([0, 0, 420, 298])'
A6_2_MEDIABOX = 'RectangleObject([0, 0, 430.08000, 307.20000])'

I_1_MEDIABOX = 'RectangleObject([0, -1416, 1987.19995, 0])'
I_2_MEDIABOX = 'RectangleObject([0, -1579.68005, 721.91998, 0])'
I_3_MEDIABOX = 'RectangleObject([0, -1669.92004, 2177.28003, 0])'
I_4_MEDIABOX = 'RectangleObject([0, -1752.23999, 2547.84009, 0])'
I_5_MEDIABOX = 'RectangleObject([0, -1825.92004, 846.71997, 0])'
I_6_MEDIABOX = 'RectangleObject([0, -2815.43994, 1733.76001, 0])'
I_7_MEDIABOX = 'RectangleObject([0, -528.23999, 1079.04004, 0])'
I_8_MEDIABOX = 'RectangleObject([0, -535.67999, 1240.31995, 0])'
I_9_MEDIABOX = 'RectangleObject([0, -6203.27979, 800.64001, 0])'

########################Definicje rozmiarow plikow z pypdf.page.mediabox#################

dir = os.path.dirname(__file__)  # katalog w ktorym jest plik *.py
sciezka = dir
########################zapis csv z wynikami#################
def save_csv(path):
    keys = ['nazwa', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'I', 'liczba stron']
    with open(path + '\\wynik.csv', 'a') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        # dict_writer.writeheader()
        dict_writer.writerow(wynik)


########################zapis csv z wynikami#################
########################analiza stron pdf#################
def analyze_pdf(path):
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
            size = str(pdf.getPage(i).mediaBox)
            if size == A1_1_MEDIABOX:
                result['a1'] += 1
            if size == A1_2_MEDIABOX:
                result['a1'] += 1
            if size == A1_3_MEDIABOX:
                result['a1'] += 1
            if size == A1_4_MEDIABOX:
                result['a1'] += 1
            if size == A1_5_MEDIABOX:
                result['a1'] += 1
            if size == A1_6_MEDIABOX:
                result['a1'] += 1
            if size == A1_7_MEDIABOX:
                result['a1'] += 1
            if size == A1_8_MEDIABOX:
                result['a1'] += 1
            if size == A1_9_MEDIABOX:
                result['a1'] += 1
            if size == A1_10_MEDIABOX:
                result['a1'] += 1
            if size == A1_11_MEDIABOX:
                result['a1'] += 1
            if size == A1_12_MEDIABOX:
                result['a1'] += 1
            if size == A1_13_MEDIABOX:
                result['a1'] += 1
            if size == A1_14_MEDIABOX:
                result['a1'] += 1
            if size == A1_15_MEDIABOX:
                result['a1'] += 1
            if size == A1_16_MEDIABOX:
                result['a1'] += 1
            if size == A1_17_MEDIABOX:
                result['a1'] += 1
            if size == A1_18_MEDIABOX:
                result['a1'] += 1
            if size == A1_19_MEDIABOX:
                result['a1'] += 1
            if size == A1_20_MEDIABOX:
                result['a1'] += 1
            if size == A1_21_MEDIABOX:
                result['a1'] += 1
            if size == A1_22_MEDIABOX:
                result['a1'] += 1
            if size == A1_23_MEDIABOX:
                result['a1'] += 1
            if size == A1_24_MEDIABOX:
                result['a1'] += 1
            if size == A1_25_MEDIABOX:
                result['a1'] += 1
            if size == A1_26_MEDIABOX:
                result['a1'] += 1
            if size == A1_27_MEDIABOX:
                result['a1'] += 1
            if size == A1_28_MEDIABOX:
                result['a1'] += 1
            if size == A1_29_MEDIABOX:
                result['a1'] += 1
            if size == A1_30_MEDIABOX:
                result['a1'] += 1
            if size == A1_31_MEDIABOX:
                result['a1'] += 1
            if size == A1_32_MEDIABOX:
                result['a1'] += 1
            if size == A1_33_MEDIABOX:
                result['a1'] += 1
            if size == A1_34_MEDIABOX:
                result['a1'] += 1
            if size == A1_35_MEDIABOX:
                result['a1'] += 1
            if size == A1_36_MEDIABOX:
                result['a1'] += 1
            if size == A1_37_MEDIABOX:
                result['a1'] += 1
            if size == A1_38_MEDIABOX:
                result['a1'] += 1
            if size == A1_39_MEDIABOX:
                result['a1'] += 1
            if size == A1_40_MEDIABOX:
                result['a1'] += 1
            if size == A1_41_MEDIABOX:
                result['a1'] += 1
            if size == A1_42_MEDIABOX:
                result['a1'] += 1
            if size == A1_43_MEDIABOX:
                result['a1'] += 1
            if size == A1_44_MEDIABOX:
                result['a1'] += 1
            if size == A1_45_MEDIABOX:
                result['a1'] += 1
            if size == A1_46_MEDIABOX:
                result['a1'] += 1
            if size == A1_47_MEDIABOX:
                result['a1'] += 1
            if size == A1_48_MEDIABOX:
                result['a1'] += 1
            if size == A2_1_MEDIABOX:
                result['a2'] += 1
            if size == A2_2_MEDIABOX:
                result['a2'] += 1
            if size == A2_3_MEDIABOX:
                result['a2'] += 1
            if size == A2_4_MEDIABOX:
                result['a2'] += 1
            if size == A3_1_MEDIABOX:
                result['a3'] += 1
            if size == A3_2_MEDIABOX:
                result['a3'] += 1
            if size == A3_3_MEDIABOX:
                result['a3'] += 1
            if size == A3_4_MEDIABOX:
                result['a3'] += 1
            if size == A3_5_MEDIABOX:
                result['a3'] += 1
            if size == A4_1_MEDIABOX:
                result['a4'] += 1
            if size == A4_2_MEDIABOX:
                result['a4'] += 1
            if size == A4_3_MEDIABOX:
                result['a4'] += 1
            if size == A4_4_MEDIABOX:
                result['a4'] += 1
            if size == A4_5_MEDIABOX:
                result['a4'] += 1
            if size == A4_6_MEDIABOX:
                result['a4'] += 1
            if size == A5_1_MEDIABOX:
                result['a5'] += 1
            if size == A6_1_MEDIABOX:
                result['a6'] += 1
            if size == A6_2_MEDIABOX:
                result['a6'] += 1
            if size == I_1_MEDIABOX:
                result['I'] += 1
            if size == I_2_MEDIABOX:
                result['I'] += 1
            if size == I_3_MEDIABOX:
                result['I'] += 1
            if size == I_4_MEDIABOX:
                result['I'] += 1
            if size == I_5_MEDIABOX:
                result['I'] += 1
            if size == I_6_MEDIABOX:
                result['I'] += 1
            if size == I_7_MEDIABOX:
                result['I'] += 1
            if size == I_8_MEDIABOX:
                result['I'] += 1
            elif size == I_9_MEDIABOX:
                result['I'] += 1

    return result

########################analiza stron pdf#################

########################TO DZIALA###########################################


for dirpath, dirs, files in os.walk(sciezka):
    parent = dirpath
    os.chdir(parent)

    for infile in glob.glob(os.path.basename('*.pdf')):
        input = PdfFileReader(file(infile, "rb"))
        page_count = str(input.getNumPages())
        wynik = analyze_pdf(os.path.abspath(infile))

        fullpath = os.path.abspath(os.path.abspath(infile))
        # print fullpath



        save_csv(sciezka)

########################TO DZIALA###########################################

