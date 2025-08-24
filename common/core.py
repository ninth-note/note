from os.path import dirname, abspath

def program_dir():
    return dirname(dirname(abspath(__file__)))

