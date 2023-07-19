import os
import sys
import pyperclip


def format_video_path(path):
    # Split the path into components
    path_parts = os.path.normpath(path).split(os.sep)

    # Get the directory name just before the file
    dir_name = path_parts[-2]

    # Get the filename without extension
    filename = os.path.splitext(path_parts[-1])[0]

    # Split filename into date and time
    date, time = filename.split(" ")

    # Replace "-" in the time with ":"
    formatted_time = time.replace("-", ":")

    # Format the output string
    output = f"{date} {formatted_time} ({dir_name} gameplay)"

    # Copy to clipboard
    pyperclip.copy(output)

    # Print the output
    print(output)
