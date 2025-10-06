# base
from dataclasses import dataclass

# operations
from operations import operations


class Executor:

    def __init__(self):
        self.context = Context()


    # plan: list[tuple[str, dict]]
    def execute(self, plan):
        for operation_name, instructions in plan:
            result = self._run_operation(operation_name, instructions)
            if result.exit_code == 0:
                self._update_context(result)
            else:
                self._handle_failure(operation_name, result)
                break
        return self.context

    def _run_operation(self, operation_name, instructions):
        operation = operations[operation_name]()
        return operation.run(self.context, instructions)

    def _update_context(self, result):
        if result.payload:
            attr_name = result.payload.binding
            value = result.payload.value
            if hasattr(self.context, attr_name):
                setattr(self.context, attr_name, value)
            else:
                msg = f"Context has no attribute '{attr_name}'"
                raise AttributeError(msg)

    def _handle_failure(self, operation_name, result):
        print(f"{operation_name} failed with {result.exit_code}: {result.error}")



@dataclass
class Context:

    file: str = None

