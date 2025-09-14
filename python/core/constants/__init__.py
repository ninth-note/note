# base
from os import environ
from os.path import join

# constants
from core.constants.locations import Locations
from core.constants.settings import Settings

# utils
from utils import PROGRAM_DIR


class Constants:

    def __init__(self, core):
        self.locations = Locations(core.conf)
        self.settings = Settings(core.conf)

