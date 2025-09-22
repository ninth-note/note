# core
from core import Core

# utility
from utils.filesystem import setup_directory


class Operation:

    def __init__(self):
        self.core = Core()


    def run(self):
        pass



class SetupDirectories(Operation):

    def run(self):
        locations = self.core.const.locations
        setup_directory(locations.notes_dir)
        setup_directory(locations.tmp_dir)



class CreateTmpNote(Operation):

    def run(self):
        pass
