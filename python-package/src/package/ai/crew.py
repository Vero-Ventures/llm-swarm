from crewai import Crew

from agents import RefactoringAgents
from tasks import RefactoringTasks
from utils import clean_python_code

# Initialize agents and tasks
agents = RefactoringAgents()
tasks = RefactoringTasks()

# Create Agents
senior_refactoring_engineer = agents.senior_refactoring_engineer_agent()
qa_refactoring_engineer = agents.qa_refactoring_engineer_agent()
chief_qa_refactoring_engineer = agents.chief_qa_refactoring_engineer_agent()


def create_crew(code: str) -> Crew:
    # Create Tasks with the read code content
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
        verbose=True,
    )


def improve_code(code: str) -> str:
    crew = create_crew(code)
    result = crew.kickoff(inputs={"code": code})
    # TODO: generalize code extraction function
    result = clean_python_code(result)
    return result
