import unittest
from mbpp_362_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 3, 3]), 3)

    def test_edge_case_empty_list(self):
        self.assertIsNone(max_occurrences([]))

    def test_edge_case_single_element_list(self):
        self.assertEqual(max_occurrences([1]), 1)

    def test_edge_case_all_equal(self):
        self.assertEqual(max_occurrences([1, 1, 1, 1, 1]), 1)

    def test_edge_case_all_distinct(self):
        self.assertEqual(max_occurrences([1, 2, 3, 4, 5]), 1)

    def test_edge_case_duplicates(self):
        self.assertEqual(max_occurrences([1, 1, 2, 2, 3, 3, 3]), 3)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(max_occurrences([-1, -1, 0, 0, 1, 1]), 1)

    def test_edge_case_large_list(self):
        self.assertEqual(max_occurrences([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,