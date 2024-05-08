import os
os.environ["SERPER_API_KEY"] = "Your Key"  # serper.dev API key
os.environ["OPENAI_API_KEY"] = "Your Key"

#################
# DEFINE AGENTS #
#################
from crewai_agents import Agent
from crewai import Task
from crewai import Crew, Process
from crewai.
from crewai_tools import SerperDevTool

from textwrap import dedent

search_tool = SerperDevTool()

# PROJECT MANAGER AGENT
project_manager = Agent(
    role='Project Manager',
    goal=dedent('''Understand the project requirements and breaks
                them down in clear, logical, actionable tasks that
                are easy to understand.'''),
    verbose=True,
    memory=True,
    backstory=dedent('''
                     An expert project manager who's been managing projects for years. They know how
                     to break down a project into clear, actionable tasks that are easy to understand.
                     They think through the project, step-by-step, and ensure everything makes sense.'''),
    allow_delegation=True
)

# SENIOR DEVELOPER AGENT
senior_developer = Agent(
    role='Senior Python Developer',
    goal='Write clean, efficient Python code that adheres to leading practices.',
    verbose=True,
    memory=True,
    backstory=dedent('''
                     An expert developer who's been writing code for years.
                     They know leading practices and does their best to write high-quality code.'''),
    allow_delegation=True
)

# SENIOR TESTER AGENT
senior_tester = Agent(
    role='Senior Python Tester',
    goal='Writes tests and ensures that code is thoroughly tested and bug-free.',
    verbose=True,
    memory=True,
    backstory=dedent('''
                     An expert tester who's been testing code for years. They're great at
                     writing tests, reviewing code, and finding errors that others might miss.'''),
    allow_delegation=True
)

#################
# DEFINE AGENTS #
#################

# Research task
understand_project_requirements = Task(
  description=dedent(
      '''Receive the project requirements, review then step-by-step, and create a development
      plan consisting of clearly defined, actionable tasks.'''),
  expected_output=dedent(
      '''A list of tasks that are easy to read, understand, and execute. Each task should
    have all the information required so that a developer can start working on it immediately.'''),
  agent=project_manager,
)

# Sign off on and deliver project
deliver_project = Task(
  description='Review the project, ensure all the tasks have been completed, and sign off on the project.',
  expected_output='A signed-off project that meets all the requirements and is ready to be run immediately.',
  agent=project_manager,
)

# Write all the code for the project
write_code = Task(
  description=dedent('''
                     Receive a series of tasks and, using leading practices, write clean, efficient code that
                     fulfill the requirements of each task.'''),
  expected_output=dedent('''
                         A script consisting of a complete program; it consists of all the tasks,
                         writtin in clean, effective code.'''),
  agent=senior_developer,
)

# Test all the code written for the project
test_code = Task(
  description=dedent('''
                     Receive a script, review the code to ensure it looks correct, and write tests to ensure
                     the code does what it should.'''),
  expected_output=dedent('''
                         A series of tests that cover all the code in the script. Each test should be written in a way
                         that it's easy to understand and should cover all the code in the script.'''),
  agent=senior_tester,
)

###############
# DEFINE CREW #
###############

# Forming the tech-focused crew with some enhanced configurations
crew = Crew(
  agents=[project_manager, senior_developer, senior_tester],
  tasks=[understand_project_requirements, write_code, test_code, deliver_project],
  process=Process.sequential,
  memory=True,
  cache=True,
  max_rpm=100,
  share_crew=True
)

result = crew.kickoff()
print(result)
