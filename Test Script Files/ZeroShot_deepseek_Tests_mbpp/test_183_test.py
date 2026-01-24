import unittest
from mbpp_183_code import count_pairs

class TestCountPairs(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(count_pairs([1, 7, 5, 9, 2, 12, 3, 2, 1], 9, 2), 3)

    def test_negative_numbers(self):
        self.assertEqual(count_pairs([-1, -7, -5, -9, -2, -12, -3, -2, -1], 9, 2), 3)

    def test_mixed_numbers(self):
        self.assertEqual(count_pairs([1, -7, 5, -9, 2, -12, 3, -2, 1], 9, 2), 3)

    def test_zero_difference(self):
        self.assertEqual(count_pairs([1, 7, 5, 9, 2, 12, 3, 2, 1], 9, 0), 0)

    def test_large_numbers(self):
        self.assertEqual(count_pairs([1000, 2000, 3000, 4000, 5000], 5, 1000), 4)

    def test_empty_array(self):
        self.assertEqual(count_pairs([], 0, 2), 0)
