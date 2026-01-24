import unittest
from mbpp_633_code import pair_OR_Sum

class TestPairORSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(pair_OR_Sum([1, 2, 3], 3), 2)

    def test_edge_case_single_element(self):
        self.assertEqual(pair_OR_Sum([1], 1), 0)

    def test_boundary_case_empty_array(self):
        self.assertEqual(pair_OR_Sum([], 0), 0)

    def test_corner_case_duplicate_elements(self):
        self.assertEqual(pair_OR_Sum([1, 1, 1], 3), 0)

    def test_corner_case_large_numbers(self):
        self.assertEqual(pair_OR_Sum([1000, 2000, 3000], 3), 2000)

    def test_corner_case_negative_numbers(self):
        self.assertEqual(pair_OR_Sum([-1, -2, -3], 3), -2)
