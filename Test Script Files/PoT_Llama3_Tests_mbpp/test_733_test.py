import unittest
from mbpp_733_code import find_first_occurrence

class TestFindFirstOccurrence(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_first_occurrence([1, 2, 3, 4, 5], 3), 2)

    def test_edge_case_found_at_start(self):
        self.assertEqual(find_first_occurrence([1, 2, 3, 4, 5], 1), 0)

    def test_edge_case_found_at_end(self):
        self.assertEqual(find_first_occurrence([1, 2, 3, 4, 5], 5), 4)

    def test_edge_case_not_found(self):
        self.assertEqual(find_first_occurrence([1, 2, 3, 4, 5], 6), -1)

    def test_edge_case_empty_list(self):
        self.assertEqual(find_first_occurrence([], 1), -1)

    def test_edge_case_single_element_list(self):
        self.assertEqual(find_first_occurrence([1], 1), 0)

    def test_edge_case_single_element_list_not_found(self):
        self.assertEqual(find_first_occurrence([1], 2), -1)
