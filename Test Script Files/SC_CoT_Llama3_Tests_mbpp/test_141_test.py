import unittest
from mbpp_141_code import pancake_sort

class TestPancakeSort(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(pancake_sort([]), [])

    def test_single_element_list(self):
        self.assertEqual(pancake_sort([1]), [1])

    def test_sorted_list(self):
        self.assertEqual(pancake_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        self.assertEqual(pancake_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        self.assertEqual(pancake_sort([3, 1, 4, 1, 5, 9, 2, 6]), [1, 1, 2, 3, 4, 5, 6, 9])

    def test_duplicates_list(self):
        self.assertEqual(pancake_sort([2, 2, 1, 3, 3, 4, 5, 5, 6]), [1, 2, 2, 3, 3, 4, 5, 5, 6])

    def test_large_list(self):
        self.assertEqual(pancake_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            pancake_sort("abc")
