import re

from crewai import Crew
from llm_swarm.ai.agents import (
    senior_developer,
    senior_qa_engineer,
    software_engineering_manager,
)
from llm_swarm.ai.tasks import (
    determine_requirements_task,
    refactoring_task,
    qa_review_task,
    consistency_check_task,
)


def create_crew(code: str, verbose=0) -> Crew:
    """
    Create a Crew instance with agents and tasks for refactoring code.
    """
    return Crew(
        agents=[
            senior_developer,
            senior_qa_engineer,
            software_engineering_manager,
        ],
        tasks=[
            determine_requirements_task,
            refactoring_task,
            qa_review_task,
            consistency_check_task,
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
        return text.strip()


def improve_code(code: str, verbose=0) -> str:
    """
    Improve code by refactoring it using a Crew instance.
    """
    crew = create_crew(code, verbose=verbose)
    result = crew.kickoff(inputs={"code": code})
    result = extract_code_block(result)
    return result
