import os.path as path
import src.yt_format.title as title
import src.archive.storage as storage
import src.argument_parser as arg_parse


def main():
    args = arg_parse.parse_args()
    print(args)
    if args.format:
        title.format_video_path(args.path)
    if path.isdir(args.path):
        lengths_by_year = storage.sum_video_lengths_by_year(args.path)
        for year, length in lengths_by_year.items():
            print(f"Total length for {year}: {length:.2f} hours")


if __name__ == "__main__":
    main()
