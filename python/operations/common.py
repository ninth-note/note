# base
from dataclasses import dataclass
from typing import Any

# core
from core import Core

# utility
from utils.filesystem import setup_directory


class Operation:

    def __init__(self):
        self.core = Core()

    def run(self, instructions = None):
        raise NotImplementedError()



@dataclass
class Result:

    exit_code: int = 0          # 0 = success
    output: Any = None          # optional payload
    error: str | None = None    # error message if failed

