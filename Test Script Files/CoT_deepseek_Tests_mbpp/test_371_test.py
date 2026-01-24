import unittest
from mbpp_371_code import smallest_missing

class TestSmallestMissing(unittest.TestCase):

    def test_typical_case(self):
        A = [-1, 0, 1, 2, 3]
        self.assertEqual(smallest_missing(A, -1, 3), 4)

    def test_negative_numbers(self):
        A = [-10, -5, 0, 1, 2, 3]
        self.assertEqual(smallest_missing(A, -10, 3), -4)

    def test_duplicates(self):
        A = [-1, 0, 1, 2, 2, 3]
        self.assertEqual(smallest_missing(A, -1, 3), 4)

    def test_empty_array(self):
        A = []
        self.assertEqual(smallest_missing(A, -1, 0), 0)

    def test_single_element(self):
        A = [0]
        self.assertEqual(smallest_missing(A, 0, 0), 1)

    def test_large_numbers(self):
        A = list(range(-1000, 1000))
        self.assertEqual(smallest_missing(A, -1000, 999), 1000)

    def test_invalid_input(self):
        A = [1, 2, 3]
        with self.assertRaises(Exception):
            smallest_missing(A, 2, 1)
