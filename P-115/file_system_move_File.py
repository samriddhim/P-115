import os

# Create source and destination file paths
source_file_path = "main.txt"
destination_file_path = "new_main.txt"  # Rename "main.txt" to "new_main.txt"

# Use os.rename() to rename the existing file
try:
    os.rename(source_file_path, destination_file_path)
    print(f"File '{source_file_path}' has been renamed to '{destination_file_path}'.")
except FileNotFoundError:
    print(f"File '{source_file_path}' not found.")
except FileExistsError:
    print(f"File '{destination_file_path}' already exists.")

# Run the code using Terminal



