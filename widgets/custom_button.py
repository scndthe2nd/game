# custom_button.py
"""Custom Widget for Button"""

import tkinter as tk

class CustomButton(tk.Button):
    """Custom Button"""
    def __init__(self, master=None, **kwargs):
        defaults = {
            'bg': 'darkblue',
            'fg': 'white',
            'font': ('Arial', 12),
            'padx': 5,
            'pady': 5
        }
        defaults.update(kwargs)
        super().__init__(master, **defaults)

# End-of-file (EOF)
