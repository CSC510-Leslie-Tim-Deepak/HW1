"""
This module provides functionality for generating random arrays using subprocess.
"""
import subprocess

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
        shuffled_num = subprocess.run(["shuf", "-i1-20", "-n1"], capture_output=True, check=True)
        arr[i] = int(shuffled_num.stdout)
    return arr
