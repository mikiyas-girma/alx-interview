#!/usr/bin/python3
"""minoperations module"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to
    result in exactly n H characters in a file
    """
    if (n < 2):
        return 0
    ops = 0
    root = 2
    while root <= n:
        if n % root == 0:
            ops += root
            n = n / root
            root -= 1
        root += 1
    return ops
