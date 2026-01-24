import unittest
from mbpp_144_code import sum_Pairs

class TestSumPairs(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_Pairs([1, 2, 3, 4], 4), 10)
        self.assertEqual(sum_Pairs([5, 6, 7, 8], 4), 40)
        self.assertEqual(sum_Pairs([9, 10, 11, 12], 4), 78)

    def test_edge_case_small_array(self):
        self.assertEqual(sum_Pairs([1], 1), 0)
        self.assertEqual(sum_Pairs([1, 2], 2), 0)
        self.assertEqual(sum_Pairs([1, 2, 3], 3), 0)

    def test_edge_case_empty_array(self):
        self.assertEqual(sum_Pairs([], 0), 0)

    def test_edge_case_negative_n(self):
        self.assertEqual(sum_Pairs([1, 2, 3], -1), 0)
        self.assertEqual(sum_Pairs([1, 2, 3], -2), 0)

    def test_corner_case_zero_array(self):
        self.assertEqual(sum_Pairs([], 0), 0)
