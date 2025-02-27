# custom_listbox.py
"""Custom Widget for Listboxes"""

import tkinter as tk

class CustomListbox(tk.Listbox):
    """Custom Listbox"""
    def __init__(self, master=None, **kwargs):
        defaults = {
            'bg': 'white',
            'fg': 'black',
            'font': ('Arial', 12),
            'selectmode': 'single'
        }
        defaults.update(kwargs)
        super().__init__(master, **defaults)

# End-of-file (EOF)
