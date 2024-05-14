import time

from dotenv import load_dotenv
load_dotenv()

from crewai import Crew

from agents import GameDevAgents
from tasks import GameDevTasks

# Initialize Agents, Tasks
agents = GameDevAgents()
tasks = GameDevTasks()

# Create agents
project_manager = agents.project_manager()
senior_python_developer = agents.senior_python_developer()
senior_python_tester = agents.senior_python_tester()

print("#################################")
print("## Welcome to the GameDev Crew ##")
print("#################################")

game_request = input("Enter the game you want to create: ")
start_time = time.perf_counter()

# Create task for breaking project down into tasks
project_tasks = tasks.understand_project_requirements(project_manager, game_request)
written_code = tasks.write_code(senior_python_developer, project_tasks)
tested_code = tasks.test_code(senior_python_tester, written_code)

# Create crew and assign tasks
crew = Crew(
    agents = [
        project_manager,
        senior_python_developer,
        senior_python_tester
    ],
    tasks = [
        project_tasks,
        written_code,
        tested_code
    ],
    verbose=True
)

output = crew.kickoff()
end_time = time.perf_counter()

print("#############################")
print("## Game Development Output ##")
print("#############################")
print(f"## Time taken: {end_time - start_time:.2f} seconds\n")
print(output)
