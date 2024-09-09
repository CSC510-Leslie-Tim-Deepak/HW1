from hw2_debugging import merge_sort

def test_reverse_sorted_array():
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]