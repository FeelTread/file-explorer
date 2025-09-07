import os
from pathlib import Path

def return_directory_contents(path):
    return [{"name": entry.name, "is_dir": entry.is_dir()} for entry in os.scandir(path)]

home = Path.home()
current_path = home

while True:
    dir_contents = return_directory_contents(current_path)
    if not dir_contents:
        print("Directory is empty")
    else:
        for item in dir_contents:
            if item["is_dir"]:
                print(f"  [DIR] {item['name']}")
            else:
                print(f"       {item['name']}")

    folder = input("select a folder: ")

    if os.path.isdir(current_path / folder):
        current_path = current_path / folder
        obj = os.scandir(current_path)
    else:
        print("Not a valid directory")