# data_functions.py
"""functions that deal with managing data"""


def datacheck(output, variable_names, default_values):
    """confirm that this variable has a datatype"""
    for variable_index, value in enumerate(output):
        if value is None:
            output[variable_index] = default_values[variable_names[variable_index]]
    return output

def explode_string(input_string, delimiter):
    """identify a delimiter and explode a string based on that delimiter"""
    string_parts = input_string.split(delimiter)
    output = tuple(string_parts)
    return output

def assemble_exploded_string(string_variables, delimiter):
    """identify a delimiter and assemble a string from a list"""
    assembled_name = ""
    for var in string_variables:
        value = globals().get(var)
        assembled_name += f"{value}{delimiter}"
    return assembled_name.rstrip(delimiter)

# End-of-file (EOF)
