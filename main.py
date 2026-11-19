import argparse
import os
import shutil
import sys


def organize_files(path):
    for filename in os.listdir(path):
        if os.path.isfile(os.path.join(path, filename)):
            ext = filename.split('.')[-1]
            ext_dir = os.path.join(path, ext)
            os.makedirs(ext_dir, exist_ok=True)
            shutil.move(os.path.join(path, filename), os.path.join(ext_dir, filename))


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Move each file in a folder into a subfolder named after its extension.",
        epilog="Example: python main.py ~/Downloads",
    )
    parser.add_argument("folder", help="folder whose files should be sorted")
    args = parser.parse_args(argv)

    if not os.path.isdir(args.folder):
        parser.error(f"not a folder: {args.folder}")

    organize_files(args.folder)
    return 0


if __name__ == "__main__":
    sys.exit(main())
