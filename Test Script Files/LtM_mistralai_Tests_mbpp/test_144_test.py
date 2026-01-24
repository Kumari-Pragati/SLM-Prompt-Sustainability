import unittest
from mbpp_144_code import sum_Pairs

class TestSumPairs(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(sum_Pairs([1, 2, 3, 4], 4), 10)
        self.assertEqual(sum_Pairs([5, 6, 7, 8], 4), 40)

    def test_edge_cases(self):
        self.assertEqual(sum_Pairs([1], 1), 0)
        self.assertEqual(sum_Pairs([1, 2], 2), 0)
        self.assertEqual(sum_Pairs([1, 2, 3], 1), 3)
        self.assertEqual(sum_Pairs([1, 2, 3], 3), 0)

    def test_boundary(self):
        self.assertEqual(sum_Pairs([1, 2, 3, 4], 1), 0)
        self.assertEqual(sum_Pairs([1, 2, 3, 4], 5), 20)

    def test_negative_numbers(self):
        self.assertEqual(sum_Pairs([-1, -2, -3, -4], 4), -10)

    def test_zero_numbers(self):
        self.assertEqual(sum_Pairs([0, 0, 0, 0], 4), 0)
