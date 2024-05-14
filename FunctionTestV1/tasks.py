from crewai import Task
from textwrap import dedent
from llama_cpp import LlamaCpp

class FunctionTestTasks:

    def improve_variable_names(self, agent, request):
        return Task(
            description=dedent(
                f'''
                Receive Python code. Ensure that all variable names are descriptive, concise, and accurate.
                Do not add comments to the code.

                Code
                ----
                {request}
                '''),
            expected_output=dedent(
                '''
                Python code with improved variable names
                '''),
                agent=agent
        )

    def add_code_comments(self, agent, request):
        return Task(
            description=dedent(
                f'''
                Receive Python code. Add comments to the code to explain its purpose and functionality.
                Only add comments that are necessary for a user to understand the code. If a line of
                code is self-explanatory, do not add a comment.

                Code
                ----
                {request}
                '''),
            expected_output=dedent(
                '''
                Python code with added comments
                '''),
                agent=agent
        )

    def review_code_comments(self, agent, request):
        return Task(
            description=dedent(
                f'''
                Receive Python code with comments. Review the code and ensure that all comments are
                accurate and helpful. If a comment is not necessary, remove it.

                Code
                ----
                {request}
                '''),
            expected_output=dedent(
                '''
                Python code with reviewed comments
                '''),
                agent=agent
        )

    def add_documentation(self, agent, request):
        return Task(
            description=dedent(
                f'''
                Add docstrings to the code to explain its purpose and functionality.
                Ensure the documentation is clear, concise, accurate, and easy to understand.

                Code
                ----
                {request}
                '''),
            expected_output=dedent(
                '''
                Python code with added documentation
                '''),
                agent=agent
        )

    # def understand_project_requirements(self, agent, request):
    #     return Task(
    #         description=dedent(
    #             f'''
    #             You will receive a description of the project. Think about what tasks are required
    #             to successfully create the project, then create a task list. These tasks are clearly
    #             defined, actionable tasks that a developer can follow.

    #             Here is the project description: {request}
    #             '''),
    #         expected_output=dedent(
    #             '''
    #             A list of tasks that are easy to read, understand, and execute. Each task should
    #             have all the information required so that a developer can immediately start working.
    #             '''),
    #         agent=agent,
    #     )

    # def write_code(self, agent, request):
    #     return Task(
    #         description=dedent(
    #             f'''
    #             You'll write a program based on the tasks provided to you.

    #             Tasks
    #             -----
    #             {request}

    #             Receive a series of tasks and, using leading practices, write clean, efficient code that
    #             fulfills the requirements of each task.
    #             '''),
    #         expected_output=dedent(
    #             '''A script consisting of a complete program: all the tasks, writtin in clean, effective Python code.'''),
    #         agent=agent,
    #     )

    # def test_code(self, agent, request):
    #     return Task(
    #         description=dedent(
    #             f'''
    #             You'll receive a script of Python code. Review the code and ensure the following:
    #             - The code has no logical errors
    #             - The code is written with Python leading practices
    #             - All functions and classes are concisely and accurately documented
    #             - Variable names are accurate and descriptive

    #             Code
    #             ----
    #             {request}
    #             '''),
    #         expected_output=dedent(
    #             '''
    #             A script consisting of the tests you wrote, whether the tests passed or failed, and
    #             a brief write-up explaining if the code meets the requirements
    #             '''),
    #             agent=agent
    #     )

# Review Jupyter notebook -- how can we use this?
# Automate testing processes -- ?
# How can we approach research -- what are the best practices? How can we use this to improve our research?
# How can we improve the code quality?
# How can we improve the documentation?
# Documentation and testing
