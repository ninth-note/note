# operations
from operations import operations


class Executor:

    # def execute_original(self, plan: list[tuple[str, dict]]):
    #     for operation_name, instructions in plan:
    #         operation = operations[operation_name]()
    #         operation.run(instructions)
    #
    # def execute_multiple(self, plan: list[tuple[str, dict]]):
    #     context = {}
    #     for operation_name, instructions in plan:
    #         operation = operations[operation_name]()
    #         try:
    #             result = operation.run(instructions, context)
    #             if isinstance(result, int) and result != 0:
    #                 print(f"{operation_name} failed with code {result}")
    #                 break
    #             context[operation_name] = result
    #         except Exception as e:
    #             print(f"{operation_name} crashed: {e}")
    #             break
    #     return context

    def __init__(self):
        # context: dict[str, object]
        self.context = {}


    # plan: list[tuple[str, dict]]
    def execute(self, plan):
        for operation_name, instructions in plan:
            result = self._run_operation(operation_name, instructions)

            if result.exit_code != 0:
                self._handle_failure(operation_name, result)
                break

            self._update_context(operation_name, result)

        return self.context

    def _run_operation(self, operation_name: str, instructions: dict) -> Result:
        operation = operations[operation_name]()
        return operation.run(instructions, self.context)

    def _handle_failure(self, operation_name: str, result: Result) -> None:
        print(f"{operation_name} failed with {result.exit_code}: {result.error}")

    def _update_context(self, operation_name: str, result: Result) -> None:
        self.context[operation_name] = result.output

