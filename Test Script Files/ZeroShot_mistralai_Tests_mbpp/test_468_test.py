import unittest
from mbpp_468_code import max_product

class TestMaxProduct(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_product([], 0), 0)

    def test_single_element(self):
        self.assertEqual(max_product([1], 1), 1)

    def test_positive_numbers(self):
        self.assertEqual(max_product([1, 2, 3, 4, 5], 5), 120)

    def test_negative_numbers(self):
        self.assertEqual(max_product([-1, -2, -3, -4, -5], 5), 120)

    def test_mixed_numbers(self):
        self.assertEqual(max_product([1, -2, 3, -4, 5], 5), 60)

    def test_zero_in_list(self):
        self.assertEqual(max_product([0, 1, 2, 3, 4], 5), 0)
