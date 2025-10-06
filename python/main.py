#!/bin/bash
"true" '''\'
P=$(which python3 2>/dev/null) || P=$(which python); exec $P "$0" "$@"
'''

# base
import argparse

# plan and execute
from executor import Executor


EXAMPLE = "example"
BASE_DIR = "..."



class Note:

    def __init__(self):
        self.executor = Executor()


    def _retrieve_cli_arguments(self):
        parser = argparse.ArgumentParser()
        # print(dir(parser))
        parser.add_argument("--name", help="... {0}".
                            format(EXAMPLE), default=EXAMPLE)
        parser.add_argument("-a", help="... {0}".
                            format(EXAMPLE), default=EXAMPLE)
        args = parser.parse_args()
        # print(args)
        return args

    def start(self):
        arguments = self._retrieve_cli_arguments()
        # print(dir(argumnets))

        # TEMP - Replace with Planner()
        plan = [
            ("setup_core_directories", {}),
            ("create_tmp_note", {}),
            ("edit_with_nvim", {}),
        ]

        self.executor.execute(plan)



if __name__ == '__main__':
    notes = Note()
    notes.start()

