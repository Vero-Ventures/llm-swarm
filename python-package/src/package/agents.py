from textwrap import dedent

from crewai import Agent
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_community.llms import Ollama
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

load_dotenv()

models = {
    # local model, not smart but fast
    "phi3": Ollama(model="phi3"),
    # local model, decent
    "llama3": Ollama(model="llama3"),
    # cloud model, decent
    "haiku": ChatAnthropic(model="claude-3-haiku-20240307", max_tokens=4096),
    # cloud model, smart but slow
    "opus": ChatAnthropic(model="claude-3-opus-20240307", max_tokens=4096),
    # cloud model, decent
    "gpt3.5-turbo": ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7, max_tokens=4096),
    # cloud model, best
    "gpt4-turbo": ChatOpenAI(
        model="gpt-4-turbo-2024-04-09", temperature=0.5, max_tokens=4096
    ),
    # cloud mode, fastest
    "groq": ChatGroq(model="llama3-8b-8192", temperature=0.5, max_tokens=4096),
}
chosen_llm = models["haiku"]


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
            llm=chosen_llm,
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
            llm=chosen_llm,
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
            llm=chosen_llm,
        )
