import unittest
from mbpp_723_code import count_same_pair

class TestCountSamePair(unittest.TestCase):

    def test_empty_lists(self):
        self.assertEqual(count_same_pair([], []), 0)

    def test_single_element_lists(self):
        self.assertEqual(count_same_pair([1], [1]), 1)
        self.assertEqual(count_same_pair([1], [2]), 0)
        self.assertEqual(count_same_pair([1, 1], [1, 1]), 2)
        self.assertEqual(count_same_pair([1, 2], [1, 2]), 2)

    def test_multiple_element_lists(self):
        self.assertEqual(count_same_pair([1, 2, 3], [1, 2, 3]), 3)
        self.assertEqual(count_same_pair([1, 2, 3], [1, 3, 2]), 2)
        self.assertEqual(count_same_pair([1, 2, 3, 4], [1, 2, 3, 4]), 4)
        self.assertEqual(count_same_pair([1, 2, 3, 4], [1, 2, 3, 5]), 3)

    def test_duplicates_in_lists(self):
        self.assertEqual(count_same_pair([1, 1, 2, 2], [1, 1, 2, 2]), 4)
        self.assertEqual(count_same_pair([1, 1, 2, 2, 3, 3], [1, 1, 2, 2, 3, 3]), 6)
