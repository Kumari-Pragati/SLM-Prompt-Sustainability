import unittest
from mbpp_415_code import max_Product

class TestMaxProduct(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_Product([]), "No pairs exists")

    def test_single_element_list(self):
        self.assertEqual(max_Product([1]), "No pairs exists")

    def test_two_elements_list(self):
        self.assertEqual(max_Product([1, 2]), (1, 2))

    def test_negative_numbers(self):
        self.assertEqual(max_Product([-1, -2]), (-1, -2))

    def test_positive_and_negative_numbers(self):
        self.assertEqual(max_Product([1, -2, 3]), (1, -2))

    def test_large_numbers(self):
        self.assertEqual(max_Product([1000000, 2000000]), (1000000, 2000000))

    def test_small_numbers(self):
        self.assertEqual(max_Product([-1000000, -2000000]), (-1000000, -2000000))

    def test_duplicates(self):
        self.assertEqual(max_Product([1, 1, 2]), (1, 2))

    def test_error_case(self):
        with self.assertRaises(TypeError):
            max_Product("not a list")
