import secrets


def random_array(arr):
    """
    Fills the input list with random numbers using the `shuf` command.
    Args:
        arr (list): A list that will be filled with random integers.
    Returns:
        list: The input list with random integers.
    """
    for i, _ in enumerate(arr):
        arr[i] = secrets.randbelow(20) + 1
    return arr
