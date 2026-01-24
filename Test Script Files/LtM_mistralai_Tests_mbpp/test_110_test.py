import unittest
from mbpp_110_code import extract_missing

class TestExtractMissing(unittest.TestCase):

    def test_simple(self):
        self.assertListEqual(extract_missing([(1, 3), (4, 6), (7, 9)], 1, 10), [(1, 1), (3, 4), (6, 7), (9, 10)])
        self.assertListEqual(extract_missing([(1, 3), (4, 6), (7, 9)], 2, 8), [(2, 3), (6, 7)])
        self.assertListEqual(extract_missing([(1, 3), (4, 6), (7, 9)], 5, 5), [(5, 5)])

    def test_edge_and_boundary(self):
        self.assertListEqual(extract_missing([(1, 3), (4, 6), (7, 9)], 0, 10), [(0, 1), (3, 4), (6, 7), (9, 10)])
        self.assertListEqual(extract_missing([(1, 3), (4, 6), (7, 9)], 10, 10), [(10, 10)])
        self.assertListEqual(extract_missing([], 1, 3), [])
        self.assertListEqual(extract_missing([(1, 3)], 1, 3), [(1, 1), (3, 3)])

    def test_complex(self):
        self.assertListEqual(extract_missing([(1, 3), (4, 6), (7, 9), (10, 12)], 1, 12), [(1, 1), (3, 4), (6, 7), (9, 10), (10, 12)])
        self.assertListEqual(extract_missing([(1, 3), (4, 6), (7, 9), (10, 12)], 2, 9), [(2, 3), (6, 7)])
        self.assertListEqual(extract_missing([(1, 3), (4, 6), (7, 9), (10, 12)], 10, 10), [(10, 10)])
        self.assertListEqual(extract_missing([(1, 3), (4, 6), (7, 9), (10, 12)], 11, 12), [(11, 12)])
