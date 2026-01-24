import unittest
from mbpp_371_code import smallest_missing

class TestSmallestMissing(unittest.TestCase):

    def test_typical_case(self):
        A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(smallest_missing(A, 0, len(A) - 1), 10)

    def test_edge_case_empty_array(self):
        A = []
        self.assertEqual(smallest_missing(A, 0, len(A) - 1), 0)

    def test_edge_case_array_with_one_element(self):
        A = [0]
        self.assertEqual(smallest_missing(A, 0, len(A) - 1), 1)

    def test_edge_case_array_with_duplicate_elements(self):
        A = [0, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(smallest_missing(A, 0, len(A) - 1), 10)

    def test_edge_case_array_with_missing_elements(self):
        A = [0, 1, 2, 3, 5, 6, 7, 8, 9]
        self.assertEqual(smallest_missing(A, 0, len(A) - 1), 4)

    def test_edge_case_array_with_negative_elements(self):
        A = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(smallest_missing(A, 0, len(A) - 1), 10)
