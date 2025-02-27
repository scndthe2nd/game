# custom_treeview.py
"""Widgets for Custom Tree Views"""
from tkinter import ttk

class CustomTreeview(ttk.Treeview):
    """Custom Tree View"""
    def __init__(self, master=None, **kwargs):
        defaults = {
            'columns': ('#1', '#2'),
            'show': 'headings'
        }
        defaults.update(kwargs)
        super().__init__(master, **defaults)

# End-of-file (EOF)
