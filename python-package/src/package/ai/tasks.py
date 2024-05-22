from textwrap import dedent

from crewai import Task


class RefactoringTasks:
    # Main code refactoring task
    def determine_reqs_task(self, agent, function):
        return Task(
            description=dedent(
                f"""\
                You will read over the given code, identify the function that needs to be changed, determine it's goal, what needs to be changed in it's logic,
                and find any style errors that should be refactored. determine if it needs to be split into
                multiple functions and if so, define them. Do not write any code, only pass along changes
                that need to be made

                Function:
                ------------
                {function}

                Your final answer must be a list of changes that must be made to the desired function to improve the function
                and refactor it with proper style, with the goal of fulfilling the request. do not include any code
                """
            ),
            agent=agent,
            expected_output="List of refactoring changes to be made",
        )

    # lower level qa reviewing task
    def write_code_task(self, agent, function):
        return Task(
            description=dedent(
                f"""\
                You are given a list of changes to be made to the desired function. Go through this list one by one with delegation
                and rewrite the code to solve all of them. You may not change the parameters of the function. Improve any comments that are currently there.
                You will be given the surrounding code for contextual understanding. Only modify the function you have been requested to change
                the final answer must be Python code for the desired function, and nothing but the code. Do not modify anything other than the function.
                try to use premade tools or imports to write the code more efficiently.

                Function:
                ------------
                {function}

                Your final answer must be only your changes on the specified function, only the Python code and nothing else.
                """
            ),
            agent=agent,
            expected_output="Python function",
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

    def check_code_task(self, agent):
        return Task(
            description=dedent(
                """
                A list of all of the changes that needed to be made was previously created, then the agent
                before you wrote some code. Take the new code and check that it meets all of the changes
                requested by the list. If there are any that were not completed, then finish them. Otherwise,
                change as little as possible. Do not change anything not requested by the list.
                try to use premade tools or imports to write the
                code more efficiently. Add docstrings if there are none

                Your final answer must be the function code, only the code and nothing else.
                """
            ),
            agent=agent,
            expected_output="Python function",
        )
