#!/usr/bin/python3
"""Task number 1 on the interview set of tasks"""


def pascal_triangle(n):
    """return list of lists of integers representing pascal tri of n"""
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    
    prev = pascal_triangle(n - 1)
    new = [1] * n
    
    for i in range(1, n - 1):
        new[i] = prev[-1][i - 1] + prev[-1][i]
    
    prev.append(new)
    return prev