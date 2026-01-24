import unittest
from mbpp_753_code import min_k

class TestMinK(unittest.TestCase):

    def test_typical_case(self):
        test_list = [(1, 2), (3, 4), (5, 1), (7, 3)]
        K = 3
        expected_output = [(5, 1), (7, 3), (3, 4)]
        self.assertEqual(min_k(test_list, K), expected_output)

    def test_edge_case(self):
        test_list = [(1, 2), (3, 4), (5, 1), (7, 3)]
        K = 0
        expected_output = []
        self.assertEqual(min_k(test_list, K), expected_output)

    def test_boundary_case(self):
        test_list = [(1, 2), (3, 4), (5, 1), (7, 3)]
        K = len(test_list)
        expected_output = test_list
        self.assertEqual(min_k(test_list, K), expected_output)

    def test_corner_case(self):
        test_list = []
        K = 5
        expected_output = []
        self.assertEqual(min_k(test_list, K), expected_output)

    def test_invalid_input(self):
        test_list = [(1, 2), (3, 4), (5, 1), (7, 3)]
        K = -1
        with self.assertRaises(ValueError):
            min_k(test_list, K)
