import unittest
from mbpp_633_code import pair_OR_Sum

class TestPairORSum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(pair_OR_Sum([1, 2, 3, 4], 4), 15)
        self.assertEqual(pair_OR_Sum([5, 6, 7, 8], 4), 60)

    def test_edge_case_empty(self):
        self.assertEqual(pair_OR_Sum([], 0), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(pair_OR_Sum([1], 1), 1)

    def test_edge_case_two_elements(self):
        self.assertEqual(pair_OR_Sum([1, 2], 2), 3)

    def test_corner_case_all_same(self):
        self.assertEqual(pair_OR_Sum([1, 1, 1, 1], 4), 0)

    def test_corner_case_all_different(self):
        self.assertEqual(pair_OR_Sum([1, 2, 3, 4, 5], 5), 31)
