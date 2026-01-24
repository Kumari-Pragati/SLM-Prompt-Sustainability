import unittest
from mbpp_75_code import find_tuples

class TestFindTuples(unittest.TestCase):
    def test_typical_use_case(self):
        test_list = [(10, 20, 30), (4, 8, 12), (15, 25, 35)]
        K = 5
        self.assertEqual(find_tuples(test_list, K), '[(10, 20, 30), (15, 25, 35)]')

    def test_edge_condition(self):
        test_list = [(1, 2, 3), (4, 5, 6)]
        K = 1
        self.assertEqual(find_tuples(test_list, K), '[(1, 2, 3), (4, 5, 6)]')

    def test_boundary_condition(self):
        test_list = [(0, 0, 0), (10, 20, 30)]
        K = 0
        self.assertEqual(find_tuples(test_list, K), '[(0, 0, 0), (10, 20, 30)]')

    def test_invalid_input(self):
        test_list = [(10, 20, '30'), (4, 8, 12), (15, 25, 35)]
        K = 5
        with self.assertRaises(TypeError):
            find_tuples(test_list, K)
