import unittest
from mbpp_723_code import count_same_pair

class TestCountSamePair(unittest.TestCase):
    def test_empty_lists(self):
        self.assertEqual(count_same_pair([], []), 0)

    def test_single_element_lists(self):
        self.assertEqual(count_same_pair([1], [1]), 1)
        self.assertEqual(count_same_pair([1], [2]), 0)

    def test_equal_lists(self):
        self.assertEqual(count_same_pair([1, 1, 2, 2], [1, 1, 2, 2]), 2)

    def test_unsorted_lists(self):
        self.assertEqual(count_same_pair([1, 2, 3, 4], [4, 3, 2, 1]), 2)

    def test_duplicates(self):
        self.assertEqual(count_same_pair([1, 1, 2, 2, 3, 3], [1, 1, 2, 2, 3, 3]), 6)

    def test_empty_list_with_non_empty_list(self):
        self.assertEqual(count_same_pair([], [1, 2, 3]), 0)

    def test_non_empty_list_with_empty_list(self):
        self.assertEqual(count_same_pair([1, 2, 3], []), 0)
