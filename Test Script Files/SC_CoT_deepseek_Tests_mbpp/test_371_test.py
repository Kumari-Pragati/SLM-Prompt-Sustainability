import unittest
from mbpp_371_code import smallest_missing

class TestSmallestMissing(unittest.TestCase):

    def test_typical_case(self):
        A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(smallest_missing(A, 0, len(A) - 1), 10)

    def test_edge_case_empty_array(self):
        A = []
        self.assertEqual(smallest_missing(A, 0, len(A) - 1), 0)

    def test_edge_case_single_element(self):
        A = [0]
        self.assertEqual(smallest_missing(A, 0, len(A) - 1), 1)

    def test_edge_case_negative_numbers(self):
        A = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(smallest_missing(A, -1, 9), 0)

    def test_edge_case_duplicates(self):
        A = [0, 1, 2, 3, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(smallest_missing(A, 0, len(A) - 1), 10)

    def test_edge_case_missing_first_element(self):
        A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(smallest_missing(A, 0, len(A) - 1), 0)

    def test_edge_case_missing_last_element(self):
        A = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(smallest_missing(A, 0, len(A) - 1), 9)

    def test_invalid_input_left_element_greater_than_right_element(self):
        A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        with self.assertRaises(AssertionError):
            smallest_missing(A, 5, 2)
