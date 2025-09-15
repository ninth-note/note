from os import makedirs
from os.path import exists


def setup_directory(directory):
    if exists(directory):
        return
    else:
       makedirs(directory)
