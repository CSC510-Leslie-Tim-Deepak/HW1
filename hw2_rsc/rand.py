"""
This module provides functionality for generating random arrays using subprocess.
"""
import random


def random_array(arr):
    """
    Fills the input list with random numbers using the `shuf` command.
    Args:
        arr (list): A list that will be filled with random integers.
    Returns:
        list: The input list with random integers.
    """
    shuffled_num = None
    for i, _ in enumerate(arr):
        arr[i] = random.randint(1, 20)
    return arr
