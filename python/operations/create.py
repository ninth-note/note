# base
from datetime import datetime

# common
from operations.common import Operation, Result


class CreateNote(Operation):

    def run(self, context, instructions = None):
        pass


class CreateTmpNote(Operation):

    def _timestamp_now(self):
        time = datetime.now()
        fmt = '%d-%m-%Y-%I:%M' 
        timestamp = time.strftime(fmt)
        return timestamp 

    def _prepare_file(self):
        name = "tmp"
        timestamp = self._timestamp_now()
        tmp_dir = self.core.const.locations.tmp_dir
        fmt = f"%s%s-%s" 
        file = fmt % (tmp_dir, name, timestamp)
        return file

    def run(self, context, instructions = None):
        file = self._prepare_file()
        try:
            open(file, "x").close()
        except OSError as e:
            return Result(exit_code=1, error=str(e))
        return Result(output=file, key="file")

