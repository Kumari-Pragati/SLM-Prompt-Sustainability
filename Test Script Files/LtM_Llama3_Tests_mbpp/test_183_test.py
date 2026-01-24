import unittest
from mbpp_183_code import count_pairs

class TestCountPairs(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(count_pairs([], 0, 0), 0)

    def test_single_element_array(self):
        self.assertEqual(count_pairs([1], 1, 0), 0)

    def test_two_elements_array(self):
        self.assertEqual(count_pairs([1, 2], 2, 0), 0)

    def test_k_is_zero(self):
        self.assertEqual(count_pairs([1, 2, 3], 3, 0), 0)

    def test_k_is_one(self):
        self.assertEqual(count_pairs([1, 2, 3], 3, 1), 1)

    def test_k_is_negative(self):
        self.assertEqual(count_pairs([1, 2, 3], 3, -1), 1)

    def test_k_is_positive(self):
        self.assertEqual(count_pairs([1, 2, 3], 3, 1), 1)

    def test_k_is_large(self):
        self.assertEqual(count_pairs([1, 2, 3, 4, 5], 5, 100), 0)

    def test_k_is_negative_large(self):
        self.assertEqual(count_pairs([1, 2, 3, 4, 5], 5, -100), 2)

    def test_k_is_positive_large(self):
        self.assertEqual(count_pairs([1, 2, 3, 4, 5], 5, 100), 2)
