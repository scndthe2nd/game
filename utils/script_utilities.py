#script_utilities.py
"""Basic Utilities"""

import base64
import sys

def exit_command():
    """Exit Command"""
    sys.exit()

def encode_image(image_path):
    """Generate a base64 string from an image, that can then be used as text in an html document.

    Args:
        image_path (_str_): path to image file image path 
        
    Returns:
        _str_: Base64 string
    """
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string
# End-of-file (EOF)
