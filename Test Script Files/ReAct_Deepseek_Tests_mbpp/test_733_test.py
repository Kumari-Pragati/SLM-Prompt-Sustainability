import unittest
from mbpp_733_code import find_first_occurrence

class TestFindFirstOccurrence(unittest.TestCase):

    def test_typical_case(self):
        A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        x = 5
        self.assertEqual(find_first_occurrence(A, x), 4)

    def test_edge_case_empty_list(self):
        A = []
        x = 5
        self.assertEqual(find_first_occurrence(A, x), -1)

    def test_edge_case_single_element_list(self):
        A = [5]
        x = 5
        self.assertEqual(find_first_occurrence(A, x), 0)

    def test_edge_case_no_occurrence(self):
        A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        x = 10
        self.assertEqual(find_first_occurrence(A, x), -1)

    def test_edge_case_all_same_elements(self):
        A = [5, 5, 5, 5, 5, 5, 5, 5, 5]
        x = 5
        self.assertEqual(find_first_occurrence(A, x), 0)

    def test_edge_case_all_different_elements(self):
        A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        x = 10
        self.assertEqual(find_first_occurrence(A, x), -1)

    def test_edge_case_first_element(self):
        A = [5, 6, 7, 8, 9]
        x = 5
        self.assertEqual(find_first_occurrence(A, x), 0)

    def test_edge_case_last_element(self):
        A = [1, 2, 3, 4, 5]
        x = 5
        self.assertEqual(find_first_occurrence(A, x), 4)
