import unittest
from mbpp_658_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 4, 2, 2, 1, 3, 4]), 2)

    def test_edge_case_single_element(self):
        self.assertEqual(max_occurrences([1]), 1)

    def test_edge_case_empty_list(self):
        self.assertEqual(max_occurrences([]), None)

    def test_edge_case_single_occurrence(self):
        self.assertEqual(max_occurrences([1, 2]), 1)

    def test_corner_case_duplicate_first_and_last(self):
        self.assertEqual(max_occurrences([1, 1, 2, 2, 1]), 1)

    def test_corner_case_duplicate_middle(self):
        self.assertEqual(max_occurrences([1, 2, 2, 2, 3]), 2)
