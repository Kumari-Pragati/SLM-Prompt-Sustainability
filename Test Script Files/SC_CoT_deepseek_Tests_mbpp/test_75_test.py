import unittest

from mbpp_75_code import find_tuples

class TestFindTuples(unittest.TestCase):

    def test_typical_case(self):
        test_list = [(4, 5, 6), (7, 8, 9), (10, 11, 12)]
        K = 2
        self.assertEqual(find_tuples(test_list, K), '[[(4, 5, 6), (7, 8, 9)]]')

    def test_edge_case(self):
        test_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        K = 1
        self.assertEqual(find_tuples(test_list, K), '[[(1, 2, 3)], [(4, 5, 6)], [(7, 8, 9)]]')

    def test_boundary_case(self):
        test_list = [(0, 0, 0), (1, 2, 3), (4, 5, 6)]
        K = 0
        self.assertEqual(find_tuples(test_list, K), '[[(0, 0, 0)], [(1, 2, 3)], [(4, 5, 6)]]')

    def test_corner_case(self):
        test_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        K = 3
        self.assertEqual(find_tuples(test_list, K), '[]')

    def test_invalid_input(self):
        test_list = [(1, 2, '3'), (4, 5, 6), (7, 8, 9)]
        K = 2
        with self.assertRaises(TypeError):
            find_tuples(test_list, K)
