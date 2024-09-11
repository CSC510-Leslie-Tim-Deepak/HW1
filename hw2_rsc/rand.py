"""
This module provides functionality for generating random arrays using subprocess.
"""
import subprocess

def random_array(arr):
    '''
    Generates an array of random numbers
    '''
    shuffled_num = None
    for i, _ in enumerate(arr):
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"],
            capture_output=True,
            check=False
        )
        arr[i] = int(shuffled_num.stdout)
    return arr
