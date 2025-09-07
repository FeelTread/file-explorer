import os
from pathlib import Path

def print_directory_contents(path):
    for entry in os.scandir(path):
        if entry.is_dir():
            print(f"  [DIR] {entry.name}")
        else:
            print(f"       {entry.name}")
    if not any(os.scandir(path)):
        print("Directory is empty")


home = Path.home()
current_path = home

while True:
    print_directory_contents(current_path)

    folder = input("select a folder: ")

    if os.path.isdir(current_path / folder):
        current_path = current_path / folder
        obj = os.scandir(current_path)
    else:
        print("Not a valid directory")