import unittest
from mbpp_183_code import count_pairs

class TestCountPairs(unittest.TestCase):
    def test_positive_pairs(self):
        self.assertEqual(count_pairs([1, 2, 3, 4, 5], 5, 1), 4)
        self.assertEqual(count_pairs([-1, 0, 1, 2, 3], 5, 1), 4)
        self.assertEqual(count_pairs([1, 2, 3, 4, 5], 5, 2), 1)
        self.assertEqual(count_pairs([-1, 0, 1, 2, 3], 5, 2), 1)

    def test_zero_pairs(self):
        self.assertEqual(count_pairs([1, 2, 3], 3, 4), 0)
        self.assertEqual(count_pairs([-1, 0, 1], 3, 0), 0)

    def test_negative_pairs(self):
        self.assertEqual(count_pairs([-1, -2, -3, -4, -5], 5, 1), 10)
        self.assertEqual(count_pairs([1, -1, 0], 3, -1), 1)

    def test_empty_array(self):
        self.assertEqual(count_pairs([], 0, 0), 0)

    def test_invalid_n(self):
        with self.assertRaises(ValueError):
            count_pairs([1, 2, 3], -1, 0)

    def test_invalid_k(self):
        with self.assertRaises(ValueError):
            count_pairs([1, 2, 3], 0, -1)
