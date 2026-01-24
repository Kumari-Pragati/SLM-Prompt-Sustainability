import unittest
from mbpp_468_code import max_product

class TestMaxProduct(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(max_product([], 0), 0)

    def test_single_element_array(self):
        self.assertEqual(max_product([1], 1), 1)

    def test_two_element_array(self):
        self.assertEqual(max_product([1, 2], 2), 2)

    def test_three_element_array(self):
        self.assertEqual(max_product([1, 2, 3], 3), 6)

    def test_negative_numbers(self):
        self.assertEqual(max_product([-1, -2, -3], 3), -6)

    def test_positive_numbers(self):
        self.assertEqual(max_product([1, 2, 3], 3), 6)

    def test_mixed_numbers(self):
        self.assertEqual(max_product([-1, 2, 3], 3), 6)

    def test_duplicates(self):
        self.assertEqual(max_product([1, 2, 2, 3], 4), 6)

    def test_edge_case(self):
        self.assertEqual(max_product([1, 2, 3, 4, 5], 5), 20)
