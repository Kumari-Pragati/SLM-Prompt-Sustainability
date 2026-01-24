import unittest
from mbpp_468_code import max_product

class TestMaxProduct(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(max_product([1, 2, 3, 4, 5], 5), 120)
        self.assertEqual(max_product([-1, -2, -3, -4, -5], 5), 120)
        self.assertEqual(max_product([0, 0, 0, 0, 0], 5), 0)
        self.assertEqual(max_product([1, 0, 3, 4, 5], 5), 15)
        self.assertEqual(max_product([1, 2, 3, 4, 5, 6], 6), 720)

    def test_empty_list(self):
        self.assertRaises(ValueError, max_product, [], 1)

    def test_negative_list_length(self):
        self.assertRaises(ValueError, max_product, [1, 2, 3], -1)

    def test_single_element_list(self):
        self.assertEqual(max_product([1], 1), 1)

    def test_single_negative_element_list(self):
        self.assertEqual(max_product([-1], 1), -1)
