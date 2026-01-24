import unittest
from mbpp_415_code import max_Product

class TestMaxProduct(unittest.TestCase):

    def test_single_element_array(self):
        self.assertEqual(max_Product([1]), (1, 1))

    def test_two_element_array(self):
        self.assertEqual(max_Product([1, 2]), (1, 2))

    def test_three_element_array(self):
        self.assertEqual(max_Product([1, 2, 3]), (1, 2))

    def test_array_with_negative_numbers(self):
        self.assertEqual(max_Product([-1, -2, -3]), (-1, -2))

    def test_array_with_positive_numbers(self):
        self.assertEqual(max_Product([1, 2, 3]), (1, 2))

    def test_array_with_zero(self):
        self.assertEqual(max_Product([0, 1]), (0, 1))

    def test_array_with_no_pairs(self):
        self.assertEqual(max_Product([1]), ("No pairs exists"))

    def test_array_with_no_pairs_and_zero(self):
        self.assertEqual(max_Product([0]), ("No pairs exists"))
