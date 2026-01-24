import unittest
from mbpp_658_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 4, 2, 2]), 2)

    def test_edge_case_empty_list(self):
        self.assertRaises(IndexError, max_occurrences, [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(max_occurrences([1]), 1)

    def test_edge_case_all_equal_elements_list(self):
        self.assertEqual(max_occurrences([1, 1, 1, 1]), 1)

    def test_edge_case_all_distinct_elements_list(self):
        self.assertEqual(max_occurrences([1, 2, 3, 4, 5]), 1)

    def test_edge_case_list_with_duplicates(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 4, 5, 5]), 2)

    def test_edge_case_list_with_duplicates_and_singletons(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 4, 5, 5, 6]), 2)

    def test_edge_case_list_with_duplicates_and_singletons_and_empty(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 4, 5, 5, 6, 7]), 2)
