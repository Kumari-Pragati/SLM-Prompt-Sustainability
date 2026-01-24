import unittest
from mbpp_141_code import pancake_sort

class TestPancakeSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(pancake_sort([]), [])

    def test_single_element(self):
        self.assertEqual(pancake_sort([1]), [1])

    def test_sorted_list(self):
        self.assertEqual(pancake_sort([1, 2, 3]), [3, 2, 1])

    def test_reverse_sorted_list(self):
        self.assertEqual(pancake_sort([3, 2, 1]), [1, 2, 3])

    def test_unsorted_list(self):
        self.assertEqual(pancake_sort([5, 3, 1, 4, 2]), [5, 4, 3, 1, 2])

    def test_duplicates(self):
        self.assertEqual(pancake_sort([5, 5, 3, 1, 4, 2]), [5, 5, 3, 1, 2, 4])
