# base
import os

# common
from operations.common import Operation, Result


class SetupCoreDirectories(Operation):

    def run(self):
        locations = self.core.const.locations
        setup_directory(locations.notes_dir)
        setup_directory(locations.tmp_dir)

