import argparse
from pathlib import Path


def get_output_dir(in_path, out_path):
    if not in_path and not out_path:
        return None
    if not out_path:
        path = in_path.parent if in_path.is_file() else in_path
        path = path / "output"
    else:
        path = out_path
    path.mkdir(parents=True, exist_ok=True)
    return path


def parse_cli_args():
    parser = argparse.ArgumentParser(description="Refactor Python code using AI")

    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument(
        "code",
        nargs="?",
        help="code (text block) to be refactored",
    )

    group.add_argument(
        "-i",
        "--in",
        dest="in_path",
        type=Path,
        help="input file or directory path for files to be refactored",
    )

    parser.add_argument(
        "-o",
        "--out",
        dest="out_path",
        type=Path,
        help="output directory for refactored files (if not provided, print to console)",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="increase verbosity level",
    )

    args = parser.parse_args()
    args.out_path = get_output_dir(args.in_path, args.out_path)

    return args
