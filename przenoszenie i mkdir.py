__author__ = 'rnakielski'

import os

root_path = 'e:\temp'
folders = ['Oslo', 'Berlin']
gh = folders
print gh
for folder in gh:
    os.mkdir(os.path.join(root_path, folder))