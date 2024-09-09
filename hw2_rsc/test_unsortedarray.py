import unittest
from hw2_debugging import merge_sort


class TestMergeSort(unittest.TestCase):
    def test_reverse_sorted_array(self):
        self.assertEqual(merge_sort([3, 1, 4, 2, 5]) == [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()