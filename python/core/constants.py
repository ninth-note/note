# base
from os import environ
from os.path import join

# utils
from utils import program_dir


class Constants:

    def __init__(self, core):
        # core
        self.core = core

        # directories
        self.archive_dir = join(self.notes_dir, 'archive')
        self.favourite_dir = join(self.notes_dir, 'favourite')
        self.timestamped_dir = join(self.notes_dir, 'timestamped')

        # file paths
        self.history_path = join(program_dir(), 'history')
        # self.program_dir = program_dir()
 

    @property
    def notes_dir(self):
       return self.core.conf.contents['notes']

    @property
    def tmp_dir(self):
       return self.core.conf.contents['tmp_notes']

