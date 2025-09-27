#!/bin/bash
"true" '''\'
P=$(which python3 2>/dev/null) || P=$(which python); exec $P "$0" "$@"
'''
import os
import datetime
import argparse

EXAMPLE = "example"
BASE_DIR = "..."

from core import Core
from executor import Executor


class Note:

    def __init__(self):
        self.core = Core() # REMOVE LATER
        self.executor = Executor() # SHOULD HANDLE ALL OPERATIONS
        # self.time = datetime.datetime.now()

    # can make methods that will be passed into the
    # default fields in the add_argument
    # which will decide on location, name, date, etc

    def location(self):
        return "location"

    def name(self):
        return "name-timestamp"

    def _retrieve_cli_arguments(self):
        parser = argparse.ArgumentParser()
        # print(dir(parser))
        parser.add_argument("--example", help="... {0}".
                            format(EXAMPLE), default=EXAMPLE)
        parser.add_argument("--name", help="... {0}".
                            format(EXAMPLE), default=EXAMPLE)
        parser.add_argument("-a", help="... {0}".
                            format(EXAMPLE), default=EXAMPLE)
        parser.add_argument("--location",
                        help="Default location of this note {0}".
                            format(self.location()),
                        default=self.location())
        args = parser.parse_args()
        print(args)
        return args


    def start(self):
        arguments = self._retrieve_cli_arguments()
        # print(dir(argumnets))

        # very basic setup
        self.executor.setup()
        name = 'tmp'
        time = datetime.datetime.now()
        timestamp = time.strftime('-%d-%m-%Y-%I:%M%p')
        file = f'%s%s%s' % (self.core.const.locations.tmp_dir, name, timestamp)

        # basic execution
        cmd = f'nvim %s' % file
        exit_code = os.system(cmd)
        print(exit_code)


if __name__ == '__main__':
    notes = Note()
    notes.start()

