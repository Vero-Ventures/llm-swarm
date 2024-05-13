import re

from crewai import Crew
from package.ai.agents import RefactoringAgents
from package.ai.tasks import RefactoringTasks

# Initialize agents and tasks
agents = RefactoringAgents()
tasks = RefactoringTasks()

# Create Agents
senior_refactoring_engineer = agents.senior_refactoring_engineer_agent()
qa_refactoring_engineer = agents.qa_refactoring_engineer_agent()
chief_qa_refactoring_engineer = agents.chief_qa_refactoring_engineer_agent()


def create_crew(code: str, verbose=0) -> Crew:
    """
    Create a Crew instance with agents and tasks for refactoring code.
    """
    refactor_task = tasks.refactoring_task(
        senior_refactoring_engineer,
        code,
    )
    qa_review_task = tasks.qa_review_task(qa_refactoring_engineer, code)
    consistency_check_task = tasks.consistency_check_task(
        chief_qa_refactoring_engineer,
        code,
    )

    return Crew(
        agents=[
            senior_refactoring_engineer,
            qa_refactoring_engineer,
            chief_qa_refactoring_engineer,
        ],
        tasks=[
            refactor_task,
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
        return ""


def improve_code(code: str, verbose=0) -> str:
    """
    Improve code by refactoring it using a Crew instance.
    """
    crew = create_crew(code, verbose=verbose)
    result = crew.kickoff(inputs={"code": code})
    result = extract_code_block(result)
    return result
