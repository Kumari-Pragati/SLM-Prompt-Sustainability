import unittest
from mbpp_753_code import min_k

class TestMinK(unittest.TestCase):
    def test_typical_use_case(self):
        test_list = [(1, 5), (2, 3), (3, 7), (4, 2), (5, 9)]
        K = 3
        expected_result = [(1, 5), (2, 3), (3, 7)]
        self.assertEqual(min_k(test_list, K), expected_result)

    def test_edge_case_K_is_zero(self):
        test_list = [(1, 5), (2, 3), (3, 7), (4, 2), (5, 9)]
        K = 0
        expected_result = []
        self.assertEqual(min_k(test_list, K), expected_result)

    def test_edge_case_K_is_greater_than_list_length(self):
        test_list = [(1, 5), (2, 3), (3, 7), (4, 2), (5, 9)]
        K = 10
        expected_result = [(1, 5), (2, 3), (3, 7), (4, 2), (5, 9)]
        self.assertEqual(min_k(test_list, K), expected_result)

    def test_invalid_input_non_integer_K(self):
        test_list = [(1, 5), (2, 3), (3, 7), (4, 2), (5, 9)]
        K = 'abc'
        with self.assertRaises(TypeError):
            min_k(test_list, K)
