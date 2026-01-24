import unittest
from mbpp_468_code import max_product

class TestMaxProduct(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_product([1, 2, 3, 4], 4), 24)

    def test_edge_case_single_element(self):
        self.assertEqual(max_product([5], 1), 5)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(max_product([-1, -2, -3, -4], 4), -6)

    def test_edge_case_all_positive_numbers(self):
        self.assertEqual(max_product([1, 2, 3, 4], 4), 24)

    def test_edge_case_all_negative_numbers(self):
        self.assertEqual(max_product([-1, -2, -3, -4], 4), -6)

    def test_edge_case_mixed_numbers(self):
        self.assertEqual(max_product([-1, 2, -3, 4], 4), 24)

    def test_invalid_input_empty_array(self):
        with self.assertRaises(ValueError):
            max_product([], 0)

    def test_invalid_input_negative_size(self):
        with self.assertRaises(ValueError):
            max_product([1, 2, 3, 4], -1)
