import time

from package.ai.crew import improve_code
from package.utils.cli import parse_cli_args


def output_result(result, out_path, verbose=0):
    if not out_path:
        print(result)
        return
    with open(out_path, "w") as output_file:
        output_file.write(result)
        if verbose:
            print(f"\nRefactored code saved to {out_path}")


def process_code(code: str, verbose=0, **kwargs):
    start_time = time.perf_counter()

    result = improve_code(code, verbose=verbose)

    if verbose:
        end_time = time.perf_counter()
        print(f"Code processing time: {end_time - start_time:.2f} seconds")

    return result


def process_file(in_path, out_path, verbose=0, **kwargs):
    if verbose:
        print(f"\nProcessing file: {in_path}")

    with open(in_path, "r") as file:
        code = file.read()

    result = process_code(code, verbose=verbose)
    output_result(result, out_path / in_path.name, verbose=verbose)


def process_directory(in_path, out_path, verbose=0, **kwargs):
    # process immediate children of the input directory (non-recursive)
    for file_path in in_path.iterdir():
        if file_path.is_file():
            process_file(file_path, out_path, verbose=verbose)


def main() -> None:
    args = parse_cli_args()

    if args.code:
        result = process_code(**vars(args))
        output_result(result, args.out_path, verbose=args.verbose)

    elif args.in_path.is_file():
        process_file(**vars(args))

    elif args.in_path.is_dir():
        process_directory(**vars(args))


if __name__ == "__main__":
    main()
