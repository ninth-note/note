# base
import os

# utility
from utils.filesystem import setup_directory

# common
from operations.common import Operation, Result, Payload


class SetupCoreDirectories(Operation):

    def run(self, context, instructions = None):
        locations = self.core.const.locations
        try:
            setup_directory(locations.notes_dir)
            setup_directory(locations.tmp_dir)
        except Exception as e:
            return Result(exit_code=1, error=str(e))
        return Result()


