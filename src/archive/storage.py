# src/archive/storage.py
import os
from moviepy.editor import VideoFileClip
import datetime


def get_video_length(path):
    clip = VideoFileClip(path)
    duration = clip.duration
    clip.close()
    return duration


def get_year_from_filename(filename: str):
    date_str = filename.split()[0]  # Get date string from filename
    date = datetime.datetime.strptime(date_str, "%Y-%m-%d")  # Parse date
    return date.year


def sum_video_lengths_by_year(path: str):
    lengths_by_year = {}

    def process_file(filepath):
        filename = os.path.basename(filepath)  # Extract the filename from the path
        year = get_year_from_filename(filename)
        video_length = get_video_length(filepath)

        if year in lengths_by_year:
            lengths_by_year[year] += video_length
        else:
            lengths_by_year[year] = video_length

    if os.path.isfile(path) and path.endswith(".mkv"):
        process_file(path)
    elif os.path.isdir(path):
        for filename in os.listdir(path):
            if filename.endswith(".mkv"):
                file_path = os.path.join(path, filename)
                process_file(file_path)

    # Convert seconds to hours and sort by year
    lengths_by_year = {
        year: length / 3600 for year, length in sorted(lengths_by_year.items())
    }

    return lengths_by_year
