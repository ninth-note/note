# base
from os.path import join

# common
from common.core import program_dir


class Config:

    def __init__(self):
        self.contents = self.get_contents()
   

    @property
    def path(self): 
        return join(program_dir(), 'config')


    def get_contents(self):
        contents = {}
        with open(self.path) as file:
            for line in file.read().splitlines():
                if '=' not in line:
                    continue
                key, value = line.split('=', 1)
                contents[key] = value
        return contents

