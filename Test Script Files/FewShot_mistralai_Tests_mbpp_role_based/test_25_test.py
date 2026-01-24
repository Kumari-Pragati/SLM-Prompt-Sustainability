import unittest
from mbpp_25_code import find_Product

class TestFindProduct(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(find_Product([1, 2, 3, 4], 4), 24)
        self.assertEqual(find_Product([5, 6, 7, 8], 4), 48)

    def test_empty_list(self):
        self.assertEqual(find_Product([], 0), 1)

    def test_single_element(self):
        self.assertEqual(find_Product([1], 1), 1)

    def test_duplicate_elements(self):
        self.assertEqual(find_Product([1, 1, 2, 3], 4), 6)

    def test_negative_numbers(self):
        self.assertEqual(find_Product([-1, -2, -3, -4], 4), 24)

    def test_zero(self):
        self.assertEqual(find_Product([0, 0, 0, 0], 4), 0)

    def test_invalid_input_length(self):
        with self.assertRaises(IndexError):
            find_Product([1, 2, 3], 5)

    def test_invalid_input_negative_index(self):
        with self.assertRaises(IndexError):
            find_Product([1, 2, 3], -1)
