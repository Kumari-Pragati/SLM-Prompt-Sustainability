import unittest
from mbpp_362_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 3, 3]), 3)

    def test_edge_case_single_element(self):
        self.assertEqual(max_occurrences([1]), 1)

    def test_edge_case_all_equal(self):
        self.assertEqual(max_occurrences([1, 1, 1, 1]), 1)

    def test_edge_case_all_distinct(self):
        self.assertEqual(max_occurrences([1, 2, 3, 4, 5]), 1)

    def test_edge_case_empty_list(self):
        self.assertRaises(IndexError, max_occurrences, [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(max_occurrences([1]), 1)

    def test_edge_case_duplicates(self):
        self.assertEqual(max_occurrences([1, 1, 2, 2, 3, 3, 3]), 3)

    def test_edge_case_duplicates_and_single_element(self):
        self.assertEqual(max_occurrences([1, 1, 2, 2, 3, 3, 3, 4]), 3)

    def test_edge_case_duplicates_and_single_element_and_distinct(self):
        self.assertEqual(max_occurrences([1, 1, 2, 2, 3, 3, 3, 4, 5]), 5)
