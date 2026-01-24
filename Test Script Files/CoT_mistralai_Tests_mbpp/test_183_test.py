import unittest
from mbpp_183_code import count_pairs

class TestCountPairs(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(count_pairs([], 0, 0), 0)

    def test_single_element(self):
        self.assertEqual(count_pairs([1], 1, 0), 0)
        self.assertEqual(count_pairs([1], 1, 1), 0)

    def test_positive_pairs(self):
        self.assertEqual(count_pairs([1, 2, 3, 2, 1], 5, 1), 2)
        self.assertEqual(count_pairs([4, 6, 5, -1, 0], 5, 1), 1)

    def test_negative_pairs(self):
        self.assertEqual(count_pairs([-1, -2, -3, -2, -1], 5, 1), 2)
        self.assertEqual(count_pairs([-4, -6, -5, 1, 0], 5, 1), 0)

    def test_zero_pairs(self):
        self.assertEqual(count_pairs([0, 0, 0, 0, 0], 5, 0), 5)

    def test_negative_k(self):
        self.assertEqual(count_pairs([1, 2, 3], 3, -1), 0)

    def test_invalid_k(self):
        self.assertRaises(ValueError, count_pairs, [1, 2, 3], 3, 0)
