import unittest
from mbpp_415_code import max_Product

class TestMaxProduct(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(max_Product([1, 2, 3, 4, 5]), (20,))

    def test_edge_case_single_element(self):
        self.assertEqual(max_Product([1]), ("No pairs exists"))

    def test_edge_case_two_elements(self):
        self.assertEqual(max_Product([1, 2]), (2,))

    def test_edge_case_empty_list(self):
        self.assertEqual(max_Product([]), ("No pairs exists"))

    def test_edge_case_single_element_list(self):
        self.assertEqual(max_Product([1, 1]), (1, 1))

    def test_edge_case_negative_numbers(self):
        self.assertEqual(max_Product([-1, -2, -3, -4, -5]), (-4, -5))

    def test_edge_case_positive_and_negative_numbers(self):
        self.assertEqual(max_Product([1, -2, 3, -4, 5]), (1 * 5,))

    def test_edge_case_duplicates(self):
        self.assertEqual(max_Product([1, 2, 2, 3, 4]), (4,))
