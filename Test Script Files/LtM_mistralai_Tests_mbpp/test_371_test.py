import unittest
from mbpp_371_code import smallest_missing

class TestSmallestMissing(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(smallest_missing([1, 2, 3], 0, 3), 4)
        self.assertEqual(smallest_missing([1, 2, 3], 1, 3), 4)
        self.assertEqual(smallest_missing([1, 2, 3], 2, 3), 4)
        self.assertEqual(smallest_missing([1, 2, 3], 3, 3), 4)

    def test_edge_and_boundary(self):
        self.assertEqual(smallest_missing([], 0, 0), 1)
        self.assertEqual(smallest_missing([1], 0, 0), 2)
        self.assertEqual(smallest_missing([1], 0, 1), 2)
        self.assertEqual(smallest_missing([1], 1, 1), 2)
        self.assertEqual(smallest_missing([1, 2], 0, 1), 3)
        self.assertEqual(smallest_missing([1, 2], 1, 1), 3)
        self.assertEqual(smallest_missing([1, 2], 0, 2), 3)
        self.assertEqual(smallest_missing([1, 2], 1, 2), 3)
        self.assertEqual(smallest_missing([1, 2, 2], 0, 2), 4)
        self.assertEqual(smallest_missing([1, 2, 2], 1, 2), 4)
        self.assertEqual(smallest_missing([1, 2, 2], 2, 2), 4)

    def test_complex(self):
        self.assertEqual(smallest_missing([1, 3, 5, 6], 0, 5), 2)
        self.assertEqual(smallest_missing([1, 3, 5, 6], 1, 5), 2)
        self.assertEqual(smallest_missing([1, 3, 5, 6], 2, 5), 4)
        self.assertEqual(smallest_missing([1, 3, 5, 6], 3, 5), 4)
        self.assertEqual(smallest_missing([1, 3, 5, 6], 4, 5), 6)
