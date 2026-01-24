import unittest
from mbpp_723_code import count_same_pair

class TestCountSamePair(unittest.TestCase):

    def test_same_length_lists(self):
        self.assertEqual(count_same_pair([1, 2, 3], [3, 2, 1]), 3)
        self.assertEqual(count_same_pair([4, 4, 4, 4], [4, 4, 4, 4]), 4)
        self.assertEqual(count_same_pair([], []), 0)

    def test_different_length_lists(self):
        self.assertEqual(count_same_pair([1, 2, 3], [1, 2]), 2)
        self.assertEqual(count_same_pair([1, 2], [1, 2, 3]), 1)
        self.assertEqual(count_same_pair([1], [1, 2]), 0)

    def test_empty_list(self):
        self.assertEqual(count_same_pair([], []), 0)
        self.assertEqual(count_same_pair([], [1]), 0)
        self.assertEqual(count_same_pair([1], []), 0)

    def test_duplicate_values(self):
        self.assertEqual(count_same_pair([1, 1, 2], [2, 1, 1]), 2)
        self.assertEqual(count_same_pair([1, 1, 1], [1, 1, 1]), 3)
        self.assertEqual(count_same_pair([1, 2, 3], [1, 2, 3]), 3)

    def test_unique_values(self):
        self.assertEqual(count_same_pair([1, 2, 3], [4, 5, 6]), 0)
        self.assertEqual(count_same_pair([4, 5, 6], [1, 2, 3]), 0)

    def test_negative_numbers(self):
        self.assertEqual(count_same_pair([-1, 2, 3], [-1, 2, 3]), 1)
        self.assertEqual(count_same_pair([1, -2, 3], [1, -2, 3]), 1)
        self.assertEqual(count_same_pair([-1, -2, 3], [-1, -2, 3]), 2)

    def test_zero(self):
        self.assertEqual(count_same_pair([0, 2, 3], [0, 2, 3]), 1)
        self.assertEqual(count_same_pair([0, 0, 3], [0, 0, 3]), 2)
        self.assertEqual(count_same_pair([0], [0]), 1)
