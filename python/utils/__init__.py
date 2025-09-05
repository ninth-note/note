from os.path import dirname, abspath

def program_dir():
    return dirname(dirname(dirname(abspath(__file__))))

