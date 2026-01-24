import unittest
from mbpp_25_code import find_Product

class TestFindProduct(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 5), 120)

    def test_edge_case_empty_array(self):
        with self.assertRaises(IndexError):
            find_Product([], 0)

    def test_edge_case_single_element_array(self):
        self.assertEqual(find_Product([1], 1), 1)

    def test_edge_case_array_with_duplicates(self):
        self.assertEqual(find_Product([1, 2, 2, 3, 3, 3], 3), 6)

    def test_edge_case_array_with_negative_numbers(self):
        self.assertEqual(find_Product([-1, -2, 3, 4, 5], 3), -2)

    def test_edge_case_array_with_zero(self):
        self.assertEqual(find_Product([0, 1, 2, 3, 4], 3), 0)

    def test_edge_case_array_with_negative_and_zero(self):
        self.assertEqual(find_Product([-1, 0, 1, 2, 3], 3), -1)

    def test_edge_case_array_with_duplicates_and_zero(self):
        self.assertEqual(find_Product([0, 1, 2, 2, 3, 3, 3], 4), 6)

    def test_edge_case_array_with_duplicates_and_negative(self):
        self.assertEqual(find_Product([-1, -2, -2, -3, -3, -3], 3), -6)

    def test_edge_case_array_with_duplicates_and_negative_and_zero(self):
        self.assertEqual(find_Product([-1, 0, 0, 1, 2, 2, 3, 3, 3], 5), 0)
