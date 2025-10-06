# base
from functools import cached_property
from os import environ
from os.path import join
from pathlib import Path

# exceptions
from core.config import ConfigError

# utility
from utils import PROGRAM_DIR


class Locations:

    def __init__(self, conf):
        self.conf = conf

        # base directories
        self.home_dir = Path.home()

        # sub directories
        self.archive_dir = join(self.notes_dir, "archive")
        self.favourites_dir = join(self.notes_dir, "favourites")
        self.timestamped_dir = join(self.notes_dir, "timestamped")

        # file paths
        self.history_path = join(PROGRAM_DIR, "history")


    @cached_property
    def notes_dir(self):
        try: 
            return self.conf.get_section_param("locations", "notes")
        except ConfigError as e:
            print(e)
            return join(self.home_dir, "notes")

    @property
    def tmp_dir(self):
        default_dir = "/tmp/notes"
        try: 
            return self.conf.get_section_param("locations", "tmp")
        except ConfigError as e:
            print(e)
            return default_dir

