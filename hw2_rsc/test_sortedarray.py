# test_merge_sort.py

from hw2_debugging import merge_sort

def test_sorted_array():
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]