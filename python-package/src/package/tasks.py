from textwrap import dedent

from crewai import Task


class RefactoringTasks:
    # Main code refactoring task
    def refactoring_task(self, agent, function):
        return Task(
            description=dedent(
                f"""\
                You will refactor this function using Python, focusing on improving its performance, readability, and maintainability while ensuring the core functionality remains unchanged:

                Function:
                ------------
                {function}

                Your final answer must be the full Python code, only the Python code and nothing else.
                """
            ),
            agent=agent,
            expected_output="Refactored Python code",
        )

    # lower level qa reviewing task
    def qa_review_task(self, agent, function):
        return Task(
            description=dedent(
                f"""\
                You are helping to improve a function by reviewing the refactored code. Check for logic errors, syntax errors, missing imports, variable declarations, mismatched brackets, and security vulnerabilities:

                Function:
                ------------
                {function}

                Your final answer must be the full Python code, only the Python code and nothing else.
                """
            ),
            agent=agent,
            expected_output="QA-reviewed Python code",
        )

    # higher level qa reviewing task
    def consistency_check_task(self, agent, function):
        return Task(
            description=dedent(
                f"""\
                You will ensure that the refactored function remains consistent with the original function's purpose and style. Confirm that there are no deviations in functionality:

                Function:
                ------------
                {function}

                Your final answer must be the full Python code, only the Python code and nothing else.
                """
            ),
            agent=agent,
            expected_output="Consistency-checked Python code",
        )
