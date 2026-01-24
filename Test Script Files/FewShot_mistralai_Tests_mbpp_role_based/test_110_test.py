import unittest
from mbpp_110_code import extract_missing

class TestExtractMissing(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(extract_missing([(1, 2), (3, 4), (5, 6), (7, 8)], 2, 5), [(2, 3), (5, 5)])
        self.assertEqual(extract_missing([(1, 2), (3, 4), (5, 6), (7, 8)], 1, 6), [(1, 2), (5, 6)])
        self.assertEqual(extract_missing([(1, 2), (3, 4), (5, 6), (7, 8)], 1, 8), [(1, 2), (5, 8)])
        self.assertEqual(extract_missing([(1, 2), (3, 4), (5, 6), (7, 8)], 2, 1), [])
        self.assertEqual(extract_missing([(1, 2), (3, 4), (5, 6), (7, 8)], 8, 8), [])

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(extract_missing([], 1, 2), [])
        self.assertEqual(extract_missing([(1, 1)], 1, 2), [(1, 1)])
        self.assertEqual(extract_missing([(1, 1)], 2, 1), [])
        self.assertEqual(extract_missing([(1, 1), (2, 2)], 1, 2), [(1, 1)])
        self.assertEqual(extract_missing([(1, 1), (2, 2)], 2, 3), [(2, 2)])
        self.assertEqual(extract_missing([(1, 1), (2, 2)], 1, 3), [(1, 1)])
