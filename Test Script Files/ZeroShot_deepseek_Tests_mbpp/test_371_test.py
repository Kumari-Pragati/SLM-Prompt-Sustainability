import unittest
from mbpp_371_code import smallest_missing

class TestSmallestMissing(unittest.TestCase):

    def test_smallest_missing_ascending(self):
        A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(smallest_missing(A, 0, len(A) - 1), 10)

    def test_smallest_missing_descending(self):
        A = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        self.assertEqual(smallest_missing(A, 0, len(A) - 1), 1)

    def test_smallest_missing_duplicates(self):
        A = [0, 1, 2, 3, 4, 4, 6, 7, 8, 9]
        self.assertEqual(smallest_missing(A, 0, len(A) - 1), 5)

    def test_smallest_missing_empty(self):
        A = []
        self.assertEqual(smallest_missing(A, 0, len(A) - 1), 0)

    def test_smallest_missing_single_element(self):
        A = [0]
        self.assertEqual(smallest_missing(A, 0, len(A) - 1), 1)

    def test_smallest_missing_negative_numbers(self):
        A = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(smallest_missing(A, 0, len(A) - 1), 0)
