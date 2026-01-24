import unittest
from mbpp_144_code import sum_Pairs

class TestSumPairs(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(sum_Pairs([1, 2, 3], 3), 4)

    def test_edge_conditions(self):
        self.assertEqual(sum_Pairs([], 0), 0)
        self.assertEqual(sum_Pairs([1], 1), 0)

    def test_boundary_conditions(self):
        self.assertEqual(sum_Pairs([1, 2, 3, 4, 5], 5), 10)
        self.assertEqual(sum_Pairs([100, 200, 300], 3), 600)

    def test_complex_cases(self):
        self.assertEqual(sum_Pairs([1, 2, 3, 4, 5, 6], 6), 15)
        self.assertEqual(sum_Pairs([-1, -2, -3, -4, -5], 5), -5)
