import unittest
from mbpp_415_code import max_Product

class TestMaxProduct(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_Product([1, 2, 3, 4]), (2, 3))

    def test_edge_case_single_element(self):
        self.assertEqual(max_Product([5]), "No pairs exists")

    def test_boundary_case_two_elements(self):
        self.assertEqual(max_Product([10, 2]), (10, 2))

    def test_corner_case_negative_numbers(self):
        self.assertEqual(max_Product([-1, -2, -3, -4]), (-1, -2))

    def test_corner_case_positive_and_negative_numbers(self):
        self.assertEqual(max_Product([-1, 2, 3, 4]), (4, 3))

    def test_corner_case_zero(self):
        self.assertEqual(max_Product([0, 1, 2, 3]), (0, 1))

    def test_corner_case_duplicate_elements(self):
        self.assertEqual(max_Product([2, 2, 3, 4]), (4, 3))

    def test_invalid_input_empty_list(self):
        with self.assertRaises(Exception):
            max_Product([])

    def test_invalid_input_non_list(self):
        with self.assertRaises(Exception):
            max_Product("not a list")
