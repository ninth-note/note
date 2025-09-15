# local
from core import Core
from utils.filesystem import setup_directory


class Controller:

    def __init__(self):
        self.core = Core()


    def setup(self):
        locations = self.core.const.locations
        setup_directory(locations.notes_dir)
        setup_directory(locations.tmp_dir)
            

    def execute(self, operation):
        pass

