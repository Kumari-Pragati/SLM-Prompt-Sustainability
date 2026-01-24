import unittest
from mbpp_753_code import min_k

class TestMinK(unittest.TestCase):
    def test_typical_input(self):
        test_list = [(1, 5), (2, 3), (3, 7), (4, 2), (5, 1)]
        K = 3
        expected_output = [(2, 3), (3, 7), (4, 2)]
        self.assertEqual(min_k(test_list, K), expected_output)

    def test_edge_case(self):
        test_list = [(1, 5), (2, 3), (3, 7), (4, 2), (5, 1)]
        K = 1
        expected_output = [(1, 5)]
        self.assertEqual(min_k(test_list, K), expected_output)

    def test_edge_case2(self):
        test_list = [(1, 5), (2, 3), (3, 7), (4, 2), (5, 1)]
        K = 5
        expected_output = [(1, 5), (2, 3), (3, 7), (4, 2), (5, 1)]
        self.assertEqual(min_k(test_list, K), expected_output)

    def test_invalid_input(self):
        test_list = [(1, 5), (2, 3), (3, 7), (4, 2), (5, 1)]
        K = 'a'
        with self.assertRaises(TypeError):
            min_k(test_list, K)

    def test_empty_list(self):
        test_list = []
        K = 3
        expected_output = []
        self.assertEqual(min_k(test_list, K), expected_output)

    def test_single_element_list(self):
        test_list = [(1, 5)]
        K = 1
        expected_output = [(1, 5)]
        self.assertEqual(min_k(test_list, K), expected_output)

    def test_k_greater_than_list_length(self):
        test_list = [(1, 5), (2, 3), (3, 7), (4, 2), (5, 1)]
        K = 10
        expected_output = [(1, 5), (2, 3), (3, 7), (4, 2), (5, 1)]
        self.assertEqual(min_k(test_list, K), expected_output)
