import unittest
from mbpp_922_code import max_product

class TestMaxProduct(unittest.TestCase):

    def test_max_product_empty_array(self):
        self.assertIsNone(max_product([]))

    def test_max_product_single_element_array(self):
        self.assertIsNone(max_product([1]))

    def test_max_product_two_element_array(self):
        self.assertEqual(max_product([1, 2]), (1, 2))

    def test_max_product_three_element_array(self):
        self.assertEqual(max_product([1, 2, 3]), (1, 2))

    def test_max_product_four_element_array(self):
        self.assertEqual(max_product([1, 2, 3, 4]), (1, 2))

    def test_max_product_five_element_array(self):
        self.assertEqual(max_product([1, 2, 3, 4, 5]), (1, 2))

    def test_max_product_negative_numbers(self):
        self.assertEqual(max_product([-1, -2, -3, -4, -5]), (-1, -2))

    def test_max_product_positive_and_negative_numbers(self):
        self.assertEqual(max_product([1, -2, 3, -4, 5]), (1, 2))

    def test_max_product_all_positive_numbers(self):
        self.assertEqual(max_product([1, 2, 3, 4, 5]), (1, 2))

    def test_max_product_all_negative_numbers(self):
        self.assertEqual(max_product([-1, -2, -3, -4, -5]), (-1, -2))
