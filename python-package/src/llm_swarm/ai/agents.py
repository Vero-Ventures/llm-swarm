from textwrap import dedent
from crewai import Agent
from langchain_community.llms import Ollama

VERBOSE = True

llama3 = Ollama(model="llama3")
code_llama = Ollama(model="codellama")

senior_developer = Agent(
    role="Senior Software Developer",
    goal=("Refactor software functions to improve efficiency and readability"),
    backstory=dedent(
        """
        You are a Senior Software Developer with a deep understanding of
        software design patterns and best practices in software development.
        Your task is to refactor code and add documentation, aiming to
        enhance performance and maintainability without altering the
        core functionality.
        """
    ),
    allow_delegation=False,
    verbose=VERBOSE,
    llm=code_llama,
)

senior_qa_engineer = Agent(
    role="Senior QA Engineer",
    goal="Review refactored code for syntactic and logical correctness",
    backstory=dedent(
        """
        You are a meticulous software quality assurance engineer
        specializing in post-refactoring reviews. You scrutinize
        refactored code for syntax errors, possible regressions, and
        maintainability, ensuring any changes made do not introduce new bugs.
        """
    ),
    allow_delegation=False,
    verbose=VERBOSE,
    llm=code_llama,
)

software_engineering_manager = Agent(
    role="Software Engineering Manager",
    goal="Oversee the entire refactoring process and confirm functionality",
    backstory=dedent(
        """
        Ensure that every piece of refactored code fulfills its intended
        functionality. You oversee the integration and testing phases,
        ensuring high-quality standards and seamless functionality.
        """
    ),
    allow_delegation=False,
    verbose=VERBOSE,
    llm=llama3,
)
