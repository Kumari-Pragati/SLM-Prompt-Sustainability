import unittest
from mbpp_468_code import max_product

class TestMaxProduct(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_product([1, 2, 3, 4], 4), 24)

    def test_edge_case_single_element(self):
        self.assertEqual(max_product([5], 1), 5)

    def test_edge_case_negative_elements(self):
        self.assertEqual(max_product([-1, -2, -3, -4], 4), -6)

    def test_boundary_case_empty_array(self):
        self.assertEqual(max_product([], 0), 0)

    def test_corner_case_all_positive(self):
        self.assertEqual(max_product([1, 2, 3, 4], 4), 24)

    def test_corner_case_all_negative(self):
        self.assertEqual(max_product([-1, -2, -3, -4], 4), -6)

    def test_corner_case_mixed_positive_negative(self):
        self.assertEqual(max_product([-1, 2, -3, 4], 4), 24)

    def test_corner_case_duplicate_elements(self):
        self.assertEqual(max_product([2, 2, 2, 2], 4), 16)
