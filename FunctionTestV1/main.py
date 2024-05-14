import time

from dotenv import load_dotenv
load_dotenv()

from crewai import Crew

from agents import FunctionTestAgents
from tasks import FunctionTestTasks

# Initialize Agents, Tasks
agents = FunctionTestAgents()
tasks = FunctionTestTasks()

# Create agents
variable_name_agent = agents.variable_name_agent()
# code_comment_agent = agents.code_comment_agent()
documentation_agent = agents.documentation_agent()

print("##################################")
print("## Welcome to the Function Crew ##")
print("##################################")

game_request = input("Enter the code you want to improve: ")
start_time = time.perf_counter()

# Create task for breaking project down into tasks
improve_variable_names_task = tasks.improve_variable_names(variable_name_agent, game_request)
# add_code_comments_task = tasks.add_code_comments(variable_name_agent, improve_variable_names_task)
add_documentation_task = tasks.add_documentation(variable_name_agent, improve_variable_names_task)

# Create crew and assign tasks
crew = Crew(
    agents = [
        variable_name_agent,
        # code_comment_agent,
        documentation_agent
    ],
    tasks = [
        improve_variable_names_task,
        # add_code_comments_task,
        add_documentation_task
    ],
    verbose=True
)

output = crew.kickoff()
end_time = time.perf_counter()

print("################################")
print("## Refactored Function Output ##")
print("################################")
print(f"## Time taken: {end_time - start_time:.2f} seconds\n")
print(output)
