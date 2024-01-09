#!/usr/bin/python3
"""
This module contains a function that returns a list of lists of integers
representing the Pascal's triangle of n.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal's triangle of n.

    Args:
        n (int): The number of rows of the triangle.

    Returns:
        list: A list of lists of integers, or an empty list if n <= 0.

    Examples:
        >>> print_triangle(pascal_triangle(5))
        [1]
        [1,1]
        [1,2,1]
        [1,3,3,1]
        [1,4,6,4,1]
    """
    # Returns an empty list if n <= 0
    if n <= 0:
        return []
    # Initialize the triangle with the first row
    triangle = [[1]]
    # Loop from the second row to the nth row
    for i in range(1, n):
        # Initialize the current row with the first element
        row = [1]
        # Loop through the previous row and add adjacent elements
        for j in range(len(triangle[i-1]) - 1):
            row.append(triangle[i-1][j] + triangle[i-1][j+1])
        # Append the last element to the current row
        row.append(1)
        # Append the current row to the triangle
        triangle.append(row)
    # Return the triangle
    return triangle

