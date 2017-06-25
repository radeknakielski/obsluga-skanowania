__author__ = 'rnakielski'

import os

dir = os.path.dirname(__file__)

for root, subdirs, files in os.walk(dir):
    for i in subdirs:
        split = i.split(".")

        try:
            print split[2]
        except Exception:
            pass
