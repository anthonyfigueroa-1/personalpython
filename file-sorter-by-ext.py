#!/usr/bin/python
import os
import shutil
import argparse
from collections import defaultdict

def parse_args():
    parse = argparse.ArgumentParser(description="Helps sort files by type, to automate cleaning of files. Very useful for downloads")

    parse.add_argument("source", help="Source directory to sort files from")
    parse.add_argument("--destination", help="Destination directory to move/copy files to")
    parse.add_argument("--copy", action="store_true", help="If used, makes a copy from source and copies files into destination")

    return parse.parse_args()

def grab_source_files(source):
    return os.listdir(source)

def get_files(items, source):
    files = []

    for item in items:
        path = os.path.join(f"{source}", item)
        if os.path.isfile(path):
            files.append(item)

    return files

def sort_by_ext(files):
    files_by_ext = defaultdict(list)

    for file in files:
        extension = os.path.splitext(file)[1].lstrip('.').lower() or 'noext'
        files_by_ext[extension].append(file)

    return files_by_ext

def create_dirs_and_sort(ext_and_files, source, destination, copy):
    for ext, files_list in ext_and_files.items():
        if not files_list:
            print(f"No files_list to sort for {ext}")
            continue
        source_path = f"{source}/"
        sorted_path = os.path.join(destination or source, f"{ext}_sorted")
        os.makedirs(sorted_path, exist_ok=True)
        
        if copy == True:
            for file in files_list:
                source_path_file = os.path.join(source_path, file)
                sorted_path_file = os.path.join(sorted_path, file)
                shutil.copy2(source_path_file, sorted_path_file)
                print(f"Copied {source_path_file} to {sorted_path_file}")
        else:
            for file in files_list:
                source_path_file = os.path.join(source_path, file)
                sorted_path_file = os.path.join(sorted_path, file) 
                shutil.move(f"{source_path}{file}", f"{sorted_path}{file}")
                print(f"Moved {source_path}{file} to {sorted_path}{file}")

def main():
    args = parse_args()

    destination = args.destination if args.destination else None
    source = args.source if args.source else None
    copy = args.copy

    items = grab_source_files(source)
    files = get_files(items, source)
    ext = sort_by_ext(files)
    create_dirs_and_sort(ext, source, destination, copy)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
