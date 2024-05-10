import argparse


def parse_cli_args():
    parser = argparse.ArgumentParser(description="Refactor Python code using AI")

    parser.add_argument(
        "path",
        type=str,
        help="File or directory path",
    )

    parser.add_argument(
        "path",
        type=str,
        help="File or directory path",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable verbose output",
    )

    return parser.parse_args()
