import unittest
from mbpp_371_code import List

from 371_code import smallest_missing

class TestSmallestMissing(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(smallest_missing([], 0, len([0]) - 1), 0)

    def test_single_element(self):
        self.assertEqual(smallest_missing([1], 0, len([1]) - 1), 1)

    def test_missing_element(self):
        self.assertEqual(smallest_missing([1, 2, 3], 0, len([1, 2, 3]) - 1), 4)

    def test_missing_element_at_beginning(self):
        self.assertEqual(smallest_missing([4, 1, 2, 3], 0, len([4, 1, 2, 3]) - 1), 1)

    def test_missing_element_at_end(self):
        self.assertEqual(smallest_missing([1, 2, 3, 4], 0, len([1, 2, 3, 4]) - 1), 5)

    def test_missing_elements(self):
        self.assertEqual(smallest_missing([1, 2, 3, 5, 6], 0, len([1, 2, 3, 5, 6]) - 1), 4)

    def test_duplicate_elements(self):
        self.assertEqual(smallest_missing([1, 1, 2, 3], 0, len([1, 1, 2, 3]) - 1), 2)

    def test_large_list(self):
        A = [i for i in range(100)]
        A[10] = 20
        A[30] = 40
        A[60] = 50
        self.assertEqual(smallest_missing(A, 0, len(A) - 1), 11)
