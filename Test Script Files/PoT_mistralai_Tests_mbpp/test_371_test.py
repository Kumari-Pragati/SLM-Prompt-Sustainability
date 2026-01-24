import unittest
from mbpp_371_code import smallest_missing

class TestSmallestMissing(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(smallest_missing([1, 2, 3], 0, 3), 4)
        self.assertEqual(smallest_missing([1, 2, 3], 1, 3), 4)
        self.assertEqual(smallest_missing([1, 2, 3], 2, 3), 4)
        self.assertEqual(smallest_missing([1, 2, 3], 3, 3), 4)
        self.assertEqual(smallest_missing([1, 2, 3], 4, 3), 5)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(smallest_missing([], 0, len([1, 2, 3])), 1)
        self.assertEqual(smallest_missing([1], 0, len([1, 2, 3])), 2)
        self.assertEqual(smallest_missing([1, 2], 0, len([1, 2, 3])), 3)
        self.assertEqual(smallest_missing([1, 2, 3], 0, 0), 1)
        self.assertEqual(smallest_missing([1, 2, 3], len([1, 2, 3]), len([1, 2, 3])), len([1, 2, 3]) + 1)
