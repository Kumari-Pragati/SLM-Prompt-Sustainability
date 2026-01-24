import unittest
from mbpp_144_code import sum_Pairs

class TestSumPairs(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(sum_Pairs([1, 2, 3, 4], 4), 10)
        self.assertEqual(sum_Pairs([5, 4, 3, 2], 4), 14)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(sum_Pairs([], 0), 0)
        self.assertEqual(sum_Pairs([1], 1), 1)
        self.assertEqual(sum_Pairs([1, 2], 2), 3)
        self.assertEqual(sum_Pairs([1, 2, 3], 3), 6)
        self.assertEqual(sum_Pairs([1, 2, 3, 4], 1), -1)
        self.assertEqual(sum_Pairs([1, 2, 3, 4], 5), -1)

    def test_negative_numbers(self):
        self.assertEqual(sum_Pairs([-1, -2, -3, -4], 4), -10)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            sum_Pairs([1, 2, 3], -1)
        with self.assertRaises(ValueError):
            sum_Pairs([], 1)
        with self.assertRaises(ValueError):
            sum_Pairs([1], 0)
