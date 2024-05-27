from textwrap import dedent
from crewai import Task
from llm_swarm.ai.agents import (
    senior_developer,
    senior_qa_engineer,
    software_engineering_manager,
)

determine_requirements_task = Task(
    description=dedent(
        """
        Analyze the provided code to identify any issues that need 
        addressing within each function. Determine the purpose of each function 
        and specify necessary changes in its logic.
        Additionally, identify any style errors that require correction.
        Assess whether the function should be split into multiple functions,
        and if so, outline the new functions.

        Original code:
        ------------
        {code}
        """
    ),
    agent=software_engineering_manager,
    expected_output=dedent(
        """
        Your output should be a list of changes needed to improve and 
        refactor the function with proper style. This includes better 
        variable names, added documentation and comments, and adherence to 
        good coding paradigms.
        Do not include any code.
        """
    ),
)

refactoring_task = Task(
    description=dedent(
        """
        Refactor the provided code to enhance its performance, 
        readability, and maintainability based on the requirements 
        determined by the Software Engineering Manager while preserving 
        its core functionality.
        Ensure the code adheres to best practices, and functions are 
        properly documented.
        Use standard library tools where applicable to write the code 
        more efficiently.

        Original code:
        ------------
        {code}
        """
    ),
    expected_output=dedent(
        """
        Your output should be refactored code documented functions
        and nothing else.
        """
    ),
    agent=senior_developer,
)

qa_review_task = Task(
    description=dedent(
        """
        You are helping to review and improve the refactored code 
        provided by the Senior Developer.
        Correct any logic errors, syntax errors, missing imports, 
        variable naming/casing, mismatched brackets, and security 
        vulnerabilities.
        """
    ),
    expected_output=dedent(
        """
        Your output should be reviewed code with documented functions. 
        If no changes were made, return the provided code.
        """
    ),
    agent=senior_qa_engineer,
)

consistency_check_task = Task(
    description=dedent(
        """
        You will ensure that the refactored function provided by 
        Senior QA Engineer satisfies all the requirements.
        Confirm that there are no deviations in functionality.
        """
    ),
    expected_output=dedent(
        """
        Your output should be consistency-checked code with 
        documented functions and nothing else.
        """
    ),
    contexts=[
        determine_requirements_task, 
        refactoring_task, 
        qa_review_task,
    ],
    agent=software_engineering_manager,
)
