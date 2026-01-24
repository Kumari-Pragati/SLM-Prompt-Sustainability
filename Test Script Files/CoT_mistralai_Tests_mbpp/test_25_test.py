import unittest
from mbpp_25_code import find_Product

class TestFindProduct(unittest.TestCase):
    def test_find_product_empty_list(self):
        self.assertEqual(find_Product([], 0), 1)

    def test_find_product_single_element(self):
        self.assertEqual(find_Product([1], 1), 1)

    def test_find_product_duplicates(self):
        self.assertEqual(find_Product([1, 1, 2], 3), 2)

    def test_find_product_increasing_sequence(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 5), 120)

    def test_find_product_decreasing_sequence(self):
        self.assertEqual(find_Product([5, 4, 3, 2, 1], 5), 120)

    def test_find_product_negative_numbers(self):
        self.assertEqual(find_Product([-1, -2, -3, -4, -5], 5), 120)

    def test_find_product_zero(self):
        self.assertEqual(find_Product([0], 1), 0)
        self.assertEqual(find_Product([0, 0], 2), 0)

    def test_find_product_invalid_input_empty_array(self):
        with self.assertRaises(IndexError):
            find_Product([], 1)

    def test_find_product_invalid_input_negative_index(self):
        with self.assertRaises(IndexError):
            find_Product([1, 2, 3], -1)
