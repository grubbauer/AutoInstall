import os
import shutil

def move_files(source_directory, destination_directory):
    # Ensure the destination directory exists
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    # List all files in the source directory
    files = os.listdir(source_directory)

    # Move each file to the destination directory
    for file in files:
        source_path = os.path.join(source_directory, file)
        destination_path = os.path.join(destination_directory, file)
        shutil.move(source_path, destination_path)
        print(f"Moved: {source_path} to {destination_path}")

source_directory = "auto"
destination_directory = "example"

move_files(source_directory, destination_directory)
shutil.copy("link.lnk", "C:/Users/Rapha/Desktop")