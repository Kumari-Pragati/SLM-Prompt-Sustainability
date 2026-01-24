import unittest
from mbpp_141_code import pancake_sort

class TestPancakeSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(pancake_sort([]), [])

    def test_single_element(self):
        self.assertEqual(pancake_sort([1]), [1])

    def test_simple_list(self):
        self.assertEqual(pancake_sort([3, 2, 1]), [1, 2, 3])

    def test_reverse_list(self):
        self.assertEqual(pancake_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_duplicates(self):
        self.assertEqual(pancake_sort([5, 5, 3, 2, 1]), [1, 2, 3, 3, 5, 5])

    def test_large_list(self):
        self.assertEqual(pancake_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_negative_numbers(self):
        self.assertEqual(pancake_sort([-3, -2, -1]), [-1, -2, -3])

    def test_mixed_numbers(self):
        self.assertEqual(pancake_sort([-2, 0, 3, -1, 2]), [-1, 0, -2, 2, 3])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            pancake_sort(1.5)
