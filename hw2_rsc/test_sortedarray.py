"""
This module contains unit tests for the merge_sort function with a reversed array.
"""
import unittest
from hw2_debugging import merge_sort


class TestMergeSort(unittest.TestCase):
    """
    Test cases for merge_sort function with a sorted array as input.
    """

    def test_reverse_sorted_array(self):
        """
        This module for merge sort use sorted array as input.
        """
        self.assertEqual(merge_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
