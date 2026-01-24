import unittest
from mbpp_723_code import count_same_pair

class TestCountSamePair(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_same_pair([1, 2, 3], [1, 2, 3]), 3)

    def test_empty_lists(self):
        self.assertEqual(count_same_pair([], []), 0)

    def test_different_lengths(self):
        self.assertEqual(count_same_pair([1, 2, 3], [1, 2]), 2)

    def test_all_different(self):
        self.assertEqual(count_same_pair([1, 2, 3], [4, 5, 6]), 0)

    def test_negative_numbers(self):
        self.assertEqual(count_same_pair([-1, -2, -3], [-1, -2, -3]), 3)

    def test_zero(self):
        self.assertEqual(count_same_pair([0, 0], [0]), 1)

    def test_large_numbers(self):
        self.assertEqual(count_same_pair([1000, 2000, 3000], [1000, 2000, 3000]), 3)
