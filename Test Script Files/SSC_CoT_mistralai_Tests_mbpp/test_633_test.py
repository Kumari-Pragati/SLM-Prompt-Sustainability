import unittest
from mbpp_633_code import pair_OR_Sum

class TestPairORSum(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(pair_OR_Sum([1, 2, 3, 4], 4), 15)
        self.assertEqual(pair_OR_Sum([5, 5, 5, 5], 4), 0)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(pair_OR_Sum([], 0), 0)
        self.assertEqual(pair_OR_Sum([1], 1), 1)
        self.assertEqual(pair_OR_Sum([1, 2], 1), 3)
        self.assertEqual(pair_OR_Sum([1, 2, 3], 0), 0)
        self.assertEqual(pair_OR_Sum([1, 2, 3], 3), 6)
        self.assertEqual(pair_OR_Sum([1, 1, 1, 1], 4), 0)

    def test_special_cases(self):
        self.assertEqual(pair_OR_Sum([0, 1, 2, 3], 4), 11)
        self.assertEqual(pair_OR_Sum([-1, 0, 1, 2], 4), 7)
        self.assertEqual(pair_OR_Sum([1, 2, 3, 4], 5), 15)
        self.assertEqual(pair_OR_Sum([5, 4, 3, 2, 1], 5), 15)
