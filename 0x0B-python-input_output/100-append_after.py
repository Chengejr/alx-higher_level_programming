#!/usr/bin/python3
"""
This module contains a function that inserts a line of text to a file,
after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line containing a specific string.

    Args:
        filename (str): The name of the file to be modified.
        search_string (str): The string to be searched in each line.
        new_string (str): The string to be inserted after the search string.

    Returns:
        None
    """
    # You must use the with statement
    with open(filename, "r+") as file:
        # Read the file contents as a list of lines
        lines = file.readlines()
        # Loop through the lines with an index
        for i, line in enumerate(lines):
            # Check if the search string is in the current line
            if search_string in line:
                # Insert the new string after the current line
                lines.insert(i + 1, new_string)
        # Go back to the beginning of the file
        file.seek(0)
        # Write the modified lines to the file
        file.writelines(lines)
