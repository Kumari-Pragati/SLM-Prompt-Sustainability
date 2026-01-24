import unittest
from mbpp_110_code import extract_missing

class TestExtractMissing(unittest.TestCase):
    def test_typical_case(self):
        test_list = [(1, 2), (3, 4), (5, 6)]
        strt_val = 0
        stop_val = 10
        expected = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
        self.assertEqual(extract_missing(test_list, strt_val, stop_val), expected)

    def test_edge_case_start(self):
        test_list = [(1, 2), (3, 4), (5, 6)]
        strt_val = 1
        stop_val = 10
        expected = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
        self.assertEqual(extract_missing(test_list, strt_val, stop_val), expected)

    def test_edge_case_stop(self):
        test_list = [(1, 2), (3, 4), (5, 6)]
        strt_val = 0
        stop_val = 5
        expected = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
        self.assertEqual(extract_missing(test_list, strt_val, stop_val), expected)

    def test_edge_case_stop_equal_start(self):
        test_list = [(1, 2), (3, 4), (5, 6)]
        strt_val = 5
        stop_val = 5
        expected = []
        self.assertEqual(extract_missing(test_list, strt_val, stop_val), expected)

    def test_empty_list(self):
        test_list = []
        strt_val = 0
        stop_val = 10
        expected = []
        self.assertEqual(extract_missing(test_list, strt_val, stop_val), expected)

    def test_single_element_list(self):
        test_list = [(1, 2)]
        strt_val = 0
        stop_val = 10
        expected = [(0, 1)]
        self.assertEqual(extract_missing(test_list, strt_val, stop_val), expected)
