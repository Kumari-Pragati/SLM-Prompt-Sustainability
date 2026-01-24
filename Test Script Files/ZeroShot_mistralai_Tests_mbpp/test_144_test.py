import unittest
from mbpp_144_code import sum_Pairs

class TestSumPairs(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_Pairs([], 0), 0)

    def test_single_element(self):
        self.assertEqual(sum_Pairs([1], 1), 0)
        self.assertEqual(sum_Pairs([-1], 1), 0)

    def test_two_elements(self):
        self.assertEqual(sum_Pairs([1, 2], 2), 0)
        self.assertEqual(sum_Pairs([-1, -2], 2), 0)
        self.assertEqual(sum_Pairs([1, -2], 2), 4)

    def test_three_elements(self):
        self.assertEqual(sum_Pairs([1, 2, 3], 3), 0)
        self.assertEqual(sum_Pairs([-1, -2, -3], 3), 0)
        self.assertEqual(sum_Pairs([1, -2, 3], 3), 10)
        self.assertEqual(sum_Pairs([1, 2, -3], 3), -3)

    def test_four_elements(self):
        self.assertEqual(sum_Pairs([1, 2, 3, 4], 4), 0)
        self.assertEqual(sum_Pairs([-1, -2, -3, -4], 4), 0)
        self.assertEqual(sum_Pairs([1, -2, 3, 4], 4), 20)
        self.assertEqual(sum_Pairs([1, 2, -3, 4], 4), 10)
        self.assertEqual(sum_Pairs([1, 2, 3, -4], 4), -4)
