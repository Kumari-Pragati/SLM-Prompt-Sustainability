import unittest
from mbpp_753_code import min_k

class TestMinK(unittest.TestCase):

    def test_typical_case(self):
        test_list = [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]
        K = 3
        expected_output = [('a', 1), ('b', 2), ('c', 3)]
        self.assertEqual(min_k(test_list, K), expected_output)

    def test_empty_list(self):
        test_list = []
        K = 3
        expected_output = []
        self.assertEqual(min_k(test_list, K), expected_output)

    def test_large_K(self):
        test_list = [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]
        K = 10
        expected_output = [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]
        self.assertEqual(min_k(test_list, K), expected_output)

    def test_negative_values(self):
        test_list = [('a', -1), ('b', -2), ('c', -3), ('d', -4), ('e', -5)]
        K = 3
        expected_output = [('e', -5), ('d', -4), ('c', -3)]
        self.assertEqual(min_k(test_list, K), expected_output)

    def test_same_values(self):
        test_list = [('a', 1), ('b', 1), ('c', 1), ('d', 1), ('e', 1)]
        K = 3
        expected_output = [('a', 1), ('b', 1), ('c', 1)]
        self.assertEqual(min_k(test_list, K), expected_output)

    def test_invalid_K(self):
        test_list = [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]
        K = -3
        with self.assertRaises(ValueError):
            min_k(test_list, K)
