import unittest
from mbpp_144_code import sum_Pairs

class TestSumPairs(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(sum_Pairs([1, 2, 3, 4, 5], 5), 4)

    def test_edge_case(self):
        self.assertAlmostEqual(sum_Pairs([1], 1), 0)

    def test_boundary_case(self):
        self.assertAlmostEqual(sum_Pairs([], 0), 0)

    def test_special_case(self):
        self.assertAlmostEqual(sum_Pairs([10, 20, 30, 40, 50], 5), 120)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sum_Pairs("not a list", 5)

        with self.assertRaises(TypeError):
            sum_Pairs([1, 2, 3], "not an integer")

        with self.assertRaises(TypeError):
            sum_Pairs([1, 2, 3], -1)

        with self.assertRaises(TypeError):
            sum_Pairs([1, 2, 3], 1.5)
