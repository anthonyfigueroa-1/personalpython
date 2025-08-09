import os
import shutil
import argparse
import json
import re

def parse_args():
    parse = argparse.ArgumentParser(description="Helps sort files by type, to automate cleaning of files. Very useful for downloads")

    parse.add_argument("--source", help="Source directory to sort files from")
    parse.add_argument("--destination", help="Destination directory to move/copy files to")
    parse.add_argument("--copy", action="store_true", help="If used, makes a copy from source and copies files into destination")

    return parse.parse_args()

def grab_source_files(source):
    return os.listdir(f"{source}")

def get_files(items, source):
    files = []

    for item in items:
        path = os.path.join(f"{source}", item)
        if os.path.isfile(path):
            files.append(item)

    return files

def sort_by_ext(files):
    grab_ext = [] 
    for file in files:
        extension = os.path.splitext(file)[1]
        temp = re.search("\.([^\']+)", extension)
        grab_ext.append(temp)
    temp_ext = []
    for ext in grab_ext:
        if ext not in temp_ext:
            temp_ext.append(ext)
    print(temp_ext)
#    for file in files:
#        match = re.match(rf"\w


def main():
    args = parse_args()

    destination = args.destination if args.destination else None
    source = args.source if args.source else None
    copy = args.copy

    items = grab_source_files(source)
    files = get_files(items, source)
    ext = sort_by_ext(files)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
