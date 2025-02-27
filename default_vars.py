#default_vars.py
"""Default Values"""

import os
from datetime import datetime
import tkinter as tk

root = tk.Tk()
root.withdraw()  # Hide the root window if you don't want it to be visible

# defaults.py
# Define shared variables
example_variables = {
    "example_string": "ExampleString",
    "example_list": ["Item1", "Item2", "Item3"],
    "example_tuple": ("Element1", "Element2", "Element3"),
    "example_dict": {"Key1": "Value1", "Key2": "Value2"},
    "example_int": 123,
    "example_float": 45.67,
    "example_bool": True,
    "example_none": None,
}

shared_variables = {
    "sample": None,
}

# Define more defaults if needed
more_defaults = {
    "sample2": None,
}

# Define filepath variables
filepath_variables = {
    'print_preview': 'view.html',
    'pdf_file_name': 'temp.pdf',
    'default_documents_path': os.path.expanduser("~\\Documents"),
    'default_path': "//asdfileserver/ASD/ASD_CIP_DIR/ASD_Domain",
    'file_extension': ".pdf",
    'wkhtmltopdf_path': "deps/wkhtmltox/bin/wkhtmltopdf.exe"
}

# Define datetime variables
datetime_variables = {
    'today': datetime.today().strftime('%Y%m%d'),
    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
}

def default_values():
    """define default values"""
    combined_defaults = {
        **example_variables,
        **shared_variables,
        **more_defaults,
        **filepath_variables,
        **datetime_variables
    }
    return combined_defaults

def get_default(key):
    """get a value from default values"""
    combined_defaults = default_values()
    return combined_defaults.get(key, "Key not found")

# Example usage
# KEY = 'file_extension'
# value = get_default(KEY)
# print(value)

# End-of-file (EOF)
