# operations
from operations import operations


class Executor:

    def __init__(self):
        # context: dict[str, object]
        self.context = {}


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
        if result.key and result.output:
            self.context[result.key] = result.output

    def _handle_failure(self, operation_name, result):
        print(f"{operation_name} failed with {result.exit_code}: {result.error}")

