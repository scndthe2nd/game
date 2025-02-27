# custom_frame.py
"""Custom Widget for Frames and Label Frame"""

import tkinter as tk
class CustomFrame(tk.Frame):
    '''Custom Frame'''
    def __init__(self, master=None, **kwargs):
        defaults = {
            'bd': 1,
            'relief': "flat",
            'padx': 0,
            'pady': 0,
        }
        defaults.update(kwargs)

        super().__init__(master, **defaults)

class CustomLabelFrame(tk.LabelFrame):
    '''Custom Label Frame'''
    def __init__(self, master=None, **kwargs):
        defaults = {
            'text': 'This is a Custom LabelFrame',
            'bd': 2,
            'relief': 'groove',
            'padx': 5,
            'pady': 5
        }
        defaults.update(kwargs)
        super().__init__(master, **defaults)
        #configure_grid(self)  # Apply grid configuration to the LabelFrame
        
# End-of-file (EOF)
