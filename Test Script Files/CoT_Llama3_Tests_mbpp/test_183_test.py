import unittest
from mbpp_183_code import count_pairs

class TestCountPairs(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(count_pairs([], 0, 0), 0)

    def test_single_element_array(self):
        self.assertEqual(count_pairs([1], 1, 0), 0)

    def test_no_pairs_array(self):
        self.assertEqual(count_pairs([1, 2, 3, 4], 4, 0), 0)

    def test_pairs_array(self):
        self.assertEqual(count_pairs([1, 2, 3, 4, 5], 5, 1), 3)

    def test_negative_pairs_array(self):
        self.assertEqual(count_pairs([-1, -2, -3, -4, -5], 5, 1), 3)

    def test_duplicates_array(self):
        self.assertEqual(count_pairs([1, 2, 2, 3, 3, 4, 5], 7, 1), 6)

    def test_k_is_zero(self):
        self.assertEqual(count_pairs([1, 2, 3, 4, 5], 5, 0), 0)

    def test_k_is_one(self):
        self.assertEqual(count_pairs([1, 2, 3, 4, 5], 5, 1), 3)

    def test_k_is_negative(self):
        self.assertEqual(count_pairs([1, 2, 3, 4, 5], 5, -1), 3)
