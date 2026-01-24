import unittest
from mbpp_468_code import max_product

class TestMaxProduct(unittest.TestCase):

    def test_max_product_empty_array(self):
        self.assertEqual(max_product([], 0), 0)

    def test_max_product_single_element(self):
        self.assertEqual(max_product([1], 1), 1)

    def test_max_product_two_elements(self):
        self.assertEqual(max_product([1, 2], 2), 2)

    def test_max_product_three_elements(self):
        self.assertEqual(max_product([1, 2, 3], 3), 6)

    def test_max_product_negative_numbers(self):
        self.assertEqual(max_product([-1, -2, -3], 3), -1)

    def test_max_product_positive_and_negative_numbers(self):
        self.assertEqual(max_product([1, -2, 3], 3), 6)

    def test_max_product_all_negative_numbers(self):
        self.assertEqual(max_product([-1, -2, -3], 3), -1)

    def test_max_product_all_positive_numbers(self):
        self.assertEqual(max_product([1, 2, 3], 3), 6)

    def test_max_product_edge_case(self):
        self.assertEqual(max_product([1, 2, 3, 4, 5], 5), 20)
