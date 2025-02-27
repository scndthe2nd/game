# custom_optionmenu.py
"""Custom Option Menus"""
import tkinter as tk

class CustomOptionMenu(tk.OptionMenu):
    """Custom Option Menu"""
    def __init__(self, master, variable, default_value, *values, **kwargs):
        # Filter out unsupported options
        supported_options = {
            key: value for key,
            value in kwargs.items() if key in ('bg', 'fg', 'font')}
        super().__init__(master, variable, default_value, *values, **supported_options)

# End-of-file (EOF)
