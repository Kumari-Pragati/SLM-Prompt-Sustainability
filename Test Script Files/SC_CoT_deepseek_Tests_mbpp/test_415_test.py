import unittest

from mbpp_415_code import max_Product

class TestMaxProduct(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_Product([1, 2, 3, 4]), (3, 4))

    def test_edge_case_single_element(self):
        self.assertEqual(max_Product([1]), "No pairs exists")

    def test_edge_case_two_elements(self):
        self.assertEqual(max_Product([1, 2]), (1, 2))

    def test_edge_case_negative_numbers(self):
        self.assertEqual(max_Product([-1, -2, -3, -4]), (-1, -2))

    def test_edge_case_all_positive(self):
        self.assertEqual(max_Product([1, 2, 3, 4]), (3, 4))

    def test_edge_case_all_negative(self):
        self.assertEqual(max_Product([-1, -2, -3, -4]), (-1, -2))

    def test_corner_case_duplicate_elements(self):
        self.assertEqual(max_Product([1, 2, 2, 4]), (2, 4))

    def test_invalid_input_empty_list(self):
        with self.assertRaises(Exception):
            max_Product([])

    def test_invalid_input_non_integer_elements(self):
        with self.assertRaises(Exception):
            max_Product([1, 2, '3', 4])
