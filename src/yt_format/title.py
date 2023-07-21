import os
import sys
import pyperclip


def format_video_path(filepath: str):
    if os.path.isdir(filepath):
        print("This is a directory. Not creating a format path.")
        return
    
    if not os.path.exists(filepath) and not os.path.isfile(filepath):
        print("File does not exist.")
        return
    # Split the path into components
    path_parts = os.path.normpath(filepath).split(os.sep)

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
