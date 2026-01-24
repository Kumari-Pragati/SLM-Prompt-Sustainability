import unittest
from mbpp_753_code import min_k

class TestMinK(unittest.TestCase):

    def test_typical_case(self):
        test_list = [(1, 5), (2, 3), (3, 7), (4, 2), (5, 9)]
        K = 3
        self.assertEqual(min_k(test_list, K), [(1, 5), (2, 3), (3, 7)])

    def test_edge_case(self):
        test_list = [(1, 5), (2, 3), (3, 7), (4, 2), (5, 9)]
        K = 0
        self.assertEqual(min_k(test_list, K), [])

    def test_edge_case2(self):
        test_list = [(1, 5), (2, 3), (3, 7), (4, 2), (5, 9)]
        K = 6
        self.assertEqual(min_k(test_list, K), [(1, 5), (2, 3), (3, 7), (4, 2), (5, 9)])

    def test_error_case(self):
        test_list = [(1, 5), (2, 3), (3, 7), (4, 2), (5, 9)]
        K = 'a'
        with self.assertRaises(TypeError):
            min_k(test_list, K)
