import unittest
from mbpp_141_code import pancake_sort

class TestPancakeSort(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(pancake_sort([]), [])

    def test_single_element_list(self):
        self.assertEqual(pancake_sort([1]), [1])

    def test_sorted_list(self):
        self.assertEqual(pancake_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        self.assertEqual(pancake_sort([5, 2, 8, 3, 1, 4]), [1, 2, 3, 4, 5, 8])

    def test_list_with_duplicates(self):
        self.assertEqual(pancake_sort([2, 2, 3, 1, 1, 4]), [1, 1, 2, 2, 3, 4])

    def test_list_with_negative_numbers(self):
        self.assertEqual(pancake_sort([-5, -2, 0, 1, 3, 4]), [-5, -2, 0, 1, 3, 4])

    def test_list_with_zero(self):
        self.assertEqual(pancake_sort([0, 1, 2, 3, 4, 5]), [0, 1, 2, 3, 4, 5])
