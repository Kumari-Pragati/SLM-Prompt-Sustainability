import unittest
from mbpp_25_code import find_Product

class TestFindProduct(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 5), 120)

    def test_edge_case_empty(self):
        self.assertIsNone(find_Product([], 0))

    def test_edge_case_single_element(self):
        self.assertEqual(find_Product([1], 1), 1)

    def test_edge_case_two_elements(self):
        self.assertEqual(find_Product([1, 2], 2), 2)

    def test_edge_case_max_element(self):
        self.assertEqual(find_Product([10, 10, 10, 10, 10], 5), 100000)

    def test_edge_case_min_element(self):
        self.assertEqual(find_Product([1, 1, 1, 1, 1], 5), 1)

    def test_edge_case_negative_elements(self):
        self.assertEqual(find_Product([-1, -2, -3, -4, -5], 5), -120)

    def test_edge_case_zero_elements(self):
        self.assertEqual(find_Product([0, 0, 0, 0, 0], 5), 0)

    def test_edge_case_duplicates(self):
        self.assertEqual(find_Product([1, 2, 2, 3, 4], 5), 12)

    def test_edge_case_duplicates_with_zero(self):
        self.assertEqual(find_Product([0, 0, 1, 2, 3], 5), 0)

    def test_edge_case_duplicates_with_negative(self):
        self.assertEqual(find_Product([-1, -2, -2, -3, -4], 5), -8)
