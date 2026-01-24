import unittest
from mbpp_110_code import extract_missing

class TestExtractMissing(unittest.TestCase):

    def test_typical_case(self):
        test_list = [(1, 3), (4, 6), (9, 16)]
        strt_val = 1
        stop_val = 16
        expected_output = [(1, 3), (4, 6), (9, 16)]
        self.assertEqual(extract_missing(test_list, strt_val, stop_val), expected_output)

    def test_edge_case(self):
        test_list = [(1, 3), (4, 6), (9, 16)]
        strt_val = 16
        stop_val = 16
        expected_output = []
        self.assertEqual(extract_missing(test_list, strt_val, stop_val), expected_output)

    def test_boundary_case(self):
        test_list = [(1, 3), (4, 6), (9, 16)]
        strt_val = 0
        stop_val = 17
        expected_output = [(0, 1), (1, 3), (4, 6), (9, 16), (16, 17)]
        self.assertEqual(extract_missing(test_list, strt_val, stop_val), expected_output)

    def test_corner_case(self):
        test_list = [(1, 3), (4, 6), (9, 16)]
        strt_val = -10
        stop_val = 10
        expected_output = [(-10, 1), (1, 3), (4, 6), (9, 10)]
        self.assertEqual(extract_missing(test_list, strt_val, stop_val), expected_output)

    def test_invalid_input(self):
        test_list = [(1, 3), (4, 6), (9, 16)]
        strt_val = 'a'
        stop_val = 16
        with self.assertRaises(TypeError):
            extract_missing(test_list, strt_val, stop_val)
