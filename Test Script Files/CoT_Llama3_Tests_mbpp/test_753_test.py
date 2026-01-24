import unittest
from mbpp_753_code import min_k

class TestMinK(unittest.TestCase):
    def test_min_k_typical(self):
        test_list = [(1, 5), (2, 3), (3, 4), (4, 2), (5, 1)]
        K = 3
        self.assertEqual(min_k(test_list, K), [(1, 5), (2, 3), (3, 4)])

    def test_min_k_edge(self):
        test_list = [(1, 5), (2, 3), (3, 4), (4, 2), (5, 1)]
        K = 1
        self.assertEqual(min_k(test_list, K), [(5, 1)])

    def test_min_k_edge2(self):
        test_list = [(1, 5), (2, 3), (3, 4), (4, 2), (5, 1)]
        K = 5
        self.assertEqual(min_k(test_list, K), [(1, 5), (2, 3), (3, 4), (4, 2), (5, 1)])

    def test_min_k_invalid_input(self):
        test_list = [(1, 5), (2, 3), (3, 4), (4, 2), (5, 1)]
        K = 'a'
        with self.assertRaises(TypeError):
            min_k(test_list, K)

    def test_min_k_empty_list(self):
        test_list = []
        K = 3
        self.assertEqual(min_k(test_list, K), [])

    def test_min_k_single_element(self):
        test_list = [(1, 5)]
        K = 1
        self.assertEqual(min_k(test_list, K), [(1, 5)])
