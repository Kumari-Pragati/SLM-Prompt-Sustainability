import unittest
from mbpp_723_code import count_same_pair

class TestCountSamePair(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_same_pair([1, 2, 3], [1, 2, 3]), 3)

    def test_edge_case_empty_list(self):
        self.assertEqual(count_same_pair([], []), 0)

    def test_edge_case_single_element_lists(self):
        self.assertEqual(count_same_pair([1], [1]), 1)
        self.assertEqual(count_same_pair([1], [2]), 0)

    def test_edge_case_single_element_lists_with_duplicates(self):
        self.assertEqual(count_same_pair([1, 1], [1, 1]), 2)
        self.assertEqual(count_same_pair([1, 1], [1, 2]), 1)

    def test_edge_case_single_element_lists_with_duplicates_and_empty(self):
        self.assertEqual(count_same_pair([1, 1], []), 0)
        self.assertEqual(count_same_pair([], [1, 1]), 0)

    def test_edge_case_single_element_lists_with_duplicates_and_empty_and_duplicates(self):
        self.assertEqual(count_same_pair([1, 1, 1], [1, 1, 1]), 3)
        self.assertEqual(count_same_pair([1, 1, 1], [1, 1]), 2)
