import unittest
from mbpp_110_code import extract_missing

class TestExtractMissing(unittest.TestCase):

    def test_typical_case(self):
        test_list = [(1, 3), (4, 6), (7, 9)]
        strt_val = 1
        stop_val = 9
        expected_output = [(1, 3), (4, 6), (7, 9)]
        self.assertEqual(extract_missing(test_list, strt_val, stop_val), expected_output)

    def test_edge_case_start_greater_than_stop(self):
        test_list = [(1, 3), (4, 6), (7, 9)]
        strt_val = 10
        stop_val = 5
        expected_output = []
        self.assertEqual(extract_missing(test_list, strt_val, stop_val), expected_output)

    def test_edge_case_start_equals_stop(self):
        test_list = [(1, 3), (4, 6), (7, 9)]
        strt_val = 5
        stop_val = 5
        expected_output = []
        self.assertEqual(extract_missing(test_list, strt_val, stop_val), expected_output)

    def test_edge_case_start_less_than_stop_no_missing(self):
        test_list = [(1, 3), (4, 6), (7, 9)]
        strt_val = 1
        stop_val = 9
        expected_output = []
        self.assertEqual(extract_missing(test_list, strt_val, stop_val), expected_output)

    def test_edge_case_start_less_than_stop_with_missing(self):
        test_list = [(1, 3), (4, 6), (8, 9)]
        strt_val = 1
        stop_val = 9
        expected_output = [(3, 8)]
        self.assertEqual(extract_missing(test_list, strt_val, stop_val), expected_output)

    def test_error_case_invalid_input(self):
        test_list = [(1, 3), (4, 6), (8, 9)]
        strt_val = 'a'
        stop_val = 9
        with self.assertRaises(TypeError):
            extract_missing(test_list, strt_val, stop_val)
