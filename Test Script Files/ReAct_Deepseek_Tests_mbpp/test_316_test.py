import unittest
from mbpp_316_code import find_last_occurrence

class TestFindLastOccurrence(unittest.TestCase):

    def test_typical_case(self):
        A = [1, 2, 3, 4, 5, 5, 6]
        x = 5
        self.assertEqual(find_last_occurrence(A, x), 5)

    def test_edge_case_single_element(self):
        A = [5]
        x = 5
        self.assertEqual(find_last_occurrence(A, x), 0)

    def test_edge_case_no_occurrence(self):
        A = [1, 2, 3, 4, 5, 6]
        x = 7
        self.assertEqual(find_last_occurrence(A, x), -1)

    def test_edge_case_empty_list(self):
        A = []
        x = 5
        self.assertEqual(find_last_occurrence(A, x), -1)

    def test_edge_case_all_same_elements(self):
        A = [5, 5, 5, 5, 5]
        x = 5
        self.assertEqual(find_last_occurrence(A, x), 4)

    def test_edge_case_negative_numbers(self):
        A = [-1, -2, -3, -2, -1]
        x = -2
        self.assertEqual(find_last_occurrence(A, x), 3)
