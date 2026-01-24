import unittest
from mbpp_25_code import find_Product

class TestFindProduct(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(find_Product([], 0))

    def test_single_element(self):
        for num in range(1, 10):
            self.assertEqual(find_Product([num], 1), num)

    def test_positive_numbers(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(find_Product(arr, len(arr)), 120)

    def test_negative_numbers(self):
        arr = [-1, -2, -3, -4, -5]
        self.assertEqual(find_Product(arr, len(arr)), 120)

    def test_mixed_numbers(self):
        arr = [1, -2, 3, -4, 5]
        self.assertEqual(find_Product(arr, len(arr)), -120)

    def test_duplicates(self):
        arr = [1, 1, 2, 3, 4, 5]
        self.assertEqual(find_Product(arr, len(arr)), 120)

    def test_zero(self):
        self.assertEqual(find_Product([0], 1), 0)
        self.assertIsNone(find_Product([0], 0))

    def test_negative_zero(self):
        self.assertEqual(find_Product([0, -0], 2), 0)

    def test_list_length_zero(self):
        self.assertIsNone(find_Product([], 0))

    def test_list_length_negative(self):
        self.assertRaises(IndexError, find_Product, [1, 2, 3], -1)
