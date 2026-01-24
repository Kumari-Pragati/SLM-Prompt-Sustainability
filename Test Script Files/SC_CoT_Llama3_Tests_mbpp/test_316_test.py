import unittest
from mbpp_316_code import find_last_occurrence

class TestFindLastOccurrence(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(find_last_occurrence([1, 2, 3, 4, 5], 4), 3)

    def test_edge_case_left(self):
        self.assertEqual(find_last_occurrence([1, 2, 3, 4, 5], 1), 0)

    def test_edge_case_right(self):
        self.assertEqual(find_last_occurrence([1, 2, 3, 4, 5], 5), 4)

    def test_edge_case_not_found(self):
        self.assertEqual(find_last_occurrence([1, 2, 3, 4, 5], 6), -1)

    def test_edge_case_empty_list(self):
        self.assertEqual(find_last_occurrence([], 5), -1)

    def test_edge_case_single_element(self):
        self.assertEqual(find_last_occurrence([5], 5), 0)

    def test_edge_case_single_element_not_found(self):
        self.assertEqual(find_last_occurrence([5], 6), -1)

    def test_edge_case_empty_list_and_element(self):
        self.assertEqual(find_last_occurrence([], 5), -1)

    def test_edge_case_negative_index(self):
        with self.assertRaises(IndexError):
            find_last_occurrence([-1, 2, 3, 4, 5], 5)

    def test_edge_case_out_of_range(self):
        with self.assertRaises(IndexError):
            find_last_occurrence([1, 2, 3, 4, 5], 6)

    def test_edge_case_negative_element(self):
        self.assertEqual(find_last_occurrence([-1, -2, -3, -4, -5], -1), 0)

    def test_edge_case_positive_element(self):
        self.assertEqual(find_last_occurrence([1, 2, 3, 4, 5], 5), 4)

    def test_edge_case_duplicates(self):
        self.assertEqual(find_last_occurrence([1, 2, 3, 3, 4, 5], 3), 3)

    def test_edge_case_duplicates_not_found(self):
        self.assertEqual(find_last_occurrence([1, 2, 3, 4, 5], 6), -1)
