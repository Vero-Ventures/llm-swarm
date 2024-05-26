import re

from crewai import Crew
from llm_swarm.ai.agents import create_agent
from llm_swarm.ai.tasks import create_task


def create_crew(code: str, verbose=0) -> Crew:
    """
    Create a Crew instance with agents and tasks for refactoring code.
    """

    # Create Agents
    variable_name_agent = create_agent("senior_python_developer")
    docstring_agent = create_agent("senior_code_documentation_expert")
    qa_agent = create_agent("senior_python_qa_tester")
    code_writer_agent = create_agent("senior_code_writer")

    # Create Tasks
    improve_variable_names_task = create_task(
        "improve_variable_names",
        agent=variable_name_agent,
        code=code,
    )
    add_docstrings_task = create_task(
        "add_docstrings",
        agent=docstring_agent,
        context=[improve_variable_names_task],
    )
    review_code_task = create_task(
        "review_code",
        agent=qa_agent,
        context=[add_docstrings_task],
    )
    write_code_task = create_task(
        "write_code",
        agent=code_writer_agent,
        context=[review_code_task],
    )

    return Crew(
        agents=[
            variable_name_agent,
            docstring_agent,
            qa_agent,
            code_writer_agent,
        ],
        tasks=[
            improve_variable_names_task,
            add_docstrings_task,
            review_code_task,
            write_code_task,
        ],
        verbose=verbose,
    )


def extract_code_block(text):
    """
    Extract code block enclosed in triple backticks from text.
    """
    # Regular expression to match code block enclosed in triple backticks
    code_block_pattern = re.compile(r"```(?:[\w+-]*)\n(.*?)```", re.DOTALL)
    if match := code_block_pattern.search(text):
        return match.group(1).strip()
    else:
        return ""


def improve_code(code: str, verbose=0) -> str:
    """
    Improve code by refactoring it using a Crew instance.
    """
    crew = create_crew(code, verbose=verbose)
    result = crew.kickoff(inputs={"code": code})
    result = extract_code_block(result)
    return result
