import unittest
from mbpp_144_code import sum_Pairs

class TestSumPairs(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_Pairs([1, 2, 3, 4], 4), 10)
        self.assertEqual(sum_Pairs([5, 6, 7, 8], 4), 40)

    def test_zero(self):
        self.assertEqual(sum_Pairs([0, 0, 0, 0], 4), 0)

    def test_negative_numbers(self):
        self.assertEqual(sum_Pairs([-1, -2, -3, -4], 4), -10)
        self.assertEqual(sum_Pairs([-5, -6, -7, -8], 4), -40)

    def test_empty_list(self):
        self.assertEqual(sum_Pairs([], 4), 0)

    def test_single_element(self):
        self.assertEqual(sum_Pairs([1], 1), 1)
        self.assertEqual(sum_Pairs([-1], 1), -1)

    def test_negative_n(self):
        self.assertEqual(sum_Pairs([1, 2, 3, 4], -1), -10)
