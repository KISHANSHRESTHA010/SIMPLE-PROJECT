import os

# Specify the directory path (use "." for current directory)
directory = "."

# List all files and directories
all_items = os.listdir(directory)

# Filter to get only files
files = [f for f in all_items if os.path.isfile(os.path.join(directory, f))]

for file in files:
    print(file)
