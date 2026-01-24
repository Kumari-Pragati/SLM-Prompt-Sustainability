import unittest
from mbpp_753_code import min_k

class TestMinK(unittest.TestCase):

    def test_typical_case(self):
        test_list = [(1, 2), (3, 4), (5, 1), (7, 6)]
        K = 3
        expected_result = [(5, 1), (7, 6), (1, 2)]
        self.assertEqual(min_k(test_list, K), expected_result)

    def test_edge_case_k_greater_than_length(self):
        test_list = [(1, 2), (3, 4), (5, 1), (7, 6)]
        K = 10
        expected_result = [(1, 2), (3, 4), (5, 1), (7, 6)]
        self.assertEqual(min_k(test_list, K), expected_result)

    def test_edge_case_empty_list(self):
        test_list = []
        K = 3
        expected_result = []
        self.assertEqual(min_k(test_list, K), expected_result)

    def test_edge_case_k_equals_zero(self):
        test_list = [(1, 2), (3, 4), (5, 1), (7, 6)]
        K = 0
        expected_result = []
        self.assertEqual(min_k(test_list, K), expected_result)

    def test_typical_case_with_duplicates(self):
        test_list = [(1, 2), (3, 4), (5, 1), (7, 6), (5, 1)]
        K = 3
        expected_result = [(5, 1), (7, 6), (1, 2)]
        self.assertEqual(min_k(test_list, K), expected_result)
