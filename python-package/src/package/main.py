import os
import time

from ai.crew import create_crew
from utils.cli import parse_cli_args
from utils.code_cleaner import clean_python_code

# Directory setup
input_dir = "../../tests/input"
output_dir = "../../tests/output"


def main(args) -> None:
    start_time = time.perf_counter()

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Process each file in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(".py"):  # Process Python files only
            file_path = os.path.join(input_dir, filename)

            # Read the input file
            with open(file_path, "r") as file:
                code_content = file.read()

            # Create Crew responsible for Refactoring
            crew = create_crew(code_content)

            # Kickoff the refactoring process
            result = crew.kickoff(inputs={"code": code_content})

            # Extract the code only
            result = clean_python_code(result)

            output_path = os.path.join(output_dir, filename)

            # Save the refactored code to the output file
            with open(output_path, "w") as output_file:
                output_file.write(result)
                print(f"\nRefactored code for {filename} saved to {output_path}")

    end_time = time.perf_counter()

    print("\n\n########################")
    print("Refactoring Completed")
    print(f"## Time taken: {end_time - start_time:.2f} seconds")
    print("########################\n")


if __name__ == "__main__":
    args = parse_cli_args()
    main(args)
