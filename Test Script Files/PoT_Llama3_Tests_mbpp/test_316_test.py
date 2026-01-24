import unittest
from mbpp_316_code import find_last_occurrence

class TestFindLastOccurrence(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_last_occurrence([1, 2, 3, 4, 5], 4), 3)

    def test_edge_case_found_at_start(self):
        self.assertEqual(find_last_occurrence([1, 2, 3, 4, 5], 1), 0)

    def test_edge_case_found_at_end(self):
        self.assertEqual(find_last_occurrence([1, 2, 3, 4, 5], 5), 4)

    def test_edge_case_not_found(self):
        self.assertEqual(find_last_occurrence([1, 2, 3, 4, 5], 6), -1)

    def test_edge_case_empty_list(self):
        self.assertEqual(find_last_occurrence([], 1), -1)

    def test_edge_case_single_element_list(self):
        self.assertEqual(find_last_occurrence([1], 1), 0)
        self.assertEqual(find_last_occurrence([1], 2), -1)

    def test_edge_case_single_element_list_not_found(self):
        self.assertEqual(find_last_occurrence([1, 2, 3, 4, 5], 6), -1)
