# automate_filename_comment.py
"""add filename as a comment to each python file"""
import os

def add_filename_comment(target_directory):
    """
    Add the filename as a comment to the first line of each Python file in the specified target_directory.

    :param target_directory: The path to the target_directory containing Python files.
    """
    for filename in os.listdir(target_directory):
        if filename.endswith(".py"):
            filepath = os.path.join(target_directory, filename)
            with open(filepath, 'r', encoding = "utf-8") as file:
                lines = file.readlines()

            if not lines[0].startswith("#"):
                lines.insert(0, f"# {filename}\n")
                with open(filepath, 'w', encoding = "utf-8") as file:
                    file.writelines(lines)

DIRECTORY = 'path/to/your/python/files'
add_filename_comment(DIRECTORY)

# EOF
