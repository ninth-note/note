# core
from core.config import Config
from core.constants import Constants
from core.history import History

class Core:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, "_initialized") and self._initialized:
            return

        # objects
        self.conf = Config()
        self.const = Constants(self)
        self.history = History(self)

        self._initialized = True

