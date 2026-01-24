import unittest
from mbpp_130_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(max_occurrences([1, 2, 3, 2, 4, 3, 1]), (1, 2))

    def test_edge_case_single_occurrence(self):
        self.assertEqual(max_occurrences([1, 2, 3]), (3, 1))

    def test_edge_case_all_occurrences_equal(self):
        self.assertEqual(max_occurrences([1, 1, 1, 1]), (1, 4))

    def test_edge_case_all_occurrences_zero(self):
        self.assertEqual(max_occurrences([]), (None, 0))

    def test_edge_case_empty_list(self):
        self.assertEqual(max_occurrences([]), (None, 0))

    def test_edge_case_single_element_list(self):
        self.assertEqual(max_occurrences([1]), (1, 1))

    def test_edge_case_duplicates(self):
        self.assertEqual(max_occurrences([1, 1, 2, 2, 2, 3, 3, 3]), (3, 3))

    def test_edge_case_duplicates_and_zero(self):
        self.assertEqual(max_occurrences([1, 1, 2, 2, 2, 3, 3, 3, 0, 0]), (3, 3))

    def test_edge_case_duplicates_and_zero_and_empty(self):
        self.assertEqual(max_occurrences([1, 1, 2, 2, 2, 3, 3, 3, 0, 0, 0]), (3, 3))
