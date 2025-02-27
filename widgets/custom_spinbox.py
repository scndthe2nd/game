# custom_spinbox.py
"""Widgets for Custom Spinboxes"""
import tkinter as tk

class CustomSpinbox(tk.Spinbox):
    """Custom Spinbox"""
    def __init__(self, master=None, **kwargs):
        defaults = {
            'from_': 0,
            'to': 10,
            'bg': 'white',
            'fg': 'black',
            'font': ('Arial', 12)
        }
        defaults.update(kwargs)
        super().__init__(master, **defaults)

# End-of-file (EOF)
