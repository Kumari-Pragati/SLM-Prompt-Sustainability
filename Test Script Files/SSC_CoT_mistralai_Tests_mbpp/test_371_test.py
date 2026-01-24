import unittest
from mbpp_371_code import smallest_missing

class TestSmallestMissing(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(smallest_missing([1, 2, 3, 4, 6, 7, 8, 9], 0, 8), 5)
        self.assertEqual(smallest_missing([1, 2, 3, 4, 6, 7, 8, 9], 1, 8), 5)
        self.assertEqual(smallest_missing([1, 2, 3, 4, 6, 7, 8, 9], 2, 8), 5)
        self.assertEqual(smallest_missing([1, 2, 3, 4, 6, 7, 8, 9], 3, 8), 5)
        self.assertEqual(smallest_missing([1, 2, 3, 4, 6, 7, 8, 9], 4, 8), 5)
        self.assertEqual(smallest_missing([1, 2, 3, 4, 6, 7, 8, 9], 5, 8), 9)
        self.assertEqual(smallest_missing([1, 2, 3, 4, 6, 7, 8, 9], 6, 8), 9)
        self.assertEqual(smallest_missing([1, 2, 3, 4, 6, 7, 8, 9], 7, 8), 9)
        self.assertEqual(smallest_missing([1, 2, 3, 4, 6, 7, 8, 9], 8, 8), 9)
        self.assertEqual(smallest_missing([1, 2, 3, 4, 6, 7, 8, 9], 9, 9), 10)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(smallest_missing([], 0, 0), 1)
        self.assertEqual(smallest_missing([1], 0, 0), 2)
        self.assertEqual(smallest_missing([1], 1, 1), 2)
        self.assertEqual(smallest_missing([1], 0, 1), 1)
        self.assertEqual(smallest_missing([1, 2], 0, 1), 3)
        self.assertEqual(smallest_missing([1, 2], 1, 1), 3)
        self.assertEqual(smallest_missing([1, 2], 0, 2), 1)
        self.assertEqual(smallest_missing([1, 2], 1, 0), 1)
        self.assertEqual(smallest_missing([1, 2], 2, 1), 3)
        self.assertEqual(smallest_missing([1, 2], 2, 2), 4)
        self.assertEqual(smallest_missing([1, 2, 2], 0, 2), 3)
        self.assertEqual(smallest_missing([1, 2, 2], 1, 2), 3)
        self.assertEqual(smallest_missing([1, 2, 2], 2, 1), 3)
        self.assertEqual(smallest_missing([1, 2, 2], 2, 2), 4)
