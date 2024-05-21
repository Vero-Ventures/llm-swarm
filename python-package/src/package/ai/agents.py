from textwrap import dedent

from crewai import Agent
from langchain_community.llms import Ollama

llm = Ollama(model="llama3")


class RefactoringAgents:
    def senior_refactoring_engineer_agent(self):
        return Agent(
            role="Senior Refactoring Engineer",
            goal="Refactor software functions to improve efficiency and readability",
            backstory=dedent(
                """\
                You are a Senior Software Engineer with a deep understanding of
                software design patterns and best practices in Python. Your task
                is to refactor code and implement documentation, aiming to enhance performance and maintainability
                without altering the core functionality."""
            ),
            allow_delegation=False,
            verbose=True,
            llm=llm,
        )

    def qa_refactoring_engineer_agent(self):
        return Agent(
            role="Refactoring Quality Assurance Engineer",
            goal="Review refactored code for syntactic and logical correctness",
            backstory=dedent(
                """\
                You are a meticulous software quality engineer specialized in
                the post-refactoring review. You scrutinize refactored code for
                syntax errors, possible regressions, and maintainability, ensuring
                the changes do not introduce new bugs."""
            ),
            allow_delegation=False,
            verbose=True,
            llm=llm,
        )

    def chief_qa_refactoring_engineer_agent(self):
        return Agent(
            role="Chief Refactoring Quality Assurance Engineer",
            goal="Oversee the entire refactoring process and confirm functionality",
            backstory=dedent(
                """\
                Leading the quality assurance for refactoring, you ensure that
                every piece of refactored code fulfills its intended functionality.
                You oversee the integration and testing phases, ensuring high-quality
                standards and seamless functionality across all modules."""
            ),
            allow_delegation=True,
            verbose=True,
            llm=llm,
        )
