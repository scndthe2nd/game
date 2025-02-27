# custom_entry.py
"""Custom Widget for Entry Fields"""

import tkinter as tk

class CustomEntry(tk.Entry):
    """Custom Entry"""
    def __init__(self, master=None, **kwargs):
        defaults = {
            'bg': 'white',
            'fg': 'black',
            'font': ('Arial', 12)
        }
        defaults.update(kwargs)
        super().__init__(master, **defaults)

# End-of-file (EOF)
