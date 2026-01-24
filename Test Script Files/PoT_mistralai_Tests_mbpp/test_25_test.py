import unittest
from mbpp_25_code import find_Product

class TestFindProduct(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 5), 120)
        self.assertEqual(find_Product([-1, -2, -3, -4, -5], 5), 120)
        self.assertEqual(find_Product([0, 0, 1, 2, 3], 5), 15)

    def test_edge_case_single_element(self):
        self.assertEqual(find_Product([1], 1), 1)

    def test_edge_case_empty_list(self):
        self.assertEqual(find_Product([], 0), 1)

    def test_edge_case_duplicates(self):
        self.assertEqual(find_Product([1, 1, 2, 3, 4], 5), 12)
        self.assertEqual(find_Product([-1, -1, -2, -3, -4], 5), 12)

    def test_corner_case_negative_numbers(self):
        self.assertEqual(find_Product([-1, 1, -2, 2, -3, 3], 6), 2)
