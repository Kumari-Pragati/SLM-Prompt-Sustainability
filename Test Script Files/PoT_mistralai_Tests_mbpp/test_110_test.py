import unittest
from mbpp_110_code import extract_missing

class TestExtractMissing(unittest.TestCase):

    def test_typical_case(self):
        self.assertListEqual(extract_missing([(1, 3), (4, 6), (7, 9)], 2, 5), [(2, 3), (4, 5)])
        self.assertListEqual(extract_missing([(0, 2), (3, 5), (6, 8), (9, 11)], 1, 7), [(1, 2), (3, 5), (6, 7)])

    def test_edge_case_start_equal(self):
        self.assertListEqual(extract_missing([(1, 3), (1, 5)], 1, 5), [(1, 3)])

    def test_edge_case_stop_equal(self):
        self.assertListEqual(extract_missing([(0, 2), (2, 4)], 0, 4), [(0, 2)])

    def test_edge_case_start_greater_stop(self):
        self.assertListEqual(extract_missing([(1, 3), (4, 6)], 5, 1), [])

    def test_edge_case_start_less_stop(self):
        self.assertListEqual(extract_missing([(1, 3), (4, 6)], 0, 0), [])

    def test_empty_list(self):
        self.assertListEqual(extract_missing([], 1, 5), [])

    def test_single_element(self):
        self.assertListEqual(extract_missing([(1, 1)], 1, 5), [(1, 1)])
