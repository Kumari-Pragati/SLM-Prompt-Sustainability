import unittest
from mbpp_110_code import extract_missing

class TestExtractMissing(unittest.TestCase):
    def test_typical_use_case(self):
        test_list = [(1, 2), (3, 4), (5, 6), (7, 8)]
        strt_val = 0
        stop_val = 10
        expected_output = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)]
        self.assertEqual(extract_missing(test_list, strt_val, stop_val), expected_output)

    def test_edge_case_start_val_zero(self):
        test_list = [(1, 2), (3, 4), (5, 6), (7, 8)]
        strt_val = 0
        stop_val = 10
        expected_output = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)]
        self.assertEqual(extract_missing(test_list, strt_val, stop_val), expected_output)

    def test_edge_case_stop_val_equal_to_last_element(self):
        test_list = [(1, 2), (3, 4), (5, 6), (7, 8)]
        strt_val = 0
        stop_val = 8
        expected_output = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)]
        self.assertEqual(extract_missing(test_list, strt_val, stop_val), expected_output)

    def test_edge_case_start_val_greater_than_stop_val(self):
        test_list = [(1, 2), (3, 4), (5, 6), (7, 8)]
        strt_val = 10
        stop_val = 5
        expected_output = []
        self.assertEqual(extract_missing(test_list, strt_val, stop_val), expected_output)
