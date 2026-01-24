import unittest
from mbpp_645_code import find_k_product

class TestFindKProduct(unittest.TestCase):
    def test_positive_numbers(self):
        test_list = [(1, 2), (3, 4), (5, 6)]
        self.assertEqual(find_k_product(test_list, 1), 60)

    def test_empty_list(self):
        test_list = []
        self.assertIsNone(find_k_product(test_list, 0))

    def test_negative_numbers(self):
        test_list = [(-1, 2), (3, -4), (-5, 6)]
        self.assertNotEqual(find_k_product(test_list, 1), 60)

    def test_k_greater_than_length(self):
        test_list = [(1, 2), (3, 4)]
        self.assertRaises(IndexError, find_k_product, test_list, 3)

    def test_k_less_than_zero(self):
        test_list = [(1, 2), (3, 4)]
        self.assertRaises(ValueError, find_k_product, test_list, -1)
