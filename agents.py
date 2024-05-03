from textwrap import dedent
from crewai import Agent
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama, OpenAI


load_dotenv()

# Initialize chosen LLM:

# local model, not smart but fast
# chosen_llm = Ollama(model="phi3")
# local model, decent
# chosen_llm = Ollama(model="llama3")
# cloud model, decent
chosen_llm = ChatAnthropic(model="claude-3-haiku-20240307", max_tokens=4096)
# cloud model, smart but slow
# chosen_llm = ChatAnthropic(model="claude-3-opus-20240307", max_tokens=4096)
# cloud model, decent
# chosen_llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7, max_tokens=4096)
# cloud model, best
# chosen_llm = ChatOpenAI(model_name="gpt-4", temperature=0.7, max_tokens=4096)


class GameAgents:
    def senior_engineer_agent(self):
        return Agent(
            role="Senior Software Engineer",
            goal="Create software as needed",
            backstory=dedent(
                """\
				You are a Senior Software Engineer at a leading tech think tank.
				Your expertise in programming in python. and do your best to
				produce perfect code."""
            ),
            allow_delegation=False,
            verbose=True,
            llm=chosen_llm,
        )

    def qa_engineer_agent(self):
        return Agent(
            role="Software Quality Control Engineer",
            goal="create prefect code, by analizing the code that is given for errors",
            backstory=dedent(
                """\
				You are a software engineer that specializes in checking code
  			for errors. You have an eye for detail and a knack for finding
				hidden bugs.
  			You check for missing imports, variable declarations, mismatched
				brackets and syntax errors.
  			You also check for security vulnerabilities, and logic errors."""
            ),
            allow_delegation=False,
            verbose=True,
            llm=chosen_llm,
        )

    def chief_qa_engineer_agent(self):
        return Agent(
            role="Chief Software Quality Control Engineer",
            goal="Ensure that the code does the job that it is supposed to do",
            backstory=dedent(
                """\
				You feel that programmers always do only half the job, so you are
				super dedicate to make high quality code."""
            ),
            allow_delegation=True,
            verbose=True,
            llm=chosen_llm,
        )
