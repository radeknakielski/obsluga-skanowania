import glob
import os
import shutil

__author__ = 'rnakielski'

srcDir = os.path.dirname(__file__) + "/"
trgDir = os.path.dirname(__file__) + "/"
tempdir = "e:\\__przenoszenie\\PRoba\\"

os.chdir(tempdir)
for file in glob.glob("*.jpg"):
    print file
    split = file.split(".")
    dir_name = split[0] + "." + split[1] + "." + split[2] + "." + split[3]
    print (srcDir + "/" + file)
    shutil.move(srcDir + file, srcDir + dir_name + "/" + file)




