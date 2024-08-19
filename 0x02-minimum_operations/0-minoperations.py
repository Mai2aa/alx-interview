#!/usr/bin/python3
'''Calculates the number of operations'''


def minOperations(n: int) -> int:
    '''Minimum operation'''
    if not isinstance(n, int) or n < 2:
        return 0

    prev = 1
    operations = cur = value = 2
    while n > value:
        reminder = n - value
        if reminder % cur == 0:
            operations += 2
            prev = cur
            value += cur
            cur = value
        elif reminder % prev == 0:
            operations += 1
            value += prev
            cur = value
    return operations
