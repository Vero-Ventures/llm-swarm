import os
import time

from package.ai.crew import improve_code
from package.utils.cli import parse_cli_args

# Directory setup
input_dir = "../../tests/input"
output_dir = "../../tests/output"


def process_file(file_path, filename="output.py"):
    print(f"Processing file: {file_path}")
    start_time = time.perf_counter()

    output_path = os.path.join(output_dir, filename)

    with open(file_path, "r") as file:
        code = file.read()

    result = improve_code(code)

    end_time = time.perf_counter()
    print(f"## Time taken: {end_time - start_time:.2f} seconds")

    # Save the refactored code to the output file
    with open(output_path, "w") as output_file:
        output_file.write(result)
        print(f"\nRefactored code for {file_path} saved to {output_path}")


def process_directory(directory_path):
    print(f"Processing directory: {directory_path}")
    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            process_file(file_path, filename=file)


def main() -> None:
    args = parse_cli_args()
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    path = args.path
    if os.path.isfile(path):
        process_file(path)
    elif os.path.isdir(path):
        process_directory(path)
    else:
        print(f"Invalid path: {path}")


if __name__ == "__main__":
    main()
