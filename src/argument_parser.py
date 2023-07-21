# src/arg_parser.py
import argparse


class ProgramArgs:
    def __init__(self, path: str, format: bool):
        self.path = path
        self.format = format

    def __str__(self) -> str:
        return f"ProgramArgs(path='{self.path}', format={self.format})"


import os


def parse_args() -> ProgramArgs:
    parser = argparse.ArgumentParser(description="Process video files in a path.")
    parser.add_argument(
        "path", type=str, help="The path to the video file or directory."
    )
    parser.add_argument(
        "--format", action="store_true", help="Format video file names.", default=False
    )

    args = parser.parse_args()

    # If path is a file, set format to True
    if os.path.isfile(args.path):
        args.format = True

    return ProgramArgs(args.path, args.format)
