import unittest
from mbpp_723_code import count_same_pair

class TestCountSamePair(unittest.TestCase):

    def test_empty_lists(self):
        self.assertEqual(count_same_pair([], []), 0)

    def test_same_elements(self):
        self.assertEqual(count_same_pair([1, 2, 3, 4], [1, 2, 3, 4]), 4)

    def test_different_elements(self):
        self.assertEqual(count_same_pair([1, 2, 3, 4], [4, 3, 2, 1]), 0)

    def test_mixed_elements(self):
        self.assertEqual(count_same_pair([1, 2, 3, 4], [1, 3, 2, 4]), 2)

    def test_duplicate_elements(self):
        self.assertEqual(count_same_pair([1, 2, 2, 3, 4], [1, 2, 2, 3, 4]), 4)
