import unittest
from mbpp_362_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 3, 3]), 3)

    def test_edge_case_empty_list(self):
        self.assertIsNone(max_occurrences([]))

    def test_edge_case_single_element_list(self):
        self.assertEqual(max_occurrences([1]), 1)

    def test_edge_case_all_equal_elements(self):
        self.assertEqual(max_occurrences([1, 1, 1, 1, 1]), 1)

    def test_edge_case_all_distinct_elements(self):
        self.assertEqual(max_occurrences([1, 2, 3, 4, 5]), 1)

    def test_edge_case_all_distinct_elements_with_duplicates(self):
        self.assertEqual(max_occurrences([1, 2, 3, 4, 5, 5]), 5)

    def test_edge_case_max_occurrences_at_first_element(self):
        self.assertEqual(max_occurrences([5, 2, 2, 3, 3, 3]), 5)

    def test_edge_case_max_occurrences_at_last_element(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 3, 5]), 5)

    def test_edge_case_max_occurrences_at_middle_element(self):
        self.assertEqual(max_occurrences([1, 2, 3, 3, 4, 5]), 5)
