import unittest
from mbpp_141_code import pancake_sort

class TestPancakeSort(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(pancake_sort([3, 2, 1, 5, 4]), [1, 2, 3, 4, 5])

    def test_already_sorted(self):
        self.assertEqual(pancake_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_single_element(self):
        self.assertEqual(pancake_sort([1]), [1])

    def test_empty_list(self):
        self.assertEqual(pancake_sort([]), [])

    def test_negative_numbers(self):
        self.assertEqual(pancake_sort([-3, -2, -1, -5, -4]), [-5, -4, -3, -2, -1])

    def test_duplicate_elements(self):
        self.assertEqual(pancake_sort([3, 2, 1, 5, 4, 4]), [1, 2, 3, 4, 4, 5])

    def test_large_numbers(self):
        self.assertEqual(pancake_sort([100, 200, 300, 400, 500]), [100, 200, 300, 400, 500])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            pancake_sort("12345")

        with self.assertRaises(TypeError):
            pancake_sort([1, 2, "3", 4, 5])

        with self.assertRaises(TypeError):
            pancake_sort(None)
