#interface_functions.py
"""Interface Functions related to Tkinter"""

from tkinter import filedialog

# Function to browse and select the test workbook
def select_output_directory(directory, path):
    """Select a directory from a browse button"""
    directory = filedialog.askdirectory(initialdir=path)
    if directory:
        directory.set(directory)
    return directory

def configure_grid(parent):
    """Set a grid so that all objects within the grid have the same weight and minimum size."""
    for cell_number in range(parent.grid_size()[0]):
        parent.grid_columnconfigure(cell_number, weight=1, minsize=20)
    for cell_number in range(parent.grid_size()[1]):
        parent.grid_rowconfigure(cell_number, weight=1, minsize=20)

def copy_to_clipboard(root, text):
    """copy a string to clipboard"""
    # Use the existing window to copy the specified text to the clipboard
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()  # Now it stays on the clipboard

def toggle_frame_visibility(frame1, frame2):
    """Toggle the visibility of a frame using tkinter"""
    if frame1.winfo_viewable():
        frame1.grid_remove()
        frame2.grid()
        print(f"Swap to {frame2}")
    else:
        frame2.grid_remove()
        frame1.grid()
        print(f"Swap to {frame1}")

# End-of-file (EOF)
