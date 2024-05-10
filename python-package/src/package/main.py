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
senior_refactoring_engineer = agents.senior_refactoring_engineer_agent()
qa_refactoring_engineer = agents.qa_refactoring_engineer_agent()
chief_qa_refactoring_engineer = agents.chief_qa_refactoring_engineer_agent()

# Welcome message
print("## Welcome to the Refactoring Crew")
print("-----------------------------------")
start_time = time.perf_counter()

# Directory setup
input_dir = "../../tests/input"
output_dir = "../../tests/output"

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
        refactor_task = tasks.refactoring_task(
            senior_refactoring_engineer,
            code_content,
        )
        qa_review_task = tasks.qa_review_task(qa_refactoring_engineer, code_content)
        consistency_check_task = tasks.consistency_check_task(
            chief_qa_refactoring_engineer,
            code_content,
        )

        output_path = os.path.join(output_dir, filename)

        # Create Crew responsible for Refactoring
        crew = Crew(
            agents=[
                senior_refactoring_engineer,
                qa_refactoring_engineer,
                chief_qa_refactoring_engineer,
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
        result = clean_python_code(result)

        # Save the refactored code to the output file
        with open(output_path, "w") as output_file:
            output_file.write(result)
            print(f"\nRefactored code for {filename} saved to {output_path}")

end_time = time.perf_counter()


print("\n\n########################")
print("## Refactoring Completed")
print(f"## Time taken: {end_time - start_time:.2f} seconds")
print("########################\n")
