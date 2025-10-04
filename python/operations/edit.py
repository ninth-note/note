# base
from os import system

# common
from operations.common import Operation, Result


class EditWithNvim(Operation):

    def run(self, context, instructions = None):
        path = context["file"]
        cmd = f'nvim %s' % path
        try:
            exit_code = system(cmd)
        except Exception as e:
            print(exit_code)
            return Result(exit_code=1, error=str(e))
        return Result()

