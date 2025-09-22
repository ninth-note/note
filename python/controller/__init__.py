# core
from core import Core

# utils
from utils.filesystem import setup_directory

# operations
from operations import operations


class Controller:

    def __init__(self):
        # is this of any use here?
        self.core = Core()


    def setup_directories(self):
        operation = operations["setup_directories"]
        operation.run()

    # def execute_operation(self, name: str, params = None):
    #     operation = operations[name]
    #     operation.run(params)


    def execute(self, plan: list[tuple[str, dict]]):
        """
            Execute sequence of operations:
                - in the given order.
                - based on user instructions. 
        """
        for operation_name, instructions in plan:
            operation = operations[operation_name]
            operation.run(instructions)
