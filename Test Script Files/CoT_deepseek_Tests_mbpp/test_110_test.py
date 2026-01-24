import unittest
from mbpp_110_code import extract_missing

class TestExtractMissing(unittest.TestCase):

    def test_typical_case(self):
        test_list = [(1, 3), (4, 6), (7, 9)]
        strt_val = 1
        stop_val = 9
        expected_output = [(1, 3), (4, 6), (7, 9)]
        self.assertEqual(extract_missing(test_list, strt_val, stop_val), expected_output)

    def test_edge_case(self):
        test_list = [(1, 3), (4, 6), (7, 9)]
        strt_val = 1
        stop_val = 1
        expected_output = []
        self.assertEqual(extract_missing(test_list, strt_val, stop_val), expected_output)

    def test_invalid_input(self):
        test_list = [(1, 3), (4, 6), (7, 9)]
        strt_val = 'a'
        stop_val = 9
        with self.assertRaises(TypeError):
            extract_missing(test_list, strt_val, stop_val)

    def test_invalid_input_2(self):
        test_list = [(1, 3), (4, 6), (7, 9)]
        strt_val = 1
        stop_val = 'b'
        with self.assertRaises(TypeError):
            extract_missing(test_list, strt_val, stop_val)

    def test_invalid_input_3(self):
        test_list = [(1, 3), (4, 6), (7, 9)]
        strt_val = 1
        stop_val = 9
        with self.assertRaises(ValueError):
            extract_missing(test_list, strt_val, stop_val)
