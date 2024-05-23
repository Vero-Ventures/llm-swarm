from textwrap import dedent
from typing import TypedDict

from crewai import Task


class TaskData(TypedDict, total=False):
    description: str
    expected_output: str


TASKS_DATA: dict[str, TaskData] = {
    "improve_variable_names": {
        "description": dedent(
            """
            Review the variable names in the Python code. Update
            the variable names so that they're accurate, concise,
            easy to read, and easy to understand. Update the variable 
            names only; don't change anything else about the functions, 
            and do not add comments anywhere in the code.

            Python Function
            ---------------
            {code}
            """
        ),
        "expected_output": "A Python function with variable names that are accurate, concise, and easy to understand.",
    },
    "add_docstrings": {
        "description": dedent(
            """
            Provide docstrings to the Python code provided below.
            Ensure the documentation is concise, accurate, and easy
            to read.
            """
        ),
        "expected_output": "A Python function with a well-written, concise, and easy to understand docstring.",
    },
    "review_code": {
        "description": dedent(
            """
            Review code and documentation and ensure it meets the
            highest standards of quality. The variable names are
            clear, concise, and accurate; the docstrings are
            accurate and descriptive, so that any developer reading
            them, even a junior developer, would understand exactly
            what they do and how to use them.
            """
        ),
        "expected_output": "A Python function with excellent variable names and a well-written docstring.",
    },
    "write_code": {
        "description": dedent(
            """
            Review the provided code and remove anything that
            is not code or docstrings.
            """
        ),
        "expected_output": "Code that contains ONLY functions and docstrings. All other information is removed.",
    },
}


def create_task(task_type, agent, code=None, context=None):
    data = TASKS_DATA.get(task_type)
    if not data:
        raise ValueError(f"No task data found for type '{task_type}'")
    description = data["description"]
    if code:
        description = description.format(code=code)
    return Task(
        description=description,
        agent=agent,
        expected_output=data["expected_output"],
        context=context or [],
    )
