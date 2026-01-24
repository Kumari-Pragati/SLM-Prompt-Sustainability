import unittest
from mbpp_110_code import extract_missing

class TestExtractMissing(unittest.TestCase):

    def test_extract_missing(self):
        test_list = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
        strt_val = 1
        stop_val = 6
        expected_output = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
        self.assertEqual(extract_missing(test_list, strt_val, stop_val), expected_output)

    def test_extract_missing2(self):
        test_list = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7)]
        strt_val = 1
        stop_val = 7
        expected_output = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7)]
        self.assertEqual(extract_missing(test_list, strt_val, stop_val), expected_output)

    def test_extract_missing3(self):
        test_list = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)]
        strt_val = 1
        stop_val = 8
        expected_output = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)]
        self.assertEqual(extract_missing(test_list, strt_val, stop_val), expected_output)

    def test_extract_missing4(self):
        test_list = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9)]
        strt_val = 1
        stop_val = 9
        expected_output = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9)]
        self.assertEqual(extract_missing(test_list, strt_val, stop_val), expected_output)

    def test_extract_missing5(self):
        test_list = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10)]
        strt_val = 1
        stop_val = 10
        expected_output = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10)]
        self.assertEqual(extract_missing(test_list, strt_val, stop_val), expected_output)
