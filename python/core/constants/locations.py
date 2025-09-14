# base
from os import environ
from os.path import join

# config exceptions
from core.config import ConfigError

# utils
from utils import PROGRAM_DIR


class Locations:

    def __init__(self, conf):
        self.conf = conf

        # sub directories
        self.archive_dir = join(self.notes_dir, "archive")
        self.favourites_dir = join(self.notes_dir, "favourites")
        self.timestamped_dir = join(self.notes_dir, "timestamped")

        # file paths
        self.history_path = join(PROGRAM_DIR, "history")


    @property
    def notes_dir(self):
        try: 
            return self.conf.get_section_param("locations", "notes")
        except ConfigError as e:
            print(e)
            return join(PROGRAM_DIR, "data")

    @property
    def tmp_dir(self):
        default_dir = "/tmp/"
        try: 
            return self.conf.get_section_param("locations", "tmp")
        except ConfigError as e:
            print(e)
            return default_dir

