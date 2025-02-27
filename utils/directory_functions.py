#directory_functions.py 
"""Directory Functions"""

import subprocess

def open_explorer(sol_directory):
    """Open the specified directory in the file explorer"""
    subprocess.run(['explorer', sol_directory], check=True)

# End-of-file (EOF)
