import unittest
from mbpp_723_code import count_same_pair

class TestCountSamePair(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_same_pair([1, 2, 3], [1, 2, 3]), 3)
        self.assertEqual(count_same_pair([4, 4, 4], [4, 4, 4]), 3)
        self.assertEqual(count_same_pair([5, 5, 6], [5, 5, 6]), 2)

    def test_edge_case_empty_lists(self):
        self.assertEqual(count_same_pair([], []), 0)
        self.assertEqual(count_same_pair([1], []), 0)
        self.assertEqual(count_same_pair([], [1]), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(count_same_pair([1], [1]), 1)
        self.assertEqual(count_same_pair([1], [2]), 0)

    def test_edge_case_different_lengths(self):
        self.assertEqual(count_same_pair([1, 2], [1, 2, 3]), 2)
        self.assertEqual(count_same_pair([1, 2], [1, 3]), 1)
        self.assertEqual(count_same_pair([1, 2], [2, 3]), 0)
