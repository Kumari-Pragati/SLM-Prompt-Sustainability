import unittest
from183_code import count_pairs

class TestCountPairs(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(count_pairs([], 0, 0), 0)

    def test_single_element(self):
        self.assertEqual(count_pairs([1], 1, 0), 0)
        self.assertEqual(count_pairs([1], 1, 1), 0)

    def test_positive_pairs(self):
        self.assertEqual(count_pairs([1, 2, 3, 2], 4, 1), 2)
        self.assertEqual(count_pairs([1, 2, 3, 2], 4, 2), 1)

    def test_negative_pairs(self):
        self.assertEqual(count_pairs([-1, -2, -3, -2], 4, 1), 2)
        self.assertEqual(count_pairs([-1, -2, -3, -2], 4, -1), 2)

    def test_zero_pairs(self):
        self.assertEqual(count_pairs([0, 1, 2, 3], 4, 0), 0)

    def test_k_greater_than_difference(self):
        self.assertEqual(count_pairs([1, 2, 3, 4], 4, 5), 0)

    def test_k_less_than_difference(self):
        self.assertEqual(count_pairs([1, 2, 3, 4], 4, -6), 0)

    def test_negative_n(self):
        with self.assertRaises(ValueError):
            count_pairs([1, 2, 3], -1, 0)

    def test_negative_k(self):
        with self.assertRaises(ValueError):
            count_pairs([1, 2, 3], 4, -1)
