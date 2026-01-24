import unittest
from mbpp_842_code import get_odd_occurence

class TestGetOddOccurrence(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(get_odd_occurrence([1, 2, 3, 4, 5], 5), 1)

    def test_edge_case_single_element(self):
        self.assertEqual(get_odd_occurrence([1], 1), 1)

    def test_edge_case_all_duplicates(self):
        self.assertEqual(get_odd_occurrence([1, 1, 1, 1, 1], 5), 1)

    def test_edge_case_all_unique(self):
        self.assertEqual(get_odd_occurrence([1, 2, 3, 4, 5], 5), -1)

    def test_edge_case_empty_array(self):
        self.assertEqual(get_odd_occurrence([], 0), -1)

    def test_edge_case_array_with_one_element(self):
        self.assertEqual(get_odd_occurrence([1], 1), 1)

    def test_edge_case_array_with_two_elements(self):
        self.assertEqual(get_odd_occurrence([1, 2], 2), 1)

    def test_edge_case_array_with_three_elements(self):
        self.assertEqual(get_odd_occurrence([1, 1, 2], 3), 1)

    def test_edge_case_array_with_duplicates(self):
        self.assertEqual(get_odd_occurrence([1, 2, 2, 3, 4], 5), 2)

    def test_edge_case_array_with_duplicates_and_unique(self):
        self.assertEqual(get_odd_occurrence([1, 2, 2, 3, 4, 5], 6), 2)
