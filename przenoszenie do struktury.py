import os
from collections import defaultdict


def find_nonempty_dirs(root_dir=r'j:\_lubartow_skanowanie\test\I_przekazanie'):
    for dirpath, dirs, files in os.walk(root_dir):
        if files:
            try:
                yield dirpath.split('\\')[5], dirpath
            except:
                pass


lista_folderow = list(find_nonempty_dirs())

with open(r'j:\_lubartow_skanowanie\test\gmina-operat.txt', 'r') as f:
    lista_gminy = [tuple(map(str, i.rstrip('\n').split(','))) for i in
                   f]  ########## plik musi miec zapis nr_operatu,nr_gminy
# print lista_gminy
# print lista_folderow


def combine_item_pairs(l1, l2):
    D = {k: [v, False] for k, v in l1}
    for key, value in l2:
        if key in D:
            D[key][1] = value
        else:
            D[key] = [False, value]
    return (tuple([key] + value) for key, value in D.iteritems())
    err_file = open(r'j:\_lubartow_skanowanie\test\I_przekazanie' + "\\Blad_DPI.txt", "a")
    err_file.write(str(ret) + '/n')
    err_file.close()


zlacz = list(combine_item_pairs(lista_gminy, lista_folderow))

zlacz2 = [list(elem) for elem in zlacz]
zlacz3 = [map(str, elem) for elem in zlacz2]

#temp = []
#for sub_list in zlacz3:
#    temp.append(sub_list[0])
#zlacz3 = temp
#print (zlacz3[0])
for item in zlacz3:
    lista = open(r'j:\_lubartow_skanowanie\test\I_przekazanie' + "\\Blad_DPI.txt", "a")
    lista.write("%s\n" % item)
    lista.close()

    #zlacz4 = [x for x in zlacz3 if x[1] != ['False']]
    #print (zlacz4)