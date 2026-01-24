import unittest
from mbpp_922_code import max_product

class TestMaxProduct(unittest.TestCase):

    def test_max_product_with_positive_numbers(self):
        self.assertEqual(max_product([1, 2, 3, 4, 5]), (5, 4))

    def test_max_product_with_negative_numbers(self):
        self.assertEqual(max_product([-1, -2, -3, -4, -5]), (-1, -2))

    def test_max_product_with_mixed_numbers(self):
        self.assertEqual(max_product([-1, -2, 3, 4, 5]), (5, 4))

    def test_max_product_with_single_number(self):
        self.assertEqual(max_product([5]), None)

    def test_max_product_with_empty_list(self):
        self.assertEqual(max_product([]), None)
