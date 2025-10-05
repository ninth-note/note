# constants
from core.constants.locations import Locations
from core.constants.settings import Settings


class Constants:

    def __init__(self, core):
        self.locations = Locations(core.conf)
        self.settings = Settings(core.conf)

