# core
from core.config import Config
from core.constants import Constants
from core.history import History

class Core:

    def __init__(self):
        # aditional setup
        # ...

        # objects
        self.conf = Config()
        self.const = Constants(self)
        self.history = History(self)

