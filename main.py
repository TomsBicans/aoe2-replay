import src.format as format
import sys


def main():
    if len(sys.argv) > 1:
        path = sys.argv[1]
        format.format_video_path(path)
    else:
        print("Please provide a path to a video file as a command-line argument.")


if __name__ == "__main__":
    main()
