#!/usr/bin/python3
<<<<<<< HEAD
""" Module for 0-minoperations"""


def minOperations(n):
    """
    minOperations
    Gets fewest # of operations needed to result in exactly n H characters
    """
    # all outputs should be at least 2 char: (min, Copy All => Paste)
    if (n < 2):
        return 0
    ops, root = 0, 2
    while root <= n:
        # if n evenly divides by root
        if n % root == 0:
            # total even-divisions by root = total operations
            ops += root
            # set n to the remainder
            n = n / root
            # reduce root to find remaining smaller vals that evenly-divide n
            root -= 1
        # increment root until it evenly-divides n
        root += 1
    return ops
=======
"""
This module contains the minOperations function that calculates
the fewest number of operations needed to result in exactly n H
characters in the file.
"""


def next_operation(
                   target: int,
                   operations: int,
                   current_characters: int,
                   add_by: int
                   ) -> int:
    """
    Recursive function to calculate the next operation
    Args:
        target (int): The target number of characters
        operations (int): The number of operations
        current_characters (int): The current number of characters
        add_by (int): The number of characters to add by
    Returns:
        int: The number of operations
    """
    if target == current_characters:
        return operations

    if target % current_characters == 0:
        return next_operation(
                              target,
                              operations + 2,
                              current_characters * 2,
                              current_characters
                              )

    return next_operation(
                          target,
                          operations + 1,
                          current_characters + add_by,
                          add_by
                          )


def minOperations(n: int) -> int:
    """
    Calculates the fewest number of operations needed to result in
    exactly n H characters in the file.
    Args:
        n (int): The target number of characters
    Returns:
        int: The fewest number of operations needed to result in
            exactly n H characters in the file.
    """
    if n <= 1:
        return 0

    return next_operation(n, 2, 2, 1)
>>>>>>> d4bd78c2c9a11a465f5070906530788731b5065c
