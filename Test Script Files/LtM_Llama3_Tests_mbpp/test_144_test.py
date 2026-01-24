import unittest
from mbpp_144_code import sum_Pairs

class TestSumPairs(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(sum_Pairs([1, 2, 3, 4, 5], 5), 15)
    def test_edge(self):
        self.assertEqual(sum_Pairs([1, 2, 3], 3), 3)
        self.assertEqual(sum_Pairs([1, 2, 3, 4, 5], 1), 1)
    def test_empty(self):
        self.assertEqual(sum_Pairs([], 0), 0)
    def test_negative(self):
        self.assertEqual(sum_Pairs([-1, -2, -3, -4, -5], 5), -15)
    def test_zero(self):
        self.assertEqual(sum_Pairs([0, 0, 0, 0, 0], 5), 0)
