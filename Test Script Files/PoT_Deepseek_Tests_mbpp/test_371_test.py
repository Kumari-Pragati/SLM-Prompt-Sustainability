import unittest
from mbpp_371_code import smallest_missing

class TestSmallestMissing(unittest.TestCase):

    def test_typical_case(self):
        A = [-1, 0, 1, 2, 3]
        self.assertEqual(smallest_missing(A, -1, 3), 4)

    def test_edge_case_with_negative_numbers(self):
        A = [-10, -5, -1, 0, 1, 2, 3]
        self.assertEqual(smallest_missing(A, -10, 3), 4)

    def test_edge_case_with_positive_numbers(self):
        A = [1, 2, 3, 4, 5]
        self.assertEqual(smallest_missing(A, 1, 5), 6)

    def test_boundary_case_with_duplicates(self):
        A = [1, 1, 1, 1, 1]
        self.assertEqual(smallest_missing(A, 1, 1), 2)

    def test_boundary_case_with_empty_array(self):
        A = []
        self.assertEqual(smallest_missing(A, -1, 1), -1)

    def test_corner_case_with_large_numbers(self):
        A = list(range(1, 10000))
        self.assertEqual(smallest_missing(A, 1, 9999), 10000)

    def test_corner_case_with_small_numbers(self):
        A = list(range(-1000, 1000))
        self.assertEqual(smallest_missing(A, -1000, 999), 1000)
