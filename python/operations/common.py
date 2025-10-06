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

    def run(self, context, instructions = None):
        raise NotImplementedError()



@dataclass
class Payload:

    binding: str = None
    value: Any = None



@dataclass
class Result:

    exit_code: int = 0          # 0 = success
    payload: Payload = None     # optional payload
    error: str | None = None    # error message if failed



class OperationError(Exception):
    """Custom exception for operation errors"""
    pass

