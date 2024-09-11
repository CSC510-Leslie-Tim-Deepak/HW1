
import secrets


def random_array(arr):

    for i, _ in enumerate(arr):
        arr[i] = secrets.randbelow(20) + 1
    return arr
