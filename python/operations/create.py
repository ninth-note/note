# common
from operations.common import Operation, Result


class CreateTmpNote(Operation):

    def run(self, instructions = None):
        name = 'tmp'
        time = datetime.datetime.now()
        timestamp = time.strftime('-%d-%m-%Y-%I:%M%p')
        file = f'%s%s%s' % (self.core.const.locations.tmp_dir, name, timestamp)

