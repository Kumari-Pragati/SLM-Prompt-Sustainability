import unittest
from mbpp_219_code import extract_min_max

class TestExtractMinMax(unittest.TestCase):
    def test_typical_use_case(self):
        test_tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        K = 3
        expected_output = (1, 2, 3, 8, 9, 10)
        self.assertEqual(extract_min_max(test_tup, K), expected_output)

    def test_edge_case_K_is_1(self):
        test_tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        K = 1
        expected_output = (1, 10)
        self.assertEqual(extract_min_max(test_tup, K), expected_output)

    def test_edge_case_K_is_last(self):
        test_tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        K = 5
        expected_output = (1, 2, 3, 8, 9)
        self.assertEqual(extract_min_max(test_tup, K), expected_output)

    def test_edge_case_K_is_zero(self):
        test_tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        K = 0
        expected_output = ()
        self.assertEqual(extract_min_max(test_tup, K), expected_output)

    def test_edge_case_K_is_greater_than_tup_length(self):
        test_tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        K = 11
        expected_output = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        self.assertEqual(extract_min_max(test_tup, K), expected_output)
