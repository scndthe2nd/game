# custom_label.py
"""Custom Widget for Label"""

import tkinter as tk

class CustomLabel(tk.Label):
    """Custom Label"""
    def __init__(self, master=None, **kwargs):
        defaults = {
            'bg': 'lightgray',
            'fg': 'black',
            'font': ('Arial', 12),
            'padx': 0,
            'pady': 0
        }
        defaults.update(kwargs)
        super().__init__(master, **defaults)
        
# End-of-file (EOF)
