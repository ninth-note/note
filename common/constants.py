# base
from os import environ
from os.path import join

# common
from common.core import program_dir
from common.config import Config


class Constants:

    def __init__(self):
        # objects
        self.conf = Config()

        # directories
        self.archive_dir = join(self.notes_dir, 'archive')
        self.favourite_dir = join(self.notes_dir, 'favourite')
        self.timestamped_dir = join(self.notes_dir, 'timestamped')

        self.history_path = join(program_dir(), 'history')
        # self.program_dir = program_dir()
 

    @property
    def notes_dir(self):
       return self.conf.contents['notes']

    @property
    def tmp_dir(self):
       return self.conf.contents['tmp_notes']

