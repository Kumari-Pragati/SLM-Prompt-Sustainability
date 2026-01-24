import unittest
from mbpp_316_code import find_last_occurrence

class TestFindLastOccurrence(unittest.TestCase):

    def test_typical_case(self):
        A = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
        x = 5
        self.assertEqual(find_last_occurrence(A, x), 5)

    def test_edge_case_single_element(self):
        A = [5]
        x = 5
        self.assertEqual(find_last_occurrence(A, x), 0)

    def test_edge_case_no_element(self):
        A = [1, 2, 3, 4, 6, 7, 8, 9]
        x = 5
        self.assertEqual(find_last_occurrence(A, x), -1)

    def test_boundary_case_first_element(self):
        A = [5, 2, 3, 4, 5, 6, 7, 8, 9]
        x = 5
        self.assertEqual(find_last_occurrence(A, x), 0)

    def test_boundary_case_last_element(self):
        A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]
        x = 5
        self.assertEqual(find_last_occurrence(A, x), 10)

    def test_corner_case_repeated_elements(self):
        A = [1, 2, 3, 4, 5, 5, 5, 7, 8, 9]
        x = 5
        self.assertEqual(find_last_occurrence(A, x), 6)
