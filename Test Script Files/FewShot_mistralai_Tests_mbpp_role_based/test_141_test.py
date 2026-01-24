import unittest
from mbpp_141_code import pancake_sort

class TestPancakeSort(unittest.TestCase):
    def test_sort_ascending(self):
        self.assertEqual(pancake_sort([3, 2, 1]), [1, 2, 3])

    def test_sort_descending(self):
        self.assertEqual(pancake_sort([3, 5, 1]), [1, 3, 5])

    def test_single_element(self):
        self.assertEqual(pancake_sort([1]), [1])

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            pancake_sort([])

    def test_negative_numbers(self):
        self.assertEqual(pancake_sort([-3, -2, -1]), [-1, -2, -3])
