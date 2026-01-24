import unittest
from mbpp_723_code import eq
from 723_code import count_same_pair

class TestCountSamePair(unittest.TestCase):

    def test_empty_lists(self):
        self.assertEqual(count_same_pair([], []), 0)

    def test_single_element_lists(self):
        self.assertEqual(count_same_pair([1], [1]), 1)
        self.assertEqual(count_same_pair([1], [2]), 0)

    def test_equal_lists(self):
        self.assertEqual(count_same_pair([1, 2, 3], [1, 2, 3]), 3)

    def test_unequal_lists(self):
        self.assertEqual(count_same_pair([1, 2, 3], [4, 5, 6]), 0)

    def test_lists_with_duplicates(self):
        self.assertEqual(count_same_pair([1, 1, 2, 2, 3], [1, 1, 2, 2, 3]), 4)
