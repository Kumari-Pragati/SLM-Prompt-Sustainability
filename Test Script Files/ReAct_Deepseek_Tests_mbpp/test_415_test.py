import unittest
from mbpp_415_code import max_Product

class TestMaxProduct(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_Product([1, 2, 3, 4, 5]), (5, 4))

    def test_single_element(self):
        self.assertEqual(max_Product([1]), "No pairs exists")

    def test_two_elements(self):
        self.assertEqual(max_Product([1, 2]), (2, 1))

    def test_negative_numbers(self):
        self.assertEqual(max_Product([-1, -2, -3, -4, -5]), (-1, -2))

    def test_mixed_numbers(self):
        self.assertEqual(max_Product([-1, 2, -3, 4, -5]), (4, 2))

    def test_zero_in_array(self):
        self.assertEqual(max_Product([0, 1, 2, 3, 4]), (4, 3))

    def test_large_numbers(self):
        self.assertEqual(max_Product([1000000, 2000000, 3000000, 4000000, 5000000]), (5000000, 4000000))

    def test_duplicate_numbers(self):
        self.assertEqual(max_Product([1, 1, 2, 3, 4]), (4, 3))
