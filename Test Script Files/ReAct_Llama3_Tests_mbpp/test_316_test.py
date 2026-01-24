import unittest
from mbpp_316_code import find_last_occurrence

class TestFindLastOccurrence(unittest.TestCase):

    def test_typical_case(self):
        A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        x = 5
        self.assertEqual(find_last_occurrence(A, x), 4)

    def test_edge_case_left(self):
        A = [1, 2, 3, 4, 5]
        x = 1
        self.assertEqual(find_last_occurrence(A, x), 0)

    def test_edge_case_right(self):
        A = [1, 2, 3, 4, 5]
        x = 5
        self.assertEqual(find_last_occurrence(A, x), 4)

    def test_edge_case_not_found(self):
        A = [1, 2, 3, 4, 5]
        x = 6
        self.assertEqual(find_last_occurrence(A, x), -1)

    def test_edge_case_empty(self):
        A = []
        x = 5
        self.assertEqual(find_last_occurrence(A, x), -1)

    def test_edge_case_single_element(self):
        A = [5]
        x = 5
        self.assertEqual(find_last_occurrence(A, x), 0)

    def test_edge_case_single_element_not_found(self):
        A = [5]
        x = 6
        self.assertEqual(find_last_occurrence(A, x), -1)
