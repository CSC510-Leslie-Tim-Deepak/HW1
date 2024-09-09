# test_merge_sort.py

from hw2_debugging import merge_sort

def test_unsorted_array():
    assert merge_sort([3, 1, 4, 2, 5]) == [1, 2, 3, 4, 5]