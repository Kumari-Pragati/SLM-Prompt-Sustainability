import unittest
from mbpp_633_code import pair_OR_Sum

class TestPairOrSum(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(pair_OR_Sum([1, 2, 3], 3), 2)

    def test_edge_conditions(self):
        self.assertEqual(pair_OR_Sum([], 0), 0)
        self.assertEqual(pair_OR_Sum([1], 1), 0)

    def test_boundary_conditions(self):
        self.assertEqual(pair_OR_Sum([0, 0], 2), 0)
        self.assertEqual(pair_OR_Sum([1, 2], 2), 3)
        self.assertEqual(pair_OR_Sum([1000, 2000], 2), 3000)

    def test_complex_cases(self):
        self.assertEqual(pair_OR_Sum([1, 2, 3, 4], 4), 10)
        self.assertEqual(pair_OR_Sum([1, 2, 3, 4, 5], 5), 20)
