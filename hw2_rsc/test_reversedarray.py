import unittest
from hw2_debugging import merge_sort


class TestMergeSort(unittest.TestCase):
    def test_reverse_sorted_array(self):
        self.assertEqual(merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()