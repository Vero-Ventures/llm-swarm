from textwrap import dedent
from crewai import Agent
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama, OpenAI


load_dotenv()

# Initialize chosen LLM:

llama = Ollama(model="llama3")
deepseek = Ollama(model="deepseek-coder:6.7b")
codellama = Ollama(model="codellama")


class RefactoringAgents:
    def requirements_agent(self):
        return Agent(
            role="Requirements Engineer",
            goal="determine the goal of the given function and what needs to be changed",
            backstory=dedent(
                """\
                You are a Senior Software Engineer with a deep understanding of
                software design patterns and best practices in Python. You have a strong understanding of
                the various tools in python that make code more efficient and effective. Your task
                is to analyze the function given to you and determine it's goal, and 
                what ways it needs to be fixed and refactored or entirely written"""
            ),
            allow_delegation=False,
            verbose=True,
            llm=llama,
    )

    def coding_agent(self):
        return Agent(
            role="Senior Software Engineer",
            goal="observe the goal of the function as given by the requirements engineer, and execute the changes",
            backstory=dedent(
                """\
                You are a software engineer who takes the required changes from the previous engineer
                and rewrites the code. Ensure everything is functioning, following best practices, and has the desired
                inputs and outputs. use proper coding style, focusing on readablility. You may not change the parameters
                of the function"""
            ),
            allow_delegation=False, 
            verbose=True,
            llm=codellama,
        )

    def code_checking_agent(self):
        return Agent(
            role="Chief Refactoring Quality Assurance Engineer",
            goal="Oversee the entire refactoring process and confirm functionality",
            backstory=dedent(
                """\
                Leading the quality assurance for refactoring.
                You oversee the integration and testing phases, ensuring high-quality
                standards and seamless functionality across all modules. All code must
                have comments and docstrings where needed"""
            ),
            allow_delegation=False,
            verbose=True,
            llm=llama,
        )