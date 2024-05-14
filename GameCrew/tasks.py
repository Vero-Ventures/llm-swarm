from crewai import Task
from textwrap import dedent

class GameDevTasks:

    def understand_project_requirements(self, agent, request):
        return Task(
            description=dedent(
                f'''
                You will receive a description of the project. Think about what tasks are required
                to successfully create the project, then create a task list. These tasks are clearly
                defined, actionable tasks that a developer can follow.

                Here is the project description: {request}
                '''),
            expected_output=dedent(
                '''
                A list of tasks that are easy to read, understand, and execute. Each task should
                have all the information required so that a developer can immediately start working.
                '''),
            agent=agent,
        )

    def write_code(self, agent, request):
        return Task(
            description=dedent(
                f'''
                You'll write a program based on the tasks provided to you.

                Tasks
                -----
                {request}

                Receive a series of tasks and, using leading practices, write clean, efficient code that
                fulfills the requirements of each task.
                '''),
            expected_output=dedent(
                '''A script consisting of a complete program: all the tasks, writtin in clean, effective Python code.'''),
            agent=agent,
        )

    def test_code(self, agent, request):
        return Task(
            description=dedent(
                f'''
                You'll receive a script of Python code. Review the code and ensure the following:
                - The code has no logical errors
                - The code is written with Python leading practices
                - All functions and classes are concisely and accurately documented
                - Variable names are accurate and descriptive

                Code
                ----
                {request}
                '''),
            expected_output=dedent(
                '''
                A script consisting of the tests you wrote, whether the tests passed or failed, and
                a brief write-up explaining if the code meets the requirements
                '''),
                agent=agent
        )

# Review Jupyter notebook -- how can we use this?
# Automate testing processes -- ?
# How can we approach research -- what are the best practices? How can we use this to improve our research?
# How can we improve the code quality?
# How can we improve the documentation?
# Documentation and testing
