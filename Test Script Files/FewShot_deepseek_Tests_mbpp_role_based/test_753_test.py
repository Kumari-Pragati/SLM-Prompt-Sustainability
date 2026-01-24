import unittest
from mbpp_753_code import min_k

class TestMinK(unittest.TestCase):
    def test_typical_use_case(self):
        test_list = [(1, 2), (3, 4), (5, 1), (7, 3)]
        K = 3
        expected_output = [(5, 1), (7, 3), (3, 4)]
        self.assertEqual(min_k(test_list, K), expected_output)

    def test_boundary_condition(self):
        test_list = [(1, 2), (3, 4), (5, 1), (7, 3)]
        K = 0
        expected_output = []
        self.assertEqual(min_k(test_list, K), expected_output)

    def test_edge_condition(self):
        test_list = [(1, 2), (3, 4), (5, 1), (7, 3)]
        K = 5
        expected_output = [(1, 2), (3, 4), (5, 1), (7, 3)]
        self.assertEqual(min_k(test_list, K), expected_output)

    def test_invalid_input(self):
        test_list = [(1, 2), (3, 4), (5, 1), (7, 3)]
        K = 'a'
        with self.assertRaises(TypeError):
            min_k(test_list, K)
