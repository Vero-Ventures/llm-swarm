from textwrap import dedent
from typing import TypedDict

from crewai import Agent
from langchain_community.llms import Ollama

llm = Ollama(model="llama3")


class AgentData(TypedDict, total=False):
    role: str
    goal: str
    backstory: str


AGENTS_DATA: dict[str, AgentData] = {
    "senior_python_developer": {
        "role": "Senior Python Developer",
        "goal": dedent(
            """
            To review Python functions and ensure that variable names are
            following best practices. Variable names are concise, descriptive,
            and easy to understand.
            """
        ),
        "backstory": dedent(
            """
            You're a Python developer who's been programming for decades. You're
            renowned for writing excellent code, and particularly for writing
            high-quality variable names.
            """
        ),
    },
    "senior_code_documentation_expert": {
        "role": "Senior Code Documentation Expert",
        "goal": "Write docstrings for Python functions.",
        "backstory": dedent(
            """
            You're a renowned code documentation expert, specifically in Python.
            You know how to write clean, concise docstrings that include all the
            information relevant to developers trying to understand a function.
            """
        ),
    },
    "senior_python_qa_tester": {
        "role": "Senior Python Quality Assurance Tester",
        "goal": dedent(
            """
            To review Python code and ensure that it follows best practices.
            Double-check that variable names are accurate and concise and that
            the docstrings accurately reflect what the function actually does.
            """
        ),
        "backstory": dedent(
            """
            You're a renowned quality assurance expert. You've been reviewing code
            for decades and ensure that code is flawless, with excellent variable
            names and docstrings.
            """
        ),
    },
    "senior_code_writer": {
        "role": "Senior Code Writer",
        "goal": dedent(
            """
            Take code and strip out everything except the code
            and docstrings.
            """
        ),
        "backstory": dedent(
            """
            You do an amazing job of getting code and stripping it
            of everything that's not code or documentation.
            """
        ),
    },
}


def create_agent(
    agent_type: str,
    llm: Ollama = llm,
    allow_delegation: bool = False,
    verbose: bool = False,
):
    agent_data = AGENTS_DATA.get(agent_type)
    if not agent_data:
        raise ValueError(f"No agent data found for type '{agent_type}'")
    return Agent(
        role=agent_data["role"],
        goal=agent_data["goal"],
        backstory=agent_data["backstory"],
        allow_delegation=allow_delegation,
        verbose=verbose,
        llm=llm,
    )
