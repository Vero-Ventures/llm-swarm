from textwrap import dedent
from crewai import Agent

from langchain_community.llms import Ollama

# Initialize LLMs for agents
ollama3 = Ollama(model="llama3")
# deepseek = Ollama(model="deepseek-coder:6.7b")

class FunctionTestAgents:

    def variable_name_agent(self):
        return Agent(
            role='Variable Name Agent',
            goal='Ensure that variable names are descriptive, concise, and accurate.',
            backstory=dedent(
                '''
                You're an expect agent that helps developers write clean, efficient code.
                Your job is to ensure that variable names are descriptive, concise, and accurate.
                Do not add comments to the code.
                '''),
            allow_delegation=False,
            verbose=True,
            llm=ollama3
    )

    def code_comment_agent(self):
        return Agent(
            role='Code Comment Agent',
            goal='Add comments to code to explain its purpose and functionality. Only add comments that are necessary for a user to understand the code.',
            backstory=dedent(
                '''
                You're an expect code commentor. Your job is to add comments to the code to explain its purpose and functionality. Only add comments that
                are necessary for a user to understand the code. You're aware that code should be self-explanatory whenever possible, and that comments
                should only be used to explain complex or non-obvious parts of the code.
                '''),
            allow_delegation=False,
            verbose=True,
            llm=ollama3
    )

    def documentation_agent(self):
        return Agent(
            role='Documentation Agent',
            goal='Document code in a way that is easy to understand and follow.',
            backstory=dedent(
                '''
                You're an expert in writing docstrings. Your documentation is clear, concise, accurate, and easy to understand.
                '''),
            allow_delegation=False,
            verbose=True,
            llm=ollama3
    )

    # def code_documentation_agent(self):
    #     return Agent(
    #         role='Code Documentation Agent',
    #         goal='Document code in a way that is easy to understand and follow.',
    #         backstory=dedent(
    #             '''
    #             You are a code documentation agent. Your job is to document code in a way that is easy to understand and follow.
    #             '''),
    #         allow_delegation=False,
    #         verbose=True,
    #         llm=deepseek
    # )

    # def project_manager(self):
    #     return Agent(
    #         role='Project Manager',
    #         goal=dedent(
    #             '''
    #             Understand the project requirements and breaks
    #             them down in clear, logical, actionable tasks that
    #             are easy to understand.
    #             '''),
    #         backstory=dedent(
    #             '''
    #             An expert project manager who's been managing projects for years. They know how
    #             to break down a project into clear, actionable tasks that are easy to understand.
    #             They think through the project, step-by-step, and ensure everything makes sense.
    #             '''),
    #         allow_delegation=False,
    #         verbose=True,
    #         llm=ollama3
    # )

    # def senior_python_developer(self):
    #     return Agent(
    #         role='Senior Python Developer',
    #         goal='Write clean, efficient Python code that adheres to leading practices.',
    #         backstory=dedent(
    #             '''
    #             An expert developer who's been writing code for years.
    #             They know leading practices and does their best to write high-quality code.
    #             '''),
    #         allow_delegation=False,
    #         verbose=True,
    #         llm=deepseek
    # )

    # def senior_python_tester(self):
    #     return Agent(
    #         role='Senior Python Tester',
    #         goal='Writes tests and ensures that code is thoroughly tested and bug-free.',
    #         backstory=dedent(
    #             '''
    #             An expert tester who's been testing code for years. They're great at
    #             writing tests, reviewing code, and finding errors that others might miss.
    #             '''),
    #         allow_delegation=False,
    #         verbose=True,
    #         llm=deepseek
    # )


# import os
# from textwrap import dedent

# from crewai_agents import Agent
# from dotenv import load_dotenv
# from langchain_anthropic import ChatAnthropic
# from langchain_community.llms import Ollama, OpenAI
# from langchain_groq import ChatGroq
# from langchain_openai import ChatOpenAI

# load_dotenv()

# # Initialize chosen LLM:

# # local model, not smart but fast
# # chosen_llm = Ollama(model="phi3")
# # local model, decent
# chosen_llm = Ollama(model="llama3")
# deepseek = Ollama(model="deepseek-coder:6.7b")
# # cloud model, decent
# # chosen_llm = ChatAnthropic(model="claude-3-haiku-20240307", max_tokens=4096)
# # cloud model, smart but slow
# # chosen_llm = ChatAnthropic(model="claude-3-opus-20240307", max_tokens=4096)
# # cloud model, decent
# # chosen_llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7, max_tokens=4096)
# # cloud model, best
# # chosen_llm = ChatOpenAI(model_name="gpt-4-turbo-2024-04-09", temperature=0.5, max_tokens=4096)
# # cloud mode, fastest
# # chosen_llm = ChatGroq(model="llama3-8b-8192", temperature=0.5, max_tokens=4096)


# class RefactoringAgents:
#     def senior_refactoring_engineer_agent(self):
#         return Agent(
#             role="Senior Refactoring Engineer",
#             goal="Refactor software functions to improve efficiency and readability",
#             backstory=dedent(
#                 """\
#                 You are a Senior Software Engineer with a deep understanding of
#                 software design patterns and best practices in Python. Your task
#                 is to refactor code and implement documentation, aiming to enhance performance and maintainability
#                 without altering the core functionality."""
#             ),
#             allow_delegation=False,
#             verbose=True,
#             llm=chosen_llm,
#         )

#     def qa_refactoring_engineer_agent(self):
#         return Agent(
#             role="Refactoring Quality Assurance Engineer",
#             goal="Review refactored code for syntactic and logical correctness",
#             backstory=dedent(
#                 """\
#                 You are a meticulous software quality engineer specialized in
#                 the post-refactoring review. You scrutinize refactored code for
#                 syntax errors, possible regressions, and maintainability, ensuring
#                 the changes do not introduce new bugs."""
#             ),
#             allow_delegation=False,
#             verbose=True,
#             llm=chosen_llm,
#         )

#     def chief_qa_refactoring_engineer_agent(self):
#         return Agent(
#             role="Chief Refactoring Quality Assurance Engineer",
#             goal="Oversee the entire refactoring process and confirm functionality",
#             backstory=dedent(
#                 """\
#                 Leading the quality assurance for refactoring, you ensure that
#                 every piece of refactored code fulfills its intended functionality.
#                 You oversee the integration and testing phases, ensuring high-quality
#                 standards and seamless functionality across all modules."""
#             ),
#             allow_delegation=True,
#             verbose=True,
#             llm=chosen_llm,
#         )
