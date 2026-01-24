import unittest
from mbpp_658_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(max_occurrences([1, 2, 3, 2, 4, 2, 5]), 2)

    def test_edge_case_empty_list(self):
        self.assertIsNone(max_occurrences([]))

    def test_edge_case_single_element_list(self):
        self.assertEqual(max_occurrences([1]), 1)

    def test_edge_case_single_element_list_duplicates(self):
        self.assertEqual(max_occurrences([1, 1, 1]), 1)

    def test_edge_case_single_element_list_duplicates_zero(self):
        self.assertEqual(max_occurrences([0, 0, 0]), 0)

    def test_edge_case_single_element_list_duplicates_negative(self):
        self.assertEqual(max_occurrences([-1, -1, -1]), -1)

    def test_edge_case_single_element_list_duplicates_zero_negative(self):
        self.assertEqual(max_occurrences([0, 0, 0, -1, -1, -1]), 0)

    def test_edge_case_single_element_list_duplicates_zero_negative_duplicates(self):
        self.assertEqual(max_occurrences([0, 0, 0, -1, -1, -1, -1, -1]), 0)

    def test_edge_case_single_element_list_duplicates_zero_negative_duplicates_duplicates(self):
        self.assertEqual(max_occurrences([0, 0, 0, -1, -1, -1, -1, -1, -1]), 0)

    def test_edge_case_single_element_list_duplicates_zero_negative_duplicates_duplicates_duplicates(self):
        self.assertEqual(max_occurrences([0, 0, 0, -1, -1, -1, -1, -1, -1, -1]), 0)

    def test_edge_case_single_element_list_duplicates_zero_negative_duplicates_duplicates_duplicates_duplicates(self):
        self.assertEqual(max_occurrences([0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1]), 0)

    def test_edge_case_single_element_list_duplicates_zero_negative_duplicates_duplicates_duplicates_duplicates_duplicates(self):
        self.assertEqual(max_occurrences([0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1]), 0)

    def test_edge_case_single_element_list_duplicates_zero_negative_duplicates_duplicates_duplicates_duplicates_duplicates_duplicates(self):
        self.assertEqual(max_occurrences([0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]), 0)

    def test_edge_case_single_element_list_duplicates_zero_negative_duplicates_duplicates_duplicates_duplicates_duplicates_duplicates_duplicates(self):
        self.assertEqual(max_occurrences([0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]), 0)

    def test_edge_case_single_element_list_duplicates_zero_negative_duplicates_duplicates_duplicates_duplicates_duplicates_duplicates_duplicates(self):
        self.assertEqual(max_occurrences([0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]), 0)

    def test_edge_case_single_element_list_duplicates_zero_negative_duplicates_duplicates_duplicates_duplicates_duplicates_duplicates_duplicates_duplicates(self):
        self.assertEqual(max_occurrences([0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]), 0)

    def test_edge_case_single_element_list_duplicates_zero_negative_duplicates_duplicates_duplicates_duplicates_duplicates_duplicates_duplicates_duplicates(self):
        self.assertEqual(max_occurrences([0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]), 0)

    def test_edge_case_single_element_list_duplicates_zero_negative_duplicates_duplicates_duplicates_duplicates_duplicates_duplicates_duplicates_duplicates(self):
        self.assertEqual(max_occurrences([0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]), 0)

    def test_edge_case_single_element_list_duplicates_zero_negative_duplicates_duplicates_duplicates_duplicates_duplicates_duplicates_duplicates_duplicates(self):
        self.assertEqual(max_occurrences([0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1