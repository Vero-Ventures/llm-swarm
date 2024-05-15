import os
import time

from crewai import Crew

from agents import RefactoringAgents
from tasks import RefactoringTasks
from utils.code_cleaner import clean_python_code

# Initialize agents and tasks
agents = RefactoringAgents()
tasks = RefactoringTasks()

# Create Agents
req_determining_agent = agents.requirements_agent()
coding_agent = agents.coding_agent()
code_checking_agent = agents.code_checking_agent()

# Welcome message
print("## Welcome to the Refactoring Crew")
print("-----------------------------------")
start_time = time.perf_counter()

# Directory setup
input_dir = "test_input"
output_dir = "test_output"

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Process each file in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".py"):  # Process Python files only
        file_path = os.path.join(input_dir, filename)

        # Read the input file
        with open(file_path, "r") as file:
            code_content = file.read()

        # Create Tasks with the read code content
        refactor_task = tasks.determine_reqs_task(
            req_determining_agent,
            code_content,
        )
        qa_review_task = tasks.write_code_task(coding_agent, code_content)
        consistency_check_task = tasks.check_code_task(
            coding_agent,
            
        )

        output_path = os.path.join(output_dir, filename)

        # Create Crew responsible for Refactoring
        crew = Crew(
            agents=[
                req_determining_agent,
                coding_agent,
                code_checking_agent,
            ],
            tasks=[
                refactor_task,
                qa_review_task,
                consistency_check_task,
            ],
            verbose=True,
        )

        # Kickoff the refactoring process
        result = crew.kickoff(inputs={"code": code_content})

        # Extract the code only
        #result = clean_python_code(result)

        # Save the refactored code to the output file
        with open(output_path, "w") as output_file:
            output_file.write(result)
            print(f"\nRefactored code for {filename} saved to {output_path}")

end_time = time.perf_counter()


print("\n\n########################")
print("## Refactoring Completed")
print(f"## Time taken: {end_time - start_time:.2f} seconds")
print("########################\n")
