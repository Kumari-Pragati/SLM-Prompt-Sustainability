import unittest
from mbpp_110_code import extract_missing

class TestExtractMissing(unittest.TestCase):

    def test_normal(self):
        self.assertListEqual(extract_missing([(1, 3), (4, 6), (7, 9), (10, 12)], 1, 12), [(1, 1), (4, 4), (7, 7), (10, 12)])
        self.assertListEqual(extract_missing([(1, 3), (4, 6), (7, 9), (10, 12)], 2, 11), [(2, 3), (4, 4), (7, 7), (10, 11)])
        self.assertListEqual(extract_missing([(1, 3), (4, 6), (7, 9), (10, 12)], 0, 12), [(1, 1), (1, 3), (4, 4), (7, 7), (10, 12)])
        self.assertListEqual(extract_missing([(1, 3), (4, 6), (7, 9), (10, 12)], 1, 0), [(1, 1)])

    def test_edge_cases(self):
        self.assertListEqual(extract_missing([(1, 3), (4, 6), (7, 9), (10, 12)], 0, 0), [])
        self.assertListEqual(extract_missing([(1, 3), (4, 6), (7, 9), (10, 12)], 12, 12), [(12, 12)])
        self.assertListEqual(extract_missing([], 1, 2), [])
        self.assertListEqual(extract_missing([(1, 1)], 0, 2), [(0, 1)])
        self.assertListEqual(extract_missing([(1, 1)], 1, 0), [(1, 1)])
