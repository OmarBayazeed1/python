#97.Use the os module to list files in a directory
import os

# Specify the directory you want to list
directory_path = '.'  # '.' means current directory

# List all files and folders
files = os.listdir(directory_path)

# Print each item
for file in files:
    print(file)
